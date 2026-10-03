# Detection-as-Code with ADS Discipline

Picture a Monday morning. The weekend on-call is wrecked. Ten thousand alerts hit the queue from a rule that shipped Friday afternoon. Nobody trusts the detection pack anymore.

This repo is the answer to that Monday. A detection pack that refuses to merge until the rule proves itself.

Every rule here ships with a written spec, a positive test that must trigger it, and a benign test that must not. CI blocks the PR if any of the three are missing. The point is not more rules. The point is rules you can trust at 3 a.m.

Built after I watched a single PowerShell rule generate 10,000 false positives over a weekend. Full story in `WRITEUP.md`.

## What it does

- Lints Sigma rules (vendor-agnostic detection logic you can convert into Elastic KQL or Splunk SPL) on every pull request
- Requires a Palantir-style ADS spec (Alerting and Detection Strategy, a documentation format that answers "why does this rule exist and what does it miss") next to every rule
- Runs an Atomic Red Team style positive test (Atomic Red Team is an open-source library of attack technique tests you can run against your own detections). The rule must fire.
- Runs a benign test (the rule must not fire)
- Converts validated Sigma to Elastic KQL (Kibana Query Language, used in Elastic) as an artifact

## Quick start

```bash
pip install -r code/requirements.txt
pytest code/tests/ -v
python code/converters/sigma_to_elastic.py code/rules/suspicious_powershell_download.yml
```

## How it works

See `diagrams/detection_pipeline.drawio`.

A pull request opens against `main`. The CI job walks `code/rules/`, pairs each `.yml` with its `.ads.md`, and fails fast if either is missing. For every pair, pytest loads the matching atomic test from `code/tests/atomic_tests/` and the matching benign file from `code/tests/benign/`. Each telemetry event runs against the rule logic. The rule must match every positive event and zero benign events. Only then does the converter emit the backend query artifact. Reviewers see test results inline on the PR. Nothing merges on a red build.

Why this matters. One rule, three SIEMs. If your shop ever migrates vendors, the detection content moves with you.

## What I learned

Writing the spec first changed everything. When I had to describe the detection strategy in English before writing YAML, half of my ideas died on the page. The ones that survived were sharper. The ADS forced me to name blind spots instead of hoping nobody would ask. "This fires on `powershell.exe -Command (New-Object Net.WebClient).DownloadString`" is a hypothesis. The atomic test is the experiment.

The second lesson was about negative tests. Positive tests are easy to write because you built the rule to catch that thing. Benign tests are humbling. The first time I ran my admin-script fixture through the download-cradle rule, it fired. The rule did not know the difference between an attacker pulling a payload and a sysadmin pulling a module from an internal repo. That is not a tuning problem. That is a design problem. The benign test caught it before prod did.

The last lesson was quieter. Detection engineering is not about writing rules. It is about building a system where bad rules cannot ship. The pipeline is the product.

## What's next

- Add Sigma backend tests for Splunk and Microsoft Sentinel
- Pull real ATT&CK Navigator coverage from the ADS categorization fields
- Wire a nightly re-run against fresh atomic telemetry so drift surfaces
- Replace the hand-rolled Sigma parser with pySigma once I trust the matching logic
- Add a `severity-drift` check that fails if a rule's priority changes without a spec update
