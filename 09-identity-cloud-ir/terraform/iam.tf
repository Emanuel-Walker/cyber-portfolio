# iam.tf
# Why: this file is where the lab is deliberately broken. Every bad pattern
# here is one I have seen in real production environments. Nothing is a
# strawman. Read the comments if you want to see why each one is bad.
# How: four pieces. EC2 instance role (reasonable). Over-privileged NHI
# role (bad). OAuth-app-shaped IAM user (bad shape). Cross-account trust
# role (weak condition).

# -----------------------------------------------------------------------
# 1. EC2 instance role. This one is reasonable. It lets the EC2 host
# use SSM for shell access and read the fake-token SSM parameter.
# -----------------------------------------------------------------------

resource "aws_iam_role" "ec2" {
  name = "${local.name_prefix}-ec2-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy_attachment" "ec2_ssm_core" {
  role       = aws_iam_role.ec2.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

resource "aws_iam_role_policy" "ec2_read_ssm_param" {
  name = "read-oauth-token"
  role = aws_iam_role.ec2.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = ["ssm:GetParameter", "ssm:GetParameters"]
      # Scoped to one parameter. This part is actually good.
      Resource = aws_ssm_parameter.fake_oauth_token.arn
    }]
  })
}

resource "aws_iam_instance_profile" "ec2" {
  name = "${local.name_prefix}-ec2-profile"
  role = aws_iam_role.ec2.name
}

# -----------------------------------------------------------------------
# 2. The over-privileged NHI. Named like a data pipeline role because
# this exact pattern shows up on data engineering teams. iam:PassRole on
# wildcard is the single most abused IAM privilege in cloud breaches.
# -----------------------------------------------------------------------

resource "aws_iam_role" "data_pipeline" {
  name = "${local.name_prefix}-data-pipeline"

  # Assume policy allows the EC2 role to assume it. In a real breach,
  # the attacker lands on the EC2 host and pivots.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { AWS = aws_iam_role.ec2.arn }
      Action = "sts:AssumeRole"
    }]
  })
}

resource "aws_iam_role_policy" "data_pipeline_too_much" {
  name = "data-pipeline-too-much"
  role = aws_iam_role.data_pipeline.id

  # Why this is bad, one line each:
  # - iam:PassRole on * means attacker can hand ANY role to a Lambda they create.
  # - lambda:* and s3:* on * means they can create the Lambda and read your buckets.
  # - sts:AssumeRole on * means they can jump to any role in any account the trust allows.
  # - secretsmanager:GetSecretValue on * means they walk your secrets.
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Action = [
        "iam:PassRole",
        "lambda:CreateFunction",
        "lambda:UpdateFunctionCode",
        "lambda:InvokeFunction",
        "s3:GetObject",
        "s3:ListBucket",
        "sts:AssumeRole",
        "secretsmanager:GetSecretValue"
      ]
      Resource = "*"
    }]
  })
}

# -----------------------------------------------------------------------
# 3. OAuth-app-shaped IAM user. We model a SaaS OAuth app as an IAM user
# because this lab is AWS-only. The point is the SHAPE: a non-human
# identity with programmatic access and more scopes than it needs.
# -----------------------------------------------------------------------

resource "aws_iam_user" "oauth_app" {
  name = "${local.name_prefix}-saas-connector"

  tags = {
    IdentityType = "non-human"
    AppName      = "northwind-drive-sync"
    # These "scopes" are metadata, not AWS-enforced. We use them later
    # in detection rules to show what the identity SHOULD have been
    # scoped to vs what it was actually granted.
    IntendedScopes = "drive.readonly.file"
    ActualScopes   = "drive.readonly,admin.directory.user.readonly,mail.send"
  }
}

resource "aws_iam_user_policy" "oauth_app_excess" {
  name = "oauth-excess-scope"
  user = aws_iam_user.oauth_app.name

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = ["s3:GetObject", "s3:ListBucket"]
        Resource = [aws_s3_bucket.customer_data.arn, "${aws_s3_bucket.customer_data.arn}/*"]
      },
      {
        # The excess. OAuth app for "sync files" does not need to read
        # IAM users. This is the detection fodder.
        Effect   = "Allow"
        Action   = ["iam:ListUsers", "iam:GetUser"]
        Resource = "*"
      }
    ]
  })
}

# NOTE: we do not create an access key via Terraform. The attack scripts
# create one at runtime, which is itself a scenario (CreateAccessKey is
# silent to default GuardDuty).

# -----------------------------------------------------------------------
# 4. Cross-account trust with weak condition. The classic.
# -----------------------------------------------------------------------

resource "aws_iam_role" "cross_account" {
  name = "${local.name_prefix}-cross-account-reader"

  # Weakness: the trust allows the SAME account (self-trust for lab
  # purposes), but the policy shape mirrors what a real two-account
  # trust looks like. ExternalId is PREDICTABLE (lives in variables,
  # defaults to a guessable value). In the real version this is the
  # "I rotated out the external ID in Jira three years ago and never
  # updated the trust policy" bug.
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect = "Allow"
      Principal = { AWS = "arn:aws:iam::${data.aws_caller_identity.current.account_id}:root" }
      Action = "sts:AssumeRole"
      Condition = {
        StringEquals = {
          "sts:ExternalId" = var.cross_account_external_id
        }
      }
    }]
  })
}

resource "aws_iam_role_policy_attachment" "cross_account_readonly" {
  role       = aws_iam_role.cross_account.name
  policy_arn = "arn:aws:iam::aws:policy/ReadOnlyAccess"
}
