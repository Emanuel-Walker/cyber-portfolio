# Scenario 05 - GuardDuty silent IAM

**Pattern:** Scattered Spider "stay resident" moves. Each action is step 1 of a real breach. None of them fire default GuardDuty.

## What it does

1. Creates a victim IAM user (lab setup).
2. `CreateAccessKey` for the victim.
3. `AttachUserPolicy` of a managed policy (stand-in for AdministratorAccess, we use ReadOnlyAccess for safety).
4. `GetAccountPasswordPolicy` (recon toward weakening).
5. Cleans up: deletes key, detaches policy, deletes user.

## GuardDuty expectation

**All three silent on default.** Even with all protection plans on, the only one that may fire is `Policy:IAMUser/RootCredentialUsage` and only if root is used, which this scenario does not do.

This is the detection gap that matters most. Writing the rule is 30 lines of Python.

## Detection

- Elastic: `iam_access_key_creation.yml`
- Panther: `iam_access_key_creation.py`
- Athena: query 5

## Run

```bash
./run.sh
```
