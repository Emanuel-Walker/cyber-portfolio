# Quickstart - Crown Jewel Triage

## Plain English

Most alert queues start with the alert's severity.

This project adds a second question:

**What asset does the alert threaten?**

A medium-severity alert on a payment system may deserve attention before a high-severity alert on a disposable development box.

## 5-minute demo

### 1. Install the only Python dependency

From the portfolio root:

```bash
cd 03-crown-jewel-triage
python3 -m pip install pyyaml
```

### 2. Score the sample alerts

Run:

```bash
python3 code/crown_jewel_scorer.py \
  --inventory code/example_asset_inventory.yaml \
  --alerts code/example_alerts.jsonl
```

**PASS:** the command prints JSON results ordered by `priority_score`.

Look for:
- `prod-payment-settlement-01`
- `mkt-laptop-chen-l`

The payment-system alert should receive a much larger priority score even though its raw severity is only medium.

### 3. Generate the human-readable queue

Run:

```bash
python3 code/run_prioritization.py \
  --inventory code/example_asset_inventory.yaml \
  --alerts code/example_alerts.jsonl \
  --out queue.md
```

Then:

```bash
cat queue.md
```

**PASS:** the table is ordered by computed priority and includes a tier-specific playbook link.

## How the asset tier is calculated

Each asset receives a 1-to-5 score for:

- business impact
- data sensitivity
- blast radius
- recovery cost

The four values are added together.

The total maps to a tier.

Some asset types then route to a more appropriate playbook.

Example:

```text
an identity provider may use the high-trust identity playbook
```

even when its raw score lands in the top band.

The full rubric is:

```text
code/models/scoring_rubric.yaml
```

## What this proves

- asset context can change alert priority
- the scoring logic is explicit and editable
- the same result can route analysts to a tier-specific response playbook
- raw SIEM severity is not the only useful prioritization input

## What this does not prove

The sample asset scores are synthetic.

A real organization would need business owners and system owners to validate:
- criticality
- dependencies
- recovery requirements
- data sensitivity

The model is only as good as the asset inventory behind it.

## Next

Read:

```text
ESSAY.md
README.md
playbooks/00-tier-definitions.md
```
