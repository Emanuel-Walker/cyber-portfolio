# Tier 1 - Crown Jewels Playbook

**BLUF.** Any alert on a Tier 1 asset gets a human in 15 minutes. The on-call is pre-authorized to isolate the host without a ticket. The CISO sees it in the morning stand-up regardless of outcome.

**SLA.** MTTD 15 minutes. MTTR 2 hours. Any breach of these is a post-mortem item.

---

## Assets this applies to

- Payment processing and settlement
- Core customer databases with regulated data (PCI, PHI, HIPAA)
- The main product's source code repository
- Code signing and release signing keys
- Core customer-facing authentication (customer SSO)
- Any single asset the CFO would name as "the thing that must not go down"

Full list for this org: see `code/example_asset_inventory.yaml` or the live CMDB tag `cj_tier=1`.

---

## Alerts this covers

Any alert. Not a specific detection list. If the alert fired on a Tier 1 asset, this playbook runs.

Common examples:
- Authentication anomalies (new logon source, service account activity outside baseline)
- Process execution anomalies
- Network egress to new destinations
- File integrity monitoring hits
- Any EDR detection, any severity
- SIEM correlations that touch the asset
- Honeypot deception triggers that correlate with Tier 1 asset traffic

---

## First 15 minutes

The clock starts when the alert fires. Not when the analyst picks it up. If your SIEM-to-pager latency is 10 minutes you have 5 minutes.

1. **Minute 0 to 3.** Acknowledge the page. Open the asset page. Confirm it is actually Tier 1 (not a stale tag). Pull the last 30 minutes of auth logs, process executions, and network egress for the host.
2. **Minute 3 to 7.** Decide: real signal or false positive. Criteria for "real signal":
   - Authentication from unexpected source IP or geography
   - Process execution outside the known baseline for this asset
   - Egress to a destination not on the allow list
   - Correlated activity on a dependency asset in the last 60 minutes
   - You cannot immediately explain it as expected behavior
3. **Minute 7 to 10.** If real signal, declare an incident. Open a bridge. Page incident commander on-call. Page the asset's owning team.
4. **Minute 10 to 15.** Containment decision. You are pre-authorized to:
   - Isolate the host from the network (EDR isolation, security group deny-all)
   - Revoke the suspect credential
   - Snapshot the asset for forensics before any destructive action
   You are not authorized to:
   - Rebuild the asset (business decision)
   - Notify customers (legal decision)
   - Public statement of any kind

---

## Investigation steps

**Hour 0 to 1:**
- Pull 24h of logs across auth, process, network, and file integrity for the asset.
- Pull logs for any identity that touched the asset in the last 24h.
- Pull logs for every dependency asset.
- Build a timeline. First access, last known good, suspect activity, current state.
- Check for persistence: new users, new scheduled tasks, new SSH keys, new API tokens, new service principals.

**Hour 1 to 2:**
- Pivot: for every suspect identity, where else did they authenticate in the last 7 days?
- For every suspect source IP, what else did it touch?
- If data egress is suspected, estimate volume and classify what was reachable.
- Document everything in the incident ticket. Future-you and the post-mortem need the breadcrumbs.

---

## Containment options

Ranked by reversibility, lowest-reversible first:

1. **Monitor-only.** Rare for Tier 1. Only acceptable if you have high confidence it is a false positive and the asset owner is on the bridge agreeing.
2. **Credential revocation.** Rotate the specific identity. Low blast radius, high forensic value.
3. **Session kill.** Terminate all active sessions on the asset. Users will reauth, you get a clean slate.
4. **Network isolation.** EDR isolation or security group deny-all. Asset stays alive for forensics but cannot reach anything.
5. **Full shutdown.** Rare. Only if you believe active exfiltration is in progress and isolation is not sufficient.
6. **Rebuild from known-good.** Business decision. Not a SOC call. Requires asset owner and CISO signoff.

---

## Communication tree

Trigger: real signal confirmed.

- **Immediate (within 15 min of confirmation):** SOC manager, incident commander on-call, asset owner on-call.
- **Within 1 hour:** CISO, VP of Engineering (if the asset is engineering-owned), VP of the business function.
- **Within 4 hours (if breach confirmed):** Legal, Communications, CEO.
- **Within 24 hours (if customer data confirmed exposed):** Privacy counsel, regulators as required by jurisdiction, affected customer notification planning.

Do not notify customers, publish statements, or speak to press without legal and comms approval. The SOC does detection and containment. Not public relations.

---

## After-action requirements

Every Tier 1 playbook run produces an after-action report within 72 hours. Required sections:

- Timeline (alert fired, detection confidence, time to human, time to containment, time to all-clear)
- Was the detection appropriate for Tier 1? If not, retune.
- Was the asset's tier correct? If this turned out to be the wrong tier, propose a re-score.
- Were playbook steps followed? Where did we deviate and why?
- What breaks before we see this again? File detection, control, or process tickets.
- SLA conformance: did we hit 15m MTTD and 2h MTTR?

The report goes to the CISO regardless of outcome. False positives on Tier 1 are not shameful. Missed detections on Tier 1 are.
