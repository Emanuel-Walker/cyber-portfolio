# Obsidian Second Brain

### For ADHD minds, security people, and busy builders who want AI as a thought partner without giving up privacy.

If your head is a browser with 94 open tabs, this repo is for you. It is a working template for an Obsidian vault that an AI coding agent helps you maintain. Local files, markdown everywhere, no SaaS lock-in, no analytics. You own every byte. The agent cleans up after you so your brain can go back to the real work.

This is not another "productivity system." It is the scaffolding behind a daily habit that scales from one messy note to a graph with thousands of linked ideas.

---

## Who this is for

- **ADHD professionals who need an external brain.** You capture everything, you forget half of it, and you blame yourself for the gap. The vault captures without judgment. The agent sorts without judgment. You get your attention back for the stuff that actually matters.
- **Security engineers who want local-first, auditable notes.** Nothing leaves your machine unless you decide. Every note is plain markdown you can `grep`, diff, encrypt, and version. If a tool breaks, your notes outlive it.
- **Builders who want AI as a thought partner.** You want a reasoning partner that reads your past work, keeps you honest about your commitments, and never pushes a vendor agenda. You want it running against files you control.

---

## What's in this repo

| File or folder | What you get |
|---|---|
| `README.md` | This page. The pitch and the quick start. |
| `STRUCTURE.md` | The folder layout. PARA plus a few additions that earn their keep. |
| `ADHD-GUIDE.md` | How to run the system when your focus is not on your side. |
| `agent-setup/` | Templates for Claude Code, Codex, and any skill-aware agent, plus install steps. |
| `workflows/` | Six concrete workflows: brain dump cleanup, daily notes, document conversion, retrospective review, callouts, skills and MCP. |
| `security/` | Local-first argument, encryption at rest, encrypted sync options, PII rules, legacy folder for your family. |
| `templates/` | Drop-in Obsidian templates for daily notes, weekly reviews, projects, people, meetings, brain dumps, book notes, idea incubator. |
| `examples/` | Four worked examples including a knowledge graph tour and a fitness tracking recipe. |

---

## Why Obsidian

Every few months a new note app ships, promises to "think with you," and then quietly starts training on your writing. Obsidian is different for a few boring reasons that matter:

1. **Your notes are plain `.md` files on your disk.** No proprietary format. No lock-in. You can open them in any text editor, pipe them into any script, and read them in 20 years.
2. **The feature surface is small and composable.** Core app, plus community plugins you choose, plus an agent you choose. No feature nobody asked for.
3. **It is agent-friendly by default.** Markdown is the native language of modern AI coding tools. An agent can read a vault, find patterns, write new files, and respect the structure. No API wrapper, no API cost.
4. **The graph is a receipt.** Every `[[wikilink]]` adds an edge. After a few months the graph becomes a visible record that you have been thinking. See `images/vault-graph-example.png`.

The current wave of discourse around AI coding agents working inside knowledge bases is pointing in one direction: markdown files on disk, an agent that respects the structure, and a human who stays in charge. This repo is one opinionated way to set that up.

---

## The core idea in three sentences

1. **A second brain** is where you store everything you want to remember without carrying it in your head.
2. **A thought partner** is an agent that reads what you have stored, surfaces patterns, and helps you make the next move.
3. **Agent-maintained** means the boring work of cleaning, linking, and routing happens while you sleep, so the vault stays usable the day you need it most.

---

## Quick start

Five commands to go from zero to a working vault with an agent plugged in.

```bash
# 1. Clone this template
git clone https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain.git my-vault
cd my-vault

# 2. Open the folder in Obsidian (File > Open vault > this folder)
#    Enable community plugins. Install Templater and Dataview to start.

# 3. Install Claude Code (or your preferred agent CLI)
npm install -g @anthropic-ai/claude-code

# 4. Copy the agent instructions template into place
cp agent-setup/CLAUDE.md.template CLAUDE.md
# Then edit CLAUDE.md and fill in the <YOUR_NAME>, <YOUR_VAULT_ROOT>, etc.

# 5. Launch the agent from the vault root
claude
```

That is the whole floor. From there you open `templates/daily-note.md`, make your first entry, and start capturing. Everything else is iteration.

---

## The hero screenshot

![A vault graph after six months of daily use](images/vault-graph-example.png)

_This is what a vault looks like after six months of daily use with an agent helping maintain it. Every dot is a note. Every line is a link. Dense clusters are the topics you actually think about. The empty areas are the ones you talk about caring about but never write down. The graph does not lie._

---

## What this template refuses to do

- It will not sync your notes to a server you do not control.
- It will not nag you with streaks and gamification. ADHD brains know what streak shame does.
- It will not pretend you need every plugin, every template, every skill on day one.
- It will not touch your Inbox folder without your permission. The Inbox is the brain dump zone. Nothing there is cleaned up unless you say so.

---

## Reasonable next steps

1. Read `STRUCTURE.md` and skim the folder names.
2. Read `ADHD-GUIDE.md` if that is relevant to you. If it is not, skip it.
3. Open `agent-setup/INSTALL.md` and get Claude Code or your agent of choice talking to the vault.
4. Pick one workflow in `workflows/` and run it this week. Just one.
5. In 30 days, open the graph view and look at what you built.

---

## Contributing

Fork it. Adapt it. If you find a workflow that improves the base template, open a PR. Keep the voice tight and the examples generic. No one else's personal content belongs in this repo.

---

<!-- obsidian-second-brain by Emanuel Walker - github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->

_Template by Emanuel Walker. [github.com/Emanuel-Walker](https://github.com/Emanuel-Walker) | [emanuelwalker.com](https://emanuelwalker.com)_

_Fork it. Adapt it. If it changes your life, buy my book Unshaken or send a note._
