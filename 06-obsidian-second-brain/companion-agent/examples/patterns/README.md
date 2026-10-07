# Companion patterns

These are three ways to shape a daily companion without changing the underlying vault architecture.

The names are shorthand for interaction styles, not claims about vendor features.

## Muse pattern — chief of staff

Use when you want the companion to help with:

- weekly planning
- project orientation
- meeting preparation
- next-action triage
- staying aware of current priorities

Context emphasis:

```text
CURRENT-SEASON.md
PROJECTS.md
PEOPLE summaries
COMPANION-RULES.md
```

Daily prompt:

```text
Using my current context:

1. What are the three things most worth moving today?
2. What has a real deadline?
3. What can wait?
4. Give me one concrete next action for the top priority.
```

## Dot pattern — reflective companion

Use when you want:

- end-of-day reflection
- journaling prompts
- noticing repeated themes
- lightweight emotional/context check-ins

Context emphasis:

```text
ABOUT-ME.md
CURRENT-SEASON.md
recent daily-note summaries
COMPANION-RULES.md
```

Daily prompt:

```text
Help me close the day.

Ask:
- what mattered
- what felt unfinished
- what I learned
- what is worth carrying into tomorrow

Then create a Vault Capture only for information worth preserving.
```

Reflection is not diagnosis.

## Grok-style pattern — lean factual context

Use when you want:

- fast factual recall
- minimal context
- short direct answers
- hard boundaries

Context emphasis:

```text
ABOUT-ME.md
CURRENT-SEASON.md
PROJECTS.md
COMPANION-RULES.md
```

Keep the Context Pack short.

Prompt:

```text
Use only the context I provided.

Answer directly.

If the answer depends on a fact that is not present, say what is missing instead of guessing.
```

## The architecture does not change

All three use the same boundary:

```text
Obsidian Vault
   |
Vault Agent
   |
curated Context Pack
   |
Companion Agent
   |
Vault Capture
   |
Vault Agent
```

Pick the interaction style that fits the job.

Do not redesign the vault for every companion product.
