"""
Panther rule: silent IAM manipulation.
Why: default GuardDuty does not alert on CreateAccessKey,
AttachUserPolicy of a managed admin policy, or password policy
changes. Each is step one of real breaches. Thirty lines of Python
fixes it.
"""

HIGH_PRIVILEGE_POLICIES = (
    "arn:aws:iam::aws:policy/AdministratorAccess",
    "arn:aws:iam::aws:policy/PowerUserAccess",
    "arn:aws:iam::aws:policy/IAMFullAccess",
)

ALLOWED_PRINCIPALS = {
    "iam-break-glass",
    "terraform-ci",
}


def rule(event) -> bool:
    actor = event.deep_get("userIdentity", "arn", default="")
    actor_name = actor.split("/")[-1] if actor else ""
    if actor_name in ALLOWED_PRINCIPALS:
        return False

    name = event.get("eventName")
    req = event.get("requestParameters") or {}

    if name == "CreateAccessKey":
        return True

    if name in ("AttachUserPolicy", "AttachRolePolicy"):
        return req.get("policyArn") in HIGH_PRIVILEGE_POLICIES

    if name in ("UpdateAccountPasswordPolicy", "DeleteAccountPasswordPolicy"):
        return True

    return False


def title(event) -> str:
    name = event.get("eventName")
    actor = event.deep_get("userIdentity", "arn", default="unknown")
    req = event.get("requestParameters") or {}

    if name == "CreateAccessKey":
        return f"CreateAccessKey for {req.get('userName', '?')} by {actor} (GuardDuty-silent)"
    if name in ("AttachUserPolicy", "AttachRolePolicy"):
        target = req.get("userName") or req.get("roleName") or "?"
        return f"{name}: {target} <- {req.get('policyArn')} by {actor}"
    return f"{name} by {actor} (password policy touched)"


def severity(event) -> str:
    # Password policy changes are HIGH, access key creation CRITICAL
    # if the user is admin-adjacent (tune to taste).
    if event.get("eventName") == "CreateAccessKey":
        return "HIGH"
    return "HIGH"


def dedup(event) -> str:
    return event.deep_get("userIdentity", "arn", default="unknown") + ":" + str(event.get("eventName"))


def alert_context(event) -> dict:
    return {
        "actor": event.deep_get("userIdentity", "arn"),
        "action": event.get("eventName"),
        "request_parameters": event.get("requestParameters"),
        "source_ip": event.get("sourceIPAddress"),
        "user_agent": event.get("userAgent"),
        "mitre": ["T1098.001"],
    }
