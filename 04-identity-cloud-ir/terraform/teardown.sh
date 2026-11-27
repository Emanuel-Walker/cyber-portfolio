#!/usr/bin/env bash
# teardown.sh
# Why: cost control. GuardDuty + CloudTrail data events run a few dollars
# a day if you forget. This script destroys everything and then double-
# checks the three resources most likely to linger (S3 bucket because of
# versioned objects, SSM parameter because of SecureString tombstones,
# GuardDuty detector because sometimes a hanging CloudTrail reference
# blocks the destroy).
# How: terraform destroy -auto-approve, then post-check with awscli.

set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
cd "$HERE"

echo "[teardown] running terraform destroy"
terraform destroy -auto-approve

PROJECT="${PROJECT:-northwind-cloud}"
REGION="${AWS_REGION:-us-east-1}"

echo "[teardown] post-check: S3 buckets with project prefix"
LINGER_BUCKETS=$(aws s3api list-buckets \
  --query "Buckets[?starts_with(Name, '${PROJECT}-')].Name" \
  --output text || true)
if [[ -n "${LINGER_BUCKETS}" ]]; then
  echo "[teardown] WARNING: lingering buckets found:"
  echo "${LINGER_BUCKETS}"
  echo "[teardown] run 'aws s3 rb s3://<bucket> --force' for each"
else
  echo "[teardown] no lingering buckets"
fi

echo "[teardown] post-check: SSM parameters"
LINGER_PARAMS=$(aws ssm describe-parameters \
  --region "$REGION" \
  --parameter-filters "Key=Name,Option=BeginsWith,Values=/${PROJECT}/" \
  --query "Parameters[].Name" --output text || true)
if [[ -n "${LINGER_PARAMS}" ]]; then
  echo "[teardown] WARNING: lingering SSM parameters:"
  echo "${LINGER_PARAMS}"
else
  echo "[teardown] no lingering SSM parameters"
fi

echo "[teardown] post-check: GuardDuty detectors"
DETECTORS=$(aws guardduty list-detectors --region "$REGION" --query 'DetectorIds' --output text || true)
if [[ -n "${DETECTORS}" && "${DETECTORS}" != "None" ]]; then
  echo "[teardown] WARNING: GuardDuty detectors still present: ${DETECTORS}"
  echo "[teardown] if you did not have GuardDuty before this lab, disable them to stop billing"
else
  echo "[teardown] no GuardDuty detectors"
fi

echo "[teardown] done. If any WARNING above, resolve before you call it clean."
