---
name: companion-context
description: Design or review a personal companion agent using separate memory, reasoning, tools, and interface layers. Use for second-brain agents, chief-of-staff agents, persistent memory, Muse-style companions, or personal AI architecture.
offline: true
---

# Companion Context Architecture

Do not treat "companion agent" as one magic application.

Separate four layers.

## Layer 1. Memory

Canonical context the user can inspect and edit.

Examples:
- Obsidian
- Markdown
- local database

Questions:
- What is stored?
- Who can read it?
- How is it deleted?
- What is intentionally excluded?

## Layer 2. Reasoning

The model or agent that interprets the context.

The memory layer should survive changing the model.

Do not make personal history depend on one vendor.

## Layer 3. Tools

Capabilities the agent can act through.

Examples:
- filesystem
- GitHub
- Home Assistant
- Raspberry Pi
- Muse Gadget SDK
- calendar
- email

Use least privilege.

A companion that can read a project index does not automatically need shell access.

## Layer 4. Interface

How the user experiences the system.

Examples:
- chat
- voice
- TV dashboard
- StackChan
- Reachy
- projector
- phone

The interface may change without changing memory.

## Companion state

Use quiet state, not addictive gamification.

Useful state:
- focused
- calm
- resting
- celebrating

Avoid:
- visible streak pressure
- guilt
- "I miss you" manipulation
- care meters whose job is to drive engagement

## Minimum viable companion

1. One canonical about-me file.
2. One current-projects file.
3. One rules file.
4. One agent charter.
5. One safe tool.
6. One visible interface.
7. One weekly review.

## Security review

Before adding a tool ask:
- Does the agent need write access?
- Does it need sudo/admin?
- Can a dedicated account do the job?
- Can only a curated context folder be exposed?
- Is there a log?
- Is there a kill switch?
- Can the integration work offline when the cloud is unavailable?

## Output

When designing a companion, return:
- architecture diagram in text
- permissions table
- context files
- event/state model
- first working milestone
- failure/degradation behavior
