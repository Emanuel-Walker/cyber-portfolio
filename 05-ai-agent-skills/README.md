---
title: AI Agent Skills
updated: 2026-10-07
---

# AI Agent Skills

## Plain English

A skill is a small instruction file that teaches an AI agent how to do one repeatable job.

Instead of pasting the same giant prompt every time, you install the skill once.

Then the agent can load it when the task matches.

This repo contains **15 reusable skills**.

## Try one in 5 minutes

Open:

```text
QUICKSTART.md
```

The demo installs the `humanizer` skill and uses it to rewrite an AI-sounding paragraph.

## The 15 skills

| Skill | What it does |
|---|---|
| `content-engine` | Drafts platform-specific content from an approved seed. |
| `humanizer` | Removes common AI-writing tells while preserving meaning. |
| `article-writing` | Drafts long-form essays, guides, posts, and papers. |
| `brand-voice` | Builds a reusable voice profile from real writing samples. |
| `prompt-optimizer` | Turns a vague prompt into a scoped, ready-to-paste prompt. |
| `drawio` | Creates and edits draw.io diagrams. |
| `file-organizer` | Proposes safe file/folder cleanup and confirms before moving files. |
| `ship-learn-next` | Turns learning material into an action and repetition plan. |
| `smart-ocr` | Extracts text from images and scanned documents. |
| `obsidian` | Automates common Obsidian vault operations. |
| `docs-readability-audit` | Checks whether a tired beginner can actually follow a README or walkthrough. |
| `web-ui-audit` | Reviews a website for accessibility, mobile usability, interaction clarity, and basic performance. |
| `repo-onboarding-audit` | Checks whether a new human or coding agent can understand, build, test, and safely modify a repo. |
| `builder-walkthrough` | Converts a technical project into a buy/install/build/test guide with placeholders and checkpoints. |
| `companion-context` | Designs personal AI systems as separate memory, reasoning, tool, and interface layers. |

## Install

Open:

```text
INSTALL.md
```

The short version is to copy a skill folder into your agent's skills directory.

Example for Claude Code:

```bash
mkdir -p ~/.claude/skills
cp -r skills/humanizer ~/.claude/skills/
```

Example for Codex:

```bash
mkdir -p ~/.codex/skills
cp -r skills/humanizer ~/.codex/skills/
```

## How a skill should be written

A useful skill answers:

1. **When should the agent use this?**
2. **When should it not use this?**
3. **What steps should it follow?**
4. **What is it allowed to change?**
5. **What does a good result look like?**
6. **What should it check before saying "done"?**

That last question matters.

Instructions are easy to write.

Quality gates are what make them useful.

## Why this belongs in a cyber portfolio

Agents are becoming part of operational workflows.

That creates the same engineering questions as any other automation:

- scope
- permissions
- repeatability
- logging
- failure modes
- testing
- human approval

The skill files in this project show how I turn informal prompting into repeatable operating instructions.

## What this does not prove

A skill does not guarantee the model will be correct.

It improves:
- consistency
- routing
- boundaries
- handoff quality

A human still owns the result.

## Upstream inspiration

Some skills were influenced by public open-source work from Vercel and Meta.

See:

```text
THIRD_PARTY_ATTRIBUTION.md
```

## License

My original skills are MIT.

Upstream material keeps its own license requirements.
