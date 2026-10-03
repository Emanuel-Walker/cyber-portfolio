"""
Panther rule: AssumeRole from unusual user-agent for the principal.
Why: see Elastic version. In production this is where you plug into
Panther's lookup tables or an ML side-car with a per-principal UA
history. The implementation below is the simple string-marker proxy.
"""

ATTACKER_UA_MARKERS = (
    "attacker-session",
    "masscan",
    "curl/7",
    "python-requests/2",
    "sqlmap",
)

# Role names that should never AssumeRole from a browser UA.
NHI_ROLES = (
    "pipeline",
    "ingest",
    "etl",
    "batch",
    "automation",
)


def rule(event) -> bool:
    if event.get("eventName") != "AssumeRole":
        return False

    ua = (event.get("userAgent") or "").lower()
    if any(marker in ua for marker in ATTACKER_UA_MARKERS):
        return True

    # NHI role with a browser-looking UA: suspicious even without a
    # known-bad marker. These roles should be called by SDK, not browser.
    role_name = (
        event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName", default="")
        or ""
    ).lower()
    if any(nhi in role_name for nhi in NHI_ROLES):
        if "mozilla/" in ua or "chrome/" in ua or "safari/" in ua:
            return True

    return False


def title(event) -> str:
    role = event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName", default="unknown")
    return f"AssumeRole with anomalous user-agent for {role}"


def severity(_event) -> str:
    return "MEDIUM"


def dedup(event) -> str:
    role = event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName", default="unknown")
    return f"{role}:{event.get('sourceIPAddress')}"


def alert_context(event) -> dict:
    return {
        "role": event.deep_get("userIdentity", "sessionContext", "sessionIssuer", "userName"),
        "source_ip": event.get("sourceIPAddress"),
        "user_agent": event.get("userAgent"),
        "mitre": ["T1078.004"],
    }
