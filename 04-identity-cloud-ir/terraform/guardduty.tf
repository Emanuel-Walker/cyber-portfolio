# guardduty.tf
# Why: the whole point of this lab is to measure what GuardDuty catches
# and what it misses. We turn on the detector with default feature set,
# then individually toggle S3 Protection on and the paid plans off so
# the matrix in detections/detection_matrix.md matches reality.
# How: aws_guardduty_detector + feature blocks. We do NOT enable
# RUNTIME_MONITORING, MALWARE_PROTECTION, or RDS_LOGIN_EVENTS because
# those cost real money and the lab is "defaults with S3".

resource "aws_guardduty_detector" "lab" {
  enable                       = true
  finding_publishing_frequency = "FIFTEEN_MINUTES"

  datasources {
    s3_logs {
      enable = true
    }
    kubernetes {
      audit_logs { enable = false }
    }
    malware_protection {
      scan_ec2_instance_with_findings {
        ebs_volumes { enable = false }
      }
    }
  }

  tags = { Name = "${local.name_prefix}-gd" }
}

# Why: optional SNS wiring. Default is OFF because most lab deploys
# will not want SNS costs or email spam.
resource "aws_cloudwatch_event_rule" "gd_findings" {
  count       = var.notify_sns_topic_arn == "" ? 0 : 1
  name        = "${local.name_prefix}-gd-findings"
  description = "Route GuardDuty findings to SNS"
  event_pattern = jsonencode({
    source      = ["aws.guardduty"]
    detail-type = ["GuardDuty Finding"]
  })
}

resource "aws_cloudwatch_event_target" "gd_sns" {
  count     = var.notify_sns_topic_arn == "" ? 0 : 1
  rule      = aws_cloudwatch_event_rule.gd_findings[0].name
  target_id = "sns"
  arn       = var.notify_sns_topic_arn
}
