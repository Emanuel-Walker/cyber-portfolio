# Detection coverage matrix

Honest breakdown of what fires where. All five scenarios run against a lab with GuardDuty on (default + S3 Protection). Rows are attacks. Columns are the tool configurations.

Legend:
- **Catch** = alert fires reliably in a reasonable window.
- **Partial** = alert *may* fire with specific preconditions (anomaly baseline present, source IP on threat list, etc.). Do not rely on it.
- **Miss** = no alert, by design or by gap.

| # | Scenario | GuardDuty default (S3 Prot on) | GuardDuty w/ all protection plans | Custom Athena | Custom Elastic | Custom Panther |
|---|---|---|---|---|---|---|
| 01 | OAuth token theft | Miss | Partial (`UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS` if attacker is outside AWS IP space) | **Catch** (Q1) | **Catch** (`oauth_token_abuse`) | **Catch** |
| 02 | NHI privilege escalation | Partial (`PrivilegeEscalation:IAMUser/AnomalousBehavior` after baseline) | Partial (same) | **Catch** (Q2) | **Catch** (`nhi_privesc_passrole`) | **Catch** |
| 03 | Cross-tenant session anomaly | Miss | Partial (`UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` only if console-mediated and from a Tor exit) | **Catch** (Q3) | **Catch** (`cross_tenant_session_anomaly`) | **Catch** |
| 04 | SaaS-to-S3 exfiltration (low-and-slow) | Miss (not a known-bad IP, under anomaly baseline threshold) | Miss (same, 200 small objects does not trigger `Exfiltration:S3/ObjectRead.Unusual` in a fresh account) | **Catch** (Q4) | **Catch** (`saas_exfil_api_pattern`) | **Catch** |
| 05 | GuardDuty-silent IAM | Miss (no finding type for `CreateAccessKey` on existing user, no finding for `AttachUserPolicy` of managed Admin without inline change) | Miss (same) | **Catch** (Q5) | **Catch** (`iam_access_key_creation`) | **Catch** |

## Totals

| Tool | Scenarios caught (out of 5) |
|---|---|
| GuardDuty default (+ S3 Protection) | 0 clean catches, 1 partial |
| GuardDuty with all protection plans | 0 clean catches, 3 partials |
| Custom Athena | 5 / 5 |
| Custom Elastic | 5 / 5 |
| Custom Panther | 5 / 5 |

## Specific GuardDuty finding types referenced

- `UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration.OutsideAWS` - fires if EC2 role creds used outside AWS. Scenario 01 depends on where you run the script. If you run on your laptop it may fire. If you run on the lab EC2 it will not.
- `UnauthorizedAccess:IAMUser/ConsoleLoginSuccess.B` - console login from Tor exit. Not applicable to API-only scenarios.
- `PrivilegeEscalation:IAMUser/AnomalousBehavior` - anomaly-based. Needs 7-14 days of baseline. Fresh lab accounts have no baseline.
- `Exfiltration:S3/MaliciousIPCaller.Custom` - only on threat-intel-matched source IPs.
- `Exfiltration:S3/ObjectRead.Unusual` - anomaly-based, same baseline requirement.
- `Policy:IAMUser/RootCredentialUsage` - fires only on root usage. None of our scenarios use root.

## Takeaways

1. **GuardDuty is a seatbelt. Not an airbag.** It catches the obvious. The targeted and the stealthy sail past.
2. **Anomaly findings need baselines.** A brand-new account or a brand-new role gets no help from the anomaly engine for the first two weeks.
3. **Detection-as-code gives you clean 5-of-5 coverage** with code that fits on a napkin. The gating factor is "did someone write the rule," not "is the data available."
