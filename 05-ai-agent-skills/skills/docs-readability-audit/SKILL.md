---
name: docs-readability-audit
description: Audit technical docs for plain-English readability and followability. Use when asked to review a README, quickstart, walkthrough, setup guide, or documentation for beginners.
offline: true
metadata:
  inspiration: vercel-labs/agent-skills writing-guidelines
---

# Docs Readability Audit

Make documentation usable by a tired person who does not already know the project.

## Trigger

Use this skill for:
- README reviews
- setup guides
- quickstarts
- walkthroughs
- public portfolio project pages
- "make this easier to follow"
- "ADHD pass"
- "read this out loud"

## The reader test

Assume the reader:
- found the repo five minutes ago
- does not know the acronyms
- will copy commands exactly
- may stop after the first error
- may return tomorrow and forget where they were

## Audit order

### 1. Plain-English opening

The first screen should answer:

1. What is this?
2. What problem does it solve?
3. What will I have when I finish?
4. How long is the first useful demo?
5. Does it cost money?

Flag any opening that begins with implementation details before answering those questions.

### 2. Jargon

On first use:
- spell out the acronym
- explain it in one sentence
- then use the acronym normally

Bad:

```text
Deploy the DCR to LAW and validate AMA.
```

Better:

```text
Create the Data Collection Rule (DCR). It tells Azure Monitor Agent what logs to send to the Log Analytics workspace.
```

### 3. Action order

Every numbered step should contain one primary action.

Prefer:

```text
Run:
[command]

PASS:
[expected result]

STOP:
[what failure means]
```

Do not hide three required actions inside one paragraph.

### 4. Copy-paste safety

Check every command for:
- current working directory assumptions
- placeholders
- shell type
- destructive behavior
- cloud cost
- credentials
- missing prerequisites

Prefer commands that work from repo root.

Prefer:

```bash
terraform -chdir=infra/aws plan
```

over instructions that depend on remembering which directory the user entered five steps ago.

### 5. Placeholders

Use unmistakable placeholders:

```text
[YOUR_API_KEY]
[AWS_REGION]
[VAULT_PATH]
```

Never use realistic fake secrets.

List all required placeholders before the first command that needs them.

### 6. Expected result

After every major command, explain what success looks like.

The reader should never have to ask:

> Did that work?

### 7. Resume point

Long guides need a visible checkpoint or status file.

A returning reader should know the next action in under one minute.

### 8. Read-aloud pass

Read the instructions as spoken language.

Flag:
- sentences that require a second read
- nested parentheticals
- unexplained acronyms
- paragraphs containing more than one decision
- references like "the above" or "as mentioned earlier"
- contradictions between buy order and build order
- stale paths

## Output

Return findings ranked by impact:

```text
CRITICAL
path:line - blocker

HIGH
path:line - likely confusion

MEDIUM
path:line - friction

PASS
what already works
```

Then propose exact replacement wording for every CRITICAL and HIGH issue.

## Before handoff

- [ ] Beginner can explain the project after reading the first screen.
- [ ] First useful demo is obvious.
- [ ] Commands can be copied.
- [ ] Placeholders are visible.
- [ ] PASS conditions exist.
- [ ] STOP conditions exist for risky steps.
- [ ] Jargon is explained once.
- [ ] Destructive and billable steps are labeled.
- [ ] A returning user knows where to resume.
