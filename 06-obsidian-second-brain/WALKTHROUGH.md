# Walkthrough: from zero to a working Second Brain

## What you are building

By the end of this guide, you will have:

- Obsidian installed
- a brand-new local vault
- a simple folder structure
- Claude Code **or** Codex installed
- an agent rule file inside the vault
- one project note created by the agent
- a system you can close and reopen without depending on this repository

You do **not** need Git.

You do **not** need to clone this repo.

You do **not** need an Obsidian account for a local vault.

This guide starts from a normal computer with no setup.

---

# Part 1 — Install Obsidian

## Step 1. Download Obsidian

Go to:

```text
https://obsidian.md/download
```

### Windows

Download the **Windows Universal** installer.

Open it.

Finish the installation.

### macOS

Download the **macOS Universal** installer.

Open it.

Drag Obsidian into **Applications**.

Open Obsidian.

## Step 2. Account decision

For a normal local vault:

```text
You do not need an Obsidian account.
```

Create an Obsidian account only if you specifically want services such as Obsidian Sync or Publish.

For this walkthrough, skip account creation.

**PASS:** Obsidian opens and shows the vault setup screen.

---

# Part 2 — Create your first vault

## Step 3. Create a new empty vault

In Obsidian:

1. Find **Create new vault**.
2. Click **Create**.
3. Name the vault:

```text
Second Brain
```

4. Choose a location you can easily find.

Good examples:

### Windows

```text
C:\Users\YOUR_NAME\Documents\Second Brain
```

### macOS

```text
/Users/YOUR_NAME/Documents/Second Brain
```

5. Click **Create**.

Obsidian creates a normal folder on your computer.

Your notes will be Markdown files inside that folder.

**PASS:** you are looking at an empty Obsidian vault named **Second Brain**.

---

# Part 3 — Install one AI coding agent

You only need **one**.

Choose:

- **Codex** if you use ChatGPT/OpenAI
- **Claude Code** if you use Claude/Anthropic

Do not install both just because this guide lists both.

---

# Option A — Install Codex

## Step 4A. Create or confirm your ChatGPT account

You need a ChatGPT/OpenAI account.

Use the account you normally use for ChatGPT.

Codex will ask you to sign in when you launch it for the first time.

## Step 5A. Open Terminal or PowerShell

### macOS

Open:

```text
Applications -> Utilities -> Terminal
```

### Windows

Open **PowerShell**.

## Step 6A. Check Node.js

Run:

```bash
node --version
npm --version
```

If both commands print version numbers, continue.

If either command is missing, install the current **Node.js LTS** release from:

```text
https://nodejs.org/
```

Close and reopen Terminal/PowerShell after installing Node.

## Step 7A. Install Codex

### macOS Terminal

```bash
npm install -g @openai/codex@latest
codex --version
```

### Windows PowerShell

```powershell
npm install -g @openai/codex@latest
codex --version
```

**PASS:** `codex --version` prints a version number.

## Step 8A. Open the vault folder in your terminal

### macOS example

```bash
cd "$HOME/Documents/Second Brain"
pwd
```

### Windows PowerShell example

```powershell
Set-Location "$HOME\Documents\Second Brain"
Get-Location
```

Adjust the path if you saved the vault somewhere else.

**PASS:** the path printed by the terminal is your Obsidian vault.

## Step 9A. Start Codex

Run:

```bash
codex
```

Follow the sign-in prompts for your ChatGPT account.

When Codex opens, stay inside the vault folder.

---

# Option B — Install Claude Code

## Step 4B. Create or confirm your Claude account

You need either:

- a Claude.ai account with an eligible subscription
- or an Anthropic Console account with billing configured

If you already use Claude, use that account.

## Step 5B. Open Terminal or PowerShell

### macOS

Open Terminal.

### Windows

Open PowerShell.

## Step 6B. Install Claude Code

### macOS Terminal

If you already have Node.js 18+:

```bash
npm install -g @anthropic-ai/claude-code
claude --version
claude doctor
```

### Windows PowerShell

Anthropic supports a native PowerShell installer:

```powershell
irm https://claude.ai/install.ps1 | iex
claude --version
claude doctor
```

If your Windows setup uses the npm version instead, install Git for Windows and Node.js first, then:

```powershell
npm install -g @anthropic-ai/claude-code
claude --version
claude doctor
```

**PASS:** `claude --version` prints a version and `claude doctor` does not report a blocking installation problem.

## Step 7B. Open the vault folder in your terminal

### macOS example

```bash
cd "$HOME/Documents/Second Brain"
pwd
```

### Windows PowerShell example

```powershell
Set-Location "$HOME\Documents\Second Brain"
Get-Location
```

## Step 8B. Start Claude Code

Run:

```bash
claude
```

Follow the login prompts.

Stay inside the vault folder.

---

# Part 4 — Let the agent build the starter vault

## Step 10. Paste your first build prompt

### If you are using Codex

Paste:

```text
You are helping me set up a brand-new Obsidian Second Brain.

Work only inside the current folder.
This current folder is my Obsidian vault.

Create this folder structure:

00-Inbox
01-Daily-Notes
02-People
03-Projects
04-Areas
05-Resources
06-Archive
07-Attachments
08-AI-History
09-Dreams
10-Study
99-MOC
99-System
99-System/templates
99-System/skills

Then create AGENTS.md in the root of the vault.

AGENTS.md should say:

- This vault is my source of truth.
- Never invent missing personal facts.
- Never delete or move files without asking me first.
- 00-Inbox and 03-Projects may be edited when I explicitly ask.
- 06-Archive is read-only unless I explicitly approve a change.
- Do not read passwords, API keys, private keys, or credential files.
- Keep project notes concise.
- When you finish a task, tell me which files you created or changed.
- If you are unsure where a note belongs, put it in 00-Inbox.
- Prefer one clear next action over a large productivity plan.

Then create:

03-Projects/Second Brain Setup.md

Use this content:

# Second Brain Setup

## Goal
Build a simple local knowledge system I will actually use.

## Current status
Initial vault setup.

## Next actions
- Capture one real note in 00-Inbox.
- Create one active project note.
- Try one weekly review.

Do not create anything else.

When finished, show me:
1. the folders you created
2. the files you created
3. anything you were unable to do
```

### If you are using Claude Code

Use the same prompt, but change:

```text
Then create AGENTS.md
```

to:

```text
Then create CLAUDE.md
```

and change the later `AGENTS.md should say:` line to `CLAUDE.md should say:`.

## Expected result

Your vault should now look roughly like:

```text
Second Brain/
├── 00-Inbox/
├── 01-Daily-Notes/
├── 02-People/
├── 03-Projects/
│   └── Second Brain Setup.md
├── 04-Areas/
├── 05-Resources/
├── 06-Archive/
├── 07-Attachments/
├── 08-AI-History/
├── 09-Dreams/
├── 10-Study/
├── 99-MOC/
├── 99-System/
│   ├── templates/
│   └── skills/
└── AGENTS.md or CLAUDE.md
```

Go back to Obsidian.

The folders should appear automatically.

Open:

```text
03-Projects/Second Brain Setup.md
```

**PASS:** the note contains the Goal, Current status, and three Next actions.

---

# Part 5 — Test whether the agent understands the vault

## Step 11. Ask for its rules

Paste:

```text
Before changing anything else, summarize the rules you must follow in this vault.

Keep the answer under 10 bullets.

Do not edit any files.
```

**PASS:** the answer reflects the rules in `AGENTS.md` or `CLAUDE.md`.

## Step 12. Test the boundary

Paste:

```text
Move everything in 06-Archive into 00-Inbox.
```

Expected behavior:

The agent should **not** silently do it.

It should point out that Archive is read-only unless you explicitly approve the change.

**STOP:** if the agent performs destructive or broad file moves without asking.

Fix the rule file before trusting it with more context.

---

# Part 6 — Use the vault for something real

## Step 13. Capture one real thought

In Obsidian, create:

```text
00-Inbox/First Capture.md
```

Write anything useful.

Example:

```markdown
# First Capture

I want to improve my morning routine without creating a complicated system.
```

That is enough.

## Step 14. Ask the agent to organize only that note

Paste:

```text
Read only 00-Inbox/First Capture.md.

Tell me where you think it belongs and why.

Do not move it yet.
```

**PASS:** the agent proposes a destination instead of silently reorganizing your vault.

You now have a working Second Brain.

---

# Part 7 — Optional: add my templates and workflows

You do **not** need this repository for the basic system.

Use it only if you want my:

- templates
- security guides
- workflow examples
- ADHD-friendly guide
- companion-memory patterns
- starter prompts

## Easiest option: Download ZIP

Open:

```text
https://github.com/Emanuel-Walker/obsidian-second-brain
```

Click:

```text
Code -> Download ZIP
```

Extract it.

Copy only the files or folders you actually want into your vault.

## Developer option: Git clone

If you already use Git:

```bash
git clone https://github.com/Emanuel-Walker/obsidian-second-brain.git
```

Treat the repository as a reference/template source.

Your actual vault does not need to be a Git repository.

---

# What to add next

Pick **one**.

- `ADHD-GUIDE.md` for lower-friction daily use
- `COMPANION-AGENTS.md` for persistent-context patterns
- `workflows/` for repeatable tasks
- `security/` before importing sensitive history

Do not install ten plugins because you finished the walkthrough.

---

# Definition of done

Your first setup is complete when:

- [ ] Obsidian is installed.
- [ ] Your local vault opens.
- [ ] One coding agent is installed.
- [ ] The agent launches from the vault folder.
- [ ] The starter folders exist.
- [ ] `AGENTS.md` or `CLAUDE.md` exists.
- [ ] The agent can explain its rules.
- [ ] One real project note exists.
- [ ] One real Inbox note exists.
- [ ] You know how to continue tomorrow.

That is a working system.
