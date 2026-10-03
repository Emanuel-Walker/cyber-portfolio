# Scenario 04 - SaaS-to-S3 exfiltration

**Pattern:** 2024 Snowflake customer breaches. Legitimate credentials, legitimate API, data walks out.

## What it does

Assumes the pipeline role and loops `GetObject` across all customer-data objects 10 times to produce 200 total GetObject events. Rate-limited to look like a normal batch job.

## CloudTrail events

- 200 `s3:GetObject` events on the customer-data bucket, under the pipeline role

## GuardDuty expectation

Silent on default. `Exfiltration:S3/MaliciousIPCaller.Custom` only fires if the source IP is on a threat list. `Exfiltration:S3/ObjectRead.Unusual` needs 7+ days of anomaly baseline and the volume to be an outlier against that baseline. 200 small objects in a fresh account will not trigger it.

## Detection

- Elastic: `saas_exfil_api_pattern.yml`
- Panther: `saas_exfil_api_pattern.py`
- Athena: query 4

## Run

```bash
./run.sh
```
