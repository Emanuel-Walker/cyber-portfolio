---
name: obsidian
description: Obsidian vault automation. Direct file ops for CRUD plus obsidian:// URIs for UI control. Fully offline, Windows-native.
platform: claude-code
offline: true
---

# Obsidian Vault Expert

Tailored for an Obsidian vault at `<your-vault-root>` on Windows.
No network calls. No external skill registries. File ops plus URI scheme only.

## When to use

- Create, read, edit, organize, or delete notes in the vault
- Find orphan notes, dead-end notes, or unresolved `[[links]]`
- Query backlinks, tags, properties across the vault
- Run a vault health check or maintenance session
- Create notes from templates (daily note, task, project, research, etc.)
- Build or update Maps of Content (MOCs)
- Any question about the vault's structure, content, or graph

## When NOT to use

- Writing Obsidian plugins (TypeScript / plugin API) - use normal coding
- Content quality review or grammar checking - different skill
- Knowledge graph theory - out of scope

## Invocation

```
/obsidian                          # Interactive - asks what you need
/obsidian health                   # Full vault health check
/obsidian orphans                  # Find orphan notes
/obsidian search "query"           # Search vault content
/obsidian backlinks "path"         # Find what links to a note
/obsidian tags                     # List all tags with counts
/obsidian daily                    # Create or append to today's daily note
/obsidian moc "Topic"              # Create or update a Map of Content
/obsidian create task "Task Title" # Create a task note from template
```

## Vault-native skills take precedence

Before invoking this skill, check whether a vault-local skill at `<your-system-folder>/skills/` handles the request. Vault-local skills are tuned to the vault's specific architecture. Generic file ops here miss those integrations.

Use this `obsidian` skill for general vault ops that specialized skills do not cover:
- Free-form Grep / Glob search across the vault
- Building a fresh MOC for a topic where no MOC exists
- Creating a note from a template provided by the user
- Health snapshots not covered by vault audit passes
- Backlink lookups for an arbitrary note
- Tag aggregation for arbitrary purposes

## Architecture: 2-tier model

```
User: /obsidian [command] [args]
     |
     v
[Tier Selection]
     |
     +---> CRUD (create, read, edit, delete, search content)?
     |       → Tier 1: Direct File Ops (Read / Write / Edit / Glob / Grep)
     |       → Always available, zero dependencies
     |
     +---> UI control (open note, trigger search panel in Obsidian)?
             → Tier 2: obsidian:// URI scheme
             → Windows: cmd.exe //c start "" "obsidian://open?vault=<name>&file=PATH"
             → From PowerShell: Start-Process "obsidian://..."
```

Tier 2 CLI graph queries are not installed on Windows. The Mac Obsidian CLI binary does not exist on Windows. For orphan / backlink / tag discovery, Tier 1 file ops do the job - slower than an indexed CLI but always works.

## Vault constants (fill in your own)

```
VAULT_PATH   = <your-vault-root>
VAULT_NAME   = <your-vault-name>
OBSIDIAN_EXE = <path to Obsidian.exe>
```

## PARA folder map (default pattern)

| Content Type | Folder |
|--------------|--------|
| Quick capture, unsorted | `inbox/` |
| Outbound (sharing, exports) | `outbound/` |
| Daily notes | `daily-notes/` |
| People (contacts, networking) | `people/` |
| Active projects with deadlines | `projects/` |
| Ongoing areas | `areas/` |
| Academic coursework | `academic/` |
| Reference, topic material | `resources/` |
| Completed / inactive | `archive/` |
| Attachments (images, PDFs) | `attachments/` |
| AI experiments | `ai/` |
| Content engine | `content-engine/` |
| Maps of Content | `moc/` |
| System: templates, dashboards, config | `system/` |
| Templates | `system/templates/` |

Rule: never write new notes to vault root. Inbox is fine for unsorted capture, but move out within a few days.

## Critical rules

1. **Check before write** - always `Glob` before `Write` to prevent overwriting existing notes
2. **Frontmatter is mandatory** - every note gets at minimum `tags`, `date`, `type`
3. **PARA placement** - file to the correct folder. Never leave new notes at vault root.
4. **Wiki-links over markdown links** - use `[[Note Name]]` for internal links
5. **No raw Templater syntax** - substitute `<% tp.date.now(...) %>` and `<% tp.file.title %>` with actual values before writing
6. **Academic coursework defaults** to `academic/` unless the user names a specific subfolder
7. **No network calls** - offline-only. Never invoke `curl`, `wget`, web fetches, or any MCP gateway.

## Command reference

### /obsidian health - vault health check

```
Step 1: Discovery via file ops
  - Glob "**/*.md" → total note count
  - Glob each PARA folder for per-folder counts
  - Grep "^---" (multiline) in *.md → identify notes WITHOUT frontmatter
  - Grep "\[\[[^\]]+\]\]" → list of all internal link targets
  - Diff link-targets against existing filenames → unresolved links

Step 2: Orphan detection
  - Build map: {filename → list of files linking to it} via Grep "[[FILENAME]]"
  - Files with zero entries = orphans

Step 3: Vault root violations
  - Glob "*.md" at vault root (depth=1) → flag any stray notes

Step 4: Report
  - Markdown summary, categorized: critical, warning, info
  - Offer to fix interactively

Step 5: Fix (if user approves)
  - Add [[links]] to orphans from related MOCs
  - Add frontmatter to notes missing it
  - Move root-level notes to PARA folders
```

### /obsidian orphans - find orphan notes

```
Step 1: Build link index via Grep across vault
Step 2: For each note, check if anything links to it
Step 3: For each orphan, suggest:
  - Which MOC should link to it (based on tags / content)
  - Whether to archive (stale > N days) to archive/
  - Whether to delete (empty stub)
```

### /obsidian create [type] "Title" - create note from template

Templates live in `system/templates/`. When a template file is missing, ask the user before scaffolding one. Never invent a template silently.

Default types:

| Type | Template file | Destination |
|------|---------------|-------------|
| `daily` | `Daily Note.md` | `daily-notes/YYYY-MM-DD.md` |
| `task` | `Task.md` | `academic/` (or user-specified) |
| `research` | `Research Note.md` | `resources/` |
| `project` | `Project.md` | `projects/` |
| `person` | `Person.md` | `people/` |
| `moc` | `MOC.md` | `moc/MOC - Topic.md` |

```
Step 1: Glob "system/templates/<Type>.md"
Step 2: If template missing, ask user before scaffolding
Step 3: Read template, substitute:
  - <% tp.date.now("YYYY-MM-DD") %>        → today's date
  - <% tp.date.now("YYYY-MM-DD HH:mm") %>  → today plus time
  - <% tp.file.title %>                    → provided title
Step 4: Check destination with Glob (prevent overwrite)
Step 5: Write the populated note
Step 6: Optionally open in Obsidian via URI
```

### /obsidian search "query" - vault search

```
Tool: Grep
  pattern="[query]"
  path="<your-vault-root>"
  glob="*.md"
  output_mode="content"
  head_limit=50
```

Case-insensitive: add `-i`. File-name search: `Glob "**/*<query>*.md"`.

### /obsidian backlinks "path" - backlink analysis

```
Step 1: Extract just the filename (without .md) from the path
Step 2: Grep
   pattern="\[\[<filename>(\||#|\]\])"   # matches [[name]], [[name|alias]], [[name#heading]]
   glob="*.md"
   output_mode="files_with_matches"
Step 3: Present hits as a backlink list
Step 4: (Optional) For outgoing links, Read the target file and Grep its body for [[...]]
```

### /obsidian tags - tag overview

```
Tool: Grep
  pattern="(?:^|\s)#[a-zA-Z][a-zA-Z0-9/_-]+"
  glob="*.md"
  output_mode="content"
Then post-process: extract tag tokens, count occurrences, sort by count.
```

Also grep frontmatter `tags:` lists.

### /obsidian daily - daily note

```
Step 1: today = current date YYYY-MM-DD
Step 2: Glob "daily-notes/{today}.md"
Step 3a: Exists → Read, offer to append a new section
Step 3b: Missing → Read system/templates/Daily Note.md, substitute, Write to daily-notes/{today}.md
Step 4: Optionally open in Obsidian (see below)
```

### /obsidian moc "Topic" - Map of Content

```
Step 1: Grep vault for the topic. Collect matching files.
Step 2: Read each match, extract title and first paragraph for context
Step 3: Categorize (by tag, by folder, by heuristic)
Step 4: Write / update moc/MOC - <Topic>.md with:
  ---
  type: moc
  tags: [moc, <topic-tag>]
  date: <today>
  ---
  # <Topic> - Map of Content
  ## <subcategory 1>
  - [[link 1]] - short blurb
  - [[link 2]] - short blurb
  ## <subcategory 2>
  ...
```

## Open a note in Obsidian (URI, Windows)

From Git Bash:

```bash
cmd.exe //c start "" "obsidian://open?vault=<name>&file=academic/My-Task.md"
```

From PowerShell:

```powershell
Start-Process "obsidian://open?vault=<name>&file=academic/My-Task.md"
```

URI-encode spaces as `%20`. Forward slashes work in the path.

## Frontmatter standards

Minimum block every new note gets:

```yaml
---
title: <% tp.file.title %>
date: <% tp.date.now("YYYY-MM-DD") %>
type: <note | research | project | task | daily | moc | person>
tags: []
status: <draft | active | done | archived>
---
```

For task notes, add:

```yaml
course: <course code if applicable>
task: <task number>
rubric_aspects: []
due: <YYYY-MM-DD>
evaluator_status: <not-submitted | submitted | revision | passed>
```

## Performance notes (file ops only)

On a ~1000-note vault:
- Search by content: 1 to 2 s (Grep)
- Orphan scan: 5 to 15 s (Grep all links, build index)
- Backlinks: ~1 s (single Grep)
- Tag aggregation: 2 to 3 s (Grep plus post-process)

If the vault grows past around 5000 notes and Tier 1 gets slow, batch discovery into per-top-level-folder passes.

## What is intentionally NOT here

- Mac binary paths
- External skill directory references
- MCP server registration
- API tokens, gateways, or marketplaces
- SessionStart hooks
- Any URL beyond the local `obsidian://` URI scheme
