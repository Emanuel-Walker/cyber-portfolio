# Workflow 01 - Brain Dump Cleanup

**When to run it:** your Inbox has 20+ files and you cannot tell what is in there anymore. Or weekly, as part of your review.

**What it does:** the agent reads your Inbox, proposes a destination for each file, and waits for you to approve before anything moves.

---

## The step-by-step

### 1. Open the agent in the vault root.

```bash
cd my-vault
claude
```

### 2. Give it this prompt.

```
Read every file in 00-Inbox/. For each one, do the following:
1. Summarize the content in one line.
2. Propose a destination folder and filename.
3. Suggest 2-5 wikilinks it should get.
4. Flag any file you cannot categorize with confidence.

Output a markdown table. Do not move anything yet.
```

### 3. Review the table.

You will get something like this:

| File | Summary | Proposed destination | Links | Confidence |
|---|---|---|---|---|
| `random thought on queues.md` | Note on backpressure in message queues | `05-Resources/Systems/Backpressure.md` | `[[Queue Theory]]`, `[[System Design]]` | High |
| `jamie coffee.md` | Notes from coffee with Jamie about career move | `02-People/Jamie_Rivera.md` (append) | `[[Career_MOC]]` | High |
| `idk check later.md` | Half-sentence, "maybe home lab vlan"  | leave in Inbox | n/a | Low |

### 4. Approve a subset.

Reply with: "Approve rows 1 and 2. Leave row 3." The agent moves the approved files and tells you what it did.

### 5. Repeat weekly.

Fifteen minutes a week keeps the Inbox from becoming an archaeological dig.

---

## Example input and output

**Input (`00-Inbox/2026-10-01-queue-note.md`):**

```
backpressure. producers faster than consumers = problem. 
tcp sliding window is the clean analogy. 
RabbitMQ has publisher confirms. kafka has consumer lag.
revisit for the queue reliability piece
```

**Agent output after approval:**

File moved to `05-Resources/Systems/Backpressure.md`. New frontmatter added:

```markdown
---
tags:
  - status/draft
  - topic/systems
  - topic/queues
created: 2026-10-01
---

# Backpressure

Producers faster than consumers equals a problem. The TCP sliding window is the clean analogy.

- RabbitMQ handles this with publisher confirms.
- Kafka surfaces it as consumer lag.

Revisit for the queue reliability piece. Related: [[Queue Theory]], [[System Design]].
```

Same content. Cleaner. Linked. Tagged. Searchable.

---

## Rules the agent respects

- It does not move anything without your approval on each batch.
- It does not rewrite the body of your note. It cleans whitespace, adds frontmatter, and adds links. Your words stay yours.
- If a note is genuinely unparseable, it stays in the Inbox for next week.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
