"""
input_sanitizer.py

Why this file exists:
    An LLM prompt is a trust boundary. Anything we paste in from logs lives on
    the attacker's side of that boundary. The sanitizer's job is to turn raw
    log fields into something safe-ish to put next to our instructions.

    It does three things, in order:
      1. Caps length so an attacker cannot flood the context window.
      2. Normalizes dangerous content: markdown, zero-width characters,
         delimiter collisions, control bytes.
      3. Flags fields that look like injection attempts. Flagging does NOT
         block the field. Blocking is a policy decision made upstream. The
         sanitizer just annotates evidence so the provenance log tells the
         truth later.

How to use it:
    sanitized, flags = sanitize_alert(alert_dict)
    sanitized is a dict with the same shape as the input, strings cleaned.
    flags is a list of dicts, one per suspicious field.
"""

from __future__ import annotations

import re
import unicodedata
from typing import Any

# Per-field byte cap. Generous enough for a real command line, strict enough
# that an attacker cannot push a 50KB "please ignore above" into context.
# Tuned down from 4096 after context_window_flood kept slipping through at
# that budget. See attacks/results_sample.md.
MAX_FIELD_LEN = 1024

# Fields we treat as untrusted no matter what. Everything else coming from
# an alert JSON is also untrusted by default. This list just makes the
# intent explicit for readers.
UNTRUSTED_FIELD_NAMES = {
    "user_agent.original",
    "user_agent",
    "file.name",
    "file.path",
    "process.command_line",
    "process.args",
    "url.full",
    "url.original",
    "http.request.referrer",
    "dns.question.name",
    "message",
    "analyst_note",
}

# Delimiter token we wrap untrusted content in before handing it to the model.
# If the attacker tries to inject this exact string we need to notice.
DELIMITER_TOKENS = ("<untrusted_field", "</untrusted_field>")

# Patterns that score high on "someone is trying to talk to the model."
# None of these are proof of malice. They are grounds for a flag plus a
# look at the provenance log later.
INJECTION_PATTERNS = [
    (re.compile(r"ignore\s+(all\s+)?(previous|above|prior)", re.I), "ignore_instructions"),
    (re.compile(r"you\s+are\s+now\s+a", re.I), "role_hijack"),
    (re.compile(r"system\s+prompt", re.I), "system_prompt_reference"),
    (re.compile(r"(^|\s)assistant\s*:", re.I), "role_marker"),
    (re.compile(r"disregard", re.I), "disregard_keyword"),
    (re.compile(r"rate\s+(this|it)?\s*(as\s+)?p[1-4]", re.I), "severity_override"),
    (re.compile(r"[A-Za-z0-9+/]{80,}={0,2}"), "possible_base64_blob"),
    (re.compile(r"</?untrusted_field", re.I), "delimiter_collision"),
]

# Markdown structural characters we strip from untrusted strings. The model
# tends to treat markdown as structure, so removing it closes an easy
# channel for structural confusion attacks.
MARKDOWN_STRIP = re.compile(r"[`*_#>|]")

# Zero-width and bidi override characters that enable homoglyph tricks.
INVISIBLE_CHARS = re.compile(
    r"[​-‏‪-‮⁠-⁯﻿]"
)


def _normalize_unicode(s: str) -> str:
    """
    Fold confusables toward their ASCII equivalents where safe.

    NFKC collapses many compatibility forms. It does NOT collapse Cyrillic
    'е' to Latin 'e'. Those are distinct code points with distinct
    semantics. That gap is a known bypass. See results_sample.md.
    """
    return unicodedata.normalize("NFKC", s)


def _strip_control(s: str) -> str:
    """Remove C0/C1 control bytes except tab and newline."""
    return "".join(
        ch for ch in s
        if ch in ("\t", "\n") or unicodedata.category(ch)[0] != "C"
    )


def _clean_string(value: str) -> str:
    """
    Full cleaning pipeline for a single untrusted string.

    Order matters: unicode normalize first (so later regexes see expected
    characters), then strip invisibles, then controls, then markdown, then
    cap length. Capping last means we never truncate inside a multi-byte
    character after normalization.
    """
    value = _normalize_unicode(value)
    value = INVISIBLE_CHARS.sub("", value)
    value = _strip_control(value)
    value = MARKDOWN_STRIP.sub("", value)
    if len(value) > MAX_FIELD_LEN:
        value = value[:MAX_FIELD_LEN] + "...[TRUNCATED]"
    return value


def _scan_for_injection(field_name: str, value: str) -> list[dict]:
    """
    Return a flag record for each injection pattern the field matches.
    Field name is included so provenance can group by location.
    """
    hits = []
    for pattern, label in INJECTION_PATTERNS:
        if pattern.search(value):
            hits.append({
                "field": field_name,
                "pattern": label,
                "sample": value[:120],
            })
    return hits


def _walk(obj: Any, path: str, flags: list[dict]) -> Any:
    """
    Recursively walk the alert dict. Every string gets cleaned and scanned.
    Keys are left alone. Numbers and bools pass through unchanged.
    """
    if isinstance(obj, dict):
        return {k: _walk(v, f"{path}.{k}" if path else k, flags) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_walk(v, f"{path}[{i}]", flags) for i, v in enumerate(obj)]
    if isinstance(obj, str):
        cleaned = _clean_string(obj)
        flags.extend(_scan_for_injection(path, cleaned))
        return cleaned
    return obj


def sanitize_alert(alert: dict) -> tuple[dict, list[dict]]:
    """
    Public entry point. Returns (sanitized_alert, flags).

    Flags is a list of dicts, each describing one suspicious match. Caller
    decides what to do with them. The provenance logger records all of them.
    """
    flags: list[dict] = []
    sanitized = _walk(alert, "", flags)
    return sanitized, flags


def wrap_for_prompt(sanitized: dict) -> str:
    """
    Serialize the sanitized alert for inclusion in the user turn.

    Each top-level field goes inside its own <untrusted_field> delimiter.
    The system prompt tells the model that anything inside those delimiters
    is data, not instruction. Nested objects are JSON-encoded as a single
    string so we only have one delimiter level to defend.
    """
    import json
    parts = []
    for key, value in sanitized.items():
        if isinstance(value, (dict, list)):
            payload = json.dumps(value, ensure_ascii=False)
        else:
            payload = str(value)
        # Defense in depth: if cleaning somehow left a delimiter token in
        # the payload, neutralize it so the model cannot be tricked into
        # thinking the field ended early.
        for tok in DELIMITER_TOKENS:
            payload = payload.replace(tok, tok.replace("<", "[").replace(">", "]"))
        parts.append(
            f'<untrusted_field name="{key}">{payload}</untrusted_field>'
        )
    return "\n".join(parts)
