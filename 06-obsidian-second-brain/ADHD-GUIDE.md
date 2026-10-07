# ADHD-friendly guide to running the vault

## The rule

The system should be easy to **restart**.

You will miss days.

You will forget where a note belongs.

You will get interested in rebuilding the system instead of using it.

That is normal for any system that depends on attention and routine.

This vault is designed to recover without a cleanup project.

## Minimum viable use

On a rough day, do only this:

1. open `00-Inbox/`
2. write the thought
3. close the app

That counts.

You do not need to:
- tag it
- link it
- move it
- format it
- summarize it

Capture first.

Organize later.

## The 10-second capture rule

If a thought takes longer than about 10 seconds to save, your capture workflow has too much friction.

A valid note can be:

```text
Ask Sam about the AWS budget alert.
```

That is enough.

## One next action

Do not ask the vault:

> What should I do with my whole life?

Ask:

```text
Read my current project note.

What is the next concrete action I can finish in 20 minutes?

Give me one answer.
```

One next action is easier to use than a perfect priority matrix.

## The restart protocol

If you disappear for a day, week, or month:

1. open the vault
2. do not reorganize anything
3. open `02-CURRENT-SEASON.md` if you use it
4. open your projects index
5. update one next action
6. continue

Do not backfill every missed day unless the missing history actually matters.

## Inbox cleanup

When the Inbox becomes noisy, ask the agent:

```text
Read 00-Inbox.

Group the notes by likely destination.

Show me the proposed moves first.

Do not move or delete anything until I approve.
```

The approval step matters.

You should never wonder where the agent moved something.

## Keep daily notes small

If you use a daily note, start with four prompts:

```markdown
## Today
- One thing that matters:
- One thing I can ignore:
- Open loop I do not want to forget:
- Note for future me:
```

That is enough.

Add fields only when you repeatedly need them.

## Hyperfocus guardrail

When you notice one project eating the whole day, write:

```markdown
## Focus check
What am I working on?
What was I supposed to be working on?
Is this still worth the next hour?
```

No score is required.

The purpose is interruption, not judgment.

## Do not gamify the vault

Avoid:
- streaks
- badges
- missed-day warnings
- giant dashboards of personal scores

A broken streak can turn a useful tool into another thing you feel behind on.

The vault should still work after a gap.

## Let the agent do boring maintenance

Good jobs to delegate:
- summarize yesterday
- build a weekly review
- find unlinked project mentions
- propose Inbox moves
- format a messy note
- update a project index after you approve changes

Do not delegate judgment just because organization is tedious.

## Read-aloud rule

If an instruction takes two reads, simplify it.

Good:

```text
Open 03-Projects.

Pick one active project.

Write the next action.
```

Bad:

```text
Review your active project ecosystem, identify dependencies, assess priority alignment, and synthesize the optimal next-step sequence.
```

The vault is supposed to reduce cognitive load.

Its instructions should sound like a person talking.

## Weekly reset

Once a week, five minutes:

```text
1. What is still active?
2. What can I archive?
3. What is the next action for each real project?
4. What am I pretending is still a priority?
```

Then stop.

Do not redesign the folder structure during the weekly reset.

## Definition of success

Ask one question:

**Did this system help me remember something or make a better next decision this week?**

If yes, keep it.

If no, remove one source of friction.

Do not add three new plugins.
