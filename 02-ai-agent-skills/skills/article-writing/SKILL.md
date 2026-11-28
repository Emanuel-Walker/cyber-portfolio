---
name: article-writing
description: Write long-form content (essays, blog posts, guides, tutorials, academic papers, newsletter issues) in a distinctive voice. Lead with the concrete artifact, explain after.
offline: true
---

# Article Writing

Write long-form that sounds like a person with a point of view, not an LLM smoothing itself into paste.

## When to activate

- Drafting academic papers, essays, task narratives, reflection pieces
- Drafting blog posts, launch posts, guides, tutorials, newsletter issues
- Turning notes, transcripts, or lecture videos into polished long-form
- Tightening structure, pacing, evidence in existing drafts

## Voice

| Context | Voice |
|---------|-------|
| Academic paper | Clean, evidence-driven, third-person, present tense for findings, cited per required style |
| Academic reflection task | First-person allowed. Still concrete and specific, not diary-padding. |
| Personal essay / blog | Operator voice: blunt, compressed, concrete, specifics over adjectives |
| Technical writeup | Code-first, artifact-first, explain after |
| Teaching / devotional | Match author tone, reverent but plain |

If the user wants a specific voice profile, run `brand-voice` first and reuse the resulting VOICE PROFILE block. Do not re-derive style here.

If no voice references are given, default to an operator voice: concrete, unsentimental, useful. Short paragraphs. Show, then say.

## Core rules

1. Lead with the concrete thing: artifact, example, screenshot, number, anecdote, code block, quote.
2. Explain after the example, not before.
3. Sentences tight unless the source voice is intentionally expansive.
4. Proof over adjectives.
5. Never invent facts, credibility, or customer evidence.
6. If academic: every claim cited in the required style. Sources match the reference list.

## Banned patterns (delete and rewrite)

- "In today's rapidly evolving landscape"
- "game-changer", "cutting-edge", "revolutionary"
- "here's why this matters" as a standalone bridge
- Fake vulnerability arcs
- Closing question added only to juice engagement
- Bio padding that does not move the argument
- Generic AI throat-clearing
- Em dashes - genre-aware. Banned in Genre A (operational, technical, academic). Allowed and encouraged in Genre B (scholarship, devotional, public writing). Natural in Genre C (journal / conversational).
- "Excited to share" / "I am thrilled to announce"
- Rule-of-three when only two examples exist

## Writing process

1. **Clarify audience and purpose.** Academic graders? Newsletter readers? Self-reflection? Pick before drafting.
2. **Build a hard outline.** One job per section. For academic work, mirror the rubric headings verbatim.
3. **Start sections with proof, artifact, conflict, or example** - never with theory or warm-up.
4. **Expand only where the next sentence earns space.**
5. **Cut templated, overexplained, or self-congratulatory passages.**
6. **Run humanizer rules in-place** while composing.

## Structure templates

### Academic performance task

```
Frontmatter:
  course, task, due, evaluator_status, rubric_aspects

# <Task title>

## A1. <Rubric aspect 1 - verbatim from rubric>
<One claim. One source. Specific detail. Cite per required style.>

## A2. <Rubric aspect 2>
<Same structure.>

## B1. <Section 2 aspect 1>
...

## References
<Formatted per required style, alphabetized>
```

Default save location: `<your-system-folder>/academic/<course-code>/<task-id>-<title>.md`

### Technical guide / how-to

```
# <Result the reader gets, stated as outcome>

<Concrete code / command / screenshot - the artifact you are explaining.>

<Why this matters in one sentence, no warm-up.>

## <Step 1 verb>
<Command and expected output.>

## <Step 2 verb>
...

## When it breaks
<Specific failure modes you have seen, not hypotheticals.>

## What to do next
<Actionable, not "exciting times ahead".>
```

### Personal essay / opinion

- Open with tension, contradiction, or a specific observation.
- One argument thread per section.
- Opinions answer to evidence.
- End on a concrete observation, not a slogan.

### Newsletter issue

- First screen does real work. No diary filler.
- Section labels only if they improve scanning.
- Every section adds something new.

## Quality gate (before delivery)

Identify the genre (A/B/C) and the destination first, then check:

**Universal:**
- [ ] Factual claims backed by provided sources
- [ ] Generic AI transitions removed (run humanizer checklist)
- [ ] Voice matches the supplied examples or VOICE PROFILE
- [ ] Every section adds something new
- [ ] Zero curly quotes, zero emojis (unless requested)
- [ ] Sentence-length variety
- [ ] First screen of the article does real work
- [ ] Specific detail present (numbers, names, dates)

**Genre A only (operational, academic, career-focused long-form, technical writeup):**
- [ ] Zero em dashes, zero en dashes, zero `--`
- [ ] BLUF first
- [ ] Active voice
- [ ] No filler ("really", "very", "just", "actually" without earned purpose)
- [ ] If academic: every paragraph has at least one citation. Reference list clean.

**Genre B (scholarship, devotional, published article):**
- [ ] Em dashes allowed for pacing. Do not strip.
- [ ] Scene opening, not thesis opening
- [ ] Show, do not tell
- [ ] Forward-looking close
- [ ] Faith (if present) stays load-bearing in devotional work. Stays subtle in public writing unless the piece invites it.

**Genre C (journal, voice notes, conversational):**
- [ ] Sounds like the author actually talking

## Save locations (default pattern)

| Type | Folder |
|------|--------|
| Academic drafts | `<your-vault-root>/academic/<course>/` |
| Publish-ready | `<your-vault-root>/outbound/` |
| Reflection / personal essay | `<your-vault-root>/self/` |
| Teaching / study notes | `<your-vault-root>/teaching/` |
| Technical writeup | `<your-vault-root>/resources/technical/` |
| Drafts in progress | `<your-vault-root>/inbox/` then move on completion |

## Related skills

- `humanizer` - apply patterns during and after composition
- `brand-voice` - derive VOICE PROFILE from real samples
- `ship-learn-next` - when input is a transcript and you want a rep plan, not an article
- `content-engine` - when output is multi-platform social, not long-form
- `obsidian` - for saving, frontmatter, MOC linkage
