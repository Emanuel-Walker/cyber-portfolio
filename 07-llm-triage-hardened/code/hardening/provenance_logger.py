"""
provenance_logger.py

Why this file exists:
    Every LLM call needs a receipt. Without one, you cannot answer the two
    questions that matter after an incident:
      1. Exactly what did we send to the model?
      2. Exactly what did it send back, before any post-processing?

    The provenance log is append-only JSONL. One line per call. Each line
    carries enough to reproduce the call offline and to prove, later, which
    prompt version made which decision.

Fields logged per call:
    ts              ISO-8601 UTC timestamp
    input_hash      SHA-256 of the raw alert bytes
    prompt_version  Version string from the system prompt header
    model           Model name sent to Ollama
    flags           Sanitizer flags for this input
    raw_output      Model output text, unmodified
    validation      "ok" or the validator's rejection tag
    verdict         Parsed verdict dict, or null if rejected
"""

from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

# Default log location. Overridable via env var so Docker and CI can point
# it somewhere mounted or ephemeral.
_DEFAULT_LOG = Path(__file__).resolve().parent.parent / "provenance.jsonl"
LOG_PATH = Path(os.environ.get("TRIAGE_PROVENANCE_LOG", _DEFAULT_LOG))


def _hash_input(raw_bytes: bytes) -> str:
    """SHA-256 of the exact bytes we read from stdin. Short-form hex."""
    return hashlib.sha256(raw_bytes).hexdigest()


def log_call(
    raw_input_bytes: bytes,
    prompt_version: str,
    model: str,
    flags: list[dict],
    raw_output: str,
    validation: str,
    verdict: dict | None,
) -> None:
    """
    Append one JSON line describing this triage call.

    This function never raises on logging failure. A broken log should not
    take down the agent. It does print a one-line stderr warning so an
    operator notices.
    """
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "input_hash": _hash_input(raw_input_bytes),
        "prompt_version": prompt_version,
        "model": model,
        "flags": flags,
        "raw_output": raw_output,
        "validation": validation,
        "verdict": verdict,
    }
    try:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError as exc:
        import sys
        print(f"[provenance] log write failed: {exc}", file=sys.stderr)
