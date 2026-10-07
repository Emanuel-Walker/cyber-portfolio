# Quickstart - Identity-First AWS Incident Response Lab

## Plain English

This project tests identity-focused cloud attacks and the detections that should catch them.

The first demo is **offline and free**.

You do not need an AWS account to run it.

## 5-minute offline demo

### 1. Enter the project

From the portfolio root:

```bash
cd 04-identity-cloud-ir
```

### 2. Run the IAM detection against a suspicious event

```bash
python3 detections/demo_iam_detection.py \
  attacks/demo_events/create_access_key.json
```

Expected:

```text
MATCH: IAM persistence / privilege-change detection
```

This event simulates an IAM access key being created.

### 3. Run the same logic against normal activity

```bash
python3 detections/demo_iam_detection.py \
  attacks/demo_events/list_buckets.json
```

Expected:

```text
NO MATCH
```

**PASS:** one event fires and the benign example stays quiet.

The demo script mirrors the core conditions from:

```text
detections/elastic_detection_rules/iam_access_key_creation.yml
```

It is intentionally not a general KQL engine.

## Optional: inspect the real AWS plan

Only do this in an AWS account you own or are authorized to use.

You need:
- Terraform 1.5+
- AWS CLI v2
- working AWS credentials

Check:

```bash
terraform version
aws --version
aws sts get-caller-identity
```

**STOP:** if the last command shows the wrong AWS account.

Then:

```bash
cp terraform/terraform.tfvars.example terraform/terraform.tfvars
```

Open:

```text
terraform/terraform.tfvars
```

Replace:

```text
you@example.com
```

with your email.

For a **plan-only** review, you can leave the example CIDR in place.

Before a real apply, replace it with your authorized source CIDR.

Run:

```bash
terraform -chdir=terraform init
terraform -chdir=terraform plan
```

**PASS:** Terraform produces a plan without creating resources.

## Do not apply casually

```text
terraform apply
```

creates real AWS resources and can create charges.

If you intentionally deploy the full lab, follow the project README and run the teardown script when finished:

```bash
./terraform/teardown.sh
```

Then verify the AWS console is clean.

## What this proves

- the project models identity-focused AWS detection gaps
- the custom rules can express behavior GuardDuty may not alert on by default
- the infrastructure is reproducible with Terraform
- the lab includes explicit teardown and safety boundaries

## What this does not prove

The offline demo does not prove GuardDuty behavior.

That comparison requires the real disposable AWS lab.

See:

```text
detections/detection_matrix.md
```

for the documented lab results.
