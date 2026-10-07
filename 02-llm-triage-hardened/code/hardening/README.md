# Hardening

Security controls around the model live here.

## Responsibilities

- sanitize untrusted alert fields
- constrain model output
- log provenance

These controls reduce risk.

They do not make prompt injection impossible.

## Rule

When changing a control:

1. rerun the offline sanitizer demo
2. rerun the 16-case attack harness when Ollama is available
3. update `attacks/results_sample.md` only when you actually performed a new sample run

Do not turn a heuristic improvement into a universal security claim.
