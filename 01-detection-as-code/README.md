# Detection-as-Code with ADS Discipline

## Plain English

Security detection rules are software.

They should be tested like software.

This project blocks a rule from shipping unless it has:

1. a written detection strategy
2. a malicious test that must fire
3. a benign test that must stay quiet

That is the project.

## Why I built it

A noisy rule can bury analysts in alerts.

A weak rule can miss the activity it was written to catch.

The fix is not "write better rules."

The fix is a pipeline that forces every rule to prove itself before merge.

## What it does

- stores detection logic in Sigma YAML
- requires an Alerting and Detection Strategy (ADS) document beside each rule
- runs positive tests against attack-like synthetic events
- runs negative tests against benign synthetic events
- blocks the CI pipeline when coverage is missing or a test fails
- converts the validated Sigma rule into Elastic KQL

## Try it

Open:

```text
QUICKSTART.md
```

The demo runs the tests and converts one rule to Elastic KQL.

## How it works

```text
Sigma rule
   |
   +--> ADS strategy exists?
   |
   +--> malicious test fires?
   |
   +--> benign test stays quiet?
   |
   v
CI passes
   |
   v
Elastic query artifact
```

See:

```text
diagrams/detection_pipeline.drawio
```

## Why Sigma

Sigma keeps the detection logic separate from one SIEM vendor.

This project currently includes an **Elastic KQL converter**.

Additional backends are future work.

Do not read "vendor-neutral rule format" as "every SIEM converter is already implemented."

## What I learned

The written strategy catches weak ideas before code does.

A rule may sound reasonable until you have to explain:
- exactly what behavior it detects
- what data it requires
- what normal activity looks similar
- what it will miss

The benign test matters just as much as the malicious test.

A rule that catches attackers and floods analysts is still a bad production rule.

## What this proves

- detection rules can be tested in CI
- false-positive checks can block merge
- documentation can be part of the engineering contract
- one source rule can produce an Elastic query artifact

## What this does not prove

Synthetic tests are not production validation.

A real environment still needs:
- correct telemetry
- baselining
- tuning
- change management
- analyst feedback

## Next work

- add tested Splunk and Microsoft Sentinel backends
- add ATT&CK Navigator coverage generation
- run detections against fresh telemetry on a schedule
- replace the small custom parser with pySigma where it improves reliability
