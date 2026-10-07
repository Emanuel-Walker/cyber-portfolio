---
name: repo-onboarding-audit
description: Audit a repository so a new human or coding agent can understand, build, test, and safely modify it. Use for repo cleanup, AGENTS.md creation, onboarding docs, or "make this repo agent-ready".
offline: true
metadata:
  inspiration: facebookincubator/muse-gadget-sdk AGENTS.md structure
---

# Repo Onboarding Audit

A good repo should work for two readers:

1. a human who wants the shortest useful path
2. an agent that needs exact technical rules

Do not force one document to do both jobs.

## Required layers

### Human README

Must explain:
- what the project is
- who it is for
- first useful result
- prerequisites
- one copy-paste start
- where to go next

### QUICKSTART or START_HERE

Must be executable.

Use:
- numbered steps
- commands
- PASS checks
- STOP checks
- cleanup

### AGENTS.md

Use for the technical operating contract:
- architecture
- supported environments
- exact tool versions
- build commands
- tests
- file ownership
- dangerous operations
- debugging signals
- "before handoff" checklist

## Audit questions

- Is there one obvious first file?
- Are supported platforms explicit?
- Are exact versions pinned where version drift breaks builds?
- Can the project be tested without hardware?
- Does hardware/cloud work have a dry-run path?
- Are secrets kept out of git?
- Are external dependencies licensed and attributed?
- Is there one canonical install path?
- Can an agent know what not to change?
- Is there a health signal after deployment?
- Is teardown documented?

## Agent handoff checklist

Before an agent says "done":

- [ ] tests run
- [ ] build succeeds
- [ ] docs match current paths
- [ ] no placeholder was silently guessed
- [ ] no secret entered source control
- [ ] changed behavior has a test or verification step
- [ ] destructive changes were confirmed
- [ ] new third-party code has license notes
