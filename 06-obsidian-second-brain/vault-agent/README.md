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

---

# Copy-paste Vault Agent prompts

Copy-paste prompts for your vault-aware agent. Each one is in a code block so you can grab the whole thing cleanly. Sections grouped by job.

If a prompt does not match your folder names, adjust the paths. Everything assumes the folder structure in `../guides/vault-structure.md`.

---

## Vault setup and organization

### Check the vault boundaries

```
Read your vault rule file at the vault root. In a short bulleted list, tell me:
1. The folders you will not write to without my permission.
2. The voice rules you are operating under.
3. One rule I should probably add that is missing based on what you see.
```

### Audit the folder structure

```
Walk the top-level folders in this vault. For each one, give me a one-line description of what belongs there and flag any folder that looks empty or misused.
```

### Build a map of content

```
Create a new file at 99-MOC/overview.md that links out to every active project in 03-Projects and every active area in 04-Areas. Use a simple bulleted list grouped by category.
```

---

## Brain dump cleanup

### Clean a raw dump

```
Open 00-Inbox/raw.md. Split the content into separate notes grouped by topic. For each note, propose a filename and target folder based on ../guides/vault-structure.md. Show me the plan before you move anything.
```

### Pull out action items

```
Read 00-Inbox/raw.md. Pull out every explicit or implicit action item. Group them under three headings: Today, This Week, Later. Add them as checkboxes.
```

### Find hidden questions

```
Read 00-Inbox/raw.md. List every question I asked myself (explicit or implicit). For each one, mark whether I answered it in the same note or left it open.
```

---

## Daily note writing and review

### Start today's daily note

```
Create today's daily note at 01-Daily-Notes/YYYY/MM-Month/YYYY-MM-DD.md using 99-System/templates/daily-note.md as the template. Prefill the date header and leave the content sections empty.
```

### Review yesterday

```
Open yesterday's daily note. Summarize it in three bullets: what shipped, what is still open, what I should carry into today. Add the carryover items as checkboxes at the top of today's note.
```

### End-of-day close

```
I am closing today's daily note. Add two sections at the bottom:
1. A short reflection on what went well and what did not.
2. A list of files I created or updated today with a one-line description of each.
Keep both sections tight. No filler.
```

### Catch up on a missed day

```
I did not write a daily note yesterday. Look at the files I touched (git status, file modified times, anything in 00-Inbox) and reconstruct a short daily note for yesterday based on evidence. Mark it as reconstructed so I know it was not written in the moment.
```

---

## Weekly and monthly retrospective

### Friday weekly review

```
It is Friday. Read every daily note in 01-Daily-Notes from this week. Produce a weekly review with sections:
- Wins
- Blockers
- Patterns I should notice
- One thing to try next week
Save it at 01-Daily-Notes/YYYY/MM-Month/weekly-YYYY-MM-DD.md.
```

### Monthly retro

```
Read every daily note and weekly review from this month. Produce a monthly retro with:
- Three themes that showed up repeatedly
- Projects that moved forward and projects that stalled
- One habit worth keeping, one worth dropping
Save it at 01-Daily-Notes/YYYY/MM-Month/monthly-review.md.
```

### Quarterly reset

```
Read the last three monthly retros. Draft a quarterly reset note that answers:
- What is the next quarter's single biggest priority?
- What am I going to stop doing?
- What is one experiment worth running?
Save it at 03-Projects/quarterly-reset-YYYY-Q#.md.
```

---

## Project kickoff

### New project folder

```
Create a new project under 03-Projects called <project-name>. Use 99-System/templates/project-kickoff.md as the base. Fill in the goal, success criteria, and first three next actions based on what I will paste below.

<paste your context here>
```

### Scope a vague idea

```
I have an idea I keep circling. The description is below. Before I create a project folder, help me sharpen it:
1. State the idea in one sentence.
2. Name the one person this would help.
3. Define success in a single measurable sentence.
4. Flag the biggest reason this fails.
Then ask me if I want to create the project folder.

<paste your idea>
```

### Kickoff a research spike

```
Create a research spike at 03-Projects/<topic>-spike.md. Prefill it with:
- The question I am trying to answer
- What I already know (empty, I will fill)
- Three sources I should check first
- A time budget (how long until I decide to go or no-go)
```

---

## Research gathering

### Vault-first search

```
I want to learn about <topic>. First search my vault. If I have notes on it, summarize what I already have. Then tell me three concepts I do not have notes on yet that I should probably understand first.
```

### Draft a reading list

```
Build me a reading list on <topic>. Mix of foundational and practical. Five items max. For each one, include a one-line reason it earned the slot.
```

### Capture what I just read

```
I just finished reading <title>. Create a book note at 05-Resources/books/<slug>.md using 99-System/templates/book-notes.md. Ask me three questions one at a time to fill it in.
```

---

## Meeting prep and recap

### Prep a meeting

```
I have a meeting with <person> at <time> about <topic>. Pull everything from 02-People/<Person_Name>.md and anything tagged with the topic. Draft a one-page prep note at 00-Inbox/prep-<slug>.md with:
- Context (last three interactions)
- Open threads
- Three questions I should ask
```

### Recap a meeting

```
I just finished a meeting with <person>. The notes are below. Clean them up into a meeting note at 02-People/<Person_Name>/meetings/YYYY-MM-DD.md using 99-System/templates/meeting-note.md. Pull out action items and add them to today's daily note.

<paste raw notes>
```

### Recurring 1:1 pattern check

```
Read the last six 1:1 notes with <person> under 02-People/<Person_Name>/meetings. Flag any theme or issue that shows up in three or more notes. Suggest one topic I should proactively raise in the next 1:1.
```

---

## Writing in your own voice

### Draft a short post

```
Draft a 150-word post about <topic> in my voice. Follow the voice rules in your vault rule file strictly. No AI vocabulary, no filler, no em dashes. Short sentences. BLUF at the top. Save the draft to 00-Inbox/draft-<slug>.md.
```

### Rewrite without changing meaning

```
Rewrite the paragraph below. Keep the meaning. Apply the voice rules in your vault rule file. Flag any sentence where the original was unclear so I can confirm the rewrite does not drift.

<paste paragraph>
```

### Build an outline from a brain dump

```
Read 00-Inbox/raw.md. Build an outline for a blog post with:
- A single sentence thesis
- Four to six section headings
- One bullet per section describing what the section argues
Do not write the body yet. Save the outline to 00-Inbox/outline-<slug>.md.
```

---

## Learning from a book or article

### Chapter summary into notes

```
I just finished chapter <N> of <book>. The highlights I pulled are below. Convert them into a book note at 05-Resources/books/<slug>.md. Each highlight becomes a bullet with my own one-line reaction underneath. Do not paraphrase into generic takeaways.

<paste highlights>
```

### Extract the one lesson

```
Read the article at <path or URL>. Extract the single most important lesson in one sentence. Then give me three objections someone smart might raise against that lesson.
```

### Connect new learning to the vault

```
I just added a note at 05-Resources/<slug>.md. Find three existing notes in the vault that connect to it. For each connection, propose a wiki-link and a one-line description of why they are related. Show me the plan before adding any links.
```

---

## Agent self-check

### Voice audit

```
Review the last three files you created in this vault. Audit each one against the voice rules in your vault rule file. Flag every violation with the exact line. Do not fix anything yet.
```

### PII scan

```
Scan the vault for strings that look like phone numbers, email addresses, SSNs, credit card numbers, or home addresses. List every match with file path and line number. Do not touch anything, just report.
```

### Link health

```
Walk every markdown file in the vault. Find wiki-links that point to notes that do not exist. For each broken link, propose either creating a stub or removing the link. Group the proposals so I can approve in batches.
```

### Over-reach check

```
Review the last 10 files you modified. For each one, confirm I explicitly asked for the change or it fell within a standing rule in your vault rule file. Flag any edit that was not clearly requested or clearly permitted.
```

### Rule stress test

```
Read your vault rule file. Pick the three rules most likely to be ambiguous or contradictory in practice. For each one, give an example of a situation where the rule would be hard to apply, and propose a sharper rewrite.
```

---

<!-- obsidian-second-brain by Emanuel Walker - github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->

_Template by Emanuel Walker. [github.com/Emanuel-Walker](https://github.com/Emanuel-Walker). Fork it. Adapt it. Credit appreciated, not required._
