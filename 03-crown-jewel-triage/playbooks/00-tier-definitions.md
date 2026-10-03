# Tier Definitions

**BLUF.** Six tiers. Each one answers a different question about an asset. Each one has a different playbook, SLA, and page list. The tier is not a severity. It is a statement about what the attacker is reaching for.

---

## The six tiers at a glance

| Tier | Name | Characteristic question | SLA (MTTD / MTTR) |
|-----:|------|-------------------------|-------------------|
| 1 | Crown Jewels | "If this is breached, do we lose the business?" | 15m / 2h |
| 2 | High-Trust Identity | "Does compromise here give the attacker everyone else's keys?" | 15m / 2h |
| 3 | Build and Deploy | "Can an attacker here push code to production unseen?" | 30m / 4h |
| 4 | SaaS Data Paths | "Can regulated data egress from here?" | 1h / 8h |
| 5 | Lateral Stepping Stones | "Does an attacker here get closer to a higher tier?" | 1h / 8h |
| 6 | Noise | "Is this standalone and recoverable?" | 4h batch / 24h |

---

## Tier 1 - Crown Jewels

The 10 to 20 assets whose compromise ends the quarter, the career, or the company. Payment processing. Core customer databases with regulated data. The ledger. The source code repo for the main product. The signing keys. If you cannot name all of them in one breath, your Tier 1 list is too long.

**Pager posture:** on-call human sees any alert within 15 minutes. No exceptions for severity, time of day, or holiday.

**Who gets looped:** SOC manager, incident commander on-call, business owner, CISO (within 1 hour if confirmed).

---

## Tier 2 - High-Trust Identity

Identity and authentication systems. SSO/IdP tenants. Cloud org admin consoles. Domain controllers. Password vaults. The MFA back-end. Compromise here is "attacker has everyone's keys," which is the worst day of your year.

Separated from Tier 1 because the playbook is different. For Tier 1 you contain the asset. For Tier 2 you contain the identities derived from it, which means mass session kill, token rotation, and reauth. Different muscle.

**Pager posture:** same as Tier 1. 15 minutes.

**Who gets looped:** identity engineering lead, SOC manager, CISO, legal if customer-facing identity (customer SSO) is affected.

---

## Tier 3 - Build and Deploy

CI/CD orchestrators (Jenkins, GitHub Actions self-hosted, GitLab Runner). Package registries. Container image registries. Artifact signing systems. Build secrets vaults.

Why separate from Tier 1: an attacker here does not need to touch production directly. They push poisoned code and production touches them. The playbook is supply chain focused.

**Pager posture:** 30 minutes to human eyes. Shorter if the pipeline runs for a Tier 1 service.

**Who gets looped:** platform engineering lead, SOC on-call, security engineering (to pull signed artifacts for comparison).

---

## Tier 4 - SaaS Data Paths

Any SaaS tenant with the ability to egress regulated data at scale. Snowflake. Workday. Salesforce. Analytics platforms. Email gateways that touch customer PII.

The threat model is exfiltration, not disruption. The playbook is DLP and egress analysis.

**Pager posture:** 1 hour MTTD. Faster if the detection is specifically for data movement.

**Who gets looped:** SaaS owner team, data governance, legal (within 24 hours if egress is confirmed and regulated).

---

## Tier 5 - Lateral Stepping Stones

Jump hosts. Bastions. VPN concentrators. Shared service accounts with cross-asset access. Any system whose value to the attacker is "it gets me closer to a higher tier."

Treat these as tripwires. Low interactive value to the business, high movement value to the attacker.

**Pager posture:** 1 hour. Investigation focus is east-west traffic since last known good login.

**Who gets looped:** infra on-call, SOC on-call, identity engineering if the stepping stone is credential-based.

---

## Tier 6 - Noise

Marketing laptops. Dev sandboxes. Honeypots (except honeypots have a deception override that bumps them to Tier 1 behavior on first touch). Internal wikis. Anything standalone, recoverable in a day, with no credentials to anywhere interesting.

**Pager posture:** batch review every 4 hours. Escalate on threshold cross (volume, novelty, correlation with higher-tier asset).

**Who gets looped:** SOC Tier 1 queue. CISO never sees these unless they cross threshold.

---

## Routing rules in plain English

- Score the asset on the four factors. Sum.
- Tier 1 is 18 to 20.
- Tier 2 or 3 is 15 to 17, split by whether the asset is identity (Tier 2) or build/deploy (Tier 3).
- Tier 4 is 11 to 14 if the asset is a SaaS data path with regulated data.
- Tier 5 is 8 to 10 or any lateral asset regardless of score.
- Tier 6 is 4 to 7 and standalone.

When in doubt between two tiers, pick the higher one. The cost of over-tiering is a slightly louder playbook. The cost of under-tiering is a buried breach.
