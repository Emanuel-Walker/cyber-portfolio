# Identity-First AWS Incident Response Lab

Every cloud breach in 2026 looks the same. No malware. No ransomware payload. No shellcode on disk. Just a stolen OAuth refresh token (a long-lived credential an app uses to get fresh access tokens without re-prompting the user), a non-human identity (service account, API key, or workload credential, often shortened to NHI) with too much power, and gigabytes of customer data walking out through a legitimate API call. GuardDuty (AWS's built-in threat detection service that reads CloudTrail and VPC flow logs) watches it happen and stays quiet.

This lab proves it. Then it ships the detections that catch it.

## What it does

- Builds a deliberately weak AWS tenant with Terraform (infrastructure-as-code tool. You describe cloud resources in HCL files, Terraform makes them exist). Includes an over-privileged IAM role, OAuth app with excess scopes, cross-account trust with a weak condition, and misconfigured S3 lifecycle.
- Runs 5 attacker scenarios drawn from real 2024-2026 breach patterns (Scattered Spider, Snowflake customer compromises, Okta token theft).
- Shows exactly what GuardDuty catches, what it misses, and names the finding types involved.
- Ships custom detections in Elastic and Panther, with a coverage matrix that compares those results against native GuardDuty behavior.
- Includes a tabletop exercise good enough to run with an actual SOC team.

## Quick start

```bash
cd terraform
cp terraform.tfvars.example terraform.tfvars   # edit region, email, etc.
terraform init && terraform apply              # ~2 minutes
cd ../attacks/01-oauth-token-theft && ./run.sh # run each scenario in order
```

When done, from the project root:

```bash
./terraform/teardown.sh
```

## How it works

Terraform stands up a small VPC, a single EC2 with an instance profile, an S3 bucket holding fake "customer data", an SSM parameter holding a fake OAuth refresh token, and an IAM role with scopes no production app should ever hold. GuardDuty is turned on with default protection plans.

Each attack script in `attacks/` uses boto3 to simulate the attacker side. Each script writes a short note to stdout about which CloudTrail events it generated and which detection rule should fire.

Diagram: `diagrams/lab_architecture.drawio`. Full writeup: `WRITEUP.md`.

## What I learned

GuardDuty is useful. It is not sufficient. The findings I expected to fire did not. Three honest surprises:

1. **`CreateAccessKey` on an existing IAM user does not generate a GuardDuty finding of its own.** It is one of the oldest moves in the Scattered Spider playbook and it is silent by default. You have to write the detection yourself or buy a tool that does.
2. **`AssumeRole` from a stolen session token looks identical to a legitimate assume-role until you correlate ASN, user-agent, and prior session geography.** None of that correlation happens in GuardDuty default.
3. **S3 data exfiltration via `GetObject` loops under a normal baseline rate does not fire `Exfiltration:S3/MaliciousIPCaller.Custom` unless the source IP is on a known-bad list.** Low-and-slow pulls from a clean VPS stay invisible.

The detection matrix in `detections/detection_matrix.md` lays out every attack scenario against the tested coverage, honestly.

## What's next

- Add Okta log integration (right now the OAuth scenario is modeled through AWS SSM instead of a real Okta tenant).
- Port the Elastic rules to Sigma generic.
- Add a Lambda-based auto-remediation playbook for scenario 05.
- Record a 10-minute Loom walkthrough.

## Cost note

Running everything above costs about **$2 to $5 end to end** if you tear down the same day. The pricey items are GuardDuty (prorated per account per hour, cheap for a few hours) and CloudTrail data events on S3 (penny-level for this volume). EC2 is a `t3.micro`.

**If you leave it running:** GuardDuty with S3 Protection + Malware Protection runs roughly $1 to $3 per day on an empty account. Not catastrophic, but not free either.

**Teardown:**

```bash
./terraform/teardown.sh
```

That script runs `terraform destroy -auto-approve` and then double-checks that the S3 bucket, SSM parameter, and GuardDuty detector are actually gone. Costs under $5 end to end if you don't forget to destroy.

## Repo layout

```
terraform/          infra as code, deploy and teardown
attacks/            5 boto3 scenarios, each with run.sh + README
detections/         Athena SQL, Elastic .yml, Panther Python, coverage matrix
tabletop/           Scattered Spider walkthrough for real teams
diagrams/           draw.io source for all 3 diagrams
WRITEUP.md          long-form writeup, read this one
```

## Safety

Every attack script only works against the lab Terraform builds. The scripts hardcode a check for resources tagged `Project=northwind-cloud` and refuse to run otherwise. Do not point them at anything you do not own.
