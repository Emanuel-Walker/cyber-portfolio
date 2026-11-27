# outputs.tf
# Why: after terraform apply, print the handful of ARNs and names the
# attack scripts need. Saves everyone 5 minutes of grep.

output "project_tag" {
  value       = var.project
  description = "Tag every attack script checks before running."
}

output "ec2_instance_id" {
  value       = aws_instance.lab.id
  description = "The lab EC2 host. Pivot target for scenario 02."
}

output "ec2_public_ip" {
  value       = aws_instance.lab.public_ip
  description = "Public IP of the lab EC2."
}

output "over_privileged_role_arn" {
  value       = aws_iam_role.data_pipeline.arn
  description = "The NHI role scenario 02 escalates with."
}

output "oauth_app_user_name" {
  value       = aws_iam_user.oauth_app.name
  description = "The OAuth-app-shaped IAM user scenario 01 attacks."
}

output "cross_account_role_arn" {
  value       = aws_iam_role.cross_account.arn
  description = "Cross-account role with weak ExternalId condition."
}

output "cross_account_external_id_param" {
  value       = aws_ssm_parameter.cross_account_external_id.name
  description = "SSM parameter where the ExternalId is discoverable (bad)."
}

output "customer_data_bucket" {
  value       = aws_s3_bucket.customer_data.id
  description = "The exfil target for scenario 04."
}

output "fake_oauth_token_param" {
  value       = aws_ssm_parameter.fake_oauth_token.name
  description = "SSM parameter path for the fake OAuth refresh token."
}

output "cloudtrail_bucket" {
  value       = aws_s3_bucket.trail.id
  description = "CloudTrail destination bucket. Point Athena here."
}

output "guardduty_detector_id" {
  value       = aws_guardduty_detector.lab.id
  description = "GuardDuty detector ID. Watch for findings here."
}

output "what_to_do_next" {
  value = <<-EOT

    Lab is up. To run the scenarios in order:

      cd ../attacks/01-oauth-token-theft && ./run.sh
      cd ../attacks/02-nhi-privilege-escalation && ./run.sh
      cd ../attacks/03-cross-tenant-session-anomaly && ./run.sh
      cd ../attacks/04-saas-to-s3-exfiltration && ./run.sh
      cd ../attacks/05-guardduty-silent-iam && ./run.sh

    Watch for GuardDuty findings in the console or:
      aws guardduty list-findings --detector-id ${aws_guardduty_detector.lab.id}

    When done, from project root:
      ./terraform/teardown.sh
  EOT
  description = "Operator next steps."
}
