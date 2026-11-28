# variables.tf
# Why: every lab should be redeployable without editing .tf files.
# How: all tunables live here, defaults are sensible for a solo lab, overrides
# go in terraform.tfvars (which is gitignored).

variable "region" {
  description = "AWS region to deploy into. us-east-1 is cheapest for GuardDuty + CloudTrail."
  type        = string
  default     = "us-east-1"
}

variable "project" {
  description = "Project tag. Attack scripts refuse to run against anything not tagged this value."
  type        = string
  default     = "northwind-cloud"
}

variable "environment" {
  description = "Environment tag. Lab-only. Do not change to prod."
  type        = string
  default     = "lab"
}

variable "owner_email" {
  description = "Email tagged on all resources so you know who to yell at if it's left running."
  type        = string
}

variable "notify_sns_topic_arn" {
  description = "Optional SNS topic for GuardDuty findings. Empty disables."
  type        = string
  default     = ""
}

variable "allowed_source_cidr" {
  description = "Source CIDR allowed to SSM/SSH into the EC2. Default is a non-routable placeholder, override to your /32."
  type        = string
  default     = "198.51.100.0/32"
}

variable "fake_oauth_refresh_token" {
  description = "Fake OAuth refresh token for the SSM parameter. Do not use a real one. Default is a clearly fake string."
  type        = string
  default     = "1//0f-FAKE-REFRESH-TOKEN-northwind-lab-DO-NOT-TRUST-abcd1234"
  sensitive   = true
}

variable "cross_account_external_id" {
  description = "ExternalId used in the deliberately weak cross-account trust. Predictable on purpose."
  type        = string
  default     = "northwind-prod-2026"
}
