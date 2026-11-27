---
name: ship-learn-next
description: Transform learning content (YouTube transcripts, lecture videos, academic readings, articles, tutorials) into actionable Ship-Learn-Next rep plans. Use when the user wants to turn advice into concrete reps, not study plans.
offline: true
allowed-tools: [Read, Write]
---

# Ship-Learn-Next Action Planner

Transform passive learning into shippable reps. 100 reps beats 100 hours of study. Learning equals doing better, not knowing more.

## When to activate

- User has a transcript, article, lecture, tutorial, or book chapter and wants to "implement the advice"
- User says "turn this into a plan" / "make this actionable"
- User wants to extract implementation steps from educational content
- User says "I watched / read X, now what should I do?"
- A lecture or reading needs to convert into reps (practice problems, drafts, labs)

## Core framework: Ship, Learn, Next

Three repeating phases per cycle:

1. **SHIP** - create something real (artifact, code, draft, demo, lab output)
2. **LEARN** - honest reflection on what happened
3. **NEXT** - plan the next iteration based on what you learned

## Save locations (adapt to your vault)

Pick destination based on what the source content is.

| Source | Save to |
|--------|---------|
| Academic lecture, reading, video | `<your-vault-root>/academic/<course>/Ship-Learn-Next - <Title>.md` |
| Technical skill development | `<your-vault-root>/resources/technical/Ship-Learn-Next - <Title>.md` |
| Personal project / business idea | `<your-vault-root>/projects/<project>/Ship-Learn-Next - <Title>.md` |
| Teaching / study content | `<your-vault-root>/teaching/Ship-Learn-Next - <Title>.md` |
| Health / fitness / habits | `<your-vault-root>/health/Ship-Learn-Next - <Title>.md` |
| Unclear / cross-domain | `<your-vault-root>/inbox/Ship-Learn-Next - <Title>.md` then move on completion |

## Workflow

### Step 1: Read the content

Read the file the user provides. Use the Read tool. No fetching from URLs.

### Step 2: Extract core lessons

Pull from the content:
- Main advice / lessons: the actual takeaways
- Actionable principles: what can be practiced
- Skills being taught: what someone learns by doing this
- Examples / case studies: real implementations to mirror

Skip: theory without application, "nice to know" content, summaries.

### Step 3: Define the quest

Ask the user (or infer if obvious from context):
1. "Based on this content, what do you want to achieve in 4 to 8 weeks?"
2. "What would success look like? Be specific."
3. "What is something concrete you could build, create, or ship?"

| Good quest | Bad quest |
|-----------|-----------|
| "Pass D481 Task 1 - submit a network security plan that hits all 8 rubric aspects" | "Get better at network security" |
| "Ship 10 cold outreach messages, get 2 responses" | "Learn about sales" |
| "Solve 20 Wireshark CTF problems on locked-down PCAPs" | "Practice Wireshark" |

### Step 4: Design Rep 1 (the smallest shippable version)

Ask:
- "What is the smallest version you could ship THIS WEEK?"
- "What do you need to learn JUST to do that?" (not everything)
- "What would 'done' look like for rep 1?"

Make Rep 1:
- Concrete and specific
- Completable in 1 to 7 days
- Produces real evidence / artifact
- Small enough not to be intimidating
- Big enough to learn something meaningful

### Step 5: Write the rep plan

Use this structure per rep.

```markdown
## Rep N: <Specific Goal>

**Ship Goal**: <Concrete deliverable>
**Timeline**: <This week / by YYYY-MM-DD>
**Success Criteria**:
- [ ] <Specific thing 1>
- [ ] <Specific thing 2>
- [ ] <Specific thing 3>

**What You Will Practice** (from the source):
- <Skill / concept 1 - source reference>
- <Skill / concept 2 - source reference>

**Action Steps**:
1. <Concrete step>
2. <Concrete step>
3. <Concrete step>
4. Ship it (publish, deploy, share, submit)

**Minimal Resources** (only for this rep):
- <Link or reference only if truly needed>

**After Shipping - Reflection**:
- What actually happened? (Specific.)
- What worked? What did not?
- What surprised you?
- Rate this rep: _/10
- One thing to try differently next time
```

### Step 6: Map future reps (2 to 5)

Each rep:
- Builds on what you learned in the previous rep
- Adds ONE new element
- Increases difficulty based on success
- References specific lessons from the source

Do not plan reps 6 through 100. Just 2 to 5. The path evolves based on what you learn in 1 and 2.

## Output structure (saved file)

```markdown
---
title: Ship-Learn-Next - <Quest Title>
type: rep-plan
date: <YYYY-MM-DD>
source: <file path or title>
status: rep-1-active
tags: [ship-learn-next, <domain>]
course: <course code if applicable>
---

# Ship-Learn-Next: <Quest Title>

## Quest Overview
**Goal**: <What you want to achieve in 4 to 8 weeks>
**Source**: [[<source file>]]
**Core Lessons** (3 to 5 actionable takeaways):
- <Lesson 1>
- <Lesson 2>
- <Lesson 3>

---

## Rep 1: <Goal>
<Full rep block from Step 5>

---

## Rep 2: <Goal>
<Brief - fills in detail after Rep 1 reflection>

## Rep 3 to 5: Future Path
- Rep 3: <one line>
- Rep 4: <one line>
- Rep 5: <one line>

*(Details evolve based on Rep 1 and 2 outcomes.)*

---

## Remember
- DOING, not studying
- Aim for 100 reps over time
- Each rep: Plan, Do, Reflect, Next
```

## Hard rules

- Do not create a study plan. Create a SHIP plan.
- Do not list all resources to read or watch. Pick minimal resources for the current rep.
- Do not accept vague goals. "Learn X" becomes "Ship Y by Z date."
- Do not overwhelm with the full journey. Focus on Rep 1.
- Do not add academic language to a personal-project plan, or vice versa. Match the register to the destination folder.
- Do not write teaching reps with secular operator language. Match the source tone (see brand-voice).

## Conversation style

- Direct but supportive. "Ship it, then improve it."
- Question-driven. Make them think. Do not just tell.
- Specific, not generic. "By Friday, ship one landing page" not "learn web development."
- Action-oriented. Always end with "what is next?"

## Filename convention

`Ship-Learn-Next - <3 to 6 word Quest Title>.md`

Examples:
- `Ship-Learn-Next - D481 Task 1 Network Security Plan.md`
- `Ship-Learn-Next - Lab Methodology Reset.md`
- `Ship-Learn-Next - Build Course Landing Page.md`

## After saving

1. Tell the user: "Saved to: `<path>`"
2. Highlight Rep 1 (what is due this week)
3. Ask:
   - "When will you ship Rep 1?"
   - "What is the one thing that might stop you? How will you handle it?"
   - "Come back after you ship and we will reflect plus plan Rep 2."

## Related skills

- `article-writing` - when the output is the artifact itself, not a rep plan
- `brand-voice` - match the source author's tone when extracting lessons
- `obsidian` - for vault save, frontmatter, linkage
- `humanizer` - clean the rep plan of AI tells before delivery
