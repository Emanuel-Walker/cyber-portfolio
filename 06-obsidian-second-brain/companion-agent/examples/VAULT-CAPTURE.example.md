# Vault Capture Example

```text
VAULT CAPTURE

Type:
Project update

Suggested destination:
03-Projects/AWS Lab.md

Summary:
The lab is ready to plan but should not be applied until the AWS budget and CLI identity are verified.

Facts to preserve:
- Terraform is installed
- AWS CLI is installed
- Budget still needs confirmation

Next action:
Run aws sts get-caller-identity and verify the account.

Questions / uncertainty:
Need to confirm which AWS profile should be used.
```

Give this block to the Vault Agent.

The Vault Agent should show the proposed file change before writing it.
