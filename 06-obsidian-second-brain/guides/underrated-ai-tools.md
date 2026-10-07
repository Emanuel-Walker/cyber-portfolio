# Underrated AI Tools You Can Actually Download

A short list of the AI tools and skills most people miss. All of these are free or have free tiers. Most of them respect your data by default. Think of this page as the shelf next to your vault.

> [!info] Plain English
> These are tools you install. Not SaaS products that watch you. Each one gives your workflow a specific superpower.

---

## Claude-specific

### 1. Official Anthropic skills repo
`github.com/anthropics/skills`

Free skill files Anthropic ships. Underrated because most people do not know they exist. Includes a **skill-creator** that writes new skills for you based on a short description.

How to use: clone the repo, pick a skill, drop its `SKILL.md` into `~/.claude/skills/<name>/SKILL.md`. Restart Claude Code. Done.

### 2. MCP servers (Model Context Protocol)
`github.com/modelcontextprotocol/servers`

Plug these into Claude Desktop or Claude Code and give your agent access to your filesystem, GitHub, Slack, Google Drive, Notion, Postgres, memory, and more. Install one, your agent suddenly has superpowers in that domain.

Start with these three:
- **filesystem** - the agent reads and writes files you authorize
- **github** - the agent can open PRs, read issues, review commits
- **memory** - gives your agent a persistent memory store across sessions

Install guide lives in each server's README. Takes 5 minutes per server.

---

## Local-first (your data stays on your machine)

### 3. Ollama
`ollama.com`

Run Llama, Mistral, Qwen, DeepSeek, and other open models on your own laptop. Free. No API cost. Your prompts and outputs never leave your machine. One command installs it, one more pulls a model.

```bash
# After installing Ollama
ollama pull llama3.1:8b
ollama run llama3.1:8b
```

### 4. LM Studio
`lmstudio.ai`

Prettier UI for running local models. Good for people who want a chat window and model management without touching the terminal. Download, click a model, chat.

### 5. Open WebUI
`openwebui.com`

Self-hosted ChatGPT clone. Works with any LLM backend (Ollama, local or remote APIs). Teams can share a single Ollama server behind it so one GPU serves the whole shop. Clean interface, prompt library, document chat.

### 6. OpenInterpreter
`github.com/OpenInterpreter/open-interpreter`

Local code execution agent. You tell it what you want. It writes Python or bash and runs it on your machine. Scary and useful. Great for data cleanup, file wrangling, batch tasks you dread doing manually.

> [!warning] Use with care
> OpenInterpreter runs real code on your machine. Always review before approving. Never point it at folders you cannot afford to lose.

---

## Coding and shipping

### 7. Aider
`aider.chat`

Command-line coding agent with git awareness. Every change is a commit. If you dislike IDE lock-in or want a true pair-programmer in the terminal, this is Cursor without the IDE.

### 8. Continue.dev
`continue.dev`

Open-source Cursor alternative. Runs inside VS Code and JetBrains. Supports local models via Ollama. Free. Great if you want AI code help without a monthly subscription.

### 9. Fabric by Daniel Miessler
`github.com/danielmiessler/fabric`

Over 200 reusable AI prompts (he calls them patterns) for things like `summarize_newsletter`, `extract_wisdom`, `create_threat_model`, `write_essay`, `analyze_malware`, `rate_content`. A CLI you pipe text into.

```bash
# Example
pbpaste | fabric --pattern extract_wisdom
```

Dramatically underrated. If you want battle-tested prompts without writing them yourself, start here.

---

## Research and knowledge

### 10. NotebookLM
`notebooklm.google.com`

Covered in detail in `workflows/08-notebooklm.md`. Google's research tool. Upload your vault notes, PDFs, YouTube links. Generate audio overviews (the podcast), video overviews, mind maps, briefing docs, study guides. Free.

### 11. Perplexity Spaces
`perplexity.ai/spaces`

Create a Space, upload your sources, ask research questions grounded in them. Think NotebookLM with sharper web search integration. Good for ongoing research threads you want the AI to come back to.

---

## Meeting and capture

### 12. Granola
`granola.ai`

AI meeting notes that run locally on macOS. Takes your rough notes and the meeting audio, produces structured meeting minutes. Does not send audio to cloud by default. Non-obvious because the market is loud with cloud-first competitors.

---

## The 10 I built (in this repo)

Live at `../05-ai-agent-skills/`. Drop any `SKILL.md` into `~/.claude/skills/<name>/SKILL.md` for Claude Code. Or paste into a Cursor rules file. Or load into any skill-aware agent.

| Skill | Does what |
|---|---|
| **content-engine** | Generates platform-ready drafts (LinkedIn, X, newsletter) |
| **humanizer** | Strips AI tells from writing |
| **article-writing** | Long-form essays and blog posts |
| **brand-voice** | Builds reusable voice profiles from your samples |
| **prompt-optimizer** | Rewrites your prompts so they actually work |
| **drawio** | Diagrams in XML with proper fonts and arrows |
| **file-organizer** | Cleans up messy folders |
| **ship-learn-next** | Turns learning content into rep plans |
| **smart-ocr** | PaddleOCR wrapper for screenshots and PDFs |
| **obsidian** | Vault automation (CRUD plus Obsidian URI commands) |

---

## The pattern worth noticing

The underrated tools share one trait. **They respect ownership.** Local models, local file access, your data on your machine, your prompts as patterns you can version. The hyped tools (big-name cloud wrappers, generic LLM chat UIs) sell convenience in exchange for your context. The underrated ones trade a little setup time for independence.

The skills in Project 5 of this repo sit in that same lane. That is why they belong on this list.

---

## How to try one this week

Pick ONE. Install it. Use it for a real task. Decide if it stays.

- **If you journal or take meeting notes:** try **Granola**.
- **If you want to break your OpenAI subscription habit:** try **Ollama** plus **Open WebUI**.
- **If you code daily:** try **Aider** or **Continue.dev**.
- **If you consume newsletters and articles:** try **Fabric** with the `extract_wisdom` pattern.
- **If you want your agent to actually touch your files:** install the **filesystem MCP** server.
- **If you want your writing to stop sounding like ChatGPT:** install the **humanizer** skill from this repo.

The point is not to install all twelve. The point is to pick the one that would change your Monday.

---

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template inside [cyber-portfolio](https://github.com/Emanuel-Walker/cyber-portfolio). Credit appreciated, not required._
