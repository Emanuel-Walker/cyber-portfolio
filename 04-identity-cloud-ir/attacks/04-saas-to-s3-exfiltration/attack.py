#!/usr/bin/env python3
"""
Scenario 04: SaaS-to-S3 exfiltration via legitimate API patterns.

Why: no malware, no encryption, no weird egress. Just a loop of
GetObject calls under a legitimate NHI identity. The 2024 Snowflake
customer breaches moved hundreds of GB this way. The point of this
scenario is to show that a low-and-slow pull from a clean source
IP does NOT fire default GuardDuty S3 Protection.

We loop over the 20 seeded objects 10 times to produce 200 GetObject
events, spaced out with a short sleep so the rate stays under any
reasonable per-principal threshold.

What CloudTrail sees:
  - 200 s3:GetObject events on the customer-data bucket
  - All under the data-pipeline role (NHI)
  - Source IP = this script's egress IP

Detection: saas_exfil_api_pattern.yml / .py
"""

import sys
import time
import boto3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.safety import assert_lab_account

PROJECT = "northwind-cloud"


def main() -> int:
    ctx = assert_lab_account()
    print(f"[04] lab confirmed: account={ctx['account']} region={ctx['region']}")

    sts = boto3.client("sts", region_name=ctx["region"])
    role_arn = f"arn:aws:iam::{ctx['account']}:role/{PROJECT}-lab-data-pipeline"
    assumed = sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName="batch-sync-job-off-hours",
    )["Credentials"]

    pipeline = boto3.Session(
        aws_access_key_id=assumed["AccessKeyId"],
        aws_secret_access_key=assumed["SecretAccessKey"],
        aws_session_token=assumed["SessionToken"],
        region_name=ctx["region"],
    )
    s3 = pipeline.client("s3")

    # Discover the customer-data bucket by prefix.
    buckets = [
        b["Name"] for b in s3.list_buckets()["Buckets"]
        if "customer-data" in b["Name"] and b["Name"].startswith(f"{PROJECT}-lab-")
    ]
    if not buckets:
        print("[04] could not find customer-data bucket")
        return 1
    bucket = buckets[0]
    print(f"[04] exfil target: s3://{bucket}")

    # List the objects.
    objs = s3.list_objects_v2(Bucket=bucket, Prefix="customers/").get("Contents", [])
    print(f"[04] found {len(objs)} objects. Will loop 10x = {len(objs)*10} GetObject.")

    bytes_pulled = 0
    for pass_idx in range(10):
        for obj in objs:
            r = s3.get_object(Bucket=bucket, Key=obj["Key"])
            bytes_pulled += r["ContentLength"]
            r["Body"].read()  # drain
            time.sleep(0.1)   # pace it
        print(f"[04] pass {pass_idx + 1}/10 complete, cumulative {bytes_pulled} bytes")

    print(f"[04] exfil complete, pulled {bytes_pulled} bytes across 200 calls")
    print("[04] done. Expected CloudTrail events: 200x s3:GetObject")
    print("[04] expected GuardDuty default: silent.")
    print("     Exfiltration:S3/MaliciousIPCaller.Custom will NOT fire")
    print("     unless the source IP is on a threat list.")
    print("     Exfiltration:S3/ObjectRead.Unusual needs anomaly baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
