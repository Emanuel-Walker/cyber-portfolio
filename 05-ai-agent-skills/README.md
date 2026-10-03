---
title: AI Agent Skills
updated: 2026-10-03
---

# AI Agent Skills

AI assistants are only as good as the instructions they load. These are mine. Fork what works.

## What this is

Ten modular skill files. Each one teaches a skill-aware AI assistant (Claude Code, Cursor, or any assistant that can load instruction modules on demand) how to do one specialized thing well.

Each skill is a single markdown file with YAML front matter and a scoped set of rules. The assistant reads it when the trigger fires and applies the logic. No code, no runtime, no plugin install. Just text that becomes behavior.

These were built for my own workflow. I am publishing them because other builders asked how I organize instructions, and because a public reference is easier to point at than a private folder. Fork, adapt, discard what does not fit.

## The ten skills

| # | Skill | What it does |
|---|-------|--------------|
| 1 | `content-engine` | Generates platform-native drafts from an approved seed. Enforces voice rules, hook formulas, and a never-publish contract. |
| 2 | `humanizer` | Strips AI writing tells from text. Rewrites inflated symbolism, promotional adjectives, rule-of-three padding, filler. Genre-aware. |
| 3 | `article-writing` | Drafts long-form writing (essays, blog posts, papers, newsletters). Leads with the artifact, explains after. |
| 4 | `brand-voice` | Builds a reusable VOICE PROFILE from real samples so downstream skills do not re-derive style on every run. |
| 5 | `prompt-optimizer` | Diagnoses a raw prompt and rewrites it as a clear, scoped, ready-to-paste prompt. Advisory only. |
| 6 | `drawio` | Creates and edits draw.io diagrams in XML. Flowcharts, architecture, sequence diagrams. Export to PNG. |
| 7 | `file-organizer` | Organizes files and folders on Windows. Finds duplicates, proposes structures, confirms before moving. |
| 8 | `ship-learn-next` | Turns learning content into a Ship-Learn-Next rep plan. 100 reps beats 100 hours of study. |
| 9 | `smart-ocr` | Extracts text from images and scanned PDFs with PaddleOCR 3.6 locally. Routes output to the right folder. |
| 10 | `obsidian` | Automates an Obsidian vault with file ops and the `obsidian://` URI scheme. Offline. |

## Install

See `INSTALL.md` for Claude Code, Cursor, and generic skill-aware assistants.

Short version for Claude Code:

```
cp -r skills/<skill-name>/ ~/.claude/skills/
```

## What you would adapt

These skills reference generic placeholders where my own workflow uses specific paths. Before using them you will want to swap:

- `<your-vault-root>` - the root path of your notes repository
- `<your-content-root>` - where your content engine lives, if you run one
- `<your-system-folder>` - where your templates, voice profiles, and automation configs live
- Voice preferences - I have specific banned words and sentence-shape rules. Yours will differ.
- Platform specifics - the content-engine skill assumes short-form video on a vertical feed. If you ship elsewhere, change the format spec.

## What is not here

Skills tied to specialized domain content, personal credentials, or anything with operational sensitivity stay private. The ten published here are the reusable, generalizable ones.

## Honest framing

These are personal instruction modules, not a product. The structure is sound. The specifics are mine. You should not run them as-is unless your workflow happens to match mine. Read the logic, keep the pattern, replace the specifics.

## License

MIT. Use it, remix it, teach from it.
