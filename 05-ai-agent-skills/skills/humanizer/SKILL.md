---
name: humanizer
description: Remove AI-writing tells from text. Detects and rewrites inflated symbolism, promotional language, -ing analyses, vague attributions, em dash overuse, rule of three, AI vocabulary, passive voice, negative parallelisms, filler. Genre-aware.
offline: true
allowed-tools: [Read, Write, Edit, Grep, Glob]
---

# Humanizer - Remove AI Writing Tells

Strip AI patterns from text. Rewrite, do not delete. Preserve meaning, match the voice.

## Registers

| Context | Register |
|---------|----------|
| Academic work | Clean, neutral, evidence-driven. Mute personality. Match the citation style the assignment calls for. |
| Personal essays, blog, newsletter | Blunt operator voice. Short sentences. Specifics. No corporate slop. |
| Technical writeups | Direct, no fluff, code-first. Show the artifact, then explain. |
| Teaching notes | Match the source author's tone. Reverent but plain. |
| Social posts | Compressed, no engagement bait. See the content-engine skill. |

Advisory for the author's own voice: no em dashes, no en dashes, no curly quotes, no bold-headed inline lists. These are personal preferences, not universal rules. Adjust to taste.

If a VOICE PROFILE already exists (see the brand-voice skill), use that instead of defaults.

## Process (every job)

1. Read input. Identify every pattern instance.
2. Write a draft rewrite. Reads natural aloud, varied sentence length, prefers `is/are/has` over `serves as/stands as`.
3. Ask: "What still tells me this is AI?" Bullet remaining tells.
4. Revise to a final rewrite. Run a final find-replace sweep before delivery.
5. Deliver: draft, still-AI bullets, final, optional short changelog.

## CONTENT PATTERNS

### 1. Inflated significance / legacy
Words: *stands/serves as, a testament, pivotal, key moment, evolving landscape, setting the stage, indelible mark, deeply rooted, marks a shift*.
Fix: state the fact without ceremony.

### 2. Promotional notability
Words: *cited in [outlet list], active social media presence, written by a leading expert*.
Fix: replace name-dropping with a specific claim from one source.

### 3. -ing endings doing fake analysis
Words: *highlighting, ensuring, reflecting, contributing to, fostering, encompassing, showcasing*.
Fix: break the dependent clause off. Make it a separate sentence or drop it.

### 4. Promotional adjectives
Words: *vibrant, rich (figurative), nestled, in the heart of, breathtaking, must-visit, stunning, profound, groundbreaking*.
Fix: replace with a concrete attribute.

### 5. Vague attribution / weasel
Words: *industry reports, observers have cited, experts argue, several sources*.
Fix: name the source or cut the claim.

### 6. "Challenges and future prospects" sections
Phrase: *Despite challenges, faces several challenges, Despite these challenges*.
Fix: name the specific challenge with a date or number.

### 7. AI vocabulary
High-frequency: *delve, crucial, intricate, tapestry, landscape, pivotal, showcase, testament, underscore, vibrant, foster, garner, enhance, key (adj), align with, leverage, robust, seamless, intuitive*.
Fix: replace with a plainer word. Often the sentence is better without the adjective.

### 8. Copula avoidance
Words: *serves as, stands as, marks, represents, boasts, features, offers*.
Fix: use `is/are/has`.

### 9. Negative parallelisms / tailing negation
Form: *Not only X but also Y* / *It is not just X, it is Y* / *, no guessing*.
Fix: state X. State Y in its own sentence if needed. Drop the contrast scaffolding.

### 10. Rule of three
*X, Y, and Z* groupings used to feel comprehensive.
Fix: keep two if two is what you have. Do not pad to three.

### 11. Elegant variation (synonym cycling)
Cycling *protagonist, main character, central figure, hero*.
Fix: pick one word, repeat it.

### 12. False ranges
*From X to Y* where X and Y are not on a scale.
Fix: list the things.

### 13. Passive voice / subjectless fragments
*No configuration file needed. The results are preserved automatically.*
Fix: active voice with a real subject.

## STYLE PATTERNS

### 14. Em dashes - genre-aware

Identify the genre first, then apply the rule.

| Genre | Use case | Em dash rule |
|-------|----------|-------------|
| **A - Operational** | Dossiers, briefings, technical writeups, career posts, academic sections | No em dashes. Replace with period, comma, colon, parens, restructure. Also catch spaced `--`. |
| **B - Scholarship / Public / Devotional** | Scholarship essays, public-facing writing, devotionals, teaching notes, published articles | Em dashes encouraged for pacing. Sentence variety. Mix long emotional sentences with short impactful ones. Do not strip. |
| **C - Conversational** | Chat replies, voice notes, journal entries | Whatever sounds like the author actually talking. Less rule-based. Em dashes acceptable. |

If unsure which genre applies, ask the user or default to Genre A.

### 15. Boldface overuse
Stop bolding inline phrases mechanically. Bold only sparingly, for true emphasis.

### 16. Inline-header vertical lists
`- **Foo:** description.` Rewrite as prose.

### 17. Title Case headings
*## Strategic Negotiations And Global Partnerships* becomes *## Strategic negotiations and global partnerships*.

### 18. Emojis
No emojis in output unless the user explicitly wants them.

### 19. Curly quotes
Replace curly quotes with straight quotes.

## COMMUNICATION PATTERNS

### 20. Chatbot artifacts
*I hope this helps, Of course, Certainly, Want me to, Let me know if* - delete.

### 21. Knowledge-cutoff disclaimers / speculative gap-fill
*As of [date], While specific details are limited, it appears that, likely grew up*. Say what is not known, or cut the sentence. Do not invent.

### 22. Sycophantic openers
*Great question. You are absolutely right.* - delete.

## FILLER / HEDGING

### 23. Filler phrases
*In order to* becomes *to*. *Due to the fact that* becomes *because*. *At this point in time* becomes *now*. *Has the ability to* becomes *can*. *It is important to note that* - drop.

### 24. Excessive hedging
*Could potentially possibly might* - say it once.

### 25. Generic positive conclusions
*The future looks bright. Exciting times ahead.* - state one concrete next step or cut.

### 26. Hyphenated compound overuse
*The team is cross-functional* becomes *the team is cross functional* (predicate position, drop hyphen). *A cross-functional team* (attributive, keep).

### 27. Persuasive authority tropes
*The real question is, at its core, in reality, fundamentally, the heart of the matter*. State the claim directly.

### 28. Signposting / announcements
*Let's dive in, here's what you need to know, let's break this down*. Cut. Do the thing.

### 29. Fragmented headers
Heading + one-line restatement + the actual content. Cut the restatement.

### 30. Diff-anchored writing
*This function was added to replace*. Describe what it is, not what changed (unless writing a changelog).

### 31. Manufactured punchlines / staccato drama
A run of short declaratives engineered to sound dramatic. One emphatic short sentence is fine. Three in a row is a tell.

### 32. Aphorism formulas
*X is the language of Y, X becomes a trap, X is not a tool but a mirror*. Replace with the concrete claim.

### 33. Conversational rhetorical openers
*Honestly, Look, Here's the thing*. As standalone hooks - delete.

## FALSE POSITIVES - DO NOT FLAG

A clean human writer can hit several patterns without AI involvement. Cluster matters more than single tells.

- Perfect grammar and consistent style. Polish is not AI.
- Formal / academic vocabulary on its own.
- One em dash. One *however*. One short emphatic sentence.
- Curly quotes alone (word processors auto-curl).
- Mixed registers in one piece.
- Letter-style openings and closings.

When unsure, look for stacked tells. Em dashes plus rule of three plus *vibrant tapestry* plus a "Conclusion" section is a confession. One *however* is nothing.

## HUMAN SIGNALS - PRESERVE

- Specific, unusual, hard-to-fabricate detail. A real address. A weird quote.
- Mixed feelings, unresolved tension.
- Dated references, slang from a specific year.
- Variety in sentence length.
- Genuine asides, parentheticals, self-corrections.

## Academic notes

Academic papers default to a clean, neutral, evidence-driven register. The personality section of general humanizer work does not apply. Graders read against a rubric, not for voice.

For academic drafts:
- Strip AI tells per sections 1 through 33 above.
- Do not add opinions or first-person reactions unless the rubric explicitly calls for reflection.
- Cite every claim per the required style. Match the reference list.
- One claim per paragraph, supported by one source minimum.
- Do not pad with rule-of-three when the prompt only asks for two examples.

## Related skills

- `brand-voice` - build a VOICE PROFILE from real samples before rewriting.
- `article-writing` - draft long-form content. Runs humanizer-style rules during composition.

## Final delivery sweep

Before returning the final rewrite, identify the genre (A/B/C), then run these checks.

**Universal (all genres):**
- [ ] Zero curly quotes
- [ ] No emojis (unless explicitly requested)
- [ ] No chatbot artifacts
- [ ] No "in conclusion" or "the future looks bright" generic closers
- [ ] Sentence-length variety (not all 12 to 20 words)
- [ ] Specific detail present (numbers, names, dates)

**Genre A (operational):**
- [ ] Zero em dashes
- [ ] Zero en dashes
- [ ] Zero `--` used as dash
- [ ] BLUF first

**Genre B (scholarship / public / devotional):**
- [ ] Em dashes allowed for pacing. Do not strip.
- [ ] Sentence variety enforced
- [ ] Scene-opening, not thesis-opening
- [ ] Forward-looking close, not summary

**Genre C (conversational / journal):**
- [ ] Sounds like the author actually talking
- [ ] Less rule-based

**Academic papers:**
- [ ] Every claim has a citation
- [ ] Third person, present tense for findings
- [ ] No first-person opinion unless the rubric calls for reflection
