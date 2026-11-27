-- cloudtrail_hunting_queries.sql
-- Why: Athena against CloudTrail is the cheapest hunting platform you own.
-- You already pay for S3 and CloudTrail. Queries cost pennies.
-- How: these assume you have run the standard CloudTrail Athena table
-- creation (CREATE EXTERNAL TABLE cloudtrail_logs ... PARTITIONED BY).
-- If you have not: AWS docs "Querying AWS CloudTrail logs" has the DDL.
--
-- Assumption: table name is "cloudtrail_logs" and it is partitioned by
-- year, month, day. Adjust the WHERE clause partition pruning to match.

-- =====================================================================
-- Query 1: OAuth token theft (scenario 01)
-- Looks for the sequence: GetParameter on a secret-shaped SSM path
-- followed within 10 minutes by CreateAccessKey or usage of the
-- identity associated with that param.
-- =====================================================================
WITH token_reads AS (
  SELECT
    eventtime,
    useridentity.arn   AS actor,
    sourceipaddress    AS src_ip,
    requestparameters  AS req
  FROM cloudtrail_logs
  WHERE year = '2026' AND month = '10'
    AND eventsource = 'ssm.amazonaws.com'
    AND eventname = 'GetParameter'
    AND regexp_like(requestparameters, '(?i)refresh_token|oauth|api_key|secret')
),
key_mints AS (
  SELECT
    eventtime,
    useridentity.arn AS actor,
    sourceipaddress  AS src_ip,
    requestparameters AS req
  FROM cloudtrail_logs
  WHERE year = '2026' AND month = '10'
    AND eventsource = 'iam.amazonaws.com'
    AND eventname = 'CreateAccessKey'
)
SELECT
  t.eventtime      AS token_read_time,
  t.actor          AS token_reader,
  k.eventtime      AS key_mint_time,
  k.req            AS key_mint_request,
  date_diff('second', from_iso8601_timestamp(t.eventtime), from_iso8601_timestamp(k.eventtime)) AS gap_seconds
FROM token_reads t
JOIN key_mints k
  ON t.actor = k.actor
 AND from_iso8601_timestamp(k.eventtime) BETWEEN from_iso8601_timestamp(t.eventtime)
                                             AND from_iso8601_timestamp(t.eventtime) + INTERVAL '10' MINUTE;

-- =====================================================================
-- Query 2: NHI privilege escalation via PassRole + Lambda (scenario 02)
-- A non-human identity (role) performs iam:PassRole and then
-- sts:AssumeRole into a role it did not previously use.
-- =====================================================================
SELECT
  eventtime,
  useridentity.sessioncontext.sessionissuer.username AS acting_role,
  eventname,
  CASE
    WHEN eventname = 'CreateFunction' THEN json_extract_scalar(requestparameters, '$.role')
    WHEN eventname = 'UpdateFunctionConfiguration' THEN json_extract_scalar(requestparameters, '$.role')
    WHEN eventname = 'AssumeRole' THEN json_extract_scalar(requestparameters, '$.roleArn')
    ELSE NULL
  END AS passed_or_assumed_role,
  sourceipaddress,
  useragent
FROM cloudtrail_logs
WHERE year = '2026' AND month = '10'
  AND useridentity.type = 'AssumedRole'
  AND eventname IN ('CreateFunction', 'UpdateFunctionConfiguration', 'AssumeRole')
  AND regexp_like(useridentity.sessioncontext.sessionissuer.username, '(?i)pipeline|ingest|etl|batch')
ORDER BY acting_role, eventtime;

-- =====================================================================
-- Query 3: cross-tenant session anomaly (scenario 03)
-- Finds AssumeRole events where the user-agent for a given role has
-- never been seen in the last 30 days.
-- =====================================================================
WITH baseline AS (
  SELECT DISTINCT
    useridentity.sessioncontext.sessionissuer.username AS role_name,
    useragent
  FROM cloudtrail_logs
  WHERE year = '2026' AND month = '10'
    AND eventname = 'AssumeRole'
    AND date_diff('day', from_iso8601_timestamp(eventtime), current_timestamp) BETWEEN 1 AND 30
),
recent AS (
  SELECT
    eventtime,
    useridentity.sessioncontext.sessionissuer.username AS role_name,
    useragent,
    sourceipaddress
  FROM cloudtrail_logs
  WHERE year = '2026' AND month = '10'
    AND eventname = 'AssumeRole'
    AND date_diff('hour', from_iso8601_timestamp(eventtime), current_timestamp) <= 24
)
SELECT r.*
FROM recent r
LEFT JOIN baseline b
  ON r.role_name = b.role_name AND r.useragent = b.useragent
WHERE b.useragent IS NULL;

-- =====================================================================
-- Query 4: SaaS-to-S3 exfiltration pattern (scenario 04)
-- A single principal makes more than N GetObject calls on a sensitive
-- bucket in a short window. Threshold set deliberately low for lab.
-- Tune for production.
-- =====================================================================
SELECT
  useridentity.arn AS actor,
  sourceipaddress,
  COUNT(*)         AS get_calls,
  SUM(COALESCE(TRY_CAST(json_extract_scalar(responseelements, '$.bytes') AS BIGINT), 0)) AS bytes_est,
  MIN(eventtime)   AS first_seen,
  MAX(eventtime)   AS last_seen
FROM cloudtrail_logs
WHERE year = '2026' AND month = '10'
  AND eventsource = 's3.amazonaws.com'
  AND eventname = 'GetObject'
  AND regexp_like(json_extract_scalar(requestparameters, '$.bucketName'), 'customer-data')
GROUP BY useridentity.arn, sourceipaddress
HAVING COUNT(*) > 100
   AND date_diff('minute', from_iso8601_timestamp(MIN(eventtime)), from_iso8601_timestamp(MAX(eventtime))) < 60;

-- =====================================================================
-- Query 5: GuardDuty-silent IAM manipulation (scenario 05)
-- The three events default GuardDuty does not alert on. Any one of
-- these on a non-admin principal is worth a human eyeball.
-- =====================================================================
SELECT
  eventtime,
  useridentity.arn    AS actor,
  eventname,
  sourceipaddress,
  useragent,
  CASE
    WHEN eventname = 'CreateAccessKey' THEN json_extract_scalar(requestparameters, '$.userName')
    WHEN eventname = 'AttachUserPolicy' THEN concat(
      json_extract_scalar(requestparameters, '$.userName'), ' <- ',
      json_extract_scalar(requestparameters, '$.policyArn'))
    WHEN eventname = 'AttachRolePolicy' THEN concat(
      json_extract_scalar(requestparameters, '$.roleName'), ' <- ',
      json_extract_scalar(requestparameters, '$.policyArn'))
    ELSE NULL
  END AS target
FROM cloudtrail_logs
WHERE year = '2026' AND month = '10'
  AND eventname IN (
    'CreateAccessKey',
    'AttachUserPolicy',
    'AttachRolePolicy',
    'UpdateAccountPasswordPolicy',
    'DeleteAccountPasswordPolicy'
  )
ORDER BY eventtime DESC;
