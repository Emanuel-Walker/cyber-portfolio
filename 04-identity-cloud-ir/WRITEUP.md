# Identity Is the 2026 Attack Surface

I was reading a breach writeup last month. A mid-size SaaS company. The attacker never ran a binary. They never touched a shell on a company host. They logged in with a stolen OAuth refresh token from a developer's leaked `.env` file, assumed a role in the customer's AWS account via a federated trust, and pulled 400 GB of data out of an S3 bucket over 11 hours using `GetObject` in a loop.

The company had GuardDuty. GuardDuty did not say a word.

I kept thinking about it. GuardDuty is not broken. It is doing exactly what it was designed to do in 2017. The problem is that the attack surface moved and the default detections did not move with it. So I built this lab to prove it to myself with specific finding types and specific log events, then I wrote the detections that would have caught the thing.

## Why identity is the surface now

Three things changed in the last two years.

**First**, nobody deploys infrastructure manually anymore. Every production app has a non-human identity (NHI) somewhere, often several. Service accounts, OAuth apps, cross-account roles, workload identity bindings. Verizon's DBIR 2024 put machine identity involvement in cloud breaches at around 40%. Everyone I know in detection says the real number is higher because most orgs cannot even inventory their NHIs.

**Second**, SaaS federation ate perimeter. The Snowflake customer breaches in 2024 did not involve any Snowflake vulnerability. Attackers hit customer SSO or stole MFA-less service credentials, logged in like normal users, and ran `SELECT * FROM customers`. From a log perspective it was a successful authentication followed by a legitimate query. There is no signature for that.

**Third**, attackers stopped bringing malware. Scattered Spider's 2023-2024 campaigns against hospitality and insurance ran on social engineering, help desk calls, and session cookie theft. Mandiant's writeup on UNC3944 reads like a social engineering playbook with some cloud API scripting at the end. No implants.

If the attacker is logging in as a legitimate identity and calling legitimate APIs, you cannot catch them with signatures. You catch them with behavior on identity.

## The target

Terraform in this repo builds a fictional org called `northwind-cloud`. It is deliberately weak in five specific ways, each tied to a scenario.

1. **Over-privileged NHI.** An IAM role named `northwind-data-pipeline` has `iam:PassRole` on wildcard, `lambda:UpdateFunctionCode` on wildcard, and `sts:AssumeRole` into a second account. This is not a strawman. I have seen worse on real data engineering teams who needed to ship fast.
2. **OAuth app with excess scopes.** Modeled as an SSM parameter holding a fake refresh token tagged with scope metadata including `drive.readonly`, `admin.directory.user.readonly`, `mail.send`. The app only needed `drive.readonly.file`. This is the exact pattern from several 2024 CASB vendor writeups.
3. **Cross-account trust with weak condition.** The trust policy allows any principal in a second account to assume the role, with a condition on `sts:ExternalId` that is checked but set to a predictable value (`northwind-prod-2026`). An attacker who gets the external ID gets the account.
4. **S3 bucket with lifecycle misconfigured for exfil.** Versioning is off. Object-level CloudTrail data events are not enabled on the bucket by default (the lab turns them on, but calls out the real-world default). Block Public Access is enabled, which is good, but presigned URL generation is not restricted.
5. **GuardDuty with default settings only.** S3 Protection on, Malware Protection off, EKS Protection N/A, RDS Protection off, Lambda Protection off. This is a majority configuration in orgs I have seen.

## The 5 scenarios

**Scenario 01 - OAuth token theft.** Script pulls the fake refresh token out of SSM (simulating the "leaked in a public commit" step) and uses it to make AWS API calls under the identity it represents. CloudTrail shows the API calls. User-agent and source IP are the only tells. The scenario demonstrates that stolen-credential usage is indistinguishable from legitimate usage without session context.

**Scenario 02 - NHI privilege escalation.** The over-privileged pipeline role uses `iam:PassRole` to attach a higher-privilege role to a new Lambda function, then invokes the Lambda to run with that role's permissions. Then it assumes the cross-account role. Classic.

**Scenario 03 - Cross-tenant session anomaly.** The attacker uses the stolen credentials from an unusual geo, unusual time of day, unusual ASN combination. This one is behavioral. No single event is bad. The pattern is bad.

**Scenario 04 - SaaS to S3 exfil.** The over-privileged role calls `GetObject` in a loop, 200 small objects, each under 1 MB, rate-limited to look like a legitimate batch job. No malware. No encryption. No egress to a weird IP.

**Scenario 05 - GuardDuty silent IAM.** Three IAM actions that do not individually trigger a GuardDuty finding under default settings:
- `CreateAccessKey` for an existing user that has not had programmatic access before
- `AttachUserPolicy` attaching an AWS-managed admin policy without any inline change
- An attempted `UpdateAccountPasswordPolicy` loosening the policy

All three show up in CloudTrail. None of them generate a default GuardDuty finding. This is the scenario that surprised me most when I confirmed it against the AWS docs.

## What GuardDuty catches, what it misses

Honest table (full version in `detections/detection_matrix.md`):

| Scenario | GuardDuty default | GuardDuty with all protection plans | Custom detections |
|---|---|---|---|
| 01 OAuth token theft | Miss | Partial (UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS if from non-AWS IP) | Catch |
| 02 NHI privesc | Partial (PrivilegeEscalation:IAMUser/AnomalousBehavior) | Partial | Catch |
| 03 Cross-tenant anomaly | Miss | Partial (UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B if console) | Catch |
| 04 S3 exfil (low-and-slow) | Miss | Miss (not a known-bad IP, under threshold) | Catch |
| 05 Silent IAM | Miss | Miss | Catch |

Default GuardDuty catches 0 to 1 of these 5 cleanly. With every protection plan enabled, maybe 2 to 3 partially. Custom detections cover all 5.

The scenario that bothered me most was 05. `CreateAccessKey` is step one of about half of the AWS IAM breaches I have read writeups for. There is no default GuardDuty finding named "someone just minted a new access key for an existing user." You have to write that rule yourself.

## The detections

For each scenario I wrote three equivalent detections:

1. **Athena SQL** against CloudTrail. If you have CloudTrail going to S3 and have not set up Athena against it yet, do that first. It is the cheapest hunting platform you will ever get.
2. **Elastic Detection Engine YAML.** Uses ECS field names (`aws.cloudtrail.event_name`, `user.name`, `source.ip`, `event.outcome`). Drop into a detection engine as is.
3. **Panther Python.** Realistic rule class with `rule()` and `title()` and `severity`. Panther is one of the better detection-as-code platforms if your org has it.

Rule logic for scenario 05 is dumb simple and that is the point. `event.action == "CreateAccessKey"` and the user has no existing access keys. Two conditions. Thirty lines of Python. It would have caught Scattered Spider at MGM.

## Honest limitations

Three things I did not do that a real version of this would do.

1. **No real Okta integration.** The OAuth scenario is modeled through AWS SSM because standing up a real Okta dev tenant for this would have doubled the scope and the cost. The detection logic would be the same shape against real Okta System Log.
2. **No multi-account.** The cross-account scenario uses a single AWS account with a self-trust. Real version needs two accounts, real external ID, real STS logs on both sides.
3. **Detection rules are not tuned.** I wrote them for correctness, not for noise. In a real environment the `CreateAccessKey` rule would fire every time an engineer onboards. You would gate it with an allowlist, a user-tag check, or a business-hours modifier. The repo includes a note on each rule about likely tuning.

## Three takeaways

1. **If your cloud detection strategy is "GuardDuty with defaults" you have an identity blind spot the size of a bus.** Enable all protection plans at a minimum. Then write custom detections for the silent cases.
2. **The cheapest detection platform you own is Athena against CloudTrail.** You already pay for CloudTrail. You already pay for S3. Athena is pennies per query. Start there.
3. **Detection-as-code is table stakes now.** YAML and Python in a Git repo with CI, not clicky-boxes in a vendor UI. If an auditor cannot see the git log for your detections, you do not have detections. You have hope.

Full repo: all 5 scenarios, 15 detections (3 formats x 5 scenarios), coverage matrix, tabletop exercise, Terraform you can deploy for a dollar.
