# Companion Agents and the Vault as Memory

The category is here. Personal AI agents are shifting from "answer my question" tools to "know me over time" partners. The whole conversation has moved from how clever the model is to how much it remembers about you between sessions. The next question is the one most people are not asking yet: what does your companion remember, what does it forget, and who else can see what it kept? An Obsidian vault is the memory layer that puts that answer back in your hands.

---

## Who this is for

- **Busy professionals** who already have an AI assistant open all day and want it to stop asking the same context questions every morning.
- **Security people** who do not love the idea of a vendor silently building a profile of them and want a canonical, inspectable, local source of truth instead.
- **ADHD builders** whose working memory leaks and who want the agent to carry the recall load without carrying it to a server they do not control.
- **Anyone** who wants their AI to actually know them, in the way a long-time coworker does, without turning their inner life into training data.

If none of those are you, the ADHD guide and workflows in this repo are probably a better place to start.

---

## What a companion agent is

A companion agent is any AI tool designed for persistent, personal context rather than one-off tasks. The common pattern looks like this: a chat interface in front, a memory store in the back, and some policy layer that decides what to keep from each conversation and what to surface in the next one. Memory is no longer a feature to call out in a changelog. In 2026 it is baseline. The question is whose memory, stored where, under what retention rules.

An Obsidian vault flips the default. Instead of letting the agent build a hidden profile of you inside its own system, you hand it a readable set of files and say: this is who I am, these are my rules, this is what I am working on. If you change your mind, you edit a file. If you want to end the relationship, you stop sharing the folder. Portable, inspectable, revocable.

---

## Profile 1: Grok

**What it is.** Grok is xAI's assistant. In 2026 it added persistent cross-session memory, where it quietly stores facts it judges worth keeping from each conversation and applies them in later ones. It also ran a Companions feature with animated 3D characters and voice, which xAI announced it would retire from the main Grok app in late 2026 (the characters moved to a separate Animates app). Treat the Companion persona layer as a moving target. Treat the memory layer as the real feature.

**What it reads from a vault well.** Short, blunt, factual files. Grok's memory is selective rather than total, so a tight "about me" document and a current-season file give the agent a clean place to anchor. Bullet lists with concrete facts (role, stack, preferences, hard rules) land well.

**What it reads from a vault poorly.** Long introspective journal entries without clear takeaways. Grok will not reliably mine a 2,000-word reflection for the one line that matters. If a thought is important, state it as a rule or a one-line fact somewhere the agent can find it.

**Vault folder structure that works best.**

```
grok-vault/
  00-ABOUT-ME.md
  01-RULES.md
  02-CURRENT-SEASON.md
  03-PEOPLE/
  04-PROJECTS/
    _index.md
  99-LOG/
    2026-10-03.md
```

Keep the top-level narrow. Grok benefits from short, high-signal files it can scan into context.

**Example starter files to seed it.**

- A one-paragraph "about me" that reads like a bio.
- A rules file: three to seven lines that say what the agent should never do.
- A current-season file: the three things that matter this quarter.

**Honest limits.** The Companion persona layer has changed twice in a year, so do not build long-term workflows that assume a specific character or voice. The memory feature is useful but opaque. You cannot fully audit what Grok decided to keep from a given conversation.

---

## Profile 2: Muse

**What it is.** Muse here is a category, not a product. The pattern is a self-built or lightly configured "chief of staff" agent that handles planning, triage, and recall for one person. Think of it as the arrangement people set up when they wire a general model (Claude, GPT, a local model) to a vault and a few tools, give it a name, and treat it like a daily operator. If you have your own Muse-like setup, this profile is written for that pattern rather than any specific vendor.

**What it reads from a vault well.** Structured, project-aware files. A chief-of-staff pattern thrives on an index of active work, a people file so it recognizes names in your inbox, and a weekly rhythm it can read and respect. It likes checklists, status fields, and dates. The more PARA-like the structure, the better.

**What it reads from a vault poorly.** Pure stream-of-consciousness capture with no routing. If every thought lives in the inbox and never gets filed, the agent spends its context budget rereading the same noise.

**Vault folder structure that works best.**

```
muse-vault/
  00-ABOUT-ME.md
  01-RULES.md
  02-CURRENT-SEASON.md
  03-PEOPLE/
    jamie-chen.md
  04-PROJECTS/
    _index.md
    cloud-security-cert.md
  05-MEETINGS/
  99-LOG/
    2026-10-03.md
```

A chief-of-staff pattern wants an index. Give it one.

**Example starter files to seed it.**

- An "about me" that includes role, working hours, and energy patterns.
- A projects index with one line per active project (status, next action).
- A people file so the agent knows who "Jamie" is when a message comes in.
- A rules file that says what the agent is allowed to decide on its own and what it must bring to you.

**Honest limits.** A self-built chief of staff is only as good as the files you feed it. If you stop updating the current-season file, the agent starts planning against stale priorities. The pattern requires a weekly five-minute refresh. Skip that and it drifts.

---

## Profile 3: Dot (and journal-pattern agents)

**What it is.** Dot was a personal AI by New Computer, pitched as a reflective companion with long-term memory, aimed at young adults using the agent like a living journal. New Computer announced its wind-down in 2025, so Dot itself is no longer the live product. The pattern it represented is very much alive: journal-first agents that build a rolling model of you out of daily reflections and voice notes. Open Dot (an open-source take) and several newer apps follow the same shape.

**What it reads from a vault well.** Dated daily entries. Short reflections with clear emotional or situational markers. A standing "about me" document that frames who the person is for the agent.

**What it reads from a vault poorly.** Pure task lists. A journal-pattern agent is not trying to run your calendar. If you load it with tickets and sprints, it will try to be helpful and miss the point. Keep operational work in a separate index and let the journal space stay reflective.

**Vault folder structure that works best.**

```
dot-vault/
  00-ABOUT-ME.md
  01-RULES.md
  02-CURRENT-SEASON.md
  03-PEOPLE/
    jamie-chen.md
  04-PROJECTS/
    _index.md
  99-LOG/
    2026-10-01.md
    2026-10-02.md
    2026-10-03.md
```

The daily log folder is the center of gravity. One file per day. Keep the rest light.

**Example starter files to seed it.**

- An "about me" that reads more like a self-introduction than a resume.
- A short list of recurring people and relationships.
- A daily entry template with three or four honest prompts.

**Honest limits.** Journal-pattern agents are reflective, not predictive. They do not plan your week. They also depend on consistency. Three entries then a two-month gap means the agent is reflecting on a frozen version of you. If you cannot keep a daily cadence, do not expect a journal-pattern agent to feel smart.

---

## Shared infrastructure (what any companion benefits from)

Different agents, same five files. If you only build five files, build these.

### 1. A canonical "about me" file

One page, written in your own voice, that answers: who I am, what I do, how I like to work, what I care about, what I am avoiding. The agent reads this first every session. Update it quarterly.

### 2. An inviolable rules file

Short. Three to seven lines. Things like: never summarize me in a condescending tone, always ask before changing a file in the projects folder, never recommend anything that costs money without flagging it. The rules file is the fence line.

### 3. A running journal

A dated folder with one file per day. Freeform is fine. The point is to give the agent a time series. Three months of daily notes beat one perfect weekly review every time.

### 4. A projects index

One file. One line per active project. Status, owner, next action, deadline if relevant. This is the file a chief-of-staff pattern reads to answer "what should I be working on today."

### 5. A people index

A folder with one file per recurring person in your life. First name, how you know them, last meaningful interaction, anything you want to remember. The agent uses this to turn a mention into context.

Everything else in this template is optional. These five are the floor.

---

## Security and disclaimers

### Security

You are feeding your personal context to a company. Read the privacy policy. Really. The sentence that matters is usually the one about training data and the one about retention after account deletion. If you cannot find either, assume the worst.

**Local models keep data on your machine. Cloud agents do not.** Tools like Ollama and LM Studio run models on your own hardware with your own disk. Cloud agents (Grok, hosted assistants, journal apps that sync) move your text to a server you do not control. Decide which parts of your life you are willing to share with a vendor and which parts you are not. For most people the answer is "share the professional stuff, keep the inner life local."

**Minimum PII rules.** Never put the following in any file an agent can read:

- Social security number
- Bank account or card numbers
- API keys, passwords, or private keys
- Medical record numbers
- Government ID numbers

If any of these need to live somewhere, use a password manager, not a vault file. See [security/04-pii-rules.md](security/04-pii-rules.md) for the full rules.

**Encrypted vaults.** If you share a device, or if your vault lives on a laptop that leaves the house, encrypt it. See [security/02-password-protect.md](security/02-password-protect.md) for an at-rest approach and [security/03-encrypted-remote-sync.md](security/03-encrypted-remote-sync.md) for sync patterns that do not hand your notes to a third party in cleartext.

**Delete and revoke.** Every agent should answer three questions clearly: how do I see what you have remembered about me, how do I delete a specific memory, and how do I wipe everything. If a tool cannot answer those in its settings, that is the answer. Walk away. For cloud tools that do offer a memory panel, visit it monthly. Delete anything you would not want screenshot.

**The thing no one warns you about.** Once you put a thought into a cloud agent whose training policy is unclear, you cannot pull it back. Even "delete my data" does not necessarily remove a reflection that already entered a model fine-tune or an eval set. Treat anything you say to a cloud agent the way you would treat a public post. If you would not say it in a group chat with coworkers, do not say it to a cloud companion. The companies will get better at this. They are not there yet.

### Disclaimers

- Not affiliated with xAI, New Computer, or any other named company.
- No endorsement of any product. This document describes a category.
- Terms of service change. A feature that exists today may not exist next quarter. The Grok Companions retirement in 2026 is a live example.
- This is not legal, security, or medical advice. Talk to a professional for your specific situation.
- Consider your jurisdiction. GDPR, CCPA, and various state biometric and health-privacy laws apply differently depending on where you live and what you journal about. If you reflect on health conditions, treat that content with the same care you would treat a medical record.

---

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template inside [cyber-portfolio](https://github.com/Emanuel-Walker/cyber-portfolio). Credit appreciated, not required._
