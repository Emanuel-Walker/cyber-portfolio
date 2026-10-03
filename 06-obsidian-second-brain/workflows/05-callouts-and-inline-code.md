# Workflow 05 - Callouts and Inline Code

**When to use it:** every time you write a note. These two tools make your vault agent-friendly and future-you friendly.

---

## Obsidian callouts

Callouts are quoted blocks with a type keyword. They render as colored boxes in Obsidian and they are a strong signal to an agent reading your notes.

### The core callouts you will actually use

```markdown
> [!note]
> A plain callout. Use when you want to pull something out of the body without
> giving it a stronger label.

> [!info]
> Reference material. Use for definitions, specs, quick facts.

> [!warning]
> Something to watch out for. Future-you will thank present-you.

> [!question]
> A question you are asking the agent, or an open question you want answered later.

> [!todo]
> A task. Agents can scan for these across the vault.

> [!quote]
> Something someone said. Attribute at the end with em dash (if you use long-form voice)
> or just a line break and the name.
```

### When to use `> [!question]`

Any time you want the agent to answer something on its next pass. Example:

```markdown
> [!question]
> Does this incident response plan work if the on-call rotation only has one person?
```

Run the agent across your vault once a week with: "Find every `> [!question]` callout. For each one, either answer it or flag it as still open."

### When to use `> [!warning]`

For anything that could burn you later. OPSEC-sensitive material, assumptions that might break, or a decision you made under pressure.

```markdown
> [!warning]
> This cert expires on 2027-04-15. Rotation is manual. Set a calendar reminder.
```

---

## Inline code with backticks

Inline code is for anything a human types verbatim or a machine would parse. Commands, filenames, API endpoints, variable names, file paths.

```markdown
Open `03-Projects/Home_Lab/00_Index.md` and run `make test`.
```

The reason this matters: agents are better at parsing inline-coded tokens than they are at parsing plain prose. When you write `pandoc input.docx -o output.md` with backticks, the agent treats it as a command. Without backticks, it is just words.

### What to backtick

- File paths: `03-Projects/Home_Lab/`
- Commands: `git commit -m "message"`
- Filenames: `.gitignore`
- Code identifiers: `useState()`, `main()`, `--verbose`
- Env vars: `OPENAI_API_KEY`
- URLs you do not want to render as a link but do want to preserve verbatim

### What not to backtick

- Normal nouns. "Open the file" does not need backticks. "Open `README.md`" does.
- Full sentences. Code fences are for that.

---

## Code fences for anything longer than a token

```markdown
```bash
cd ~/vault
pandoc input.docx -o 00-Inbox/output.md
claude
```
```

The language tag after the opening fence helps both the renderer and the agent. Use `bash`, `python`, `yaml`, `markdown`, `json`, or whatever applies. If you do not know, leave it blank. Any fence is better than no fence.

---

## Why this makes your vault agent-friendly

An agent reading your vault runs on structure. Callouts and code fences are the clearest structural signals in markdown. A note full of plain prose is harder to parse than a note where the questions, warnings, and commands are visually tagged. You will feel the difference the first time you ask an agent to "find all my open questions across the vault." That query is impossible on prose-only notes. It is trivial on a vault where `> [!question]` is the convention.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
