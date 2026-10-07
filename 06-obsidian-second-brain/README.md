# Obsidian Second Brain

## Plain English

This project is a folder of Markdown notes plus a rulebook for an AI agent.

The notes are the memory.

The agent helps you search, summarize, connect, and organize that memory when you ask.

You can change the agent later without rebuilding the notes.

That is the whole idea.

## Start here

If you want to try it:

```text
QUICKSTART.md
```

The quickstart gets you to:
- a working vault structure
- an agent charter
- one agent-created project note

without making you read the whole repo first.

For the longer beginner guide:

```text
WALKTHROUGH.md
```

## What problem this solves

Useful context gets scattered across:
- chat histories
- browser tabs
- random documents
- meeting notes
- screenshots
- your own memory

AI assistants make that worse when the important context exists only inside one vendor's chat history.

This project gives the human a canonical source of truth:

```text
plain Markdown files on disk
```

The agent reads the files you choose.

## What is included

| Area | What it gives you |
|---|---|
| `setup/` | bootstrap scripts for macOS/Linux and Windows |
| `agent-setup/` | charters for Claude Code, Codex, and AGENTS.md-aware tools |
| `templates/` | daily notes, projects, meetings, people, books, and reviews |
| `workflows/` | repeatable jobs such as brain-dump cleanup and conversation import |
| `security/` | privacy, PII, encryption, backup, and sync guidance |
| `ADHD-GUIDE.md` | low-friction operating rules for people who lose systems when they become too complicated |
| `COMPANION-AGENTS.md` | how to use the vault as an inspectable memory layer for a persistent assistant |
| `starter-prompts.md` | prompts you can paste directly into an agent |

## The architecture

```text
Your notes
   |
   v
Obsidian vault
   |
   v
Agent charter
   |
   v
AI agent you choose
   |
   v
Search / summarize / draft / organize
```

The vault is not the model.

The model is not the memory.

Keeping them separate is the point.

## What "local-first" means here

Your notes are normal local files.

That does **not** mean every AI agent runs locally.

If you use a hosted AI service, content you send to that service leaves your computer.

Read:

```text
security/
```

before adding sensitive material.

## Agent boundaries

The included charters show one way to define:
- which folders are read-only
- which folders the agent may edit
- what requires approval
- what the agent must never read
- how to handle missing facts
- when to create session notes

You should change those rules for your own vault.

## Companion-agent pattern

A useful persistent assistant needs more than chat history.

At minimum it needs:

1. an `ABOUT-ME` file
2. a rules file
3. a current-priorities file
4. a projects index
5. context for recurring people or topics

The vault keeps those files visible and editable by the human.

Read:

```text
COMPANION-AGENTS.md
```

for the deeper pattern.

## What this project refuses to do

- no streaks
- no mandatory daily ritual
- no hidden database you cannot inspect
- no assumption that one AI vendor should own your long-term context
- no silent writes to protected folders
- no claim that an agent "knows you" better than the files and permissions you actually give it

## What this proves

This project demonstrates:
- local-first knowledge organization
- portable agent instructions
- workflow design
- privacy boundaries
- human-readable memory
- beginner-focused documentation

## What this does not prove

It does not prove:
- an AI agent will always follow the charter
- local files make a cloud model private
- more notes automatically create better reasoning
- a companion agent should have unrestricted access to your life

Human review still matters.

## Next

Start with:

```text
QUICKSTART.md
```

Then choose one workflow.

Not eight.

One.
