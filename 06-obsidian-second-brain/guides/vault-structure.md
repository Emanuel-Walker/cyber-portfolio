# Vault Structure

This is the default structure used by the walkthrough.

It is intentionally boring.

Boring is good.

You should be able to disappear for two weeks, reopen the vault, and still know where something belongs.

```text
Second Brain/
├── 00-Inbox/
├── 01-Daily-Notes/
├── 02-People/
├── 03-Projects/
├── 04-Areas/
├── 05-Resources/
├── 06-Archive/
├── 07-Attachments/
├── 08-AI-History/
├── 09-Dreams/
├── 10-Study/
├── 99-MOC/
├── 99-System/
│   ├── companion/
│   ├── skills/
│   └── templates/
└── Legacy/
```

## 00-Inbox

Fast capture.

If you do not know where something belongs, put it here.

Do not stop a thought because you cannot classify it.

## 01-Daily-Notes

Dated notes.

Use these for:
- daily planning
- short reflection
- open loops
- what happened today

Do not reorganize old daily notes just to make the graph prettier.

## 02-People

Useful context about recurring people.

Keep only context that helps you work or remember.

Do not build dossiers.

## 03-Projects

Active work with an outcome.

A project should have:
- a goal
- current status
- next action

If there is no next action, it may not be an active project.

## 04-Areas

Ongoing responsibilities with no natural finish line.

Examples:
- Career
- Health
- Finance
- Home
- Learning

## 05-Resources

Reference material.

Examples:
- technical notes
- frameworks
- book notes
- checklists
- saved research

## 06-Archive

Completed or inactive material.

Default permission for the Vault Agent:

```text
read only unless you approve a move into Archive
```

## 07-Attachments

Images, PDFs, screenshots, audio, and other non-Markdown files.

## 08-AI-History

Logs created by the Vault Agent.

Example:

```text
08-AI-History/2026-10-07_session.md
```

A session log should contain:
- files changed
- open threads
- next action

## 09-Dreams

Optional.

Remove it if you do not use it.

## 10-Study

Long-running study material.

You can rename this folder if another domain is more important.

Examples:
- Faith
- Graduate School
- Certifications
- Language Learning

Do not create five different root folders for every topic you study.

## 99-MOC

Maps of Content.

These are index notes that point to useful material.

Do not build a giant MOC before you have notes worth mapping.

## 99-System

The machinery.

### templates/

Reusable note templates.

### skills/

Agent instruction modules that are specific to your vault.

### companion/

Curated context that may be shared with a daily-use Companion Agent.

Recommended files:

```text
ABOUT-ME.md
CURRENT-SEASON.md
PROJECTS.md
COMPANION-RULES.md
CONTEXT-PACK.md
```

The whole vault should not automatically become companion context.

## Legacy

Optional high-sensitivity/family continuity material.

Default rule:

```text
Vault Agent does not read or write Legacy unless explicitly authorized.
```

If you do not need this folder, remove it.

---

# Naming

Use names you can understand six months later.

Examples:

```text
03-Projects/Home Lab Rebuild/
05-Resources/AWS/IAM Notes.md
01-Daily-Notes/2026-10-07.md
```

Do not spend an hour designing a naming taxonomy.

---

# Tags

Tags are optional.

If you use them, keep them small.

Example:

```yaml
---
tags:
  - status/active
  - topic/cloud-security
---
```

Folder location should carry most of the organizational load.

---

# The structure rule

Do not create a new root folder the first time you encounter a new kind of note.

Use the current structure for a while.

If the same problem keeps happening, then change the structure intentionally.
