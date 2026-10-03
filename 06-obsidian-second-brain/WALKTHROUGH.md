# Walkthrough: From Zero to a Working Vault + AI Agent

Start here. This file is written for a total beginner. If you have never installed Obsidian, never used an AI coding tool, and never written a line of markdown, you are the target reader.

By the end you will have a working second brain on your laptop, an AI agent that reads it, and a daily habit that scales.

---

## BLUF

- You will install Obsidian (a free note app), pick an AI agent, and point the agent at your notes.
- You will copy a ready-made folder structure and a charter file (CLAUDE.md) that teaches the agent your rules.
- You will paste five starter prompts to prove the agent is working.
- At the end you will have a repeatable daily workflow and a path to import your past AI chats.

---

## Before you start

- **Time:** about 90 minutes end to end. 20 minutes for install, 20 for structure, 20 for the agent, 30 for the first real pass.
- **Cost:** $0 if you use the free tiers. If you want unlimited agent usage, budget $20 a month for Claude or ChatGPT.
- **Skill level:** zero. If you can download an app and copy a folder, you can finish this walkthrough.
- **What you need:** a laptop (macOS, Windows, or Linux), an internet connection for the install, and a free hour.

> [!info] Plain English
> A **vault** is a folder of plain text files on your computer. An **AI agent** is a program that reads and writes those files when you ask it to. That is the entire mental model. No cloud account required.

---

## Step 1 - Install Obsidian

Obsidian is a free app that opens a folder of markdown files and shows them like a wiki. It does not upload your notes anywhere.

### Download

Go to [obsidian.md](https://obsidian.md) and click the download button for your operating system.

### macOS

1. Open the downloaded `.dmg` file.
2. Drag the Obsidian icon into Applications.
3. Open Launchpad, click Obsidian. On first launch, macOS may ask if you trust the app. Click Open.

### Windows

1. Run the downloaded `.exe` installer.
2. Follow the prompts. Default install path is fine.
3. Obsidian opens automatically when install finishes. If not, find it in the Start menu.

### Linux

1. Download the AppImage or `.deb` for your distro.
2. For AppImage, `chmod +x Obsidian-*.AppImage` then run it.
3. For `.deb`, `sudo dpkg -i Obsidian-*.deb`.

### First launch and create your vault

1. Obsidian opens to a welcome screen.
2. Click **Create new vault**.
3. Name it something you will recognize. `my-brain` is fine. `second-brain-2026` is fine.
4. Pick a location you will remember. Your Documents folder is a safe default.
5. Click **Create**.

You now have an empty vault. The folder exists on your disk. You could open it in Finder, File Explorer, or a terminal and see an empty directory with one hidden `.obsidian/` folder inside. That hidden folder stores Obsidian settings. Leave it alone.

### Recommended first plugins

In Obsidian, open **Settings → Community plugins**. Click **Turn on community plugins**. Then install these four:

- **Templater** - lets the templates in this repo auto-fill dates and prompts.
- **Dataview** - lets you query your notes like a database.
- **Advanced Tables** - keeps markdown tables readable.
- **Natural Language Dates** - type `@today` and get the date.

That is enough. Do not install more until you miss something specific.

---

## Step 2 - Pick your AI agent

Three solid options. You only need one. Read all three paragraphs before you pick.

### Option A: Claude Code (recommended for first-timers)

Claude Code is a command-line tool from Anthropic. You run it inside your vault folder from a terminal. It reads a file called `CLAUDE.md` at the vault root and uses that as its rulebook.

- **How to install:** `npm install -g @anthropic-ai/claude-code` or `pipx install claude-code`.
- **How to pay:** needs an Anthropic API key (pay per use, cheap) or a paid Claude.ai plan ($20 a month, flat).
- **Why pick this:** the charter format in this repo was built for Claude Code first. Everything in the `agent-setup/CLAUDE.md.template` just works. The CLI is text-only but the output is clean and the agent handles multi-file work well.
- **Downside:** command-line only. If a terminal scares you, read Option C.

### Option B: Codex (OpenAI's agent)

Codex is OpenAI's coding agent. You can run it through ChatGPT Plus or through the API.

- **How to install:** available in ChatGPT Plus web interface or via the OpenAI API.
- **How to pay:** $20 a month for ChatGPT Plus, or pay-per-use with the API.
- **Why pick this:** if you already have ChatGPT Plus, no new account needed. The agent is capable and the ecosystem is familiar.
- **Downside:** uses `CODEX.md` or `AGENTS.md` instead of `CLAUDE.md`. We ship a template for both. Context handling with local files is less mature than Claude Code.

### Option C: Cursor (visual IDE, generous free tier)

Cursor is an editor that looks and feels like VS Code, with an AI chat built in. You open your vault folder in Cursor and talk to the agent in a sidebar.

- **How to install:** download from [cursor.com](https://cursor.com).
- **How to pay:** free tier is generous. Pro is $20 a month if you hit the free limit.
- **Why pick this:** visual UI, no terminal needed. If you have never used a command line, start here.
- **Downside:** Cursor is a full code editor. It can edit anything, which means you have to be more careful with the charter boundaries.

**Recommendation.** If you have used a terminal before, pick Claude Code. If you have never used a terminal, pick Cursor. If you already pay for ChatGPT Plus, Codex is reasonable. All three work with the templates in this repo.

The rest of this walkthrough uses Claude Code as the example. The steps map one-for-one to the others. Where they differ, there is a note.

---

## Step 3 - Set up the vault structure

You now have an empty Obsidian vault. Time to pour in the folder structure and the agent charter from this repo.

### Grab this repo

```bash
# Pick a convenient parent folder
cd ~/Documents

# Clone the portfolio
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git

# The template lives in 06-obsidian-second-brain
ls cyber-portfolio/06-obsidian-second-brain
```

Do not have git? Download the repo as a ZIP from the GitHub page and unzip it.

### Copy the structure into your vault

Open your vault folder. Create the folders below. On macOS and Linux you can run this in a terminal from your vault root. On Windows, use File Explorer or the PowerShell equivalent.

```bash
cd ~/Documents/my-brain   # or wherever your vault lives

mkdir -p 00-Inbox
mkdir -p 01-Daily-Notes
mkdir -p 02-People
mkdir -p 03-Projects
mkdir -p 04-Areas
mkdir -p 05-Resources
mkdir -p 06-Archive
mkdir -p 07-Attachments
mkdir -p 08-AI-History
mkdir -p 99-System
mkdir -p Legacy
```

> [!info] Plain English
> This is the **PARA structure** (Projects, Areas, Resources, Archive) with a few extras. The numbered folders force them to sort in a sensible order. See `STRUCTURE.md` for the full explanation.

### Copy the templates

```bash
# From the cloned repo, copy the ready-made templates
cp -r ~/Documents/cyber-portfolio/06-obsidian-second-brain/templates ~/Documents/my-brain/99-System/templates
```

On Windows PowerShell:

```powershell
Copy-Item -Recurse "$HOME\Documents\cyber-portfolio\06-obsidian-second-brain\templates" "$HOME\Documents\my-brain\99-System\templates"
```

### Put CLAUDE.md at the vault root

This is the most important file. The agent reads it on every session.

```bash
cp ~/Documents/cyber-portfolio/06-obsidian-second-brain/agent-setup/CLAUDE.md.template ~/Documents/my-brain/CLAUDE.md
```

Then open `CLAUDE.md` in Obsidian and fill in the `<ANGLE_BRACKET>` placeholders. One line each. Short beats clever.

> [!warning] Important
> `CLAUDE.md` has to sit at the vault root, not inside a subfolder. Claude Code only auto-loads it from the current working directory root.

For Codex users, use `CODEX.md.template` instead. For Cursor and other `AGENTS.md`-aware tools, use `AGENTS.md.template`.

---

## Step 4 - Point your agent at the vault

### Claude Code (recommended)

Open a terminal.

**macOS or Linux:**
```bash
cd ~/Documents/my-brain
claude
```

**Windows (PowerShell):**
```powershell
Set-Location "$HOME\Documents\my-brain"
claude
```

The first time you run `claude`, it will ask you to log in or paste an API key. Follow the prompts.

Once the agent is running, you should see a prompt. The agent has already read your `CLAUDE.md` because the file is at the current working directory root. That is the entire discovery mechanism. No config file, no path setting.

### Cursor

1. Open Cursor.
2. **File → Open Folder** and pick your vault folder.
3. Open the AI chat sidebar (keyboard shortcut varies, usually `Cmd/Ctrl + L`).
4. Cursor reads `AGENTS.md` from the folder you opened. If it does not, paste the contents of your `AGENTS.md` into the system prompt field in Cursor settings.

### Codex / ChatGPT agent

Launch the agent with your vault as the working directory. If you are using the web ChatGPT, drag your `CODEX.md` into the chat and tell the agent to use it as the charter for the session.

---

## Step 5 - First prompts (prove the agent is working)

Paste these five prompts one at a time. Each one is a check that the agent is reading your vault correctly.

### Prompt 1: Charter check

```
Summarize the voice rules you are operating under. Keep it to a bulleted list under 10 lines.
```

**What good looks like.** The agent lists the rules you put in `CLAUDE.md`. If it makes up rules you did not write, the charter is not loaded.

### Prompt 2: Folder boundary check

```
List the folders in this vault you are not allowed to write to without my explicit permission.
```

**What good looks like.** The agent names `Legacy/` and either `00-Inbox/` or `01-Daily-Notes/`, depending on which rules you kept. If it says "none," the boundary rules are not loaded.

### Prompt 3: Structure check

```
Read the vault root. List the top-level folders and give a one-line description of what each one is for based on STRUCTURE.md.
```

**What good looks like.** The agent returns the numbered folders in order with short descriptions. If the folders are missing, go back to Step 3.

### Prompt 4: Linking behavior check

```
If I mention a person named Jamie Rivera in a note and Jamie has no note yet, what do you do?
```

**What good looks like.** The agent says it would create a stub in `02-People/Jamie_Rivera.md` with a draft tag, link to it from the current note, and flag it for review. If it says it would just add the name as plain text, the linking rule is weak.

### Prompt 5: Voice check

```
Write me a two-sentence description of what I had for breakfast this morning in my voice.
```

**What good looks like.** The agent asks what you had for breakfast first (because it has no data). This confirms it will not fabricate. If it invents a breakfast, your charter needs a stronger "never fabricate" rule.

If all five pass, your setup is working. Move on.

---

## Step 6 - Daily usage (10 starter prompts)

These are the prompts you will use again and again. Paste them straight into your agent.

### 1. Clean up a brain dump

```
I just pasted a brain dump into 00-Inbox/raw.md. Read it, split it into separate notes by topic, place each one in the right folder based on STRUCTURE.md, and show me the list before you move anything.
```

### 2. Write today's daily note

```
Create today's daily note at 01-Daily-Notes/YYYY/MM-Month/YYYY-MM-DD.md using 99-System/templates/daily-note.md as the template. Prefill the date and leave the prompt sections empty for me.
```

### 3. Review yesterday

```
Open yesterday's daily note and give me a three-bullet summary: what got done, what is still open, what I should carry forward into today.
```

### 4. Prep for a meeting

```
I have a meeting with Jamie Rivera at 2pm about the Q4 launch. Pull everything from 02-People/Jamie_Rivera.md and anything tagged #q4-launch. Draft a one-page prep note with context, open threads, and three questions I should ask.
```

### 5. Weekly review

```
It is Friday. Read all daily notes from this week in 01-Daily-Notes. Produce a weekly summary with sections: wins, blockers, patterns I should notice, one thing to try next week.
```

### 6. Kick off a new project

```
Create a new project folder under 03-Projects called project-name using 99-System/templates/project-kickoff.md. Fill in the goal, success criteria, and first three next actions based on what I will paste below.
```

### 7. Convert a document

```
I just pasted raw text from a PDF into 00-Inbox/doc.md. Clean it up: fix line breaks, add headings, pull out the key quotes into a callout block, and save the result to 05-Resources with a clear filename.
```

### 8. Research a topic

```
I want to learn about zero trust architecture. Search my vault for anything I already have on it. If nothing, tell me. Then build me a reading list of five concepts I should understand first.
```

### 9. Find missing links

```
Scan the last 10 daily notes. Find any mention of a person, project, or topic that is not wiki-linked but probably should be. Show me the list before you add any links.
```

### 10. Agent self-audit

```
Review the last three files you created in this vault. Audit them against the voice rules in CLAUDE.md. Flag any violations. Then flag any possible PII (phone numbers, SSNs, home addresses). Do not fix anything yet.
```

For a longer list by category, see `starter-prompts.md` in this folder.

---

## Step 7 - Import your past conversations

Your old ChatGPT and Claude.ai chats contain months of context about you. Importing them gives your new vault-aware agent a running start.

Full guide: [`workflows/07-import-past-conversations.md`](workflows/07-import-past-conversations.md).

Short version:

1. Export your data from ChatGPT (**Settings → Data Controls → Export data**).
2. Export your data from Claude.ai (**Settings → Privacy → Export data**).
3. Convert the JSON files into one markdown file per conversation. The workflow page includes a short Python script.
4. Drop the markdown files into `08-AI-History/<platform>/`.
5. Ask your agent:

```
Read everything in 08-AI-History. Give me a one-page summary of recurring themes, open questions, and projects I was working on. Flag anything sensitive that should move to a private folder.
```

> [!warning] Privacy
> These exports contain every chat you ever had. Review before you drop them anywhere that syncs to a cloud you do not control.

---

## Step 8 - Make it yours

The template is a starting point. Over the first two weeks, customize `CLAUDE.md`.

### Add your voice rules

What phrases do you want the agent to never use? What phrases are yours? Add them under a `## Voice rules` section. Short bullets.

Example:

```markdown
## Voice rules

- Short sentences.
- No AI vocabulary (delve, leverage, utilize, robust, seamless, moreover).
- No em dashes.
- Active voice.
- "BLUF" (bottom line up front) at the top of any brief.
```

### Add your focus areas

What are you working on this quarter? Who are the people the agent should know about? What is off-limits? Add a `## Current focus` section.

### Add your off-limits folders

Any folder with private content gets a hands-off rule.

```markdown
## Never do

- Never touch 00-Inbox/ without my per-file permission.
- Never modify files in Legacy/ for any reason.
- Never write to 01-Daily-Notes/ unless I ask for a new daily note.
```

Each time you catch the agent doing something you did not want, add a rule. The charter is a living document.

---

## Troubleshooting

### 1. The agent is not reading CLAUDE.md

**Symptom.** It answers Step 5 prompts with generic advice instead of your rules.

**Fix.** Check three things.
1. File is at the vault root, not nested in a subfolder.
2. File is named exactly `CLAUDE.md`, not `claude.md` or `CLAUDE.md.txt`.
3. You launched the agent from inside the vault folder (`cd` into it first).

### 2. `claude: command not found`

**Symptom.** Terminal says the command does not exist.

**Fix.** Node and npm have to be installed. On macOS, `brew install node`. On Windows, download from [nodejs.org](https://nodejs.org). Then rerun `npm install -g @anthropic-ai/claude-code`. If the install succeeds but the command still is not found, restart your terminal.

### 3. Agent wants to edit my Inbox

**Symptom.** You said no-touch, but it keeps proposing changes in `00-Inbox/`.

**Fix.** Add the rule twice in your charter, once in `## Always do` and once in `## Never do`. Some agents need the rule reinforced. Also check for conflicting rules higher up in the file.

### 4. The templates do not expand variables

**Symptom.** You copied `daily-note.md`, but the `<% tp.date.now() %>` text is still raw instead of showing today's date.

**Fix.** The Templater plugin is not installed or not enabled. Open **Settings → Community plugins** and confirm Templater is on. Then **Settings → Templater → Template folder location** should point at `99-System/templates`.

### 5. Obsidian cannot find my notes

**Symptom.** You can see the files in your file manager but Obsidian shows an empty vault.

**Fix.** You opened the wrong folder. In Obsidian, click the vault switcher icon (bottom left), then **Open folder as vault**, and pick the exact folder that contains your `.md` files.

---

## Where to go next

- **[`STRUCTURE.md`](STRUCTURE.md)** - the full folder layout and the reasoning behind it.
- **[`workflows/`](workflows/)** - eight specific workflows (brain dump cleanup, daily notes, document conversion, retroactive review, callouts, skills and MCP, past conversation import, NotebookLM).
- **[`security/`](security/)** - local-first setup, encryption, PII rules, backup habits.
- **[`starter-prompts.md`](starter-prompts.md)** - longer prompt library by category.
- **[`examples/`](examples/)** - worked examples including the knowledge graph tour.
- **[`COMPANION-AGENTS.md`](COMPANION-AGENTS.md)** - using the vault as the memory layer for other personal AI agents.

---

<!-- obsidian-second-brain by Emanuel Walker - github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->

_Template by Emanuel Walker. [github.com/Emanuel-Walker](https://github.com/Emanuel-Walker). Fork it. Adapt it. Credit appreciated, not required._
