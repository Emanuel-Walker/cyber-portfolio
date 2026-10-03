# Workflow 8: Turn your vault notes into a NotebookLM knowledge source

Your vault is the raw material. NotebookLM is the mill. You feed it your markdown, and it hands you back audio overviews, video overviews, mind maps, study guides, and briefing docs grounded in your own thinking. The sources stay yours. The outputs are generated on top of them.

This workflow takes about 20 minutes end to end once your notes are ready.

> [!info] Plain English
> You pick notes from your vault. You upload them to NotebookLM. You press a button. You get a podcast about your own ideas, or a short video, or an infographic style mind map. All grounded in what you actually wrote, not what the model guessed.

> [!warning] As of 2026-10-03
> NotebookLM features change often. Google adds and removes outputs (audio overview, video overview, mind map, timeline, study guide, briefing doc, FAQ). Interface and prompts below reflect what was available as of this date. Adjust if the UI has moved.

---

## When to use NotebookLM instead of your vault agent

Your Claude Code or Codex agent is great for reading, writing, and routing inside the vault. NotebookLM is great for turning a cluster of notes into something you consume.

| You want | Use |
|---|---|
| An agent to clean up and organize your notes | Vault agent (Claude Code, Codex) |
| A 15-minute audio summary of your week to listen to on a walk | NotebookLM Audio Overview |
| A short video explainer of a project to send a stakeholder | NotebookLM Video Overview |
| A visual mind map of a research cluster | NotebookLM Mind Map |
| An exec briefing on a project you have been drafting | NotebookLM Briefing Doc |
| A study guide for a book or course you have been taking notes on | NotebookLM Study Guide |

Rule of thumb. Vault agent for input and curation. NotebookLM for output and comprehension.

---

## Step 1 - Pick the notes you want to feed in

NotebookLM accepts up to 50 sources per notebook. Markdown files work. PDFs work. URLs work. YouTube links work. Google Docs work.

Open your vault. Decide the scope.

- **Weekly review notebook** - all 7 daily notes from the past week.
- **Project notebook** - the project README, the WRITEUP, any research notes, any meeting notes tied to the project.
- **Book notebook** - the book notes file plus any reflection notes referencing it.
- **Career notebook** - your resume, portfolio README, any Gray Space style essays.
- **Second brain overview notebook** - your top-level MOC files plus the current season snapshot.

Keep each notebook focused. One cluster, one notebook. Mixing a weekly review with your book notes dilutes the outputs.

---

## Step 2 - Prep the markdown for upload

NotebookLM reads markdown files cleanly. One prep tip pays off.

Ask your vault agent to concatenate your chosen notes into one single markdown file per notebook topic.

Paste this prompt into Claude Code or Codex pointed at your vault:

```
I want to feed a NotebookLM notebook with my notes on <TOPIC>. 

Please:
1. Find every note in my vault that is relevant to <TOPIC>. Include daily notes if they mention it.
2. Concatenate them into a single markdown file at `08-AI-History/notebooklm-exports/<TOPIC>-source.md`.
3. At the top, add a short section headed "## Context for the reader" that explains who I am in one paragraph and what this collection is about.
4. For each original note, use a H2 header with the note title and date. Preserve the original content verbatim below each header.
5. Strip any `#private` tagged notes entirely. Flag them in a sidebar list at the end so I can review.

When done, give me the file path to upload.
```

The one combined file is easier to manage inside NotebookLM than 20 separate ones. You can always add more sources later.

---

## Step 3 - Upload to NotebookLM

1. Open [notebooklm.google.com](https://notebooklm.google.com) and sign in with a Google account.
2. Click **New notebook** (or **New**, depending on UI).
3. Give it a name that matches the topic. Example: "Weekly Review 2026-10-03" or "AWS IR Lab Research."
4. Click **Add source**.
5. Upload the markdown file you just generated. If you want to add related YouTube videos, articles, or PDFs, add them now.
6. Wait a few seconds. NotebookLM reads and indexes the sources.

You should see your source appear in the left panel. The main area shows a chat interface and a studio section with output options.

---

## Step 4 - Generate the outputs

The studio panel shows the available outputs. Click one. Each has a customization option.

### Audio Overview (the podcast)

Two AI hosts have a 10-30 minute conversation about your sources. This is the signature feature.

Click **Audio Overview** then **Customize** before generating.

Paste one of these into the customization box:

**For a weekly review listen on a walk:**
```
Focus on patterns across my daily notes this week. What did I actually ship, what did I avoid, what questions kept coming up. 
Tone: honest friend over coffee, not corporate recap. 
Length: 12-15 minutes. 
Audience: me, reflecting while walking.
Call out any contradictions between what I said I would do and what I actually did.
```

**For a project explainer:**
```
Explain this project to a smart senior leader who has 15 minutes. 
Lead with the problem. Then the approach. Then the honest limits. 
Tone: operator talking to another operator, not marketing.
Length: 12 minutes.
Audience: a hiring manager or a technical executive who is deciding whether this person understands their craft.
End with the one question I should be asked next.
```

**For a book or research summary:**
```
Walk me through the big ideas, the surprising claims, and the places where my own notes argue with the source. 
Tone: curious teacher.
Length: 20 minutes.
Audience: me revisiting this in 6 months.
Flag anything I highlighted but never acted on.
```

**For a career portfolio recap:**
```
This is a cyber and AI portfolio from an early-career builder. 
Give a listener a mental map of what this person builds, how they write, and what they would be strong at hiring for.
Tone: warm but direct.
Length: 15 minutes.
Audience: someone who just saw this portfolio linked on LinkedIn.
```

Click **Generate**. Takes a few minutes. Download the MP3 when ready. Drop it into your vault at `07-Attachments/audio/` and link it from the relevant note.

### Video Overview

A short narrated slideshow version of the audio. Same customization approach. Shorter output. Great for sharing with a stakeholder who will not sit through a 15-minute podcast.

Customization prompts:

**For a stakeholder update:**
```
I need a 3-5 minute visual explainer of this project for a non-technical sponsor. 
Lead with why this matters in business terms. 
Show the before and after.
End with what I need from them next.
Tone: confident but humble.
```

**For a conference lightning talk prep:**
```
Treat this as the script for a 5-minute lightning talk. 
One idea per slide. Big claims up front, evidence second.
Audience: a room of peers who already know the basics.
End with a provocation that invites questions.
```

### Mind Map

Visual map of concepts and connections across all sources. No prompt needed. Click **Mind Map**. Export as image. Drop it into your vault at `07-Attachments/images/` and embed it in your project note.

### Briefing Doc

A tight executive-style summary with sources cited. Great for sharing a project status without writing it yourself.

Customization prompt:
```
Write this as a one-page briefing doc for an executive sponsor.
Section 1: Current state in two paragraphs.
Section 2: What changed since the last update.
Section 3: Open decisions needing input.
Section 4: Next milestone and date.
No corporate language. No hype. Facts and asks.
```

### Study Guide

Structured breakdown. Good for turning a book, course, or dense research cluster into something you can review in sections.

Customization prompt:
```
Create a study guide organized by concept, not by source.
For each concept: definition, why it matters, worked example from the sources, and 2 questions I should be able to answer.
Target reader: me reviewing this in a month to prep for a project or interview.
```

### FAQ

Generates likely questions and answers from the sources. Useful before a meeting where you expect pushback.

Customization prompt:
```
Generate the 10 hardest questions a skeptical reviewer would ask about this work.
For each, give the honest answer from the sources, including any gaps or weak spots.
Tone: direct. No defensive language.
```

### Timeline

Pulls dates and events from your sources into a visual chronology. Great for review of multi-month projects or life phases.

No prompt needed, but you can refine with a follow-up chat: "Collapse all events older than 60 days into a single pre-era block."

---

## Step 5 - Chat with your sources

Below the studio is a chat panel. Ask questions. NotebookLM answers using only your sources and cites which source each claim came from.

Good questions to ask:

```
What is the most important idea across all of these notes that I have not acted on yet?
```

```
Where do my notes contradict themselves? Point to specific files.
```

```
If I had to delete half of these sources, which half would preserve the most insight? Why?
```

```
What are the top 3 recurring themes? Which notes are the strongest evidence for each?
```

```
Which of my open questions in these notes has already been answered elsewhere in the same set and I missed it?
```

Each answer cites the source. You can click a citation to jump to the exact passage.

---

## Step 6 - Pull the outputs back into your vault

The point of this workflow is not to let NotebookLM own your knowledge. The point is to use it as a transformer, then bring the output home.

For each notebook you build:

1. Download the audio MP3 (if generated). Save to `07-Attachments/audio/<topic>-<date>.mp3`.
2. Export the mind map as PNG. Save to `07-Attachments/images/<topic>-mindmap-<date>.png`.
3. Copy the briefing doc, study guide, or FAQ as markdown. Save to a new note in `05-Resources/notebooklm/<topic>-briefing-<date>.md` or similar.
4. Create one summary note in your vault titled `<topic> NotebookLM Review <date>.md` that links to all the above and includes your own 3-5 bullets of "what I actually took from this."

Your vault stays the system of record. NotebookLM is the mill, not the warehouse.

---

## Privacy and limits to know

- NotebookLM processes your sources on Google's servers. Do not upload anything you would not send to a Google product.
- Free tier has daily caps on audio overviews and chat queries. Google One AI Premium raises those.
- Audio overviews work in English well. Other languages are improving but variable.
- Mind maps and video overviews are newer features. They may be missing or renamed depending on when you read this.
- Sources are not used to train Google models by default (as of 2026-10-03) but policies change. Read the current terms before uploading sensitive work.
- If a source gets removed from your notebook, the generated outputs still exist and still reference it. Clean up outputs you no longer want to keep.

---

## When NOT to use NotebookLM

- When your notes contain PII, financial detail, medical history, legal strategy, or client confidential content. Keep those in your encrypted local vault.
- When you need the output in real time. NotebookLM generation takes minutes.
- When your source is small enough that your vault agent could answer the question directly. Do not add a cloud round-trip for a question Claude Code can answer in 10 seconds.
- When you want long-term memory that persists across sessions. NotebookLM is per-notebook. Your vault is permanent.

---

## The one-notebook-per-project habit

The highest-leverage use of NotebookLM is one notebook per active project. You feed it:

- The project README
- The project WRITEUP
- Any meeting notes
- Any decision logs
- Any related research

Every two weeks, you generate a fresh briefing doc and a 10-minute audio recap. You listen on your commute. You walk back into the project with context already loaded.

This is the closest thing to a project pair you can have for free.

---

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template inside [cyber-portfolio](https://github.com/Emanuel-Walker/cyber-portfolio). Credit appreciated, not required._
