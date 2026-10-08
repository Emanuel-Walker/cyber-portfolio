# Vault Agent

The Vault Agent is the **worker** for the Obsidian vault.

Use a file-aware coding agent such as:

- Codex
- Claude Code

The complete beginner setup is in:

```text
../README.md
```

You do not need this page to finish the build.

## Its job

The Vault Agent may help you:

- capture and organize notes
- maintain project notes
- create summaries and Maps of Content
- process Inbox items
- prepare the Companion Context Pack
- keep a session log

It should **not** silently:

- delete files
- move large groups of files
- read secrets
- rewrite old personal history
- read `Legacy/` without explicit permission

## The worker boundary

A good default:

| Folder | Default |
|---|---|
| `00-Inbox/` | read/write when asked |
| `03-Projects/` | read/write |
| `06-Archive/` | read only unless approved |
| `07-Attachments/` | no deletion without approval |
| `99-System/` | read/write, ask before deleting rules |
| `Legacy/` | off limits by default |

## One useful validation prompt

```text
Do not edit anything.

Read your vault rule file.

Tell me:
1. what you can edit
2. what requires approval
3. what is off limits
4. where you put something when you are unsure

Keep it concise.
```

The optional scripts and rule-file templates in this folder are accelerators.

The main `README.md` remains the canonical walkthrough.
