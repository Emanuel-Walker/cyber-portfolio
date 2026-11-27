#!/usr/bin/env python3
"""Offline demo for the prompt-injection input sanitizer.

Usage:
    python code/demo_sanitizer.py data/sample_alerts/injected_user_agent.json
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from hardening.input_sanitizer import sanitize_alert


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python code/demo_sanitizer.py [ALERT.json]", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    alert = json.loads(path.read_text(encoding="utf-8"))
    sanitized, flags = sanitize_alert(alert)

    print("Detected injection signals:")
    if not flags:
        print("  none")
    else:
        for flag in flags:
            print(f"  - {flag['field']}: {flag['pattern']}")

    print()
    print("Sanitized user_agent.original:")
    print(sanitized.get("user_agent", {}).get("original", "[missing]"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
