---
name: file-organizer
description: Organize files and folders on Windows 11. Find duplicates, propose structures, automate cleanup. Uses Git Bash and PowerShell. Defaults to a configurable inbox folder.
offline: true
---

# File Organizer (Windows)

Reduce clutter without manual cognitive overhead. Default starting point: `<your-vault-root>/inbox/`, usually the worst hotspot for unsorted screenshots, PDFs, and dropped files.

## When to use

- An inbox folder is a swamp of pasted images and unsorted PDFs
- Files are scattered across Downloads, Desktop, and inbox
- Duplicate files eating space (zip backups, repeated screenshots)
- Folder structure drifted and no longer matches your convention
- Starting a new project and need a good scaffold
- Cleaning up before zipping or archiving

## Default target

Unless the user specifies otherwise, work on `<your-vault-root>/inbox/` first. Common content types in a typical inbox:

- Reference PDFs (route to a resources folder)
- Academic PDFs (route to academic / coursework folder)
- Pasted screenshots (route to attachments by date)
- Medical or financial PDFs (route to appropriate area)
- Loose markdown drafts (route to drafts or archive)
- Backups and zip files (route to archive or delete after confirmation)

Always confirm the routing plan before moving anything. Inbox files are often mid-flight.

## How to invoke

```
help me organize my inbox
find duplicates in the vault
clean up old files I have not touched in 6+ months
review my projects folder and suggest a better structure
```

## Workflow

### 1. Understand scope

Ask:
- Which directory? (default: inbox)
- Main problem? (cannot find things / duplicates / drift / messy)
- Any files or folders to avoid? (active drafts, sensitive)
- Aggressiveness? (conservative / moderate / comprehensive)

### 2. Analyze current state

Use Git Bash:

```bash
# Overview
ls -la "<your-vault-root>/inbox/"

# File types and counts
find "<your-vault-root>/inbox" -maxdepth 1 -type f \
  | sed 's/.*\.//' | sort | uniq -c | sort -rn

# Largest files
du -sh "<your-vault-root>/inbox"/* 2>/dev/null \
  | sort -rh | head -20

# Files modified > 6 months ago
find "<your-vault-root>/inbox" -maxdepth 1 -type f -mtime +180
```

Or PowerShell for richer metadata:

```powershell
$target = "<your-vault-root>\inbox"

# File-type breakdown
Get-ChildItem -Path $target -File |
  Group-Object Extension |
  Sort-Object Count -Descending |
  Format-Table Count, Name

# Largest files
Get-ChildItem -Path $target -File |
  Sort-Object Length -Descending |
  Select-Object -First 20 Name, @{N='SizeMB';E={[math]::Round($_.Length/1MB, 2)}}, LastWriteTime

# Stale files (older than 6 months)
Get-ChildItem -Path $target -File |
  Where-Object { $_.LastWriteTime -lt (Get-Date).AddMonths(-6) } |
  Select-Object Name, LastWriteTime
```

Summarize findings: total files, total size, file-type breakdown, date ranges, obvious issues.

### 3. Find duplicates

PowerShell hash-based detection:

```powershell
$target = "<your-vault-root>"

Get-ChildItem -Path $target -Recurse -File |
  Get-FileHash -Algorithm MD5 -ErrorAction SilentlyContinue |
  Group-Object Hash |
  Where-Object Count -gt 1 |
  ForEach-Object {
    [PSCustomObject]@{
      Hash  = $_.Name
      Count = $_.Count
      Paths = ($_.Group | ForEach-Object { $_.Path })
    }
  } |
  Format-List
```

Or Git Bash:

```bash
find "<your-vault-root>" -type f -exec md5sum {} + \
  | sort | uniq -w32 -dD
```

For each duplicate set: show all paths, show sizes and dates, recommend which to keep, always confirm before deleting.

### 4. Propose structure

Present plan before changing anything:

```markdown
# Organization plan: inbox

## Current state
- 158 files, 412 MB
- 110 pasted screenshots
- 22 PDFs
- 13 markdown files
- 8 images
- 5 other

## Proposed routing

| Pattern | Destination |
|---------|-------------|
| Pasted screenshots YYYY-MM | <your-vault-root>/attachments/screenshots/YYYY-MM/ |
| Reference PDFs (topic A) | <your-vault-root>/resources/topic-a/ |
| Academic PDFs | <your-vault-root>/academic/<course>/ |
| Medical PDFs | <your-vault-root>/health/records/ |
| Financial PDFs | <your-vault-root>/finance/ |
| Loose markdown drafts | <your-vault-root>/drafts/ |
| Audio files | <your-vault-root>/attachments/audio/ |

## Files needing your decision
- large_backup.zip (368 MB) - keep, delete, or move to archive?
- ancestry_dna.txt (17 MB) - family or self?

Ready to proceed? (yes / modify / abort)
```

### 5. Execute (after approval)

```powershell
# Create folder structure
New-Item -ItemType Directory -Force -Path "attachments\screenshots\YYYY-MM"

# Move files (preserves modification time by default)
Move-Item -Path "inbox\Pasted image *.png" -Destination "attachments\screenshots\YYYY-MM\"

# Verify
Get-ChildItem "attachments\screenshots\YYYY-MM\" | Measure-Object
```

Rules:
- Confirm before deleting anything (period)
- Log every move
- Preserve modification dates
- Handle filename conflicts gracefully (Move-Item -Force only if approved)
- Stop and ask if anything unexpected happens

### 6. Summary

```markdown
# Done

- Created 7 new folders
- Moved 143 files
- Found 0 duplicates (or N listed for review)
- 15 files left in inbox flagged for decision

## Maintenance tips
- Weekly: sort new pasted images out of inbox into dated folders
- Monthly: run the duplicate check against attachments
- Quarterly: archive completed project folders

## Quick commands
- `find inbox -type f -mtime -7` - files added this week
- `du -sh inbox/*` - see what is eating space
- `Get-ChildItem inbox | Group-Object Extension` - type breakdown
```

## Default folder cheat sheet (adapt to your vault)

| Content | Folder |
|---------|--------|
| Pasted images, screenshots, audio | `<your-vault-root>/attachments/<topic>/<YYYY-MM>/` |
| Academic coursework | `<your-vault-root>/academic/<course>/` |
| Technical references | `<your-vault-root>/resources/technical/` |
| Teaching / study notes | `<your-vault-root>/teaching/` |
| Medical / health | `<your-vault-root>/health/` |
| Finance / receipts | `<your-vault-root>/finance/` |
| Family / legacy | `<your-vault-root>/self/family/` |
| Drafts in progress | `<your-vault-root>/inbox/` then move on completion |
| Completed / inactive | `<your-vault-root>/archive/` |

## Related skills

- `obsidian` - for vault-aware file operations (frontmatter, MOC)
- `smart-ocr` - if the inbox has images needing text extraction before routing
