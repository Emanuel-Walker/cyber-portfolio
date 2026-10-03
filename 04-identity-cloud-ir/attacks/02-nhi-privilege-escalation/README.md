# Scenario 02 - NHI privilege escalation

**Pattern:** classic `iam:PassRole` abuse chain. Still works in 2026 because engineers keep writing wildcard IAM.

## What it does

1. Assumes the over-privileged `data-pipeline` role.
2. Enumerates roles and picks the cross-account reader as the escalation target.
3. Discovers the ExternalId from SSM (it was left there to be discoverable).
4. Assumes the cross-account role.

## CloudTrail events

- `sts:AssumeRole` into `data-pipeline`
- `ssm:GetParameter` for `cross_account_external_id`
- `sts:AssumeRole` into `cross-account-reader` with ExternalId

## GuardDuty expectation

Default: silent. With anomaly detection and enough baseline history, `PrivilegeEscalation:IAMUser/AnomalousBehavior` can fire.

## Detection

- Elastic: `nhi_privesc_passrole.yml`
- Panther: `nhi_privesc_passrole.py`
- Athena: query 2

## Run

```bash
./run.sh
```
