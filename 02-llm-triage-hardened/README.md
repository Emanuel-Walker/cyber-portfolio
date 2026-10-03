# Prompt-Injection-Hardened LLM SOC Triage Assistant

A local-only LLM triage agent that reads SIEM-style alerts and returns structured
severity, ATT&CK mapping, and suggested actions. The twist: it ships with a prompt
injection test harness that fires 16 attack payloads at the agent and tells you,
in plain English, which ones got through.

If the Tier 1 queue in 2026 is going to lean on language models, those models
have to survive attacker-controlled strings in log fields. That is the whole
problem this project tries to measure honestly.

Companion to "The Agent on the Desk" (Gray Space, June 2026). That essay named the problem. This repo ships the fix.

## What it does

- Takes an Elastic-style alert JSON on stdin and returns a strict JSON verdict
- Runs every untrusted field through a sanitizer that encodes, caps, and flags
- Validates model output against a JSON schema and rejects freeform drift
- Logs provenance for every call: input hash, prompt version, model, raw output
- Ships 16 named injection payloads and a runner that scores them pass or fail

## Quick start

```bash
ollama pull llama3.1:8b
pip install -r code/requirements.txt
cat data/sample_alerts/suspicious_powershell.json | python code/triage_agent.py
```

To run the attack harness against the agent:

```bash
python code/attacks/run_attacks.py --out code/attacks/results.md
```

## How it works

Alert JSON lands on stdin. The input sanitizer walks every string field marked
untrusted, caps length, strips markdown and control characters, and flags
suspicious patterns. The sanitized payload gets wrapped in XML-like delimiters
and dropped into a static system prompt. Ollama returns a response. The output
validator parses it against a JSON schema. Anything that does not match gets
rejected and logged as a failure, not a verdict. See `diagrams/architecture.drawio`.

## What I learned

Hardening is a filter, not a wall. In the harness run that ships in
`code/attacks/results_sample.md`, 12 of 16 payload families were blocked at the
sanitizer or the output validator. Four slipped through.

The ones that got through were not the loud ones. Direct "IGNORE PREVIOUS
INSTRUCTIONS" strings were easy. The attacks that worked were the quiet ones:

- Unicode homoglyphs that render as "severity" but hash as something else
- Context window flood that pushed real alert content past the attention budget
- Benign-looking wrappers that framed the injection as a legitimate alert field
- Base64-encoded instructions the model decoded on its own and followed

The sanitizer caught the obvious stuff. The model still has judgment problems
when the attacker is polite.

## What's next

- Add an output-side heuristic that compares severity against alert field stats
- Try a second model as a judge on the first model's output
- Add a canary token in the system prompt and detect leakage in output
- Fuzz the sanitizer itself with mutation testing

License: MIT. Not affiliated with any employer. No real alerts included.
