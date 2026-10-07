# Quickstart - AI Agent Skills

## Zero-to-hero path

A skill is a small instruction package that teaches an AI coding agent how to do one repeatable job.

You need one coding agent first.

Choose **Codex** or **Claude Code**.

### Option A — Codex

1. Make sure you can sign in to ChatGPT.
2. Install Node.js LTS from:

```text
https://nodejs.org/
```

3. Open Terminal or PowerShell.
4. Verify:

```bash
node --version
npm --version
```

5. Install Codex:

```bash
npm install -g @openai/codex@latest
codex --version
```

6. Run:

```bash
codex
```

Follow the sign-in flow.

### Option B — Claude Code

Create/sign in to your Claude account.

Use Anthropic's current official installation instructions.

macOS with Node.js available:

```bash
npm install -g @anthropic-ai/claude-code
claude --version
claude doctor
```

On Windows, use Anthropic's supported Windows method or WSL/Git Bash according to the current Claude Code docs.

### 2. Get the skill files

You do not need Git.

Beginner route:

```text
GitHub -> Code -> Download ZIP
```

Extract the ZIP.

Open:

```text
cyber-portfolio/05-ai-agent-skills/
```

Developer route:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/05-ai-agent-skills
```

Then continue below.

## What you will learn

A skill is a folder that teaches an AI agent how to perform one repeatable job.

The important file is:

```text
SKILL.md
```

A good skill tells the agent:

- what the skill does
- when to use it
- when not to use it
- what steps to follow
- what a good result looks like
- what to check before handoff

By the end, you will:

- install Codex or Claude Code
- download the skill library
- run the Humanizer skill explicitly
- optionally install a skill into your agent setup
- install a starter pack
- create your own tiny skill
- test whether the skill actually changes agent behavior

You do not need Git.

---

# Part 1 — Choose one coding agent

Pick one.

## Option A — Codex

Use this if you already use ChatGPT/OpenAI.

## Option B — Claude Code

Use this if you already use Claude/Anthropic.

Do not install both just to complete this walkthrough.

---

# Part 2A — Install Codex

## Step 1A. Create or confirm your ChatGPT account

Open:

```text
https://chatgpt.com
```

Sign in.

## Step 2A. Install Node.js

Google:

```text
Node.js LTS
```

Use:

```text
https://nodejs.org/
```

Install the current LTS release.

Close and reopen your terminal.

Check:

### Windows PowerShell

```powershell
node --version
npm --version
```

### macOS Terminal

```bash
node --version
npm --version
```

## Step 3A. Install Codex

```bash
npm install -g @openai/codex@latest
codex --version
```

On Windows, if PowerShell blocks `npm`, try:

```powershell
npm.cmd install -g @openai/codex@latest
codex --version
```

**PASS:** Codex prints a version.

---

# Part 2B — Install Claude Code

## macOS

Install Node.js 18+ first.

Then:

```bash
npm install -g @anthropic-ai/claude-code
claude --version
claude doctor
```

## Windows

Anthropic currently supports Windows through WSL or Git for Windows / Git Bash.

### WSL route

Open PowerShell as Administrator:

```powershell
wsl --install
```

Restart if prompted.

Open the Linux terminal.

Install Node.js 18+.

Then:

```bash
npm install -g @anthropic-ai/claude-code
claude --version
claude doctor
```

**PASS:** Claude Code prints a version and the doctor command does not report a blocking problem.

---

# Part 3 — Get the skill library

## Beginner method

Open:

```text
https://github.com/Emanuel-Walker/cyber-portfolio
```

Choose:

```text
Code -> Download ZIP
```

Extract it.

Open:

```text
cyber-portfolio-main/05-ai-agent-skills
```

## Developer method

Optional:

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/05-ai-agent-skills
```

---

# Part 4 — Open a terminal in the skill project

## Windows

Open the `05-ai-agent-skills` folder.

Click the File Explorer address bar.

Type:

```text
powershell
```

Press Enter.

## macOS

Open Terminal.

Type:

```bash
cd 
```

Drag the folder into Terminal.

Press Enter.

**PASS:** the terminal is inside `05-ai-agent-skills`.

---

# Part 5 — Inspect one skill before using it

Open:

```text
skills/humanizer/SKILL.md
```

Look at the front matter.

You should see fields similar to:

```yaml
---
name: humanizer
description: ...
---
```

Then read the instructions.

This is important.

Do not install random public skills without reading them first.

Skills can contain:
- instructions
- scripts
- references
- templates
- assets

Treat them like code.

---

# Part 6 — Run the skill explicitly

This is the most reliable first test.

Launch your agent from the `05-ai-agent-skills` folder.

## Codex

```bash
codex
```

## Claude Code

```bash
claude
```

Then paste:

```text
Read:

skills/humanizer/SKILL.md

Use that skill strictly on this paragraph:

"In today's rapidly evolving threat landscape, organizations must leverage robust, scalable solutions to seamlessly integrate advanced detection capabilities. Moreover, by utilizing cutting-edge AI, security teams can delve into unprecedented insights that empower proactive defense."

Return:
1. the rewritten paragraph
2. five specific skill rules you applied
```

Expected behavior:

The rewrite should remove or reduce words such as:

```text
leverage
robust
seamlessly
utilizing
delve
moreover
```

It should also become shorter and more direct.

**PASS:** the output clearly reflects rules from the skill file.

This proves the skill itself works before you worry about automatic discovery.

---

# Part 7 — Install one skill

This repo includes helper scripts.

## macOS / Linux

For Codex:

```bash
bash scripts/install-skill.sh codex humanizer
```

For Claude Code:

```bash
bash scripts/install-skill.sh claude humanizer
```

## Windows PowerShell

Codex:

```powershell
.\scripts\install-skill.ps1 -Agent codex -Item humanizer
```

Claude:

```powershell
.\scripts\install-skill.ps1 -Agent claude -Item humanizer
```

The installer refuses to silently overwrite an existing skill folder.

**PASS:** it prints:

```text
PASS: install complete.
```

---

# Part 8 — Verify the installed files

## Codex example

Check:

```text
~/.codex/skills/humanizer/SKILL.md
```

## Claude example

Check:

```text
~/.claude/skills/humanizer/SKILL.md
```

On Windows, `~` means your user home directory.

If your current agent version uses a different skills/plugin mechanism, the explicit-read workflow from Part 6 still works.

Do not confuse:

```text
the skill file is valid
```

with:

```text
my exact agent build auto-discovers this folder
```

Those are separate questions.

---

# Part 9 — Install a starter pack

The project includes three packs.

## Builder pack

```text
repo-onboarding-audit
builder-walkthrough
web-ui-audit
prompt-optimizer
```

Install:

```bash
bash scripts/install-skill.sh codex builder-pack
```

or:

```powershell
.\scripts\install-skill.ps1 -Agent codex -Item builder-pack
```

## Writing pack

Includes writing/humanization skills.

## Second Brain pack

Includes:
- Obsidian workflow skill
- companion-context skill
- file organizer
- docs readability audit

Do not install every skill just because it exists.

Install what you will actually use.

---

# Part 10 — Build your first skill

Create:

```text
skills/my-first-skill/
```

Inside it create:

```text
SKILL.md
```

Paste:

```markdown
---
name: next-action
description: Use when the user has too many tasks and needs one concrete next action.
---

# Next Action

Use this skill when the user gives you a messy task list or says they are stuck.

1. Identify the single outcome that matters most.
2. Choose one action that can be completed in 20 minutes or less.
3. Return only:
   - Next action
   - Why this one
   - Definition of done

Do not create a full productivity system.

Before handoff, confirm the action is concrete and physically doable.
```

Save it.

---

# Part 11 — Test your new skill

In Codex or Claude Code:

```text
Read:

skills/my-first-skill/SKILL.md

Use it on this list:

- clean up my portfolio
- study AWS
- reply to emails
- reorganize all my notes
- update one broken project walkthrough
```

Expected shape:

```text
Next action:
...

Why this one:
...

Definition of done:
...
```

**PASS:** the agent chooses one action instead of giving you another giant list.

---

# Part 12 — Improve the skill

Ask:

```text
Audit skills/my-first-skill/SKILL.md.

Tell me:
1. when the trigger is too vague
2. where the instructions could conflict
3. one test case that should invoke it
4. one test case that should NOT invoke it

Do not edit the file yet.
```

That is skill engineering.

The hard part is not writing Markdown.

The hard part is making the instructions:
- narrow
- discoverable
- testable
- safe
- reusable

---

# Common problems

## Agent ignores the skill

Use the explicit form:

```text
Read path/to/SKILL.md and use it strictly.
```

Then diagnose discovery separately.

## Installer says the folder already exists

That is intentional.

Read the existing installed skill first.

Remove or update it deliberately.

## Skill triggers too often

Tighten the `description` front matter.

The description should explain:
- what the skill does
- when it should be considered

## Skill produces inconsistent output

Add an output contract.

Example:

```text
Return exactly:
1. Finding
2. Evidence
3. Fix
```

---

# Definition of done

- [ ] Codex or Claude Code installed
- [ ] skill library downloaded
- [ ] Humanizer skill inspected
- [ ] Humanizer explicitly tested
- [ ] one skill installed
- [ ] starter pack understood
- [ ] your own SKILL.md created
- [ ] custom skill tested
- [ ] trigger/boundary audit completed

You now understand the skill system well enough to build your own reusable agent workflows.
