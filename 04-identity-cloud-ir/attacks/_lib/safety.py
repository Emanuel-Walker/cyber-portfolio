"""
safety.py
Why: every attack script in this repo refuses to run against any AWS
account that does not have the lab's Project tag. We do not want a copy-
paste accident to run these against a real environment.
How: pull the Project tag from one of the known lab resources and bail
out if it does not match.
"""

import os
import sys
import boto3
from botocore.exceptions import ClientError

EXPECTED_PROJECT = os.environ.get("LAB_PROJECT", "northwind-cloud")


def assert_lab_account(region: str | None = None) -> dict:
    """
    Confirm we are pointed at the lab. Returns a dict with the account
    ID and region so the caller can log it. Exits non-zero on mismatch.
    """
    region = region or os.environ.get("AWS_REGION", "us-east-1")
    sts = boto3.client("sts", region_name=region)
    try:
        ident = sts.get_caller_identity()
    except ClientError as exc:
        print(f"[safety] cannot call sts:GetCallerIdentity: {exc}", file=sys.stderr)
        sys.exit(2)

    # Check at least one lab-tagged resource exists. We use GuardDuty
    # detectors as the probe because the lab creates exactly one.
    gd = boto3.client("guardduty", region_name=region)
    detectors = gd.list_detectors().get("DetectorIds", [])
    if not detectors:
        print(
            f"[safety] no GuardDuty detector in {region}. "
            f"This script only runs against the deployed lab.",
            file=sys.stderr,
        )
        sys.exit(2)

    tags = gd.list_tags_for_resource(
        ResourceArn=f"arn:aws:guardduty:{region}:{ident['Account']}:detector/{detectors[0]}"
    ).get("Tags", {})

    if tags.get("Project") != EXPECTED_PROJECT:
        print(
            f"[safety] detector tag Project={tags.get('Project')!r} does not match "
            f"expected {EXPECTED_PROJECT!r}. Refusing to run.",
            file=sys.stderr,
        )
        sys.exit(2)

    return {"account": ident["Account"], "region": region, "project": EXPECTED_PROJECT}
