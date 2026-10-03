# Quickstart - Crown Jewel Triage

> [!info] Plain English
> Most security teams rank alerts by a severity dropdown. This project ranks alerts by what each one puts at risk. A payment processor at the top. A marketing laptop at the bottom. You will see the scoring run and a prioritized queue written to a markdown file. Takes about 5 minutes.

## 5-minute demo

BLUF. You will score a sample asset inventory, run alerts through the prioritization engine, and open the generated queue. The payment processor should rank P1. A marketing laptop should rank P6. If that ordering holds, the model works.

Prerequisites.

```bash
python --version   # need 3.10 or newer
pip install pyyaml
```

Step 1 - setup.

```bash
cd 03-crown-jewel-triage
python -c "import yaml; print(yaml.__version__)"
```

What you see. The command prints the installed PyYAML version. No import errors.

Step 2 - run the scorer and the prioritization pass.

```bash
python code/crown_jewel_scorer.py \
  --inventory code/example_asset_inventory.yaml \
  --out code/scored_assets.json

python code/run_prioritization.py \
  --assets code/scored_assets.json \
  --alerts code/example_alerts.jsonl \
  --out queue.md
```

What you see. The scorer prints one line per asset with its four-factor breakdown (business criticality, data sensitivity, attacker desire, blast radius) and a composite tier from P1 to P6. The prioritization step reads the scored file, joins it to the alerts stream, and writes `queue.md`.

```
payment-processor-01    crit=5 sens=5 desire=5 blast=4  -> P1
customer-db-primary     crit=5 sens=5 desire=4 blast=3  -> P2
build-server-ci         crit=4 sens=3 desire=4 blast=5  -> P2
marketing-laptop-14     crit=1 sens=1 desire=1 blast=1  -> P6
```

Step 3 - validate.

```bash
head -40 queue.md
```

What you see. A markdown table ordered by tier. The payment processor alert sits at the top with its tier-based playbook link. The marketing laptop alert is at the bottom. Severity on the raw alert does not change the position. That is the whole thesis of the project. Attackers do not care about your severity dropdown. They care about what they can reach.

## What this proves

- An asset-tied scoring rubric that replaces severity dropdowns with a defensible, auditable number.
- Alert routing that answers "what does this threaten" instead of "how loud is this."
- Tier-based playbooks (P1 through P6) that give analysts a concrete next move instead of a shrug.

## Add screenshots here

Capture these while running the demo and drop them in a `screenshots/` folder next to this file.

- `screenshots/01-inventory-yaml.png` - `example_asset_inventory.yaml` open with the four factors visible
- `screenshots/02-scorer-output.png` - terminal showing P1 to P6 assignments
- `screenshots/03-queue-md-top.png` - top of `queue.md` with payment processor at P1
- `screenshots/04-queue-md-bottom.png` - bottom of `queue.md` with marketing laptop at P6
- `screenshots/05-playbook-link.png` - clicking the P1 playbook link opens the right file in `playbooks/`

## Common issues

- `FileNotFoundError: code/scored_assets.json`. You skipped Step 2a. The scorer has to run before `run_prioritization.py` because the second script reads the first script's output.
- Queue puts the marketing laptop above the payment processor. Weights in `code/models/weights.yaml` were edited and no longer sum to 1.0. Reset the file and rerun.
- `yaml.scanner.ScannerError` on load. The sample inventory uses two-space indentation. If your editor expanded tabs, re-save the file as spaces only.
