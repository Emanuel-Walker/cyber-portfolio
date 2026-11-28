#!/usr/bin/env python3
"""Small offline demonstration of the IAM access-key detection.

This is intentionally NOT a general KQL engine. It mirrors the core conditions
from detections/elastic_detection_rules/iam_access_key_creation.yml so someone
can verify the idea without deploying AWS.

Usage:
    python detections/demo_iam_detection.py attacks/demo_events/create_access_key.json
"""

import json
import sys
from pathlib import Path

SUSPICIOUS_ACTIONS = {
    "CreateAccessKey",
    "UpdateAccountPasswordPolicy",
    "DeleteAccountPasswordPolicy",
}
ALLOWLIST_USERS = {"iam-break-glass", "terraform-ci"}
HIGH_PRIVILEGE_POLICIES = {
    "AdministratorAccess",
    "PowerUserAccess",
    "IAMFullAccess",
}


def matches(event: dict) -> bool:
    detail = event.get("detail", event)
    action = detail.get("eventName") or event.get("event", {}).get("action")
    user = (
        detail.get("userIdentity", {}).get("userName")
        or event.get("user", {}).get("name")
        or ""
    )

    if user in ALLOWLIST_USERS:
        return False

    if action in SUSPICIOUS_ACTIONS:
        return True

    if action in {"AttachUserPolicy", "AttachRolePolicy"}:
        params = detail.get("requestParameters", {})
        policy_arn = str(params.get("policyArn", ""))
        return any(name in policy_arn for name in HIGH_PRIVILEGE_POLICIES)

    return False


def main() -> int:
    if len(sys.argv) != 2:
        print(
            "Usage: python detections/demo_iam_detection.py [EVENT.json]",
            file=sys.stderr,
        )
        return 2

    path = Path(sys.argv[1])
    event = json.loads(path.read_text(encoding="utf-8"))

    if matches(event):
        print("MATCH: IAM persistence / privilege-change detection")
        return 0

    print("NO MATCH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
