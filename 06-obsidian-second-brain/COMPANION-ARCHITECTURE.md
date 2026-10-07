# Companion agent architecture

## Plain English

A companion agent is not one app.

It is four separate layers that work together.

```text
MEMORY -> REASONING -> TOOLS -> INTERFACE
```

Keeping those layers separate means you can replace one without rebuilding your digital life.

## 1. Memory

This vault is the memory layer.

It holds:
- what you want the agent to know
- current projects
- people
- preferences
- rules
- daily notes
- long-term reference material

The important part is that **you can inspect and edit it**.

The agent should not be the only place your history exists.

## 2. Reasoning

This is the model or agent you choose.

Examples:
- Codex
- Claude Code
- Cursor
- another local or hosted model

The reasoning layer reads selected context and helps you think or act.

Change the model later if you want.

Your Markdown files remain.

## 3. Tools

Tools let the agent do something besides talk.

Examples:
- edit a note
- check GitHub
- run a safe command on a Raspberry Pi
- query Home Assistant
- read device health
- update a project tracker

Every tool is a permission decision.

The question is not:

> Can the agent do this?

The question is:

> What is the smallest permission it needs to do this safely?

## 4. Interface

This is where you experience the companion.

Examples:
- chat window
- voice
- TV dashboard
- StackChan
- Reachy Mini
- projector
- phone
- e-paper display

The body is not the brain.

You should be able to replace the interface without losing memory.

## Example Muse stack

```text
Obsidian vault
    |
    v
Agent / model
    |
    +------> GitHub
    |
    +------> Home Assistant
    |
    +------> Raspberry Pi
    |
    v
StackChan / dashboard / projector
```

## Context files that earn their keep

A companion does not need your entire life in every prompt.

Start with five files.

### About me

One page.

Who you are, how you work, what matters.

### Rules

What the agent may and may not do.

### Current season

What matters this month or quarter.

### Projects index

One line per active project.

Include:
- status
- next action
- deadline if real

### People index

Context for names that appear repeatedly.

## Companion state

A useful companion can have a quiet state without becoming a Tamagotchi.

Good:

```text
calm
focused
resting
celebrating
```

These states can change:
- a face expression
- dashboard accent
- ambient projection
- one optional nudge

Avoid:
- guilt
- visible streak pressure
- care meters
- fake emotional dependency
- notifications whose purpose is engagement

## Tool permission example

| Tool | Default |
|---|---|
| Read selected vault files | allow |
| Write project notes | allow with folder rules |
| Delete notes | ask |
| GitHub read | allow if connected |
| GitHub write | ask or scope |
| Raspberry Pi health | allow |
| Arbitrary shell command | avoid for beginner setup |
| sudo/admin | do not grant by default |

## Muse Gadget SDK

Meta's open-source Muse Gadget SDK gives us a real device bridge.

It includes:
- a Linux SDK for Raspberry Pi
- an ESP32 SDK
- M5Stack CoreS3 support
- file, command, and device-health capabilities on Linux
- extensible custom commands

Read:

```text
MUSE-GADGET-SDK.md
```

Our recommended first integration uses a dedicated unprivileged Linux user and a small shared folder.

## First companion milestone

Do not build a digital person.

Build this:

1. agent reads your projects index
2. agent reads your rules
3. agent writes one approved project note
4. agent can read Raspberry Pi health
5. dashboard shows one companion state

That is enough to prove the architecture.
