# Tests

These tests are the merge gate.

They prove two different things:

```text
positive test -> attack-like event must match
benign test   -> normal event must not match
```

Both matter.

Run:

```bash
pytest code/tests/ -v
```

A detection that catches the bad event but also catches normal administration is not ready.
