# ADHD Guide to Running This Vault

This is the honest guide. If you have ADHD, you have probably tried a dozen systems. They worked for 11 days then collapsed under the weight of their own rules. This one is designed to collapse gracefully and rebuild in five minutes.

Nothing here is medical advice. If you need medical help, go get it. This is just a working method for keeping an external brain alive when your internal one is not cooperating.

---

## Why ADHD brains need external systems

Working memory is where ideas live while you are using them. ADHD brains have less working memory on tap than neurotypical brains, and the tap is easier to turn off by stress, mood, or a loud noise. That is not a character flaw. It is a hardware spec.

An external brain gives you three things your head cannot reliably provide:

1. **Persistence.** The idea you had at 11pm is still there at 9am.
2. **Non-judgmental storage.** The file does not care how messy you were when you wrote it.
3. **Pattern surfacing.** With an agent reading your notes, patterns show up that you would never catch by rereading.

---

## The hyperfixation meter

Hyperfixation is one of the superpowers of an ADHD brain. It is also the reason you forget to eat. The meter is a one-line practice at the end of each day:

```
## Hyperfixation Meter
**Primary fix today:** rebuilding the home lab network
**Strength:** 8/10
Notes: Lost 4 hours to tuning pfSense rules. Shipped a working VLAN. Did not eat lunch.
Was this productive or displacement? Productive, but at the cost of the actual priority
(the quarterly review). Tomorrow, 90 min cap on lab work before 2pm.
```

A number plus a sentence. That is all. The point is not to beat yourself up. The point is to give the agent a time series it can review with you later. After 30 days you can ask the agent: "What did I hyperfixate on this month? Where was it productive and where was it displacement?" You will be surprised.

---

## Brain dump culture

No shame in capture. The `00-Inbox/` folder exists so you can dump a thought in under 10 seconds and get back to what you were doing. The rules:

- One thought per file is fine. Ten thoughts in one file is also fine.
- Grammar does not matter. Spelling does not matter.
- Date stamps help. Topics help. Neither is required.
- The agent will not touch the Inbox unless you ask. There is no silent cleanup that mysteriously loses something.

When the Inbox gets too full, run the brain dump cleanup workflow in `workflows/01-brain-dump-cleanup.md`. The agent reads each file, suggests where it should go, and waits for your approval before moving anything.

---

## The agent as a non-judgmental processor

A well-configured agent will never say "you should have organized this better." It will never shame you for a messy note. It will not ask why you did not finish the project you started six weeks ago.

What it will do:

- Summarize what you wrote.
- Suggest links to related notes.
- Flag patterns across weeks.
- Backfill the structured parts of a note when you only wrote the messy parts.
- Ask one clarifying question when it genuinely cannot tell what you meant.

The CLAUDE.md template in `agent-setup/` includes the voice rules that keep the agent from drifting into therapist cosplay or productivity-coach lecturing.

---

## Daily check-in system

A short morning check-in and a longer evening close is the rhythm that holds everything together.

**Morning (90 seconds)**
```
## Today
- Mood (1-10):
- Sleep (hours):
- One thing I will not drop today:
- One thing I will say no to:
```

**Evening (3-5 minutes)**
```
## Evening Close
- What I actually did:
- What I did not do that I thought I would:
- What is still open:
- Hyperfixation meter: X/10 - what was it
- One line for future me:
```

The agent can parse these fields and build a weekly or monthly rollup for you. No manual tracking required.

---

## Retroactive forgiveness workflow

Missed three days? A week? A month? Fine. You are allowed to come back.

Instead of trying to reconstruct the lost days by memory, use the retroactive workflow:

1. Open the agent in the vault.
2. Say: "I missed the last X days. Help me backfill from texts, calendar events, and git commits."
3. Point it at whatever source you have access to. For most people this is a calendar export, a text message search, and the git log of their work projects.
4. The agent drafts a short daily note for each missed day. You review and keep what rings true.

This is not journaling. This is making sure the time series stays usable. If a trend starts to show in your health or focus, the gap days do not break the signal.

---

## Hard rule: do not gamify the vault

Streaks, badges, and dopamine hits are a trap for ADHD brains. The first time you break a streak, the whole system starts to feel like a failure and you abandon it.

The vault is a tool. Tools do not keep score. If you miss a week, the vault is still there. The graph still works. The agent still reads what you have. Walk back in and keep going.

The only metric that matters is: did the external brain help you make a better decision this week? If yes, keep going. If no, change one thing and try again.

---

## Three gentle recommendations

1. **Keep the daily note template short.** Five fields max. If it takes more than 90 seconds to fill, you will stop filling it.
2. **Let the agent write the boring parts.** Weekly reviews, monthly rollups, meeting summaries. These are mental tax. Offload them.
3. **Reread one random daily note from six months ago, once a month.** You will catch patterns about yourself the agent cannot catch.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
