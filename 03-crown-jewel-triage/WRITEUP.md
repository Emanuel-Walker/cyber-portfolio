# Crown Jewel Triage: Rebuilding SOC Priority Around What the Attacker Wants

## The scene

A Tier 1 analyst I was mentoring pinged me at 2 a.m. during a shift. She had an alert open, a lateral movement signature on an internal host, and the SIEM called it Medium. She wrote:

> "I don't know if this is P2 or P3. The hostname looks weird. Do I escalate or finish my queue?"

I didn't have a good answer. Not a real one.

I asked what the host did. She didn't know. I asked who owned it. She didn't know. I asked if it talked to anything sensitive. She didn't know. Not because she was bad at her job. Because nobody had ever told her. The CMDB was three years stale. The asset tags in the SIEM were half-populated. The severity dropdown was the only thing she had, and she knew in her gut it was lying.

That is the problem this project is trying to fix.

## Why severity-based triage is broken

Severity is a label a detection engineer picked when they wrote the rule, usually six months ago, usually in a hurry, usually without knowing which hosts in your environment the rule would fire on. Severity does not know your business. It does not know that the host called `app-07` is actually the payment settlement service and the host called `prod-db-cluster-01` is actually a dev sandbox someone forgot to rename.

Three failure modes I see over and over:

**1. The buried P3.** A credential-stuffing attempt against the SSO admin console gets scored Medium because it is "just" a failed login burst. Nobody looks at it for six hours. Meanwhile the attacker has rotated IPs and is now 40,000 attempts in. By the time anyone catches it the attacker has moved on to password spray with better tradecraft and your detection has a one-shift head start.

**2. The screaming P1.** A new EDR deployment on a dev team's laptops fires 300 Highs about PowerShell encoded commands. All 300 are benign developer tooling. The queue fills up. The analyst who has been on shift for six hours stops reading them carefully. The 301st is real, from a different host, and gets closed as a dupe.

**3. The misclassified blast.** An alert on an endpoint fires Low because the alert is "non-interactive logon anomaly." The endpoint is a jump host used by the on-call DBA to reach every production database. The attacker is one `ssh` away from everything that matters. The analyst closes it in 90 seconds because the queue is deep and Low means Low.

Every one of those failures has the same root cause. The alert told the analyst how loud the detection felt. It did not tell the analyst what the attacker was reaching for.

## The reframe

The industry already has a name for this. Crown jewels. NIST uses it. CISA uses it. Mandiant and Gartner build threat models around it. The idea is simple. A small number of assets carry most of the risk. You do not defend every host equally. You identify what matters, you concentrate your watch there, and you accept risk on the rest.

Civilian SOCs know the term and almost never operationalize it. Call it a Key Asset model if "crown jewels" sounds too marketing. Either way, the idea is the same:

> Prioritize alerts by what the attacker is trying to reach, not by what the alert happens to say.

An alert on a Tier 1 asset gets human eyes in 15 minutes, no matter what the severity label says. An alert on a Tier 6 asset waits for the batch review, no matter how loud it is, unless it meets a specific escalation threshold.

That is the whole idea. The rest of this project is the plumbing to make it real.

## The 4-factor Key Asset score

Every asset in your inventory gets scored 1 to 5 on four factors. Total score maps to one of six tiers. The rubric is in `code/models/scoring_rubric.yaml`. Short version:

**Business impact.** If this asset is unavailable for 4 hours, does the business lose revenue, violate a contract, or hit the news? A payment processor is a 5. A dev sandbox is a 1. The question is not "is this important to IT." It is "is this important to the P&L."

**Data sensitivity.** What is the most sensitive data this asset touches, processes, or has credentials to reach? Regulated data (PCI, PHI, HIPAA-covered, financial records) is a 5. Public marketing content is a 1. Note the "has credentials to reach" clause. A build server with a cloud admin key is a 5 even if the server itself has nothing on it.

**Blast radius.** If this asset is fully compromised, how many other assets fall with it? A domain controller is a 5. A single contractor laptop with no persistent access is a 1. SSO is almost always a 5. CI/CD is almost always a 5. People underscore blast radius more than any other factor.

**Recovery cost.** If this asset is destroyed or ransomed, what is the real cost to restore to a known-good state? Includes rebuild time, data loss window, customer notification, legal exposure. A customer-data warehouse with weekly backups and no replica is a 5. An auto-scaling stateless container is a 1.

Add the four. Map to tier. Done.

- 18 to 20: Tier 1, Crown Jewels
- 15 to 17: Tier 2, High-Trust Identity (if the asset is an identity system) or Tier 3 (if it is build/deploy)
- 11 to 14: Tier 4, SaaS data paths
- 8 to 10: Tier 5, Lateral stepping stones
- 4 to 7: Tier 6, Noise

The tiers are not a strict linear ordering. Tier 2 and Tier 3 are different kinds of important and get different playbooks. Same for Tier 4 and Tier 5. See `playbooks/00-tier-definitions.md`.

## Playbook by tier, not by alert type

Here is the shift that makes this real. Stop writing playbooks per alert type. Start writing playbooks per tier.

A traditional SOC playbook library looks like this:

- `playbook_bruteforce.md`
- `playbook_powershell_encoded.md`
- `playbook_dns_tunneling.md`
- `playbook_impossible_travel.md`
- ... 200 more

Every one of those playbooks says some version of "investigate the alert, check the host, check the user, decide." They are generic because they have to be. They cannot know what the asset is worth.

A tier-based library looks like this:

- `tier1-crown-jewels.md`: ANY alert touches this, you page a human in 15 minutes. Pre-authorized to isolate the host without waiting for ticket approval. Communications tree is primed, legal is on the ping list, the CISO sees it in the morning stand-up no matter what.
- `tier5-lateral-stepping-stones.md`: Any auth or process anomaly gets a 1-hour SLA. Focus is on movement. First action is to pull session tokens and check for east-west traffic since the last known good login.
- `tier6-noise.md`: Batch review every 4 hours. Only escalate if the alert crosses a threshold (volume, novelty, or correlation with a higher-tier asset).

Each tier playbook in this repo includes assets covered, alerts covered, first 15 minutes, investigation steps, containment options, communication tree, and after-action requirements. They are shorter and more specific than per-alert playbooks because they can assume what the asset is worth.

## Rebuilding the dashboard

If you prioritize by tier, your dashboard has to measure by tier. The Grafana JSON in `dashboards/` has five panels, all grouped by tier:

- **MTTD by tier.** How long from alert fired to human eyes, split by tier. Tier 1 should be under 15 minutes 95% of the time. If it is not, that is a staffing problem, not a tool problem.
- **MTTR by tier.** From alert to closure. Tier 1 under 2 hours, Tier 6 under 24. These are starting numbers. Tune to your business.
- **Queue depth by tier.** Count of open alerts per tier. If Tier 1 queue is ever greater than zero for more than 15 minutes, something is wrong.
- **False positive rate by tier.** This is the panel that drives detection engineering. High FP on Tier 1 means a detection needs tuning now, because every FP burns the on-call. High FP on Tier 6 is tolerable because the batch absorbs it.
- **SLA conformance by tier.** Rolling 7-day percentage of alerts closed inside the tier SLA. This is what the CISO sees.

Nowhere on this dashboard is the word "severity." Severity is still in the data. It is just not the organizing principle anymore.

## Honest limitations

Four things this doesn't solve:

**1. It doesn't replace severity. It layers on top.** Severity is still a useful signal from the detection engineer about how confident they are in the detection. Tier is a signal about how much the business cares. You multiply them. You don't swap them.

**2. The asset inventory is the hard part.** If your CMDB is garbage, this gives you garbage. The code can read a YAML. It cannot tell you what your assets are. Expect the first pass of your Tier 1 list to take a week of conversations with the business, not a weekend of SQL.

**3. Tiering drifts.** An asset that was Tier 4 last quarter can become Tier 2 after a product launch. Reviewing the tier list quarterly is non-optional.

**4. Analysts have to buy in.** If you roll this out without walking the team through the reasoning, they will keep triaging by severity because that is what the UI shows them. The dashboard rebuild is as much culture work as it is engineering.

## Three takeaways

1. **Prioritize by what the attacker wants.** Severity tells you how loud the alert is. Tier tells you how much it matters that the alert is on this asset. The attacker is reaching for tier, not severity.

2. **Playbook by tier, not by alert type.** You will write fewer playbooks, they will be more specific, and your Tier 1 analysts will actually read them.

3. **Measure what you prioritize.** If your dashboard still groups by severity, your team will still think in severity. Rebuild the dashboard. The behavior follows.

The code in this repo is a prototype. The idea is not. Fortune 500 SOCs that have adopted a version of this quietly for years outperform their peers on MTTR for the alerts that actually matter. Open source it. Make it the default. Stop burying real attacks under alert labels an analyst picked in a hurry.
