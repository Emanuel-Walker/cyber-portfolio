# main.tf
# Why: single entry point. Terraform discovers all .tf files in the dir,
# but keeping an explicit "orchestrator" file makes the deploy order and
# cross-file dependencies readable at a glance.
# How: provider, required_providers, data sources, common locals, tags.

terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.5"
    }
  }
}

provider "aws" {
  region = var.region

  default_tags {
    tags = local.common_tags
  }
}

# Why: attack scripts use these tags to confirm they are hitting the lab
# and nothing else. If someone copies a script and points it elsewhere,
# the tag check fails.
locals {
  common_tags = {
    Project     = var.project
    Environment = var.environment
    Owner       = var.owner_email
    ManagedBy   = "terraform"
    Purpose     = "identity-first-ir-lab"
  }
  name_prefix = "${var.project}-${var.environment}"
}

# Random suffix so S3 bucket names are globally unique even if someone
# else deploys this lab. S3 does not care that you own the account.
resource "random_id" "suffix" {
  byte_length = 4
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
