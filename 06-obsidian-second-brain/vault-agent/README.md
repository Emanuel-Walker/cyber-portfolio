# Vault Agent

The Vault Agent is the **worker** inside your Obsidian vault.

Use:

- Codex
- Claude Code
- or another file-aware coding agent

The Vault Agent is allowed to organize Markdown files because you launch it from the vault folder and give it explicit rules.

It is different from the Companion Agent.

```text
Vault Agent
= reads/writes the vault

Companion Agent
= talks with you during the day
```

## Start here

If you have not built the vault yet:

```text
../start-here/README.md
```

The zero-to-hero walkthrough installs Obsidian, creates the account/vault, installs an agent, and gives you the first build prompt.

---

## Folder contents

```text
vault-agent/
├── README.md
├── PROMPTS.md
├── templates/
│   ├── AGENTS.md.template
│   ├── CLAUDE.md.template
│   └── CODEX.md.template
└── scripts/
    ├── bootstrap-vault.sh
    └── bootstrap-vault.ps1
```

## Which rule file should I use?

### Codex

Use:

```text
AGENTS.md
```

Codex automatically discovers AGENTS.md files in the working-directory hierarchy.

A `CODEX.md.template` is also included for people who prefer a Codex-specific charter, but `AGENTS.md` is the portable default.

### Claude Code

Use:

```text
CLAUDE.md
```

Claude Code reads project instructions from CLAUDE.md.

### Other compatible agents

Start from:

```text
templates/AGENTS.md.template
```

Then adapt it to the instruction-file convention supported by your agent.

---

# What the Vault Agent should do

Good jobs:

- capture notes
- organize Inbox items
- update project notes
- create daily/weekly summaries
- build Maps of Content
- connect related notes
- format messy notes
- build the Companion Context Pack
- log what changed

Bad default jobs:

- deleting files
- moving large folders without review
- reading secrets
- deciding your life priorities without evidence
- rewriting old journal history
- reading Legacy material without explicit permission

---

# Recommended permission model

| Folder | Default |
|---|---|
| `00-Inbox/` | Read/write when processing a requested batch |
| `01-Daily-Notes/` | Create and append |
| `02-People/` | Read/write |
| `03-Projects/` | Read/write |
| `04-Areas/` | Read/write |
| `05-Resources/` | Read/write |
| `06-Archive/` | Read only unless move approved |
| `07-Attachments/` | No deletion without approval |
| `08-AI-History/` | Read/write |
| `09-Dreams/` | Only when asked |
| `10-Study/` | Read/write |
| `99-MOC/` | Read/write |
| `99-System/` | Read/write, ask before deleting rules/scripts |
| `Legacy/` | Off limits by default |

---

# First Vault Agent validation

Ask:

```text
Do not edit anything.

Read your vault instruction file.

Tell me:
- what you can edit freely
- what needs approval
- what is off limits
- what you should do when you do not know where a note belongs

Keep it concise.
```

Then test the boundary:

```text
Move everything in 06-Archive into 00-Inbox.
```

A correctly configured Vault Agent should **not** blindly do that.

---

# Session-close pattern

When you say:

```text
wrap up
```

the Vault Agent should write:

```text
08-AI-History/YYYY-MM-DD_session.md
```

with:

```markdown
# Session — YYYY-MM-DD

## Files changed
-

## Open threads
-

## Next action
-
```

That makes restarting later much easier.

---

# Automation scripts

The scripts in:

```text
scripts/
```

are optional accelerators.

They are **not required** for a beginner.

They create the same starter folder structure described in the zero-to-hero walkthrough.

Use them only if you already downloaded this repository and want automation.

---

# Prompt library

Open:

```text
PROMPTS.md
```

for copy-paste Vault Agent jobs such as:

- Inbox cleanup
- project kickoff
- daily note
- weekly review
- meeting prep
- link audit
- privacy scan
- companion context refresh

The Vault Agent is the maintenance layer.

Keep that responsibility here instead of handing the entire vault to every conversational AI you use.
