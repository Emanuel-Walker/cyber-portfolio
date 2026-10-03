---
name: brand-voice
description: Build a durable VOICE PROFILE from real source material (your posts, papers, messages), then reuse it across content, outreach, and papers instead of re-deriving style each time. Fully offline. Local samples only.
offline: true
---

# Brand Voice

Build a reusable VOICE PROFILE from real samples. The point is not literary analysis. The point is operational reuse across `article-writing`, `humanizer`, `content-engine`, and any other long-form work.

## When to activate

- User wants content in a specific voice (their own, or someone else's they are imitating)
- More than one downstream output is planned, so re-deriving style each time wastes effort
- The existing content lane needs a reusable style system instead of one-off mimicry

## Source priority (local files only)

Use the strongest real source set available, in this order:

1. Recent personal notes, journal entries, daily notes
2. Existing articles, essays, papers in the vault
3. Past outbound messages or DMs the user kept
4. Technical writeups
5. Teaching notes if matching a teaching voice

Do not use generic platform exemplars or AI-written drafts as source material.
Do not fetch external samples from the web. This skill is offline.

If the user has fewer than 3 strong samples on file, ask them to paste 3 to 5 samples into the conversation before deriving a profile.

## Collection workflow

1. Gather 5 to 20 representative samples when available.
2. Prefer recent material unless the user says older writing is more canonical.
3. Separate "public voice" (publish-ready, polished) from "private working voice" (messages, drafts) if they clearly split.
4. If the user is writing for two distinct contexts (academic paper vs. personal essay), derive two profiles. They will diverge.

## What to extract

- **Rhythm**: sentence length distribution. Short, medium, long mix?
- **Compression vs explanation**: dense or expansive?
- **Capitalization norms**: title case, sentence case, mixed?
- **Parenthetical use**: heavy, light, none?
- **Question frequency**: rhetorical, rare, bait?
- **Claim sharpness**: hedged or sharp? Numbers and mechanisms or adjectives?
- **Transitions**: explicit connectors (*however, therefore*) or section breaks?
- **What the author never does**: banned moves. Often the most useful signal.

## VOICE PROFILE schema

Output this exact structure. Save to `<your-system-folder>/voice/<profile-name>.md` for reuse.

```yaml
---
profile_name: <e.g. personal, academic, teaching>
derived_from: [list of source file paths]
derived_on: <YYYY-MM-DD>
sample_count: <integer>
register: <academic | operator | conversational | technical | reverent | mixed>
---

# VOICE PROFILE - <name>

## Rhythm
- Median sentence length: <words>
- Range: <short..long>
- Paragraph length: <short / medium / long>
- Rhythm pattern: <e.g. "short punch then expand", "even mid-length", "varied">

## Diction
- Vocabulary level: <plain / mixed / elevated>
- Signature words: [<list of words the author uses distinctively>]
- Banned words from samples: [<words they never use that AI defaults to>]
- Numbers / mechanisms / receipts vs adjectives: <ratio observation>

## Punctuation
- Em dashes: <yes/no - note if heavy or absent>
- Parentheticals: <heavy / light / none>
- Curly quotes: <yes/no>
- Bold inline: <yes/no>
- Lists: <prose / bulleted / numbered>

## Structure
- Openings: <how the author starts paragraphs and sections>
- Transitions: <what bridges sections>
- Closings: <how they end: punch, fade, summary?>

## Stance
- Hedging level: <none / light / heavy>
- Question use: <bait / rhetorical / rare>
- First-person frequency: <% if measurable>
- Opinion injection: <how often, how strong>

## Hard bans (do not write these)
- <List of moves the author never makes>
- <Phrases / patterns observed absent from the samples>

## Cliches and bait to avoid
- <Author-specific filler if any observed>
- AI patterns the author does not use - list to enforce

## Example phrases (verbatim from samples)
- "<quote 1>"
- "<quote 2>"
- "<quote 3>"
```

## Default profile system (three genres)

If no live samples exist yet, start with this three-genre split and refine as samples come in. Many authors use different genres for different work, so profile per genre, not universal.

```yaml
profile_name: genre-a-operational
register: operator
genre: A
```

- **When to use**: dossiers, briefings, technical writeups, career posts, operational notes
- **Rhythm**: short to medium sentences. Punch then expand. Occasional fragment.
- **Diction**: plain. Specifics win. No business jargon. No academic warm-up.
- **Punctuation**: no em dashes. Light parentheticals. Sentence case headings.
- **Stance**: blunt, direct. Strong claims when warranted. No bait questions. Minimal hedging.
- **Hard bans**:
  - "delve", "tapestry", "landscape" (as abstract noun), "pivotal", "underscore" (verb)
  - "Let's dive in", "here's what you need to know"
  - "Excited to share", "I am thrilled"
  - Rule of three when only two examples exist
  - Generic positive conclusions ("the future looks bright")
  - Bold-headed inline lists
  - Bait questions tacked on the end
  - Sycophantic openers, AI cadence

```yaml
profile_name: genre-b-public-devotional
register: public
genre: B
```

- **When to use**: scholarship essays, public-facing writing, devotionals, teaching, published articles
- **Rhythm**: sentence variety. Mix long emotional sentences with short impactful ones.
- **Diction**: scene over thesis. Show, do not tell. Sensory detail.
- **Punctuation**: em dashes allowed for pacing.
- **Stance**: open with scene not thesis. One central arc per piece. Forward-looking close.
- **Hard bans**:
  - AI cadence ("It is important to note", "Furthermore")
  - Performance language
  - "Excited to share", "I am thrilled"
  - Bait questions
  - Generic positive conclusions

```yaml
profile_name: genre-c-conversational
register: conversational
genre: C
```

- **When to use**: chat replies, voice notes, journal entries
- **Rhythm**: whatever sounds like the author actually talking. Less rule-based.
- **Diction**: real conversation register.
- **Punctuation**: natural.

**Academic papers**: use `genre-a-operational` with `register: academic` override. Mute personality, third-person, present tense for findings, evidence per claim, cited per required style.

**Technical writeups**: use `genre-a-operational` with `register: technical` override. Code-first, artifact-first, terse, command examples before prose.

**Default in ambiguity**: ask the user which genre. If you cannot ask, default to Genre A operational.

## Persistence

- Save profiles to `<your-system-folder>/voice/<profile-name>.md`
- Reference them from `article-writing` and `content-engine` by file path
- Reuse the latest confirmed profile across related tasks in the same session
- Update profiles when new representative samples appear. Do not rebuild from scratch each time.

## Downstream use

Run this skill BEFORE or INSIDE:

- `article-writing` (long-form drafts)
- `content-engine` (social posts)
- `humanizer` (so the rewrite matches your voice, not generic "natural human")
- Any outreach, cold email, or reflection work

## Hard bans (universal)

Delete and rewrite if you see these in output:

- Fake curiosity hooks
- "Not X, just Y"
- "No fluff" as a self-description
- Forced lowercase
- LinkedIn thought-leader cadence
- Bait questions
- "Excited to share"
- Generic founder-journey filler
- Corny parentheticals

## Notes on adaptation

The original personal version pulled from `x-api` for live posts. Removed here. If you want to derive a profile from your social posts, paste them into the conversation or save them to a file first. This skill is offline by design.
