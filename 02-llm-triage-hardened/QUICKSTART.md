# Quickstart - Prompt-Injection-Hardened LLM Triage

## 5-minute demo

BLUF. You will run the triage agent on a clean alert and a poisoned alert, then run the 16-payload attack harness. The agent should return structured P-levels on both alerts and the harness should block 12 of 16 attacks.

Prerequisites.

```bash
# Ollama local LLM runtime
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.1:8b
ollama serve &
# Python deps
pip install pydantic jsonschema requests
```

Step 1 - setup.

```bash
cd 02-llm-triage-hardened
pip install -r code/requirements.txt
```

What you see. Pydantic, jsonschema, and the Ollama client install cleanly. `ollama list` shows `llama3.1:8b` in the local model table.

Step 2 - run the agent on a benign alert.

```bash
python code/triage_agent.py --alert data/alerts/benign_login.json
```

What you see. Structured JSON on stdout. Priority is `P4`. The `rationale` field is one short paragraph. The `schema_valid` field is `true`. Something like:

```json
{"priority": "P4", "rationale": "Successful login from a known...", "schema_valid": true, "provenance": {...}}
```

Step 2b - run the agent on a prompt-injected alert.

```bash
python code/triage_agent.py --alert data/alerts/injected_phishing.json
```

What you see. The agent returns a valid P-level anyway (usually P2 or P3). The injection payload in the alert body does not change the output schema. The agent either refuses the injected instruction outright or reports the attempt in the rationale and still returns a well-formed P-level.

Step 3 - run the attack harness.

```bash
python code/attacks/run_attacks.py
```

What you see. Sixteen payloads fire against the agent one at a time. The harness prints a results table and a final tally. Expect `12/16 blocked, 4/16 bypassed`. The four bypasses are named in the output (role-play framing, nested instruction wrapper, Unicode confusable, chained-tool reference).

Step 3b - validate.

Open `code/attacks/results_sample.md` and compare it to your run. Your bypass count should match within one. If every attack succeeds, the hardening prompt did not load. Check that `code/hardening/system_prompt.md` is being read by `triage_agent.py`.

## What this proves

- Local LLM wired into a defensive workflow with schema-validated output, so a model drift or injection cannot corrupt downstream automation.
- Honest red-team of my own system with a named list of what still breaks, not a marketing claim of full coverage.
- Companion engineering to a published essay, showing I ship the code that backs the argument.

## Add screenshots here

Capture these while running the demo and drop them in a `screenshots/` folder next to this file.

- `screenshots/01-benign-alert-p4.png` - agent output on `benign_login.json`
- `screenshots/02-injected-alert-held.png` - agent output on `injected_phishing.json` with injection resisted
- `screenshots/03-attack-harness-table.png` - 12/16 blocked table
- `screenshots/04-bypass-named.png` - one of the 4 bypasses with the rationale showing why it slipped
- `screenshots/05-schema-validation.png` - a schema-valid output next to a schema-invalid one (force an invalid run by stripping the hardening prompt)

## Common issues

- `connection refused on 127.0.0.1:11434`. Ollama is not running. Start it with `ollama serve` and confirm with `curl http://127.0.0.1:11434/api/tags`.
- First call takes 60+ seconds. The model is loading into memory. Subsequent calls return in 3 to 8 seconds on a modern laptop.
- Attack harness reports `0/16 blocked`. The hardening prompt is not being injected. Verify the agent loads `code/hardening/system_prompt.md` before each call and that the file is not empty.
