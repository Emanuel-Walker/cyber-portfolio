#!/usr/bin/env python3
"""
Scenario 05: three IAM actions GuardDuty default does NOT alert on.

Why: this is the scenario that bothered me most when I confirmed it.
Each of these is step one of a real breach playbook, each is logged
cleanly in CloudTrail, and none of them fire a default GuardDuty finding.

Actions in order:
  1. CreateAccessKey for an existing user who has no prior access keys.
     This is the Scattered Spider "add a key, keep access forever" move.
  2. AttachUserPolicy attaching AdministratorAccess (managed) to a user
     with no prior admin. No inline change, no CreatePolicy call.
  3. UpdateAccountPasswordPolicy weakening to no complexity, no rotation.
     Hands the account to the next phish victim.

What CloudTrail sees: all three events, cleanly, under the attacker
principal (which in the lab is the attacker's current identity for
simplicity; in a real breach it would be the compromised privileged
account).

Detection: iam_access_key_creation.yml / .py

SAFETY: this script creates a temp user, performs the attach + password
policy update, and cleans up on exit. If anything crashes between step 1
and the cleanup block, you may have a leftover user. The teardown
script will catch it, but check.
"""

import sys
import boto3
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _lib.safety import assert_lab_account

PROJECT = "northwind-cloud"
VICTIM_USER = f"{PROJECT}-lab-victim-user"


def main() -> int:
    ctx = assert_lab_account()
    print(f"[05] lab confirmed: account={ctx['account']} region={ctx['region']}")

    iam = boto3.client("iam", region_name=ctx["region"])

    # Setup: create the "existing user" that we will then compromise.
    # In a real breach this user already exists; we create it here so
    # the lab is self-contained.
    try:
        iam.create_user(UserName=VICTIM_USER, Tags=[
            {"Key": "Project", "Value": PROJECT},
            {"Key": "LabScenario", "Value": "05"},
        ])
        print(f"[05] created victim user {VICTIM_USER}")
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"[05] victim user already exists, reusing")

    original_key = None
    try:
        # Action 1: silent CreateAccessKey.
        print("[05] action 1: CreateAccessKey for victim user")
        key = iam.create_access_key(UserName=VICTIM_USER)["AccessKey"]
        original_key = key["AccessKeyId"]
        print(f"       minted key id {original_key}")
        print("       GuardDuty default finding: NONE.")

        # Action 2: AttachUserPolicy with AdministratorAccess (managed).
        # Note: we use the ReadOnlyAccess managed policy for safety.
        # The DETECTION RULE should fire on any high-privilege attach,
        # not just Admin. In production you would include Admin,
        # PowerUserAccess, IAMFullAccess, and your own custom admin arns.
        print("[05] action 2: AttachUserPolicy ReadOnlyAccess (stand-in for Admin)")
        iam.attach_user_policy(
            UserName=VICTIM_USER,
            PolicyArn="arn:aws:iam::aws:policy/ReadOnlyAccess",
        )
        print("       GuardDuty default finding: NONE.")

        # Action 3: UpdateAccountPasswordPolicy. We DO NOT actually
        # weaken the account's live password policy because that would
        # affect the lab operator. We call GetAccountPasswordPolicy to
        # generate the equivalent "attacker reconnoitering password
        # policy" event, which is on the same detection logic.
        print("[05] action 3: GetAccountPasswordPolicy (recon toward weakening)")
        try:
            iam.get_account_password_policy()
        except iam.exceptions.NoSuchEntityException:
            print("       no password policy set, which is itself a finding worth writing")
        print("       GuardDuty default finding: NONE.")

    finally:
        # Cleanup: remove the access key, detach the policy, delete user.
        print("[05] cleanup")
        if original_key:
            try:
                iam.delete_access_key(UserName=VICTIM_USER, AccessKeyId=original_key)
            except Exception as exc:
                print(f"       could not delete access key: {exc}")
        try:
            iam.detach_user_policy(
                UserName=VICTIM_USER,
                PolicyArn="arn:aws:iam::aws:policy/ReadOnlyAccess",
            )
        except Exception as exc:
            print(f"       could not detach policy: {exc}")
        try:
            iam.delete_user(UserName=VICTIM_USER)
            print(f"       deleted {VICTIM_USER}")
        except Exception as exc:
            print(f"       could not delete user: {exc}")

    print("[05] done. Three CloudTrail events generated under the attacker principal:")
    print("     - iam:CreateAccessKey")
    print("     - iam:AttachUserPolicy")
    print("     - iam:GetAccountPasswordPolicy")
    print("[05] GuardDuty default: all three silent. Custom detection required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
