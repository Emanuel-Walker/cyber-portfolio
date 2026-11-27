# storage.tf
# Why: scenario 04 is S3 exfiltration. We need a bucket with some fake
# "customer data" and a lifecycle config that lets exfil look like normal
# access patterns. Also enable CloudTrail S3 data events because this is
# NOT the AWS default and is one of the honest gaps the writeup calls out.
# How: bucket + 200 small text objects + CloudTrail with data events on.

resource "aws_s3_bucket" "customer_data" {
  bucket        = "${local.name_prefix}-customer-data-${random_id.suffix.hex}"
  force_destroy = true

  tags = { Name = "${local.name_prefix}-customer-data" }
}

# Block Public Access ON. This is good hygiene. We are not using "public
# bucket" as the weakness here; the weakness is identity.
resource "aws_s3_bucket_public_access_block" "customer_data" {
  bucket                  = aws_s3_bucket.customer_data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "customer_data" {
  bucket = aws_s3_bucket.customer_data.id
  rule {
    apply_server_side_encryption_by_default { sse_algorithm = "AES256" }
  }
}

# Why intentionally misconfigured: versioning OFF. Attacker in scenario
# 04 could overwrite objects with empty content before exfil and the
# original data is gone. In a real breach you want versioning ON so
# forensics has the history.
resource "aws_s3_bucket_versioning" "customer_data" {
  bucket = aws_s3_bucket.customer_data.id
  versioning_configuration {
    status = "Disabled"
  }
}

# Seed fake customer data. 20 small JSON objects (we tune down from 200
# to 20 so terraform apply does not take forever; attack script loops
# over them multiple times to generate the "200 GetObject calls" pattern).
resource "aws_s3_object" "fake_customer" {
  count   = 20
  bucket  = aws_s3_bucket.customer_data.id
  key     = "customers/record-${format("%03d", count.index)}.json"
  content = jsonencode({
    id    = count.index
    name  = "Fake Customer ${count.index}"
    email = "customer${count.index}@example.com"
    note  = "Synthetic test data. Not real PII."
  })
  content_type = "application/json"
}

# -----------------------------------------------------------------------
# CloudTrail with S3 data events. This is the key enablement for every
# detection rule in detections/ that references GetObject.
# -----------------------------------------------------------------------

resource "aws_s3_bucket" "trail" {
  bucket        = "${local.name_prefix}-trail-${random_id.suffix.hex}"
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "trail" {
  bucket                  = aws_s3_bucket.trail.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_policy" "trail" {
  bucket = aws_s3_bucket.trail.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid    = "AWSCloudTrailAclCheck"
        Effect = "Allow"
        Principal = { Service = "cloudtrail.amazonaws.com" }
        Action   = "s3:GetBucketAcl"
        Resource = aws_s3_bucket.trail.arn
      },
      {
        Sid    = "AWSCloudTrailWrite"
        Effect = "Allow"
        Principal = { Service = "cloudtrail.amazonaws.com" }
        Action   = "s3:PutObject"
        Resource = "${aws_s3_bucket.trail.arn}/AWSLogs/${data.aws_caller_identity.current.account_id}/*"
        Condition = {
          StringEquals = { "s3:x-amz-acl" = "bucket-owner-full-control" }
        }
      }
    ]
  })
}

resource "aws_cloudtrail" "lab" {
  depends_on = [aws_s3_bucket_policy.trail]

  name                          = "${local.name_prefix}-trail"
  s3_bucket_name                = aws_s3_bucket.trail.id
  include_global_service_events = true
  is_multi_region_trail         = true
  enable_log_file_validation    = true

  # Why: S3 object-level data events are OFF by default on every trail
  # you have ever created. Without this block, GetObject does not show
  # up in CloudTrail. Half the detection rules in this repo rely on it.
  event_selector {
    read_write_type           = "All"
    include_management_events = true

    data_resource {
      type   = "AWS::S3::Object"
      values = ["${aws_s3_bucket.customer_data.arn}/"]
    }
  }
}
