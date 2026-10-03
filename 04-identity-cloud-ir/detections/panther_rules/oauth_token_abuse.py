"""
Panther rule: OAuth refresh token read by unexpected principal.
Why: see Elastic version. Panther's Python schema gives us richer
control for allowlist logic.
"""

ALLOWED_READERS = {
    "northwind-cloud-lab-ec2-role",
    "ops-automation",
}

TOKEN_PATH_MARKERS = ("refresh_token", "oauth", "api_key", "secret")


def rule(event) -> bool:
    if event.get("eventSource") != "ssm.amazonaws.com":
        return False
    if event.get("eventName") != "GetParameter":
        return False

    req = event.get("requestParameters", {}) or {}
    param_name = (req.get("name") or "").lower()
    if not any(marker in param_name for marker in TOKEN_PATH_MARKERS):
        return False

    actor = event.deep_get("userIdentity", "arn", default="")
    # Strip trailing session segment for role sessions.
    actor_name = actor.split("/")[-1] if actor else ""
    return actor_name not in ALLOWED_READERS


def title(event) -> str:
    actor = event.deep_get("userIdentity", "arn", default="unknown")
    param = (event.get("requestParameters") or {}).get("name", "unknown")
    return f"SSM token read by unexpected principal {actor} on {param}"


def severity(_event) -> str:
    return "HIGH"


def dedup(event) -> str:
    return event.deep_get("userIdentity", "arn", default="unknown")


def alert_context(event) -> dict:
    return {
        "actor": event.deep_get("userIdentity", "arn"),
        "source_ip": event.get("sourceIPAddress"),
        "user_agent": event.get("userAgent"),
        "parameter_name": (event.get("requestParameters") or {}).get("name"),
        "mitre": ["T1552.007"],
    }
