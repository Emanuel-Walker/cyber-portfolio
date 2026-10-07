# Terraform

This folder creates the disposable AWS lab.

## Safe first step

From the project root:

```bash
terraform -chdir=terraform init
terraform -chdir=terraform plan
```

Review the plan before apply.

## Before apply

Verify:

```bash
aws sts get-caller-identity
```

Then confirm:
- correct account
- lab-only environment
- budget exists
- source CIDR is intentional
- teardown path is understood

## Cleanup

Use:

```bash
./terraform/teardown.sh
```

Then verify the AWS console.

A successful destroy command is not a substitute for checking that billable resources are gone.
