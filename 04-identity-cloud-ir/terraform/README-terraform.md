# Terraform - deploy and destroy

## Prerequisites

- Terraform 1.5 or newer
- AWS CLI v2 with credentials that can create IAM, EC2, S3, SSM, CloudTrail, GuardDuty
- Region default is `us-east-1`. Override in `terraform.tfvars`.

## Deploy

```bash
cp terraform.tfvars.example terraform.tfvars
# edit terraform.tfvars with your /32 and email
terraform init
terraform plan
terraform apply
```

Apply takes about 90 seconds. The last output block tells you exactly what to run next.

## Destroy

Preferred:

```bash
./teardown.sh
```

The script runs `terraform destroy -auto-approve` and then post-checks for lingering S3 buckets, SSM parameters, and GuardDuty detectors.

Manual fallback if the script hits an issue:

```bash
terraform destroy -auto-approve
aws s3 rb s3://<bucket> --force     # for any bucket the destroy skipped
aws guardduty delete-detector --detector-id <id>
```

## Cost warning

| Resource | Daily cost if left running |
|---|---|
| GuardDuty detector (default + S3 Protection) | ~$1 to $3 |
| CloudTrail S3 data events | ~$0.10 (lab volume) |
| EC2 t3.micro | ~$0.25 |
| S3 storage (20 tiny objects) | ~$0.00 |
| CloudWatch Logs (VPC Flow) | ~$0.05 |

End to end a full-day run is under **$5**. A quick deploy-attack-destroy cycle is under **$1**.

## Region defaults

`us-east-1` is cheapest for GuardDuty and has the fastest CloudTrail event propagation. If you must use another region, override:

```hcl
# terraform.tfvars
region = "us-west-2"
```

## Known good versions

- Terraform: 1.9.x
- AWS provider: 5.60+
- AWS CLI: 2.17+
