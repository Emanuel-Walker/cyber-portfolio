---
name: prompt-optimizer
description: Take a raw prompt, diagnose gaps, and rewrite it as a clear, scoped, ready-to-paste prompt. Advisory only. Never executes the task itself.
offline: true
---

# Prompt Optimizer

Diagnose a draft prompt, point out what is missing, propose the right skill or workflow, and output a ready-to-paste optimized prompt. **Advisory only. Do not execute the task.**

## When to use

- User says "optimize this prompt" / "improve my prompt" / "rewrite this prompt"
- User says "help me write a better prompt for..."
- User pastes a draft and asks for feedback or enhancement
- User says "I do not know how to prompt for this"

## When NOT to use

- User wants the task done directly ("just do it") - execute it, do not optimize
- User says "optimize this code" / "optimize performance" - that is refactoring, different skill
- User wants a skill inventory - list skills directly, do not run this pipeline

## Hard rule: advisory only

Do NOT write code, create files, run commands, or take implementation action inside this skill. Output is diagnosis plus optimized prompt only. If the user says "just do it" / "stop optimizing", tell them to make a normal task request instead.

## Context to personalize the optimized prompt

Adapt these to your own setup. The point is: the optimizer should know enough about the user's environment to route the prompt correctly.

- **Environment**: OS, shell, offline-only or networked
- **Vault / repo path**: the primary content root
- **Content domains**: what the user actually works on (academic, technical, personal, teaching)
- **Voice preferences**: banned words, sentence-shape rules
- **Format preferences**: how the user wants deliverables shaped (verbatim Q+A, prose, code-first)
- **Installed skills**: so the optimizer can route to the right one

If the user's prompt touches one of these domains, the optimized prompt should reference the right folder, register, and downstream skill.

## Installed skills (route prompts toward these)

| Skill | When to suggest in an optimized prompt |
|-------|----------------------------------------|
| `obsidian` | Anything that touches a notes vault - note creation, search, backlinks, MOC, frontmatter |
| `humanizer` | Drafts that need AI tells stripped before delivery |
| `article-writing` | Long-form drafts (papers, essays, posts, guides) |
| `brand-voice` | Multi-output content where voice consistency matters |
| `ship-learn-next` | Source is a lecture / transcript / reading and the user wants action, not a summary |
| `content-engine` | Social posts (short-form, long-form social, newsletter) |
| `file-organizer` | Cleaning up inbox folders, deduping, restructuring |
| `drawio` | Diagrams (flowchart, architecture, sequence) |
| `smart-ocr` | Extract text from images or scanned PDFs |

## Pipeline

### Phase 1: intent detection

Classify the task.

| Category | Signals | Example |
|----------|---------|---------|
| New artifact | build, create, draft, write | "Draft a paper section" |
| Fix / debug | broken, error, does not work | "My query returns nothing" |
| Refactor / tidy | clean up, restructure, organize | "Organize my inbox" |
| Research / how-to | how to, what is, explain | "How do I sign LDAP traffic" |
| Review / audit | review, audit, check | "Audit my walkthrough" |
| Plan / design | plan, design, architecture | "Plan my next 4 projects" |
| Transform content | turn X into Y, summarize, extract | "Turn this lecture into a rep plan" |
| Voice / writing | sound like me, in my voice, less AI | "Make this not sound like a chatbot" |

### Phase 2: scope assessment

| Scope | Heuristic | Approach |
|-------|-----------|----------|
| TRIVIAL | Single file, 1 to 2 line answer | Direct execution, no skill chain |
| LOW | Single skill, single output | One skill invocation |
| MEDIUM | 2 to 3 skills chained, one domain | Sequential, name the chain |
| HIGH | Multi-domain, 5+ files, ambiguous | `/plan` first, then phased |
| EPIC | Multi-session, branching outcomes | Break into separate sessions |

### Phase 3: missing-context detection

Scan for missing info. If 3+ critical items are missing, ask up to 3 clarifying questions before producing the optimized prompt.

- [ ] Domain - which content lane?
- [ ] Target scope - files, folders, specific note, vault-wide?
- [ ] Output destination - which folder? saved as file or inline?
- [ ] Voice / register - academic, operator, technical, reverent?
- [ ] Acceptance criteria - how does the user know it is done?
- [ ] Reference material - what existing notes / sources should it use?
- [ ] Scope boundaries - what NOT to do?
- [ ] Format - verbatim Q+A? prose? code? diagram?
- [ ] One-shot risk - is this a one-shot assessment or a draft to iterate on?

### Phase 4: workflow recommendation

For LOW: name one skill plus the action.
For MEDIUM: name the skill chain in order.
For HIGH / EPIC: start with a planning command or a session resume point.

## Output format

Present analysis in this exact structure.

### Section 1: prompt diagnosis

**Strengths**: what the original prompt does well.

**Issues**:

| Issue | Impact | Fix |
|-------|--------|-----|
| (problem) | (consequence) | (how to fix) |

**Needs clarification**: numbered questions, if any.

### Section 2: recommended chain

| Step | Skill / Action | Purpose |
|------|----------------|---------|
| 1 | `<skill>` | ... |
| 2 | `<skill>` | ... |
| 3 | save to `<path>` | ... |

### Section 3: optimized prompt (full)

Inside a single fenced code block. Self-contained. Includes:

- Clear task description with domain context
- Voice register and any banned moves
- File paths (vault folders, save destinations)
- Skill chain at the right steps
- Acceptance criteria
- Scope boundaries (what NOT to do)
- Format spec

### Section 4: optimized prompt (quick)

Compact one-liner for repeat use. Example patterns:

| Intent | Quick pattern |
|--------|---------------|
| Draft academic section | `Draft <section> for <course> Task <N>. Cite per style. Save to <academic path>. Apply humanizer.` |
| Clean a draft of AI tells | `Apply humanizer to <file>. No em dashes, no curly quotes, deliver final rewrite only.` |
| Lecture to action plan | `Ship-learn-next on <transcript>. Save to <academic path>.` |
| Organize inbox | `file-organizer on <inbox path>. Propose plan first. Confirm before moves.` |
| Build diagram | `Draw.io of <thing>. Output XML. Save to <diagrams path>.` |
| Vault search | `Obsidian search "<query>". Show top 20 matches with context.` |

### Section 5: enhancement rationale

| Enhancement | Reason |
|-------------|--------|
| (what was added) | (why it matters) |

### Footer

> Not what you need? Tell me what to adjust, or make a normal task request if you want execution instead of prompt optimization.

## Example

**User input:**
> help me write a paper section about defense in depth

**Diagnosis:**
- **Strengths**: clear topic.
- **Issues**:
  - No course or task context - which course?
  - No section type (intro, body, case study?)
  - No length target
  - No reference material specified
  - No save destination
- **Needs clarification**:
  1. Which course / task number?
  2. Section type - intro, body paragraph, comparison, case study?
  3. Approximate word count or rubric aspects to address?

**Optimized prompt (full):**

```
Draft a body section on "defense in depth" for <course code> Task <N>.

Context:
- Vault root: <your-vault-root>
- Save to: <your-vault-root>/academic/<course>/<task-id>-defense-in-depth.md
- Register: academic, third-person, present tense, cited per required style
- Word target: ~500 words
- Rubric aspects this section must hit: <paste rubric aspects>

Workflow:
1. Run brand-voice (use the academic profile if it exists, otherwise default academic register)
2. Run article-writing - structure as: claim, mechanism, example, citation
3. Use existing notes in <your-vault-root>/resources/technical/ as evidence if they apply
4. Apply humanizer in-place during composition (no em dashes, no AI vocabulary)
5. Final sweep: every paragraph has at least one citation

Format:
- Frontmatter: course, task, rubric_aspects, due, evaluator_status
- Section heading matches the rubric aspect verbatim
- No curly quotes, no emojis
- References section at the bottom, formatted per required style

Do not:
- Insert opinions or first-person unless the rubric calls for reflection
- Pad with rule-of-three when two examples are enough
- Add "in conclusion" or generic closers
```

**Optimized prompt (quick):**

```
Draft <course> Task <N> body section "defense in depth" (~500w, cited, hits rubric <aspects>). Save <academic path>. Chain: brand-voice, article-writing, humanizer.
```

## Related skills

This skill REFERENCES other skills. It does not replace them. After producing an optimized prompt, the user runs it normally and the relevant skill executes.
