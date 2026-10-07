# Attack scenarios

Controlled AWS lab scenarios live here.

## Rule

These scenarios are for:

```text
owned or explicitly authorized lab resources only
```

Each scenario should explain:
- what behavior it produces
- what telemetry should record it
- what native GuardDuty behavior is expected
- what custom detection should see it
- how cleanup works

## Offline demo events

```text
demo_events/
```

contains synthetic JSON for the no-AWS quickstart.

Those files do not execute an attack.
