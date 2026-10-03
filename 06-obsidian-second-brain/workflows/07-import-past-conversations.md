# Workflow 7: Import your past ChatGPT and Claude.ai conversations

Your old chats are a goldmine. Months of context about what you care about, how you talk, what you were building, who you were figuring out. Importing them gives a brand new vault-aware agent a running start instead of a cold open.

This workflow takes about 30 minutes once your exports land in your email.

---

## Why bother

- Your old chats remember projects you forgot about.
- They expose recurring questions (good signal for what to build next).
- They show how your voice actually sounds in real conversation.
- A vault-aware agent can read all of them at once and summarize patterns in a way you cannot do by scrolling.

> [!info] Plain English
> You are moving your chat history from the vendor's cloud into plain markdown files on your laptop. Once they are in your vault, your new agent reads them like any other note.

---

## Step 1 - Export from ChatGPT

1. Open [chat.openai.com](https://chat.openai.com) and sign in.
2. Click your profile icon, then **Settings**.
3. Go to **Data Controls**.
4. Click **Export data**, then **Confirm export**.
5. Check your email. OpenAI sends a download link within a few hours (sometimes a day).
6. Click the link. You get a ZIP file. Save it somewhere you can find.
7. Unzip it. The file you want is `conversations.json`.

---

## Step 2 - Export from Claude.ai

1. Open [claude.ai](https://claude.ai) and sign in.
2. Click your profile, then **Settings**.
3. Go to **Privacy**.
4. Click **Export data**, then confirm.
5. Check your email. Anthropic sends the link within a few hours.
6. Click the link. You get a ZIP. Unzip it.
7. The main file is `conversations.json`. Same shape as ChatGPT, different schema.

---

## Step 3 - Convert JSON to markdown

Save the script below as `convert_chats.py` next to your `conversations.json`.

```python
# convert_chats.py
# Reads one conversations.json file (ChatGPT or Claude.ai export shape)
# and writes one .md file per conversation into an output folder.
# Teacher-voice comments so you can read along as it runs.

import json
import os
import re
from datetime import datetime
from pathlib import Path

# Change these two lines if you want different paths.
INPUT_FILE = "conversations.json"          # the export file
OUTPUT_DIR = "converted_markdown"          # where the .md files land

# Pick which export shape you have. "chatgpt" or "claude".
PLATFORM = "chatgpt"


def slugify(text, max_len=60):
    """Turn a conversation title into a safe filename."""
    text = re.sub(r"[^a-zA-Z0-9\s-]", "", text or "untitled")
    text = re.sub(r"\s+", "-", text).strip("-").lower()
    return text[:max_len] or "untitled"


def convert_chatgpt(conversations, out_dir):
    """ChatGPT export shape: list of conversations with a mapping of message nodes."""
    for convo in conversations:
        title = convo.get("title", "untitled")
        created = convo.get("create_time")
        date_str = (
            datetime.fromtimestamp(created).strftime("%Y-%m-%d")
            if created
            else "unknown-date"
        )
        slug = slugify(title)
        filename = f"{date_str}_{slug}.md"

        # Walk the message tree in order.
        mapping = convo.get("mapping", {})
        messages = []
        for node in mapping.values():
            msg = node.get("message")
            if not msg:
                continue
            author = msg.get("author", {}).get("role", "unknown")
            parts = msg.get("content", {}).get("parts", [])
            body = "\n".join(p for p in parts if isinstance(p, str))
            if body.strip():
                messages.append((author, body))

        write_markdown(out_dir / filename, title, date_str, messages)


def convert_claude(conversations, out_dir):
    """Claude.ai export shape: list of conversations with a flat chat_messages array."""
    for convo in conversations:
        title = convo.get("name", "untitled")
        created = convo.get("created_at", "")
        date_str = created[:10] if created else "unknown-date"
        slug = slugify(title)
        filename = f"{date_str}_{slug}.md"

        messages = []
        for msg in convo.get("chat_messages", []):
            author = msg.get("sender", "unknown")  # "human" or "assistant"
            body = msg.get("text", "")
            if body.strip():
                messages.append((author, body))

        write_markdown(out_dir / filename, title, date_str, messages)


def write_markdown(path, title, date_str, messages):
    """Write a single conversation to markdown."""
    lines = [
        f"# {title}",
        "",
        f"**Date:** {date_str}",
        f"**Source:** {PLATFORM}",
        "",
        "---",
        "",
    ]
    for author, body in messages:
        lines.append(f"## {author}")
        lines.append("")
        lines.append(body)
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(exist_ok=True)

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Both platforms wrap conversations differently. Normalize here.
    conversations = data if isinstance(data, list) else data.get("conversations", [])

    if PLATFORM == "chatgpt":
        convert_chatgpt(conversations, out_dir)
    else:
        convert_claude(conversations, out_dir)

    count = len(list(out_dir.glob("*.md")))
    print(f"Wrote {count} markdown files to {out_dir.resolve()}")


if __name__ == "__main__":
    main()
```

Run it:

```bash
python convert_chats.py
```

You get a `converted_markdown/` folder with one `.md` file per conversation. The filenames are date-slug format like `2026-03-14_debugging-the-auth-middleware.md`.

---

## Step 4 - Where to put the files in your vault

Keep platforms separate so you can tell them apart later.

```bash
mkdir -p 08-AI-History/chatgpt
mkdir -p 08-AI-History/claude

# Move your converted files in
mv converted_markdown/*.md 08-AI-History/chatgpt/
```

Repeat for the Claude.ai export, dropping those files into `08-AI-History/claude/`.

Final shape:

```
08-AI-History/
  chatgpt/
    2026-03-14_debugging-the-auth-middleware.md
    2026-04-02_q2-planning.md
    ...
  claude/
    2026-07-01_essay-draft-review.md
    ...
```

---

## Step 5 - Ask your agent to summarize

Paste this into your agent:

```
Read everything in 08-AI-History. Group the conversations by topic and give me:

1. The three recurring themes across all my chats.
2. Open questions I asked more than once that I never fully resolved.
3. Projects I started talking about but never shipped.
4. One pattern in how I think that would be useful for you to remember going forward.

Flag any conversation that contains sensitive information (financials, health, legal, people other than me by full name) and recommend moving it to a private folder.
```

Expect a one-page summary. If the output is thin, run it against one platform folder at a time instead of both at once (context window limits).

---

## Privacy note

Chat exports contain **everything**. Every half-finished thought, every work frustration, every personal question you asked an AI at 2am.

Before you drop them into any folder that syncs anywhere:

- Review the summary your agent produces. Flagged conversations are the ones most likely to need a different home.
- Move anything sensitive to a private folder outside your vault, or into a vault folder that you explicitly do not sync.
- If you plan to publish or share your vault structure, add `08-AI-History/` to your `.gitignore` or your sync tool's exclusion list.
- Consider deleting the raw ZIP and `conversations.json` once the markdown is in place. You can always re-export.

See [`../security/04-pii-rules.md`](../security/04-pii-rules.md) and [`../security/06-everyday-good-practices.md`](../security/06-everyday-good-practices.md) for more.

---

<!-- obsidian-second-brain by Emanuel Walker - github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->

_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
