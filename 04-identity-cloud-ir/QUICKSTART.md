# Quickstart - Identity-First AWS Incident Response Lab

## 5-minute demo

BLUF. You will run `terraform plan` to confirm the lab builds cleanly, then run a detection rule against a sample CloudTrail event. The demo stops at `plan`. Running `apply` creates real AWS resources and real charges. Do that only in a sandboxed account you own.

Warning. `terraform apply` costs money. GuardDuty alone is roughly $4 per day. If you apply, run `./terraform/teardown.sh` the same day. For the 5-minute demo, stop at `plan`.

Prerequisites.

```bash
terraform version          # need 1.5 or newer
aws --version              # AWS CLI v2
aws sts get-caller-identity  # confirms your creds are loaded
python --version           # need 3.10 or newer
pip install boto3
```

Step 1 - setup.

```bash
cd 04-identity-cloud-ir/terraform
cp terraform.tfvars.example terraform.tfvars
terraform init
```

What you see. Terraform downloads the AWS provider and prints `Terraform has been successfully initialized!`. The `.terraform/` directory now exists.

Step 2 - run plan (not apply).

```bash
terraform plan
```

What you see. Terraform prints a diff and a final summary line close to `Plan: 15 to add, 0 to change, 0 to destroy`. The resource list includes a VPC, two IAM roles with intentional weaknesses, a GuardDuty detector, an S3 bucket with logging, Secrets Manager entries, and an EC2 instance. If the count is far off, the `.tfvars` file is missing values.

STOP HERE unless you are in a sandbox account. Running `apply` creates billable resources.

Step 3 - run a detection rule against sample CloudTrail JSON.

```bash
cd ../detections
python elastic_detection_rules/run_rule.py \
  --rule elastic_detection_rules/console_login_without_mfa.yml \
  --event ../attacks/sample_events/console_login_no_mfa.json
```

What you see. The rule evaluator loads the KQL-equivalent logic, feeds in the sample CloudTrail event, and prints a match. Something like:

```
MATCH: console_login_without_mfa
  user: attacker-persona-01
  sourceIP: 198.51.100.42
  mfaUsed: false
  severity: high
```

Step 3b - validate.

Run the same rule against a benign event to confirm it stays quiet.

```bash
python elastic_detection_rules/run_rule.py \
  --rule elastic_detection_rules/console_login_without_mfa.yml \
  --event ../attacks/sample_events/console_login_with_mfa.json
```

What you see. `NO MATCH`. The rule only fires on logins that lack MFA.

## What this proves

- Infrastructure-as-code lab that provisions real identity weaknesses safely and tears down cleanly.
- Custom Elastic rules that close named GuardDuty gaps, with the gap list documented in `detections/detection_matrix.md`.
- A Scattered Spider tabletop in `tabletop/` that ties attack paths to detection coverage, not just a checklist.

## Add screenshots here

Capture these while running the demo and drop them in a `screenshots/` folder next to this file.

- `screenshots/01-terraform-init.png` - init success
- `screenshots/02-terraform-plan-summary.png` - the `Plan: 15 to add` line
- `screenshots/03-rule-match.png` - detection rule firing on the no-MFA event
- `screenshots/04-rule-no-match.png` - same rule staying quiet on the MFA-enabled event
- `screenshots/05-detection-matrix.png` - `detection_matrix.md` open showing GuardDuty vs custom coverage

## Common issues

- `Error: No valid credential sources`. The AWS CLI is not configured for this shell. Run `aws configure` or export `AWS_PROFILE`.
- `terraform plan` prints `Error: Invalid value for variable`. The `.tfvars` file still has placeholder values. Fill them in or set them with `-var`.
- You accidentally ran `apply`. Run `./terraform/teardown.sh` right now. Confirm with `terraform state list` returning empty, then check the AWS console for lingering GuardDuty detectors and NAT gateways. Those are the two that keep billing after a bad teardown.
