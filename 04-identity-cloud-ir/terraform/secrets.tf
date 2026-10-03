# secrets.tf
# Why: scenario 01 (OAuth token theft) needs something that looks and
# smells like a leaked OAuth refresh token. In the real breach pattern,
# an engineer commits a .env file to a public repo and an attacker greps
# GitHub for refresh-token-shaped strings. We model that with an SSM
# SecureString parameter the lab EC2 can read.
# How: one SecureString, tagged with the fake scope metadata so detection
# rules can reference "expected scope" vs "actual scope".

resource "aws_ssm_parameter" "fake_oauth_token" {
  name  = "/${local.name_prefix}/saas/northwind-drive-sync/refresh_token"
  type  = "SecureString"
  value = var.fake_oauth_refresh_token

  description = "Fake OAuth refresh token for lab scenario 01. Not a real token."

  tags = {
    SensitivityLabel = "secret"
    IntendedScopes   = "drive.readonly.file"
    ActualScopes     = "drive.readonly,admin.directory.user.readonly,mail.send"
  }
}

# Also stash the predictable external ID in SSM so scenario 02 can
# "discover" it the same way an attacker would (grep through parameter
# store once they have credentials).
resource "aws_ssm_parameter" "cross_account_external_id" {
  name  = "/${local.name_prefix}/ops/cross_account_external_id"
  type  = "String"
  value = var.cross_account_external_id

  description = "ExternalId for cross-account role. Should be rotated and secret. Lab leaves it discoverable on purpose."
}
