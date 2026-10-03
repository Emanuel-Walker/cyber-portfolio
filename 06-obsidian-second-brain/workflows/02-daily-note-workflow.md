# Workflow 02 - Daily Note Workflow

**When to run it:** every working day. Morning and evening.

**What it does:** gives the vault a time series it can analyze. Builds a habit without demanding too much.

---

## Morning (90 seconds)

Open or create `01-Daily-Notes/YYYY/MM-MonthName/YYYY-MM-DD.md` using the template at `templates/daily-note.md`.

Fill the top section only:

```markdown
## Today
- Mood (1-10): 6
- Sleep (hours): 7
- One thing I will not drop today: review the audit findings
- One thing I will say no to: starting a new side project
```

That is it. Close the file. Go to work.

---

## Through the day

Capture into `00-Inbox/` as thoughts land. One file per idea is fine. Ten thoughts in one file is also fine. The Inbox is for speed, not shape.

If something belongs in the daily note (a mood shift, a win, a problem), append it to the daily note under a `## Captures` heading. Timestamp with `## 14:32` or whatever is quick.

---

## Evening close (3-5 minutes)

Fill the rest of the daily note.

```markdown
## Evening Close
- What I actually did:
  - Shipped the audit draft
  - Two hours on the home lab network
- What I did not do:
  - The gym block I promised myself
- Still open:
  - Review the audit draft tomorrow
  - Call back the plumber

## Hyperfixation Meter
**Primary fix today:** home lab network
**Strength:** 7/10
Was it productive? Yes, but it ate the gym block. Tomorrow, cap it at 60 min.

## Agent Note - Session Close
Have the agent write this section. It summarizes files touched today, open threads,
and one honest line. See the daily-note template for the exact shape.
```

Save. Done.

---

## Weekly rollup (handled by the agent)

Every Sunday evening, ask the agent:

```
Read every daily note from this week. Build a weekly review in templates/weekly-review.md
shape. Save to 01-Daily-Notes/YYYY/MM-MonthName/WYY-WK-NN_review.md.
```

The agent surfaces patterns you will not catch on your own. Example: "You hit a 9/10 hyperfixation on home lab three times this week. The gym block was skipped on all three of those days. Flagging because you said last month you did not want to repeat that pattern."

---

## ADHD-friendly notes

- If you miss a day, write "missed" in the daily note and move on. No streak math.
- If you miss a week, run the retroactive review workflow in `workflows/04-retroactive-review.md`.
- The template is intentionally short. If you add fields, drop one. Five fields is the ceiling.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
