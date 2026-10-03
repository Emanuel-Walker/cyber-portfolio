# The Weekend 10,000 Alerts Taught Me To Stop Writing Rules

It was a Friday push. The rule was eighteen lines of Sigma. It looked for `powershell.exe` with a command line containing `DownloadString` or `IEX`. Classic download cradle. I had tested it in my lab against an Atomic Red Team payload and it caught every variant. I merged it, kicked off the deploy, and went to dinner.

Saturday morning the on-call ping came in. 2,400 alerts overnight. By Sunday it was past 10,000. Every one of them was a legitimate configuration management agent pulling modules from an internal artifact server. The rule did exactly what I asked it to do. I just had not asked carefully enough.

That Monday the team lead did not yell. She said one thing: "I do not trust the detection pack anymore." That was worse than yelling. The whole value of a SOC detection is that an analyst picks up the ticket believing it means something. Burn that trust and every rule in the pack is now suspect. Nobody triages hard when they expect false positives.

## The problem

Detection engineering suffers from the same disease as early-career software engineering. We ship code without tests because the code is small and the author is confident. Then we go home. The code runs for 72 hours against production traffic we never saw in the lab, and we come back to a graveyard.

I needed a system where I could not ship a rule unless three things existed. One: a written spec explaining what the rule does, why it fires, what it misses, and when it will false-positive. Two: a positive test with telemetry that must trigger the rule. Three: a benign test with telemetry that must not. If any of those were missing, the pull request stays open.

## The build

The spec format is lifted straight from Palantir's Alerting and Detection Strategy framework. It is not a template to decorate the YAML. It is the design doc that forces you to think before you type. Here is the categorization block for my rebuilt PowerShell rule.

```markdown
## Categorization
- ATT&CK Technique: T1059.001 (PowerShell)
- ATT&CK Sub-Technique: T1105 (Ingress Tool Transfer)
- Kill Chain Phase: Delivery, Installation
```

Simple. But writing it meant I had to decide: is this a PowerShell abuse detection, or a download-cradle detection? The answer changes what field I key on. The first version keyed on `process.name == powershell.exe`. The rebuild keys on `process.command_line` patterns that are specific to in-memory download, with `powershell.exe` as a secondary filter. Different ATT&CK ID, different detection surface.

The CI side was a GitHub Actions workflow. The core idea is a pytest harness that walks the rules directory and refuses to pass if any rule is naked.

```python
def test_every_rule_has_spec_and_tests(rule_path):
    """
    This test is the gate. If it fails, the PR cannot merge.
    We check three things for every Sigma rule.
    First the ADS spec file exists next to it.
    Second a positive atomic test exists for the rule's ATT&CK ID.
    Third a benign fixture exists under the same ATT&CK ID.
    """
    ads_path = rule_path.with_suffix(".ads.md")
    assert ads_path.exists(), f"Missing ADS spec for {rule_path.name}"
```

The matching logic reads each event in the atomic YAML, applies the Sigma selection logic, and asserts a match. Then it runs the benign file and asserts no match. Both halves have to pass. If a rule catches the attacker telemetry but also lights up the backup agent, the build fails and tells you which event broke it.

The converter is a hundred lines of straight Python that walks a Sigma detection block and emits a KQL string suitable for Elastic. I did not use pySigma on purpose. I wanted to understand the mapping before I imported it. The converter is also exercised by the test suite, which means a bad field mapping gets caught before a backend ever sees the query.

## The gotcha

The honest ugly part. My first benign test was too clean. It was a fixture of `powershell.exe -NoProfile -Command Get-Service`. Of course the rule did not fire on that. The rule was never going to fire on that. I was patting myself on the back for passing a test that was not a test.

The second pass I grabbed real sanitized telemetry from the weekend blowup. The config agent did `powershell.exe -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadString('https://internal-artifacts/...')"`. That is the exact pattern my old rule caught. If my new rule still caught it, I had learned nothing.

I had to add a filter on the destination domain and a hash check on the parent process. Both are documented in the ADS Blind Spots section because now the rule misses a scenario where an attacker lives inside the internal artifact server. That is a real gap. The ADS writes it down instead of pretending it does not exist.

## Results

In lab testing the new rule catches eight out of nine Atomic Red Team variants of T1059.001 download cradles. The ninth uses a base64-encoded command and will be covered by a separate decoder rule I have not written yet. False positive rate on the sanitized production weekend is zero out of the 10,000 historical alerts. The one weakness is documented. The spec, the positive test, and the benign test all shipped in the same pull request.

More important than the numbers: nobody on the team has asked me "do I need to triage this one or is it probably noise" since the pipeline went live. The ticket shows up, they work it. That is the whole job.

## Three takeaways you can steal

**Write the spec first, write the rule second.** If you cannot explain in a paragraph why the rule fires, you cannot explain in a ticket why the analyst should care. The ADS is not paperwork. It is the design.

**Benign tests are harder than positive tests. Prioritize them.** A positive test proves your rule works on the thing you built it for. A benign test proves it does not work on the thing you did not. The second question is where production breaks you.

**Make the pipeline refuse the merge, not the human.** Code review catches typos. Code review does not catch "this rule will false-positive at 2 a.m. on Sunday." Only a test does. Put the test in CI and let it be the one that says no.
