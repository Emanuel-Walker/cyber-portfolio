"""
output_validator.py

Why this file exists:
    The system prompt tells the model to return strict JSON. The model
    usually complies. Sometimes it does not. Sometimes an attacker in the
    input convinces it to add a prose preamble or an extra field. Sometimes
    the model invents a new severity string because it felt poetic.

    The validator does not try to repair any of that. If the output does
    not match the schema, it is rejected. A rejected output is logged as a
    failure, not treated as a verdict. That single rule kills most of the
    fun an attacker can have with the output channel.

How to use it:
    verdict, error = validate_output(raw_model_text)
    verdict is a dict if the output was valid, else None.
    error is None if valid, else a short string explaining why it failed.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator

# Load the schema once at import time. If the schema file is bad we want
# that failure to happen loudly at startup, not at request time.
_SCHEMA_PATH = Path(__file__).resolve().parent.parent / "prompts" / "output_schema.json"
with _SCHEMA_PATH.open("r", encoding="utf-8") as f:
    _SCHEMA = json.load(f)
_VALIDATOR = Draft202012Validator(_SCHEMA)

# Regex that pulls the first JSON object out of a response. The model is
# supposed to return pure JSON. If it wraps the JSON in prose or a markdown
# fence we try to recover the object, but we do NOT try to fix the JSON
# itself. Recovery is best-effort for user experience, not security.
_JSON_OBJECT = re.compile(r"\{.*\}", re.DOTALL)


def _extract_json_object(text: str) -> str | None:
    """
    Pull the first balanced JSON object out of raw model text.

    This handles the common case where the model prefixes its output with
    'Here is the triage verdict:' or wraps it in ```json fences. If no
    object is found, return None and let the caller reject.
    """
    text = text.strip()
    # Strip markdown code fences if present. The system prompt forbids
    # them but the model is a mood ring.
    if text.startswith("```"):
        text = text.strip("`")
        if text.lower().startswith("json"):
            text = text[4:]
    match = _JSON_OBJECT.search(text)
    return match.group(0) if match else None


def validate_output(raw_text: str) -> tuple[dict | None, str | None]:
    """
    Validate model output against the triage schema.

    Returns (verdict, None) on success. Returns (None, error_string) on any
    failure. The error string is safe to log but should never be shown back
    to the model in a retry loop. Retry loops are a known channel for
    adversarial examples to anchor themselves.
    """
    candidate = _extract_json_object(raw_text)
    if candidate is None:
        return None, "no_json_object_found"

    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError as exc:
        return None, f"json_decode_error: {exc.msg}"

    errors = sorted(_VALIDATOR.iter_errors(parsed), key=lambda e: e.path)
    if errors:
        # Collapse the first error into a short tag. We do not surface the
        # full validator error to callers because it can echo attacker
        # content back into logs. The provenance logger already has the
        # raw output stored separately.
        first = errors[0]
        tag = "/".join(str(p) for p in first.absolute_path) or "root"
        return None, f"schema_violation:{tag}:{first.validator}"

    return parsed, None
