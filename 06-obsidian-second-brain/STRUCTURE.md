# Vault Structure

A good vault structure is boring and consistent. The structure below extends PARA (Projects, Areas, Resources, Archive) with a few folders that solve problems PARA leaves open.

The rule: numbered prefixes keep the order stable in your file browser, hyphens keep names clean, and each folder has a single job.

---

## The folders

### `00-Inbox/`
Brain dump zone. Anything you capture that does not have a home yet lands here. The agent does not touch this folder without your explicit permission on a per-batch basis. This is the pressure valve for an ADHD brain.
_Example: `2026-10-03 random idea about threat hunting.md`_

### `01-Daily-Notes/`
One note per day. Use the template in `templates/daily-note.md`. These are time-stamped and non-negotiable. Do not reorganize them later. Future-you reads them chronologically.
_Example: `2026/10-October/2026-10-03.md`_

### `02-People/`
One note per person who matters. Collaborators, mentors, friends, direct reports. The agent uses these notes to connect the right person to the right project when it surfaces patterns.
_Example: `Jamie Rivera.md`_

### `03-Projects/`
Active, time-bounded work. If it has a start, a desired outcome, and an end, it goes here. When done, move the whole folder to `06-Archive/`.
_Example: `Home Lab Rebuild 2026-Q4/`_

### `04-Areas/`
Ongoing responsibilities with no end date. Health, Finance, Career, Learning, Home. Each area has its own folder with its own index note.
_Example: `04-Areas/Health/Health_Index.md`_

### `05-Resources/`
Reference material you want to find later. Frameworks, cheat sheets, saved articles, documentation. Organized by topic, not by project.
_Example: `05-Resources/Networking/TCP_State_Machine.md`_

### `06-Archive/`
Done, retired, or deprecated. Nothing is deleted. Everything that leaves the active folders lands here with a date-stamped move. If you need something back, it is a search away.
_Example: `06-Archive/2025-Projects/Old_Site_Rebuild/`_

### `07-Attachments/`
Binary files. PDFs, images, voice memos, screenshots. Keep them out of your writing folders so your text stays greppable.
_Example: `07-Attachments/screenshots/2026-10-03_dashboard.png`_

### `08-AI-History/`
Everything your agent produces or imports. Session logs, exported ChatGPT and Claude.ai conversations, and NotebookLM source files. Keep platforms and purposes in subfolders (`sessions/`, `chatgpt/`, `claude/`, `notebooklm-exports/`).
_Example: `08-AI-History/sessions/2026-10-03_vault_cleanup_session.md`_

### `09-Dreams/` (optional)
If you track dreams, keep them separate. They are useful for pattern work with the agent but should not pollute your main project graph.
_Example: `09-Dreams/Entries/2026-10-03_office_dream.md`_

### `10-Study/` or `10-Faith/` (optional)
A domain-specific folder for a body of knowledge you return to constantly. Could be scripture study, could be a formal course, could be a specific technical stack you are mastering. Keep it siloed so you can swap it out without disturbing the rest of the vault.
_Example: `10-Study/Cryptography/Elliptic_Curves_notes.md`_

### `99-MOC/`
Maps of Content. Index notes that link out to everything in a given area. Think of these as the home pages of your vault. Start with one MOC per Area and build out as needed.
_Example: `99-MOC/Career_MOC.md`_

### `99-System/`
Templates, scripts, agent configuration, audit files. The machinery that keeps the vault running. Non-content.
_Example: `99-System/scripts/daily_rollup.py`_

### `Legacy/` (recommended)
A separate folder your family can access if something happens to you. Letters, locations of important documents, a reference to where your password manager lives, your wishes. More in `security/05-legacy-folder.md`. Encrypt this one with a key your next of kin can get to.
_Example: `Legacy/Letters/to_my_sister.md`_

---

## Naming rules

- Folders use `##-Name` with hyphens.
- Files use `Title_Case.md` or `YYYY-MM-DD_description.md`.
- Never create empty stubs. They add noise to the graph and lie about what the vault contains.
- Never invent root folders on a whim. If a new root is warranted, think about it for a week first.

---

## Tagging convention

Use frontmatter tags, not inline. Keep them short and composable.

```yaml
---
tags:
  - status/draft
  - type/project-note
  - topic/incident-response
---
```

Reserved status tags: `status/draft`, `status/needs-review`, `status/stable`, `status/archived`.
Reserved privacy tag: `#private`. Files with this tag are also excluded by `.gitignore` if the filename contains `private` (git cannot read tags, so the convention is belt and suspenders).

---

## Why this structure holds up

The numbered prefixes mean the folder order never changes. The split between active and reference material means your daily workspace stays small. The `99-` prefix pushes system folders to the bottom where you only see them when you need them. The legacy folder means your work survives you.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
