# Companion agents and the vault as memory

## Plain English

A companion agent is an assistant that is useful across many sessions because it can work from persistent context.

The important part is not the personality.

It is the memory design.

A good setup lets you answer:

- What does the agent know about me?
- Where is that information stored?
- Can I correct it?
- Can I delete it?
- Which files may it read?
- Which files may it change?
- What happens if I switch models?

This project uses an Obsidian vault as the human-owned memory layer.

## The four kinds of context

Do not dump the entire vault into every conversation.

Separate context by job.

### 1. Stable profile

Changes slowly.

Examples:
- role
- working preferences
- communication preferences
- long-term goals
- permanent boundaries

A simple file:

```text
00-ABOUT-ME.md
```

### 2. Current season

Changes every few weeks or months.

Examples:
- current priorities
- active constraints
- what you are intentionally ignoring
- upcoming deadlines

A simple file:

```text
01-CURRENT-SEASON.md
```

### 3. Active work

Changes often.

Examples:
- projects
- next actions
- blockers
- open questions

Keep an index:

```text
03-Projects/_index.md
```

### 4. History

Past notes, meetings, reflections, and session logs.

History is useful when the agent needs evidence.

It should not automatically become the prompt for every task.

## Minimal companion folder

You can build a useful pattern with this:

```text
00-ABOUT-ME.md
01-RULES.md
02-CURRENT-SEASON.md

03-People/
04-Projects/
  _index.md

99-Log/
```

That is enough.

You do not need a vector database on day one.

## What each file does

### ABOUT-ME

One page.

Write facts and preferences you expect to remain useful.

Do not turn it into an autobiography.

### RULES

Three to ten rules.

Examples:

```text
- Never invent missing facts.
- Ask before deleting or moving files.
- Do not read Legacy/.
- Keep operational notes concise.
```

### CURRENT-SEASON

What matters now.

A good version answers:

```text
What am I focused on?
What am I not focused on?
What deadlines are real?
What is the next decision I need to make?
```

Update it when priorities change.

### PROJECTS INDEX

One line per active project.

Example:

```markdown
| Project | Status | Next action |
|---|---|---|
| Portfolio cleanup | Active | Validate every quickstart |
| AWS lab | Stable | Record walkthrough |
```

This is more useful to a planning agent than 200 pages of history.

### PEOPLE

Use this only when recurring people matter to the workflow.

Do not build dossiers.

Keep relevant context:
- relationship or role
- open thread
- last important interaction

## Three companion patterns

### Chief-of-staff pattern

Best for:
- active projects
- planning
- meeting prep
- follow-up

Reads:
- current season
- projects index
- relevant people/project notes

Avoid giving it the whole journal by default.

### Study-partner pattern

Best for:
- learning
- certifications
- research
- spaced review

Reads:
- study notes
- questions
- prior mistakes
- learning goals

The agent should cite the notes it used.

### Journal/reflection pattern

Best for:
- reviewing dated notes
- identifying repeated themes
- preparing weekly or monthly reflections

This pattern needs stronger privacy boundaries.

Reflection is not diagnosis.

An agent noticing a pattern does not make the pattern true.

## Memory vs session log

These are different.

### Memory

Facts or context worth using again.

### Session log

What the agent did during one work session.

Example:

```text
Files changed
Open threads
Next action
```

Do not automatically promote every session detail into permanent memory.

## Write permissions

Start narrow.

| Area | Suggested default |
|---|---|
| About me | read only |
| Rules | read only |
| Current season | ask before overwrite |
| Projects | read/write |
| Daily notes | append or ask |
| Archive | read only |
| Legacy/private | no access |

The exact policy is yours.

The point is to make it explicit.

## What makes this portable

The memory is Markdown.

The agent charter is Markdown.

If you switch from one compatible coding agent to another, you can reuse the same source material and rewrite only the small adapter/rules file.

Your history does not need to live inside one chat product.

## Privacy rule

Do not store secrets in the vault just because it is local.

Keep these in a password manager or purpose-built secure store:
- passwords
- API keys
- private keys
- financial account credentials
- government identifiers

If a cloud agent can read a file, assume that file may be sent to the provider during the task.

## First useful test

Do not try to build a digital best friend.

Try this:

1. create `00-ABOUT-ME.md`
2. create `01-RULES.md`
3. create `02-CURRENT-SEASON.md`
4. create `04-Projects/_index.md`
5. launch your agent in the vault
6. ask:

```text
Based only on my current-season file and project index, what are my three active priorities?

Cite the files you used.
```

**PASS:** the answer comes from the files, not invented context.

Then ask:

```text
What do you not know that would change your recommendation?
```

A good companion should know its gaps.
