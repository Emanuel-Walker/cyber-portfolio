# Obsidian Second Brain

A beginner-friendly way to build a local Markdown knowledge system with:

- Obsidian
- Codex or Claude Code as the **Vault Agent**
- an optional **Companion Agent** for daily use
- reusable workflows and templates
- clear privacy boundaries
- optional Obsidian Sync later

## Start here

If you are starting from zero:

```text
start-here/README.md
```

That walkthrough starts with:

```text
what to Google
-> what to download
-> what account to create
-> where to click
-> what command to type
-> what prompt to paste
-> what files should appear
-> how to test the result
```

You do **not** need Git.

You do **not** need to clone this repo to build the system.

## The architecture

```text
OBSIDIAN VAULT
Your local Markdown memory
        |
        v
VAULT AGENT
Codex / Claude Code
Organizes and maintains files
        |
        v
CURATED CONTEXT PACK
Small reviewed context
        |
        v
COMPANION AGENT
Muse / Dot / ChatGPT / Claude / other
Daily conversation and capture
```

## Repo map

```text
start-here/
  README.md              Zero-to-hero walkthrough

vault-agent/
  README.md              Worker-agent architecture
  PROMPTS.md             Copy-paste maintenance prompts
  templates/             AGENTS / CLAUDE / CODEX examples
  scripts/               Optional bootstrap automation

companion-agent/
  README.md              Daily-use companion architecture and prompts

guides/
  adhd-friendly-use.md
  vault-structure.md

templates/               Note templates
workflows/               Repeatable Vault Agent workflows
security/                Privacy and sync guidance
examples/                Example use cases
images/                  Example visuals
```

## Vault Agent vs Companion Agent

### Vault Agent

Use Codex, Claude Code, or another file-aware coding agent.

It is the worker.

It can:
- create notes
- organize Inbox items
- update projects
- link notes
- build summaries
- generate the Companion Context Pack

Open:

```text
vault-agent/README.md
```

### Companion Agent

Use Muse, Dot, ChatGPT, Claude, or another conversational assistant.

It is the daily interface.

It should normally receive a **small curated context pack**, not unrestricted access to your entire vault.

Open:

```text
companion-agent/README.md
```

## Why Obsidian

The vault is a normal folder containing Markdown files.

That means:
- you can inspect your memory
- you can edit it without the AI
- you can change AI providers later
- you can back it up with normal file tools
- the model is not the only place your history exists

## Accounts and Sync

A local Obsidian vault works without an account.

The walkthrough still recommends creating an Obsidian account early so you are ready if you later choose **Obsidian Sync** or Publish.

Obsidian Sync is optional and requires its own subscription.

Sync is not a backup.

See:

```text
security/
start-here/README.md
```

## What this project refuses to do

- no hidden memory database you cannot inspect
- no forced streaks
- no "you missed a day" guilt
- no assumption that every assistant needs the whole vault
- no silent mass file moves
- no claim that local notes automatically make a cloud AI private

## Want my templates?

You can simply browse and copy the individual files you want.

Or download the repository as a ZIP:

```text
Code -> Download ZIP
```

Git clone is for people who already use Git.

It is not a prerequisite for the system.

## First recommendation

Do not read the entire repo.

Open:

```text
start-here/README.md
```

Build the first working version.

Then come back for templates and workflows.
