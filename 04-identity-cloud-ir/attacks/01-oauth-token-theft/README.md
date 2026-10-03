# Scenario 01 - OAuth token theft

**Pattern:** 2024 Snowflake customer breaches, Okta customer token theft, generic SaaS compromise through leaked `.env` files.

## What it does

1. Pulls a fake OAuth refresh token out of SSM (models "token leaked in a public commit").
2. Mints an access key for the OAuth-app-shaped IAM user (models "exchange refresh for access").
3. Uses the stolen identity to call `iam:ListUsers`, which is outside the app's intended scope.

## CloudTrail events generated

- `ssm:GetParameter` against the fake-token parameter
- `iam:CreateAccessKey` for `northwind-cloud-lab-saas-connector`
- `iam:ListUsers` with the OAuth-app user as the actor

## GuardDuty expectation

None of these generate a default GuardDuty finding. The paid plan with Lambda/EKS/Malware Protection does not help either. Custom detection required.

## Detection

- Elastic: `detections/elastic_detection_rules/oauth_token_abuse.yml`
- Panther: `detections/panther_rules/oauth_token_abuse.py`
- Athena: query 1 in `detections/cloudtrail_hunting_queries.sql`

## Run

```bash
./run.sh
```
