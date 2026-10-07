# Detections

Custom detection content and the coverage comparison live here.

## Verified implementation folders

- `elastic_detection_rules/`
- `panther_rules/`

## Offline teaching demo

```text
demo_iam_detection.py
```

This small script mirrors the core IAM conditions for the public quickstart.

It is not a general Elastic query engine.

## Evidence

```text
detection_matrix.md
```

documents measured lab behavior and distinguishes:

```text
catch
partial
miss
```

Do not turn a `partial` into a guaranteed catch in public copy.
