"""
Panther rule: NHI PassRole chain to higher-privilege role.
Why: see Elastic version. Tune HIGH_PRIVILEGE_MARKERS to your estate.
"""

HIGH_PRIVILEGE_MARKERS = (
    "admin",
    "poweruser",
    "cross-account",
    "root-emulation",
    "ops-break-glass",
)

TRIGGERING_ACTIONS = {
    "CreateFunction",
    "UpdateFunctionConfiguration",
    "UpdateFunctionCode",
    "RunInstances",
    "PassRole",
}


def rule(event) -> bool:
    if event.deep_get("userIdentity", "type") != "AssumedRole":
        return False
    if event.get("eventName") not in TRIGGERING_ACTIONS:
        return False

    req = event.get("requestParameters") or {}
    # Collect the role being passed from any of the plausible fields.
    candidates = [
        (req.get("role") or ""),
        ((req.get("iamInstanceProfile") or {}).get("arn") or ""),
        (req.get("roleArn") or ""),
    ]
    passed = " ".join(c.lower() for c in candidates if c)
    if not passed:
        return False
    return any(marker in passed for marker in HIGH_PRIVILEGE_MARKERS)


def title(event) -> str:
    actor = event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName", default="unknown")
    action = event.get("eventName")
    return f"NHI {actor} performed {action} toward a high-privilege role"


def severity(_event) -> str:
    return "HIGH"


def dedup(event) -> str:
    return event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName", default="unknown")


def alert_context(event) -> dict:
    return {
        "acting_role": event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName"),
        "action": event.get("eventName"),
        "source_ip": event.get("sourceIPAddress"),
        "user_agent": event.get("userAgent"),
        "request_parameters": event.get("requestParameters"),
        "mitre": ["T1548"],
    }
