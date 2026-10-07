# Identity-First AWS Incident Response Lab

## Plain English

Many cloud incidents involve stolen credentials, over-privileged identities, or legitimate API calls used for the wrong purpose.

Those behaviors can be harder to spot than malware on a host.

This project builds a disposable AWS lab to test that problem.

## What I built

The lab includes:

- Terraform infrastructure
- intentional IAM and identity weaknesses
- five controlled attack scenarios
- AWS CloudTrail telemetry
- GuardDuty comparison testing
- custom Elastic detections
- custom Panther detections
- a detection coverage matrix
- a Scattered Spider tabletop exercise
- teardown automation

All example names and data are synthetic.

## Try it safely

Start with:

```text
QUICKSTART.md
```

The first demo is offline and free.

It runs one custom IAM detection against:
- a suspicious synthetic event
- a benign synthetic event

You do not need an AWS account for that demo.

## Full lab architecture

Terraform creates a small AWS environment with:
- IAM identities and roles
- an EC2 target
- an S3 bucket with fake customer data
- a fake token stored in AWS Systems Manager Parameter Store
- GuardDuty
- CloudTrail

The attack scenarios generate controlled cloud activity against those lab resources.

The detection matrix records what the tested controls saw.

## The five scenarios

See:

```text
attacks/
```

The scenarios cover identity and credential behaviors such as:
- token access
- privilege changes
- cross-account/session anomalies
- S3 access patterns
- IAM persistence actions

Attack scripts include lab-scope checks.

Do not point them at systems you do not own or have authorization to test.

## Detection coverage

Verified public detection implementations include:

```text
detections/elastic_detection_rules/
detections/panther_rules/
```

The comparison results are documented in:

```text
detections/detection_matrix.md
```

That document separates:
- catch
- partial
- miss

instead of treating every native alert as guaranteed coverage.

## GuardDuty lesson

Native cloud detections are useful.

They are not a substitute for environment-specific detection engineering.

Some behaviors depend on:
- anomaly baselines
- source reputation
- enabled protection plans
- event context

That is why the project compares native findings with custom rules.

## Cost and teardown

The offline demo costs nothing.

The real AWS lab creates billable resources.

Cost varies by:
- region
- how long the lab runs
- enabled GuardDuty features
- event volume

Before deployment:
- use an AWS account you own
- create a budget
- confirm your current AWS identity

When finished:

```bash
./terraform/teardown.sh
```

Then verify the AWS console is clean.

## What this proves

- Terraform can make the lab repeatable
- controlled attack scenarios can generate identity-focused telemetry
- custom rules can cover behaviors not reliably surfaced by native findings alone
- teardown and scope checks can be part of the lab design

## What this does not prove

It does not prove:
- GuardDuty never detects the documented behaviors
- one lab result applies to every AWS account
- the custom detections are production-tuned for another organization

Cloud detections depend on configuration, baseline, telemetry, and environment.

## Where to go next

```text
QUICKSTART.md
detections/detection_matrix.md
tabletop/
WRITEUP.md
```
