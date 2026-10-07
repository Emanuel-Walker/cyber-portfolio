# Detection rules

Sigma source rules live here.

Each rule should have a matching written detection strategy and tests.

When adding a rule:

1. write the strategy
2. add malicious telemetry
3. add benign telemetry
4. run pytest
5. convert the rule
6. review the output

Do not merge a rule because the YAML parses.
