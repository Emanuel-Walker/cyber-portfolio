# Quickstart - Prompt-Injection-Hardened LLM Triage

## Plain English

This project asks one question:

**What happens when a security alert contains text that tries to manipulate the AI reading it?**

The first demo is fully offline. No model is required.

## 5-minute demo

### 1. Install the Python dependencies

From the portfolio root:

```bash
cd 02-llm-triage-hardened
python3 -m pip install -r code/requirements.txt
```

**PASS:** the install finishes without an error.

### 2. Inspect a poisoned alert

Run:

```bash
python3 code/demo_sanitizer.py data/sample_alerts/injected_user_agent.json
```

You should see injection signals similar to:

```text
Detected injection signals:
  - user_agent.original: ignore_instructions
  - user_agent.original: severity_override
```

The exact list may contain additional flags.

**What this proves:** the input sanitizer recognizes obvious attempts to talk to the model through attacker-controlled log fields.

### 3. See what the model would receive

Run:

```bash
python3 code/triage_agent.py \
  --input data/sample_alerts/injected_user_agent.json \
  --dry-run
```

**PASS:** the alert appears inside `<untrusted_field>` wrappers.

No Ollama call is made in dry-run mode.

## Optional: run the real local model

Install Ollama using its current official instructions.

Then:

```bash
ollama pull llama3.1:8b
ollama serve
```

Open a second terminal in this project and run:

```bash
python3 code/triage_agent.py \
  --input data/sample_alerts/suspicious_powershell.json
```

**PASS:** the agent returns structured JSON that matches the project schema.

If you see:

```text
ollama_error
```

check that `ollama serve` is still running.

## Optional: run all 16 injection tests

With Ollama running:

```bash
python3 code/attacks/run_attacks.py \
  --out code/attacks/results.md
```

A sample run included with the project blocked 12 of 16 payload families.

Your result may differ by model version and environment.

That variability is part of the lesson.

## What this proves

- attacker-controlled strings are treated as untrusted data
- model output is schema-validated before downstream use
- failures are measured instead of hidden
- prompt-injection defenses reduce risk but do not eliminate it

## What this does not prove

It does **not** prove the agent is immune to prompt injection.

The included sample results document four bypass classes.

Read:

```text
code/attacks/results_sample.md
```

## Next

Read:

```text
README.md
WRITEUP.md
```

Then inspect:

```text
code/hardening/
```
