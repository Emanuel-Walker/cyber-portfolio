# Models

Human-editable scoring rules live here.

Current source of truth:

```text
scoring_rubric.yaml
```

The four asset factors are:

- business impact
- data sensitivity
- blast radius
- recovery cost

Do not add a hidden fifth factor only in Python.

If the model changes, update:
- rubric
- scorer
- README
- quickstart example
