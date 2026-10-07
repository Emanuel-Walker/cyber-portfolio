# Prompt-Injection-Hardened LLM SOC Triage Assistant

## Plain English

Security alerts contain attacker-controlled text.

If an AI assistant reads those alerts, the attacker may be able to place instructions inside fields such as:
- user agent
- URL
- process command line
- file name
- message text

This project tests that trust boundary.

## What I built

A local SOC triage assistant that:

- reads one alert JSON object
- sanitizes every string field
- wraps alert content as untrusted data
- calls a local Ollama model
- requires the model to return a strict JSON schema
- logs provenance for each call
- runs a 16-payload prompt-injection test harness against itself

The included sample run blocked 12 of 16 payload families.

Four bypass classes remained.

That is documented on purpose.

## Try it

Start with:

```text
QUICKSTART.md
```

The first demo is offline.

You can inspect the sanitizer without installing Ollama.

## Architecture

```text
alert JSON
   |
   v
input sanitizer
   |
   v
untrusted-field wrapper
   |
   v
local LLM
   |
   v
output schema validator
   |
   +--> valid verdict
   |
   +--> reject malformed output
```

Provenance logging records:
- input hash
- prompt version
- model
- sanitizer flags
- raw model output
- validation result

## Why the harness matters

A prompt-injection defense should be tested against attacks.

The harness injects 16 payload families into an alert field and checks whether the model's severity is improperly steered or whether malformed output gets through validation.

Sample results:

```text
code/attacks/results_sample.md
```

The failures are more useful than a fake "secure" badge.

## Known bypass classes in the sample run

The documented sample includes failures involving:
- Unicode lookalikes
- indirect severity manipulation
- context-window flooding
- polite/benign-looking framing

Read the result file for the exact behavior.

## What this proves

- attacker-controlled log text can be treated as a trust boundary
- schema validation can stop malformed downstream output
- prompt-injection controls can be tested repeatedly
- a security project can document what still fails

## What this does not prove

It does not prove:
- immunity from prompt injection
- the same 12/16 result on every model version
- production readiness
- that a sanitizer can determine whether every contextual claim is true

Model behavior changes.

Defenses need retesting.

## Project map

```text
code/triage_agent.py              main CLI
code/hardening/                   sanitizer, validator, provenance
code/attacks/                     payloads + harness
data/sample_alerts/               synthetic alerts
code/attacks/results_sample.md    documented sample result
WRITEUP.md                        deeper engineering notes
```

## Next work

- stronger Unicode-confusable handling
- corroboration against asset/context data
- canary detection for prompt leakage
- mutation testing against the sanitizer
