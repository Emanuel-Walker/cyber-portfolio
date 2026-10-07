# Companion Agent

The Companion Agent is the **daily-use assistant** that talks with you.

Examples might include:

- Muse
- Dot
- ChatGPT
- Claude
- another conversational assistant

This folder describes a pattern.

It does **not** claim that every companion product automatically connects to Obsidian.

The safest model is:

```text
Obsidian Vault
      |
      v
Vault Agent
Codex / Claude Code
      |
      v
Curated Context Pack
      |
      v
Companion Agent
Muse / Dot / ChatGPT / Claude / other
```

The Companion Agent should not be your file-maintenance worker.

That is the Vault Agent's job.

---

# What the Companion Agent is for

Good daily uses:

- morning planning
- quick capture
- decision support
- study prompts
- project check-ins
- reflection
- reminders about active priorities
- turning conversation into a clean Vault Capture

The companion is the conversational layer.

The vault remains the inspectable memory layer.

---

# The companion context folder inside your vault

Create:

```text
99-System/companion/
```

Use these files:

```text
99-System/companion/
├── ABOUT-ME.md
├── CURRENT-SEASON.md
├── PROJECTS.md
├── COMPANION-RULES.md
└── CONTEXT-PACK.md
```

## ABOUT-ME.md

Stable context.

Keep it short.

```markdown
# About Me

## Basics
- Name:
- Role:
- Time zone:
- What I am building toward:

## How I work
- I prefer:
- I dislike:
- When I get stuck:
- A useful assistant response looks like:

## Boundaries
- Never:
- Always ask before:
```

## CURRENT-SEASON.md

What matters **now**.

```markdown
# Current Season

## Top three priorities
1.
2.
3.

## What I am not focusing on
-

## Real deadlines
-

## Current constraints
-
```

## PROJECTS.md

A tiny index.

```markdown
# Active Projects

| Project | Status | Next action |
|---|---|---|
| Second Brain Setup | Active | Capture one real note |
```

Do not paste 200 project notes into the companion.

## COMPANION-RULES.md

How the companion should behave.

Starter version:

```markdown
# Companion Rules

- Use the context I provide.
- Do not invent memories.
- If a missing fact could change the answer, ask.
- Keep daily guidance concise.
- Do not guilt me about missed days or streaks.
- Do not act like you have direct access to my vault unless you actually do.
- Prefer one useful next action.
- Separate fact from inference.
```

---

# Build the Context Pack

The Context Pack is the small file that leaves the vault.

Ask the Vault Agent:

```text
Read only:

99-System/companion/ABOUT-ME.md
99-System/companion/CURRENT-SEASON.md
99-System/companion/PROJECTS.md
99-System/companion/COMPANION-RULES.md

Create:

99-System/companion/CONTEXT-PACK.md

Use this structure:

# Companion Context Pack
## About Me
## Current Priorities
## Active Projects
## Interaction Rules
## Last Updated
## Sources

Keep the file under 1,500 words.

Do not add information that is not supported by the source files.
```

Read the generated file yourself.

That is the file you share.

---

# How to sync context with a companion

Different companion products support different features.

Use the least-permission option available.

## Option 1 — File upload

Upload:

```text
CONTEXT-PACK.md
```

Then say:

```text
Use this as my current context.

It may become stale.

If something is missing or contradictory, ask me instead of inventing an answer.
```

## Option 2 — Persistent knowledge/context feature

If your companion supports a knowledge, memory, file, or workspace feature:

Add the **curated companion files** or Context Pack.

Do not connect the entire vault by default.

## Option 3 — Connector or automated sync

If the companion supports a legitimate connector or integration:

Scope it to:

```text
99-System/companion/
```

when possible.

Do not grant write access just because read access is available.

## Option 4 — Manual paste

Paste CONTEXT-PACK.md into the conversation.

This is boring.

It is also easy to understand and audit.

---

# First companion prompt

After providing the context:

```text
You are my daily Companion Agent.

Use the companion context I provided.

Your job is to help me:
- remember current priorities
- think through decisions
- capture useful information
- stay oriented to active projects

Do not claim access to files or systems you cannot actually access.

Do not invent memories.

If something should be saved to my vault, create a Vault Capture instead of pretending you saved it.

Keep normal daily answers concise unless I ask for depth.

When useful, end with one concrete next action.
```

---

# Morning prompt

```text
Good morning.

Based only on my current companion context:

1. What are my three active priorities?
2. What is the one thing most worth moving today?
3. What can probably wait?
4. What information is stale or missing?

Keep it short.
```

# Midday reset

```text
I got pulled off track.

Using my current priorities, give me:

1. what I was trying to move
2. one 20-minute next action
3. one thing I can ignore until later

Do not create a full new plan.
```

# Decision prompt

```text
I need to decide this:

[DECISION]

Use my current context.

Give me:
- the real decision
- the strongest option
- the biggest tradeoff
- what missing fact could change the recommendation

Do not give me five equally weighted options unless the decision is genuinely ambiguous.
```

# End-of-day prompt

```text
Help me close the day.

Ask me only what you need to produce:

- what moved
- what is still open
- what matters tomorrow
- anything worth saving to the vault

Then produce a Vault Capture.
```

---

# Vault Capture format

The Companion Agent should not silently edit the vault.

Ask it to produce:

```text
VAULT CAPTURE

Type:
Suggested destination:
Summary:
Facts to preserve:
Next action:
Questions / uncertainty:
```

Then give that block to the Vault Agent:

```text
Process this Vault Capture.

Show me the proposed file changes first.

Do not write anything until I approve.

[PASTE VAULT CAPTURE]
```

---

# Refresh the companion context

Do this when:

- priorities materially change
- a major project starts/ends
- the companion repeatedly references stale context
- once a week, if weekly refresh is useful to you

Ask the Vault Agent:

```text
Refresh 99-System/companion/CONTEXT-PACK.md from the four source files.

Show me a short diff summary afterward.

Do not add inferred facts.
```

Then replace/update the companion's old context.

---

# Privacy rules

Do not put these in the Context Pack:

- passwords
- API keys
- private keys
- recovery codes
- banking credentials
- government identification numbers
- information you do not want sent to the companion's provider

The Context Pack should be useful without becoming a copy of your private life.

---

# Companion architecture rule

Keep this boundary:

```text
Vault Agent = write/organize
Companion Agent = converse/capture
```

A product can eventually do both.

But you should only combine those roles after you can explain:

- what it can read
- what it can write
- where memory lives
- how you correct it
- how you revoke access
- what leaves your device

Until then, separation is a feature.


---

# Supporting examples

The README is the canonical guide.

Small copyable examples live under:

```text
companion-agent/examples/
├── CONTEXT-PACK.example.md
└── VAULT-CAPTURE.example.md
```

Use them as shapes, not personal-data templates.
