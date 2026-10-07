# Attack harness

This folder measures whether untrusted text can steer the triage model.

## Run

With Ollama running:

```bash
python3 code/attacks/run_attacks.py --out code/attacks/results.md
```

Offline inspection:

```bash
python3 code/attacks/run_attacks.py --dry-run
```

## Important

A changed model version may produce a changed score.

The harness is the durable artifact.

The sample score is not a guarantee.
