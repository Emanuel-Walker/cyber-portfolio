# Scenario 03 - Cross-tenant session anomaly

**Pattern:** Scattered Spider post-help-desk-reset login from residential proxy or commercial VPS. Nothing individually bad. The combo is bad.

## What it does

Assumes the pipeline role with a user-agent string that signals "this is not our normal fleet" and runs harmless-looking enumeration.

In a real environment the detection also correlates:
- Source IP ASN (datacenter vs residential vs corporate)
- Geographic distance from last session for same principal
- Time of day vs principal's historical pattern

## CloudTrail events

- `sts:AssumeRole` with the attacker UA
- `iam:ListRoles`, `s3:ListBuckets`, `sts:GetCallerIdentity` with the same UA

## GuardDuty expectation

Silent on default. Not a known-bad IP, not a Tor exit.

## Detection

- Elastic: `cross_tenant_session_anomaly.yml`
- Panther: `cross_tenant_session_anomaly.py`
- Athena: query 3

## Run

```bash
./run.sh
```
