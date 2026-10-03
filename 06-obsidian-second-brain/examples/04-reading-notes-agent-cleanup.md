# Example - Reading Notes to Structured Summary

**The point:** rough reading notes are low value. Structured summaries, linked to the rest of your vault, are high value. The agent does the structuring. You keep the thinking.

---

## The input

You read a technical paper and dumped notes into `00-Inbox/`. The raw file looks like this:

```
some paper about detection engineering lifecycle
3 phases but author says 5 is more honest - ideation, implementation, validation, response, retire
most teams skip validation. that is why coverage is garbage
MITRE ATT&CK references everywhere
compare to our incident response notes in projects
retire step is novel - most frameworks dont acknowledge detections should die
```

Classic brain dump. Useful fragments. No structure.

---

## The prompt

```
Read 00-Inbox/raw_detection_eng_notes.md. Produce a clean reading note in
05-Resources/Detection_Engineering/<paper_slug>.md with:

1. One-sentence summary.
2. The core model (3 to 7 bullets).
3. What is novel or contrarian in this piece.
4. How it connects to existing notes in the vault. Specifically check for links to
   03-Projects/, 05-Resources/Security/, and any ATT&CK-related notes.
5. What I disagreed with or want to pressure-test.
6. Three questions I would ask the author.

Use operational voice. No em dashes. No AI vocabulary.
Tag status/needs-review.
```

---

## The output

```markdown
---
tags:
  - type/reading-note
  - topic/detection-engineering
  - status/needs-review
source: 
read-date: 2026-10-01
---

# Detection Engineering Lifecycle - Five Phases

## Summary
A reframing of the detection engineering lifecycle from 3 phases to 5, naming
validation and retirement as the two most-skipped steps.

## The core model
- **Ideation** - what are we trying to catch and why
- **Implementation** - write the detection, deploy it
- **Validation** - prove it fires on the real behavior and only on the real behavior
- **Response** - the detection fires, now what
- **Retirement** - the detection is noisy, outdated, or redundant - kill it

## What is novel
- Explicit retirement step. Most frameworks treat detections as additive forever.
- Validation elevated to a peer phase, not a sub-step of implementation.

## Connections in the vault
- [[03-Projects/Threat_Hunting_Program/00_Index]] - our validation gap is the same one
- [[05-Resources/Security/MITRE_ATTACK_Reference]] - author leans heavily on this taxonomy
- [[05-Resources/Security/Incident_Response_Playbook]] - response phase overlaps with our existing playbook

## Pushback
- The retirement step is right in spirit but the author gives no criteria for when to retire.
  A detection with 2% true positive rate on monitored behavior might still be worth keeping
  if the alternative is blind spots. Need a cost model.
- Author assumes a mature detection team. Teams of two cannot run a 5-phase lifecycle.

## Questions for the author
1. What is the retirement criteria? Specifically, when does noise outweigh signal?
2. How does this model scale down to a 1-person detection team?
3. Is validation separate from CI, or is validation CI?

> [!question]
> Can we adopt the 5-phase model in our next quarterly plan without blowing up the roadmap?
```

Note what the agent did and did not do:

- It did add structure, link to existing vault notes, and tag the file for review.
- It did not invent citations. It left the `source:` field blank for you to fill.
- It did not change your opinions. The pushback section used your actual critique.
- It added a `> [!question]` callout that you can revisit on your next weekly review pass.

---

## Why this compounds

Six months in, you have 40 reading notes in the same shape. The agent can scan all of them and tell you "every paper you read on detection engineering flags validation as the broken step. That is a signal you keep returning to. Is it the next project?" You could not get that answer from raw notes. You can get it from structured ones.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
