# Tier 6 - Noise Playbook

**BLUF.** Batch review every 4 hours. Escalate only on threshold cross. Do not let Tier 6 traffic clog the queue in front of Tier 1.

**SLA.** 4-hour batch MTTD. 24-hour MTTR for anything that stays Tier 6 after batch review.

---

## Assets this applies to

- Marketing laptops
- Dev sandboxes with no production credentials
- Internal wikis, intranet servers
- Standalone contractor laptops
- Honeypots (with the deception override, below)
- Any asset scoring 4 to 7 on the 4-factor rubric that is standalone and recoverable in a day

---

## Alerts this covers

Any alert on an asset in this tier. Severity label from the SIEM is ignored for queue position. These wait for the batch unless they cross threshold.

---

## Batch review process

**Every 4 hours, on a defined schedule (00:00, 04:00, 08:00, 12:00, 16:00, 20:00 UTC or your SOC's shift pattern):**

1. Pull all Tier 6 alerts opened since last batch.
2. Group by asset, by user, by detection name. Look for clusters.
3. For each cluster, apply the threshold rules below. Clusters that cross threshold escalate out of Tier 6.
4. Clusters that do not cross threshold: close with disposition, note trends for the detection engineering backlog.
5. Document the batch review in a 5-line summary at the end of each shift.

---

## Escalation thresholds

A Tier 6 alert escalates to Tier 5 behavior (1-hour MTTD, individual investigation) when any of the following:

- **Volume.** More than 10 alerts on the same asset in 1 hour.
- **Novelty.** A detection fires that has not fired on this asset in the last 30 days.
- **User overlap.** The user on the alert is a known administrator of a higher-tier asset.
- **Credential overlap.** The alert involves a credential that is also used on a higher-tier asset.
- **Correlation.** Within 1 hour, an alert on this Tier 6 asset correlates with any alert on a Tier 1 through Tier 4 asset. Attacker tradecraft often starts in Tier 6.
- **Deception trigger.** For honeypots: any first-touch alert escalates immediately. The whole point of a honeypot is that it should never be touched. First touch is signal, not noise.

---

## First-touch actions (batch)

Per cluster during batch:

1. Confirm asset is still correctly tiered. A dev sandbox that got repurposed for prod data is no longer Tier 6.
2. Confirm the user context (interactive user, service account, scheduled task) is expected for this asset.
3. If the cluster has a plausible benign explanation (developer tooling on a dev sandbox, marketing tool install on marketing laptop), close with disposition "known-benign" and add to the detection tuning backlog.
4. If no plausible benign explanation, escalate the whole cluster.

---

## Investigation steps (post-escalation)

Follow the playbook of the escalated tier. For most Tier 6 escalations, that is Tier 5. For honeypot or correlation triggers, follow the correlated tier.

---

## Containment options

Rarely needed at the Tier 6 level. If containment is required, the alert has already escalated and the correct playbook applies.

For legitimate Tier 6 containment (e.g. a marketing laptop running a cryptominer):

1. EDR isolate the host.
2. Hand to desktop support for reimage.
3. No credential rotation needed unless the user also has access to higher-tier assets. Check first.

---

## Communication tree

- **Normal batch:** SOC Tier 1 queue. Shift lead reviews the 5-line summary.
- **Threshold escalation:** follows the escalated tier's communication tree.
- **CISO never sees Tier 6 unless an escalation triggered.**

---

## After-action requirements

Not per-alert. Per-month:

- What was the Tier 6 volume this month? Trending up or down?
- Which detections produced the most Tier 6 noise? Candidates for tuning.
- How many Tier 6 alerts escalated to higher tiers this month? If zero, our thresholds may be too loose. If high, our tiering may be off.
- Any Tier 6 asset that generated 20+ alerts this month: reassess tier.
