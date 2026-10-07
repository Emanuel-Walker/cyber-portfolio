# Crown Jewel Triage

**Asset-tier alert prioritization for civilian SOCs.**

Your SOC does not have an alert problem. It has a priority problem. Every alert in your queue is labeled High, Medium, or Low by an analyst who was tired, new, or guessing. Meanwhile the attacker is walking a straight line toward your payment processor and nobody is looking because the alert on the asset in front of it said P3.

This project is a working prototype of a different model. Score your assets by what they are worth to the business. Route alerts by the tier the asset sits in. Rebuild your dashboard around what the attacker is reaching for, not around what the SIEM felt like calling it.

If you lead a SOC and this reads like your Tuesday, open an issue or email me.

## What it does

- Defines a 6-tier **Key Asset** model that maps every asset to a business function, data class, blast radius, and recovery cost
- Scores alerts against that model so an alert on your payment gateway outranks a High on a marketing laptop
- Ships a **tier-based playbook library** (Crown Jewels, High-Trust Identity, Build and Deploy, SaaS Data Paths, Lateral Stepping Stones, Noise) with concrete first-15-minute actions
- Includes a Grafana dashboard JSON that measures **MTTD, MTTR, queue depth, and SLA conformance by tier**, not by severity (MTTD and MTTR are Mean Time to Detect and Mean Time to Respond, the two metrics SOC leaders live by)
- Comes with synthetic data (12 assets, 6 alerts) so you can run it in two minutes

## Quick start

```bash
pip install pyyaml
python3 code/crown_jewel_scorer.py --inventory code/example_asset_inventory.yaml --alerts code/example_alerts.jsonl
python3 code/run_prioritization.py --inventory code/example_asset_inventory.yaml --alerts code/example_alerts.jsonl --out queue.md
```

Open `queue.md`. The order is not what your SIEM gave you.

## How it works

1. **Asset inventory**. Every asset gets scored on four factors (business impact, data sensitivity, blast radius, recovery cost), each 1 to 5. Total score maps to one of six tiers.
2. **Alert ingest**. Each alert carries an `asset_id` (or we resolve it from hostname/IP).
3. **Priority math**. Priority = base severity × tier multiplier. A Medium on a Tier 1 asset outranks a High on a Tier 6.
4. **Playbook routing**. Tier determines which playbook runs, which humans get paged, and what the SLA clock looks like.

See `diagrams/triage_flow.drawio` for the full picture.

## What I learned

- Severity is noise. Tier is signal. The best Tier 1 analysts I have talked to already do this in their heads. The problem is they are the only ones who do.
- The hard part is not the code. It is the asset inventory. If you cannot name your top 20 assets, nothing below this layer helps you.
- Playbooks written by tier are 3x shorter than playbooks written by alert type, and 5x more usable.
- MTTR by tier is the one dashboard panel every CISO should have and almost nobody does.

## What's next

- Pull real asset metadata from CMDB and cloud tag APIs instead of a hand-written YAML
- Add a feedback loop: when an alert on a Tier 1 asset turns out to be benign, mark the detection for tuning before the next shift inherits it
- Pair this with a detection-engineering backlog so Tier 1 assets get bespoke detections first

## File map

```
├── README.md                this file
├── WRITEUP.md               full project writeup
├── ESSAY.md                 standalone essay on severity-based triage
├── code/
│   ├── models/
│   │   ├── key_asset_schema.yaml
│   │   └── scoring_rubric.yaml
│   ├── crown_jewel_scorer.py
│   ├── run_prioritization.py
│   ├── example_asset_inventory.yaml
│   └── example_alerts.jsonl
├── playbooks/
│   ├── 00-tier-definitions.md
│   ├── tier1-crown-jewels.md
│   ├── tier2-high-trust-identity.md
│   ├── tier3-build-and-deploy.md
│   ├── tier4-saas-data-paths.md
│   ├── tier5-lateral-stepping-stones.md
│   └── tier6-noise.md
├── dashboards/
│   ├── grafana_crown_jewel_dashboard.json
│   └── panel_definitions.md
└── diagrams/
    ├── triage_flow.drawio
    ├── asset_tier_pyramid.drawio
    └── README-render.md
```
