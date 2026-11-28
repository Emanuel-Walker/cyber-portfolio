# AGENTS.md - Cyber Portfolio

This file is for coding agents working on this public portfolio.

Human entry point:

```text
README.md
```

## Purpose

This repository is a public portfolio of completed cybersecurity, cloud, AI, and knowledge-system projects. Project 1 (Maniverse AI Lab), Project 4 (Neuply) and Project 5 (Pip) are write-ups. Their code is not in this repo, so their claims rest on screenshots, test results and a written account.

Do not mix private R&D into the public portfolio.

A project belongs here only when the artifact exists and the claim can be demonstrated from the repository.

## Project map

```text
01-maniverse-ai-lab/
02-ai-agent-skills/
03-obsidian-second-brain/
04-neuply/
05-pip/
06-detection-as-code/
07-llm-triage-hardened/
08-crown-jewel-triage/
09-identity-cloud-ir/
website/
```

## Documentation rule

Every project should answer:

1. What problem does this solve?
2. What did Emanuel build?
3. What can a reader run right now?
4. What should happen when it works?
5. What does the project not prove?

Prefer:
- plain English before jargon
- copy-paste commands
- one primary action per numbered step
- PASS / STOP checks
- explicit cost and safety warnings

## Claim rule

Never write a public claim just because it sounds plausible.

Before adding a claim:
- verify the file exists
- verify the command exists
- verify the backend/integration is actually implemented
- distinguish sample results from guarantees
- label future work as future work

Examples:
- do not claim Splunk conversion if only Elastic conversion exists
- do not claim private Muse hardware integrations in Project 3
- do not turn a documented test result into a universal security guarantee

## Public/private boundary

The public Second Brain is:
- Obsidian / Markdown
- agent charters
- workflows
- security guidance
- ADHD-friendly usage rules
- companion-memory patterns

Project 1 is a write-up only. Its Azure section is planned and must stay labeled as planned until real screenshots exist. Never add results, counts or screenshots for work that has not been done. The write-up also leaves out the voice robot because it is not built.

Neuply and Pip are write-ups only. Do not publish their source code here unless the owner says so. Do not claim a real iPhone test, App Store release, real users or live AI features until they exist.

Private Muse hardware, StackChan, Raspberry Pi gadget bridges, projection mapping, and unfinished experiments do not belong here until they are independently built, tested, and intentionally published.

## Project 2 skills

Reusable skills live at:

```text
02-ai-agent-skills/skills/<skill-name>/SKILL.md
```

Read the matching skill when relevant.

Useful review skills:
- `docs-readability-audit`
- `web-ui-audit`
- `repo-onboarding-audit`
- `builder-walkthrough`
- `companion-context`

## Before changing a project README

Verify every referenced path.

A project README walkthrough must not contain:
- nonexistent files
- unsupported command flags
- stale counts
- placeholder secrets that look real

## Safety

Cloud and offensive-security examples must stay inside owned or explicitly authorized labs.

Do not weaken scope checks or teardown instructions for convenience.

## Before handoff

- [ ] changed paths exist
- [ ] commands match the code's actual CLI
- [ ] counts match the sample data
- [ ] website copy matches README claims
- [ ] resume copy matches implemented artifacts
- [ ] no private R&D leaked into public docs
- [ ] third-party adaptations are attributed
