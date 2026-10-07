# Code

The LLM triage pipeline lives here.

## Start here

```text
triage_agent.py
```

Pipeline:

```text
alert -> sanitize -> prompt wrapper -> Ollama -> validate -> provenance
```

## Folders

- `hardening/` = input/output controls
- `attacks/` = adversarial test harness
- `prompts/` = system prompt
- `demo_sanitizer.py` = offline first demo

Use `../QUICKSTART.md` before reading every file.
