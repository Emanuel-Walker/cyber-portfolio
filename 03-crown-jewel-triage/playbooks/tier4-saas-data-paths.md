# Tier 4 - SaaS Data Paths Playbook

**BLUF.** The threat model is exfiltration, not disruption. The playbook is egress analysis, DLP tuning, and tenant admin containment. Legal gets involved early if regulated data is in scope.

**SLA.** MTTD 1 hour. MTTR 8 hours.

---

## Assets this applies to

- Snowflake, BigQuery, Databricks, Redshift tenants with regulated data
- Workday, SuccessFactors, BambooHR, other HRIS with full employee records
- Salesforce, HubSpot, other CRMs with customer PII
- Marketo, Pardot, Mailchimp, other marketing automation with customer contact data
- Email gateways (Proofpoint, Mimecast) with customer-sensitive mail flow
- Analytics and BI platforms (Looker, Tableau Online, Mode) with regulated-data connections

---

## Alerts this covers

- Large query result sets (row-count anomalies on sensitive tables)
- Bulk export (CSV download, scheduled report with unusual recipient)
- New external share (Snowflake data share, Salesforce external user, Workday API consumer)
- Admin role grant inside the SaaS tenant
- API key creation outside change-window
- OAuth app consent with high-sensitivity scopes
- New data egress destination (new S3 bucket, new FTP, new email forwarding rule)
- Mail forwarding rule to external address

---

## First 15 to 30 minutes

1. **Minute 0 to 10.** Pull the SaaS admin audit log for the last 60 minutes. What changed, by whom, from where.
2. **Minute 10 to 20.** Quantify the egress. How many rows, how many records, what classes of data. If this is Snowflake-like, run the query that recreates the suspect query's row count without actually re-exporting.
3. **Minute 20 to 30.** Containment decision:
   - Revoke the suspect user/service account
   - Expire any data share, external user grant, or API key created in the suspect window
   - If a mail forwarding rule, delete it and preserve a copy for forensics

---

## Investigation steps

**Hour 0 to 2:**
- Pull every query / API call the suspect principal made in the last 7 days.
- For each sensitive table, pull the full access history for the suspect window.
- Determine data classes exposed. Count records. Map to data classification tags.
- Check for persistence: new API keys, new OAuth apps, new scheduled reports, new webhook destinations.

**Hour 2 to 8:**
- If regulated data confirmed exposed, loop privacy counsel.
- Prepare the dataset summary: what, how many records, which customers.
- Preserve audit logs. SaaS vendors have short default retention. Pull and store.
- Request vendor-side investigation support if the SaaS has unusual auth patterns on the vendor's side (impossible travel, source IPs you cannot explain).

---

## Containment options

1. **Account suspension.** Suspect user disabled, sessions killed.
2. **Scope reduction.** Suspect user's permissions reduced to minimum. Useful if you want to keep forensic visibility.
3. **Share revocation.** Every external share, external user, API key created in the suspect window is expired.
4. **IP allowlist tightening.** If the SaaS supports IP allowlists and the attacker was outside corporate IP space, enable or tighten.
5. **Tenant-wide session reset.** Every user reauths. Noisy. Appropriate when admin compromise suspected.

---

## Communication tree

- **Immediate:** SaaS owner team, SOC on-call.
- **Within 2 hours:** CISO, data governance lead.
- **Within 4 hours (regulated data egress suspected):** Privacy counsel, legal.
- **Within 24 hours (regulated data egress confirmed):** Regulators per jurisdiction, affected customer notification planning, comms.

---

## After-action requirements

- Did we have DLP on this egress path? If no, Tier 4 ticket.
- Did the SaaS vendor's logs cover the window we needed? If no, this is a vendor conversation.
- Was the suspect principal's permission scope appropriate for their role? Least-privilege review for the role.
- SLA conformance.
- Report to CISO within 72 hours. Include a regulated-data impact summary even if no egress confirmed.
