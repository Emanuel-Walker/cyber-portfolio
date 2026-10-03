#!/usr/bin/env python3
"""
Scenario 03: cross-tenant / session anomaly.

Why: in the Scattered Spider pattern, attackers log in from residential
proxies or commercial VPS providers after calling a help desk and getting
MFA reset. The individual API calls look fine. The pattern is: unusual
geo + unusual ASN + unusual time + first-time user-agent.

We cannot actually relocate traffic from a script. What we CAN do is
inject a session with a weird user-agent string (which CloudTrail records)
and run it at an odd hour. The detection rule in Elastic/Panther looks
for the user-agent + principal pattern that would correlate with ASN
in a real environment.

What CloudTrail sees:
  - sts:AssumeRole with an unusual userAgent
  - subsequent iam/s3 calls with the same unusual userAgent

Detection: cross_tenant_session_anomaly.yml / .py
"""

import sys
import boto3
from botocore.config import Config
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.safety import assert_lab_account

PROJECT = "northwind-cloud"

# Why this user-agent: Scattered Spider has been observed using fresh
# Chrome-on-Linux UAs that do not match the org's normal fleet. We pick
# something obviously-not-boto3 to make the detection rule firable.
ATTACKER_UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 (northwind-lab-attacker-session)"


def main() -> int:
    ctx = assert_lab_account()
    print(f"[03] lab confirmed: account={ctx['account']} region={ctx['region']}")

    cfg = Config(user_agent_extra=ATTACKER_UA)
    sts = boto3.client("sts", config=cfg, region_name=ctx["region"])

    pipeline_role_arn = f"arn:aws:iam::{ctx['account']}:role/{PROJECT}-lab-data-pipeline"
    print(f"[03] assuming pipeline role with unusual UA")
    assumed = sts.assume_role(
        RoleArn=pipeline_role_arn,
        RoleSessionName="offhours-contractor-01",
    )["Credentials"]

    anomaly = boto3.Session(
        aws_access_key_id=assumed["AccessKeyId"],
        aws_secret_access_key=assumed["SecretAccessKey"],
        aws_session_token=assumed["SessionToken"],
        region_name=ctx["region"],
    )

    print("[03] poking around with the anomalous session")
    _ = anomaly.client("iam", config=cfg).list_roles()
    _ = anomaly.client("s3", config=cfg).list_buckets()
    _ = anomaly.client("sts", config=cfg).get_caller_identity()

    print("[03] done. Expected CloudTrail events:")
    print("     - sts:AssumeRole with userAgent containing 'northwind-lab-attacker-session'")
    print("     - iam:ListRoles, s3:ListBuckets, sts:GetCallerIdentity with same UA")
    print("[03] expected GuardDuty default: silent (not a known-bad IP).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
