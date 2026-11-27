---
name: content-engine
description: Generate platform-native drafts inside a content engine folder. Enforces hard rules (write-zone discipline, no fabrication, no publishing). Reads from a seed bank and voice samples, applies a hook-formula framework, writes needs-review drafts. Never auto-promotes.
offline: true
---

# Content Engine

This skill is the drafting layer that sits on top of an existing content engine at `<your-content-root>/`. It does not replace your harvester, classifier, or ingestion scripts. Those still run as scripts. This skill handles the draft generation stage: take an approved seed, apply a hook formula, match the author's voice, output a `needs-review` draft.

## Hard rules

These are non-negotiable. Violating any of them means the draft is wrong, even if it reads well.

1. **Write zone only**: write exclusively to `<your-content-root>/` subfolders. Every other vault file is read-only.
2. **status: needs-review always**: every generated file has `status: needs-review` in frontmatter. The author promotes to `approved`. The skill never does.
3. **Direct quotations are immutable**: when quoting scripture, books, or any canonical text, quote verbatim from the stored source. Never paraphrase. If text is not available: `[QUOTE: SOURCE REF - NEED SOURCE]`.
4. **No fabrication**: missing quote, stat, or story - write `NEED SOURCE`. Never invent. Never assume.
5. **Sensitive-topic review required**: topics flagged in your own hard-rules file need an `opsec_review: true` or equivalent sensitivity tag plus a loud warning banner above the draft body. Strip identifying detail before draft.
6. **Private categories stay private**: journal, personal reflection, family-of-origin, or any flagged category - no drafts without explicit per-seed instruction from the author.
7. **No publishing**: this skill never publishes, approves, or voices content on the author's behalf. Output is text only, into the drafts folder.
8. **Respect trigger flags**: do not surface seeds with `trigger_flag: *` or `opsec_review: true` in recommendations without explicit clearance.

Adapt rule 3 and rule 5 to your own domain. If you have specialized domain content with sensitivity needs, encode them here.

## Folder map (write zone pattern)

| Folder | What goes here |
|--------|----------------|
| `01_Seed_Bank/<category>/` | Harvested seeds. Read-only for this skill. Harvester writes them. The author promotes. |
| `02_Voice_Samples/` | The author's writing samples. Read before any draft. |
| `03_Intel/` | Channel data, top performers, proven formulas. Read for context. |
| `04_Calendar/` | Weekly plans, cadence tracker. Read for posting cadence. |
| `05_Generated_Drafts/` | Write zone. All drafts land here as `draft_YYYY-MM-DD_<title>.md` with `status: needs-review`. |
| `06_Scripts/` | Automation scripts. Do not modify. |
| `07_Logs/` | Run logs. Append a generation-log entry per draft session. |
| `00_Dashboard.md` | Dashboard hub. Read to see top seeds. Never edit. |

## Seed categories (default set - adapt to your content lanes)

| Category | What it is | Platforms |
|----------|------------|-----------|
| `book` | Multi-chapter narrative, memoir arc, universal story | Book chapter drafts |
| `teaching` | Instructional, pulpit-ready, lecture-ready | Teaching outlines |
| `brand_public` | Leadership, mentorship, career - the public lane | LinkedIn, X |
| `content_short_form` | Short-form video script, under 60s spoken | Shorts, Reels, TikTok |
| `content_long_form` | Blog, long-form social, newsletter | Newsletter, blog |
| `lifestyle` | Personal brand, day-in-life, process content | Image feeds |
| `journal` | Private. Reflection. Never published unless the author promotes. | n/a |

## Hook formula framework (short-form video)

Encode your own hook formulas. Here is a seven-formula skeleton you can adapt. The key is that each formula has a documented performance record (proven, untested, retired) so the skill can rotate between proven safe ground and deliberate experiments.

| # | Name | Structure | Status |
|---|------|-----------|--------|
| 1 | Reframe | "You are not X, you are Y" | Example proven formula |
| 2 | Contrast Yes | "World says X. The truth says Y about [topic]" | Top performer |
| 3 | Anchor Quote | "See [source ref]..." + verbatim quote + 20s application | Proven |
| 4 | Already-There | "You may not see X yet, but it is already Y" | Highest retention |
| 5 | If-Then | "If X happened then, Y can happen now" | Untested |
| 6 | Contrast Pair | "The lie says X. The truth says Y" | Untested |
| 7 | Direct Address | "This is for the person who [specific struggle]" | Proven |

Default rotation: lean on the proven formulas for safe ground. Pitch untested formulas deliberately to fill gaps. Always state which formula a draft uses in frontmatter.

## Voice genres

| Genre | Use for | Rules |
|-------|---------|-------|
| **A - Operational** | Career, public brand, technical, long-form industry writing | BLUF first, active voice, short sentences, no filler. |
| **B - Public / Devotional** | Public writing, devotionals, teaching, short-form video | Open with scene not thesis. Sentence variety. Show, do not tell. Forward-looking close. |
| **C - Journal / Raw** | Personal reflection only (never published unless promoted) | Natural voice, less structured, more honest. |

Always read `02_Voice_Samples/` before drafting. Pull 2 to 3 representative passages into context first.

## Short-form format spec (adapt to your platform)

| Element | Spec |
|---------|------|
| Orientation | Vertical 9:16 |
| Length | 25 to 40 seconds spoken |
| Hook timing | Starts at 0:00. Zero preamble. |
| Setting | Consistent (car interior, clean light background, studio) |
| Caption overlay | Bold, 3 to 6 words, visible in first frame |
| Hashtags | Encode your platform-specific tag strategy here. Ban irrelevant tags. |

## Output rules (apply to every draft)

- BLUF first - conclusion before explanation.
- Short and blunt. No padding.
- Chunked - numbered steps or bullets over walls of text.
- No AI cadence.

## Workflow

### Step 1: Determine intent

Ask or infer:
- Which seed? (path to a file in `01_Seed_Bank/<category>/`)
- Which category? (must match seed's `category:` frontmatter)
- Which platform target?
- Which formula? (only for content_short_form)
- Any sensitivity or trigger flags on the seed?

### Step 2: Pre-flight checks

- [ ] Seed exists and has `status: approved` (or the author said develop this specific file)
- [ ] Seed is NOT `category: journal` unless explicitly promoted
- [ ] If `opsec_review: true` - STOP. Ask for per-seed clearance.
- [ ] If `trigger_flag` - STOP. Ask.
- [ ] All quoted material is from the canonical source. If not, write `[QUOTE: REF - NEED SOURCE]`.

### Step 3: Load voice context

Read `02_Voice_Samples/` files relevant to the genre. If a VOICE PROFILE exists at `<your-system-folder>/voice/<name>.md`, use that as the canonical reference.

### Step 4: Draft

**For content_short_form:**

```markdown
---
status: needs-review
draft_of: <seed file path>
category: content_short_form
platform: [shorts, tiktok, reels]
genre: B
formula: <N - Name>
formula_rationale: <why this formula fits this seed>
caption_phrase: <3 to 6 word overlay>
estimated_length_seconds: <25 to 40>
hashtags: [<platform tags>]
opsec_review: false
trigger_flag: none
created: <YYYY-MM-DD>
tags: [needs-review, content-short-form, formula-<N>]
---

# <Working title - 3 to 6 words>

## Caption overlay
**<3 to 6 word phrase>**

## Spoken script (25 to 40s)
<Open with hook at 0:00 - no preamble.>

<Body - applies the formula.>

<Quote verbatim from canonical source or marked NEED SOURCE.>

<Application - 1 to 2 sentences max.>

<Close - forward-looking.>

## Hashtags
<platform tags>

## Notes
- Setting: <setting>
- Caption visible in first frame: yes
- Review checklist before posting:
  - [ ] Quotes match source
  - [ ] Length 25 to 40s when spoken aloud
  - [ ] No sensitive content leaked
```

**For content_long_form (newsletter, long post):**

```markdown
---
status: needs-review
draft_of: <seed file path>
category: content_long_form
platform: [newsletter | blog | long-post]
genre: <A | B>
opsec_review: false
trigger_flag: none
created: <YYYY-MM-DD>
tags: [needs-review, content-long-form]
---

# <Title>

<Hook - concrete artifact, observation, number. No preamble.>

<Body - one claim, supported. Specifics over adjectives.>

<Application - practical, forward-looking.>

<Close - actionable. No bait questions.>
```

**For teaching (lecture or sermon outline):**

```markdown
---
status: needs-review
draft_of: <seed file path>
category: teaching
genre: B
opsec_review: false
trigger_flag: none
created: <YYYY-MM-DD>
tags: [needs-review, teaching]
---

# <Teaching title>

## Big idea (one sentence)
<...>

## Text / source
<Verbatim. Mark NEED SOURCE if unavailable.>

## Outline
1. <Point 1>
2. <Point 2>
3. <Point 3>

## Personal application
<Author's voice, drawn from voice samples. No paraphrased sources.>

## Close
<Forward-looking.>
```

**For brand_public (career, leadership posts):**

Genre A operational. BLUF first. Short.

### Step 5: Save

Filename: `draft_YYYY-MM-DD_<short_title>.md` in `05_Generated_Drafts/`.

If the filename already exists, append `_v2`, `_v3`, etc. Never overwrite.

### Step 6: Log

Append to `07_Logs/generation_runs.md`:

```markdown
## <YYYY-MM-DD HH:MM> - Draft generated by content-engine skill
- Seed: <path>
- Category: <category>
- Formula: <N - Name> (if content_short_form)
- Output: 05_Generated_Drafts/<filename>
- Genre: <A | B | C>
- Flags: <none | listed>
```

### Step 7: Tell the author

Output:
- "Saved to `05_Generated_Drafts/<filename>`. Status: needs-review."
- One-line summary of the formula choice and genre.
- Any `NEED SOURCE` or `NEED USER INPUT` markers that require attention.
- Do not suggest publishing. Do not call it final. Do not offer to schedule it.

## What this skill is NOT

- Not the harvester. Seeds come from your ingestion scripts. This skill drafts from existing seeds. It does not create new ones.
- Not the classifier. Categories come from your classifier. This skill respects the category on the seed.
- Not the publisher. Nothing leaves the vault from here.
- Not a ghostwriter. The author authors everything. Drafts are starting points.
- Not for journal content. Journal seeds are private by default.

## Related skills

- `brand-voice` - derive and reuse VOICE PROFILE from voice samples.
- `humanizer` - final sweep on every draft.
- `article-writing` - for long-form blog and newsletter pieces.
- `ship-learn-next` - for converting a transcript into a rep plan, not a draft.
- `obsidian` - for vault-aware ops, frontmatter, MOC linkage.

## Typical cross-skill chain

```
1. brand-voice - load the matching voice profile
2. content-engine - draft using formula N, save to 05_Generated_Drafts/
3. humanizer - final sweep on the saved draft
4. obsidian - link the draft into the dashboard if the author asks
```
