# Install Guide

Zero to a working vault with an agent plugged in. About 20 minutes if you are new to Obsidian.

---

## Step 1 - Install Obsidian

Download from [obsidian.md](https://obsidian.md) and install. Open it, click "Open folder as vault," and point it at your clone of this repo.

Recommended first plugins (Settings > Community plugins):

- **Templater** - makes the templates in `templates/` actually work.
- **Dataview** - lets you query your notes like a database.
- **Advanced Tables** - keeps markdown tables sane.
- **Natural Language Dates** - type `@today` and get a date.

You do not need more than this to start.

---

## Step 2 - Pick an agent

Three solid options. Pick one.

### Option A: Claude Code (recommended)

```bash
npm install -g @anthropic-ai/claude-code
```

Then from your vault root:

```bash
cp agent-setup/CLAUDE.md.template CLAUDE.md
# Edit CLAUDE.md and fill in the placeholders.
claude
```

Claude Code reads `CLAUDE.md` at the vault root as its charter. Done.

### Option B: OpenAI Codex or compatible GPT agent

```bash
cp agent-setup/CODEX.md.template CODEX.md
# Edit the placeholders.
```

Launch Codex with the vault as working directory. Confirm it loaded the charter by asking: "What folder is off limits?" It should answer with `Legacy/`.

### Option C: Any `AGENTS.md`-aware agent (Cursor, Continue.dev, Hermes)

```bash
cp agent-setup/AGENTS.md.template AGENTS.md
# Edit the placeholders.
```

Point the agent at the vault root. Most of these tools pick up `AGENTS.md` automatically.

---

## Step 3 - Fill in the placeholders

Open the charter file you just copied. Replace every `<ANGLE_BRACKET>` with your real values:

- `<YOUR_NAME>` - how you want the agent to address you
- `<YOUR_VAULT_ROOT>` - absolute path to this folder
- `<YOUR_PRIMARY_FOCUS>` - one line about what you are working on this quarter
- `<YOUR_ROLE_OR_FOCUS>` - what you do, in one line
- `<YOUR_LONG_HORIZON>` - where you want to be in two years

Keep each value to one line. The charter is a reference the agent rereads often. Short is better.

---

## Step 4 - Validate the setup

Start the agent and run these three checks:

1. **Charter loaded?** Ask: "Summarize the voice rules you are operating under." You should get a short list that matches your charter.
2. **Folder permissions working?** Ask: "List the folders you are not allowed to write to." It should name `Legacy/` and either `00-Inbox/` conditionally or `01-Daily-Notes/` (append only), depending on the template.
3. **Linking behavior?** Ask: "If I mention a person named Jamie who has no note yet, what do you do?" It should say it creates a draft stub and surfaces it.

If any of these fail, the charter is not being loaded. Check the file is at the vault root and named exactly `CLAUDE.md`, `CODEX.md`, or `AGENTS.md`.

---

## Step 5 - Drop in your first daily note

```bash
mkdir -p "01-Daily-Notes/$(date +%Y)/$(date +%m-%B)"
# or on Windows PowerShell:
# New-Item -ItemType Directory -Path "01-Daily-Notes\$(Get-Date -Format yyyy)\$(Get-Date -Format 'MM-MMMM')" -Force
```

Open `templates/daily-note.md`, copy its contents into a new file named `YYYY-MM-DD.md`, and start writing. That is day one.

---

## Troubleshooting

**The agent is ignoring the voice rules.**
Make sure `CLAUDE.md` (or your charter file) is in the vault root, not nested in a subfolder. Agents only auto-load the charter from the working directory root.

**The agent wants to edit my Inbox.**
Reread the folder permissions section in your charter. Make sure `00-Inbox/` is marked no-write without permission. Some agents need the rule stated twice to internalize it.

**I want to add new behaviors.**
Add them to your charter under a new section. Keep rules short and testable. If a rule cannot be verified by asking the agent a question, it is not a rule.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
