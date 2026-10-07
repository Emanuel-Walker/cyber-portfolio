# Code

The asset scoring and alert prioritization engine lives here.

## Main scripts

```text
crown_jewel_scorer.py
run_prioritization.py
```

## Inputs

- `example_asset_inventory.yaml`
- `example_alerts.jsonl`
- `models/scoring_rubric.yaml`

## First demo

Use:

```text
../QUICKSTART.md
```

## Rule

Do not change a score factor or tier mapping in code without updating the rubric and documentation.

The scoring model should stay inspectable by a non-programmer.
