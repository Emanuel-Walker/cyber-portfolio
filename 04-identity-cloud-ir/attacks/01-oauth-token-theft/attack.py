#!/usr/bin/env python3
"""
Scenario 01: OAuth token theft.

Why: in the real pattern, an engineer commits a .env file to a public
GitHub repo. The file contains a long-lived OAuth refresh token for a
SaaS app with excess scopes. An attacker greps the file, exchanges the
refresh token, and starts calling SaaS APIs under the app identity.

We model this in AWS because standing up a real Okta tenant for a lab
doubles the cost. The SHAPE is identical:
  - fetch a long-lived credential from "a public place" (the SSM param)
  - use that credential to call APIs the app has excess scope for
  - leave a CloudTrail audit trail that LOOKS legitimate

What CloudTrail sees:
  - ssm:GetParameter against the fake-oauth-token param  (the "theft")
  - iam:CreateAccessKey against the oauth-app user       (minting creds)
  - iam:ListUsers / iam:GetUser                           (excess scope abuse)

Detection: see detections/elastic_detection_rules/oauth_token_abuse.yml
and detections/panther_rules/oauth_token_abuse.py.

SAFETY: refuses to run outside the lab (see _lib/safety.py).
"""

import sys
import time
import boto3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.safety import assert_lab_account

PROJECT = "northwind-cloud"
PARAM_NAME = f"/{PROJECT}-lab/saas/northwind-drive-sync/refresh_token"
OAUTH_USER = f"{PROJECT}-lab-saas-connector"


def main() -> int:
    ctx = assert_lab_account()
    print(f"[01] lab confirmed: account={ctx['account']} region={ctx['region']}")

    ssm = boto3.client("ssm", region_name=ctx["region"])
    iam = boto3.client("iam", region_name=ctx["region"])

    # Step 1: "theft". Pull the token from SSM. In the real breach this
    # is the git-grep moment. In our lab it is a GetParameter call.
    print("[01] fetching fake OAuth refresh token from SSM")
    token = ssm.get_parameter(Name=PARAM_NAME, WithDecryption=True)["Parameter"]["Value"]
    print(f"[01] token prefix: {token[:14]}... (truncated)")

    # Step 2: convert the long-lived token into short-lived usable creds.
    # In the real Okta/Google flow this is a refresh exchange. Our AWS
    # analog is CreateAccessKey on the user that represents the app.
    # This is a REAL IAM action that CloudTrail records.
    print(f"[01] minting new access key for {OAUTH_USER}")
    key = iam.create_access_key(UserName=OAUTH_USER)["AccessKey"]
    print(f"[01] got key id {key['AccessKeyId']}")

    # Step 3: use the stolen identity. Call something the OAuth app has
    # excess scope for. IAM ListUsers is the "list all people in the
    # tenant" equivalent to admin.directory.user.readonly.
    print("[01] using stolen identity to call iam:ListUsers (excess scope)")
    stolen = boto3.Session(
        aws_access_key_id=key["AccessKeyId"],
        aws_secret_access_key=key["SecretAccessKey"],
        region_name=ctx["region"],
    )
    # Brief pause so IAM eventual consistency does not reject the first call.
    time.sleep(8)
    users = stolen.client("iam").list_users()["Users"]
    print(f"[01] listed {len(users)} IAM users under stolen identity")

    print("[01] done. Expected CloudTrail events:")
    print("     - ssm:GetParameter on", PARAM_NAME)
    print("     - iam:CreateAccessKey userName=", OAUTH_USER)
    print("     - iam:ListUsers (sourceIdentity will be", OAUTH_USER, ")")
    print("[01] expected GuardDuty: NO default finding fires on any of these.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
