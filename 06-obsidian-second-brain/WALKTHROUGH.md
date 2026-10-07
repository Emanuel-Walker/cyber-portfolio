# Walkthrough: from zero to a working Second Brain

## What you are building

By the end, you will have:

- an Obsidian vault made of local Markdown files
- a clear folder structure
- an AI-agent charter
- one project note created by the agent
- a safe place to add more workflows later

This guide assumes no Obsidian experience.

## Time

Plan for about 30 minutes for the first working version.

You can stop after Step 5.

Everything after that is optional.

## 1. Get the repo

### Standalone version

```bash
git clone https://github.com/Emanuel-Walker/obsidian-second-brain.git my-brain
cd my-brain
```

### Portfolio version

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/06-obsidian-second-brain
```

**PASS:** the folder contains `README.md`, `templates/`, and `agent-setup/`.

## 2. Build the vault structure

Do not create every folder by hand.

### macOS or Linux

For Codex:

```bash
bash setup/bootstrap-vault.sh codex
```

For Claude Code:

```bash
bash setup/bootstrap-vault.sh claude
```

For Cursor or another AGENTS.md-aware tool:

```bash
bash setup/bootstrap-vault.sh generic
```

### Windows PowerShell

For Codex:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\setup\bootstrap-vault.ps1 -Agent codex
```

Change `codex` to `claude` or `generic` if needed.

**PASS:** the script prints:

```text
PASS: vault folders created.
PASS: templates copied...
PASS: agent charter ready...
```

## 3. Edit the charter

The bootstrap created one of:

```text
CODEX.md
CLAUDE.md
AGENTS.md
```

Open that file.

Replace every placeholder that looks like:

```text
<YOUR_NAME>
<YOUR_VAULT_ROOT>
<YOUR_PRIMARY_FOCUS>
```

Keep answers short.

Do not add:
- passwords
- API keys
- private keys
- bank information
- government identifiers

The charter is a rulebook, not a secrets file.

## 4. Open the vault in Obsidian

Install Obsidian from its official site.

Then choose:

```text
Open folder as vault
```

Pick this repo folder.

You should see folders such as:

```text
00-Inbox
01-Daily-Notes
02-People
03-Projects
04-Areas
05-Resources
...
99-System
```

**PASS:** the folders appear in the left sidebar.

### Optional plugins

You do not need community plugins for the first agent test.

Add plugins only when a workflow needs them.

If you use the included Templater syntax later, install Templater at that point.

## 5. Launch your agent from the vault

Install your chosen agent using its current official instructions.

Then launch it with this folder as the working directory.

### First validation prompt

Paste:

```text
Summarize the rules in my agent charter.

Keep it under 10 bullets.
Do not edit any files.
```

**PASS:** the answer matches the charter you edited.

### Permission check

Paste:

```text
Which folders are you not allowed to edit freely?

Answer only from my charter.
```

**PASS:** the agent names the protected folders.

**STOP:** if it says it has unrestricted access.

Fix the charter before continuing.

## 6. Create the first project note

Paste:

```text
Create a project note for "Second Brain Setup" under 03-Projects.

Include:
- goal
- current status
- next three actions

Do not edit any other folder.
Show me the file path when you are done.
```

**PASS:** one new project note appears under `03-Projects/`.

Open it in Obsidian.

That is the first complete loop:

```text
local memory -> agent instructions -> controlled write -> human review
```

## 7. Add one daily workflow

Do not automate everything.

Pick one workflow from:

```text
workflows/
```

Recommended first choice:

```text
01-brain-dump-cleanup.md
```

Use it for a week before adding another.

## 8. Add companion-style context

If you want the agent to carry useful context between sessions, read:

```text
COMPANION-AGENTS.md
```

Start with four small files:

```text
00-ABOUT-ME.md
01-RULES.md
02-CURRENT-SEASON.md
04-Projects/_index.md
```

Then ask:

```text
Based only on my current-season file and project index, what are my three active priorities?

Cite the files you used.
```

The goal is not personality.

The goal is reliable context.

## 9. Security before scale

Before importing old chats or sensitive notes, read:

```text
security/
```

Important distinction:

```text
local notes != local AI
```

A hosted agent may receive the content it reads.

Decide what you are willing to send before connecting private material.

## 10. Import old AI conversations later

The conversation-import workflow lives at:

```text
workflows/07-import-past-conversations.md
```

Do this only after the basic vault works.

Old chat exports are high-context and high-privacy.

Do not make them Step 1.

## Definition of done

Your first setup is complete when:

- [ ] Obsidian opens the vault
- [ ] the charter has no placeholders
- [ ] the agent can summarize its rules
- [ ] the agent identifies protected folders correctly
- [ ] one project note exists
- [ ] you know which workflow you will try first

Stop there.

A smaller system you use is better than a perfect system you keep redesigning.

## If you get stuck

### Agent ignores the charter

Check:
- the charter file is at the vault root
- you launched the agent from the vault root
- the filename matches the agent setup you chose

### Templates show raw Templater syntax

Install and enable the Templater plugin.

Then point its template folder at:

```text
99-System/templates
```

### Obsidian looks empty

You opened the wrong folder.

Use **Open folder as vault** and select the folder containing `00-Inbox/`.

### You stopped for a week

Do not rebuild the system.

Open the vault.

Read `02-CURRENT-SEASON.md` if you created it.

Continue with the next useful note.
