"""
Panther rule: high-volume GetObject on a sensitive bucket.
Why: see Elastic version. Panther's dedup key gives us a cheap
threshold without a dedicated counter.
"""

SENSITIVE_BUCKET_MARKERS = (
    "customer-data",
    "pii",
    "finance",
    "payroll",
    "customers-prod",
)

# This rule should fire on each event but Panther's dedup window will
# collapse to one alert per (principal, bucket) per hour. Use Panther's
# built-in event summary to see "how many in the window".


def rule(event) -> bool:
    if event.get("eventSource") != "s3.amazonaws.com":
        return False
    if event.get("eventName") != "GetObject":
        return False

    bucket = (event.get("requestParameters") or {}).get("bucketName", "").lower()
    if not any(marker in bucket for marker in SENSITIVE_BUCKET_MARKERS):
        return False

    # Only alert on NHI principals. Human analysts occasionally pull data
    # one-off and we do not want to light them up.
    return event.deep_get("userIdentity", "type") == "AssumedRole"


def title(event) -> str:
    actor = event.deep_get("userIdentity", "arn", default="unknown")
    bucket = (event.get("requestParameters") or {}).get("bucketName", "unknown")
    return f"NHI {actor} is pulling objects from sensitive bucket {bucket}"


def severity(_event) -> str:
    return "HIGH"


def dedup(event) -> str:
    actor = event.deep_get("userIdentity", "arn", default="unknown")
    bucket = (event.get("requestParameters") or {}).get("bucketName", "unknown")
    return f"{actor}:{bucket}"


def dedup_period_minutes() -> int:
    return 60


def threshold() -> int:
    # Only alert if the rule fires at least 100 times within the dedup window.
    return 100


def alert_context(event) -> dict:
    return {
        "actor": event.deep_get("userIdentity", "arn"),
        "bucket": (event.get("requestParameters") or {}).get("bucketName"),
        "source_ip": event.get("sourceIPAddress"),
        "user_agent": event.get("userAgent"),
        "mitre": ["T1537"],
    }
