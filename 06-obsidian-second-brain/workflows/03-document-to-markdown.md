# Workflow 03 - Document to Markdown

**When to run it:** you have a PDF, a Word doc, a scanned page, or a voice memo you want in your vault.

**Why it matters:** your agent cannot read what is not in markdown. The vault only compounds in value when everything inside it is text-greppable.

---

## The toolchain

Three tools. Each one has a job.

| Tool | Job | Why it matters |
|---|---|---|
| **pandoc** | Convert any text document to clean markdown | The universal converter. Handles docx, html, rtf, epub, odt, latex, and more. |
| **Whisper** (openai-whisper or whisper.cpp) | Transcribe audio to text | Local, fast, surprisingly accurate. Voice memos become searchable notes. |
| **PaddleOCR** | Extract text from images and scanned PDFs | Handles handwriting and multi-column PDFs better than most alternatives. |

Install once, use forever.

```bash
# pandoc
# macOS: brew install pandoc
# Windows: winget install JohnMacFarlane.Pandoc
# Linux: apt install pandoc

# whisper
pip install openai-whisper
# or for the fast C++ port: https://github.com/ggerganov/whisper.cpp

# PaddleOCR
pip install paddleocr paddlepaddle
```

---

## Recipe 1: Word or PDF to markdown

```bash
# Word
pandoc input.docx -o output.md

# PDF (text-based, not scanned)
pandoc input.pdf -o output.md
```

Drop `output.md` into `00-Inbox/`. Run the brain dump cleanup workflow on it.

---

## Recipe 2: Scanned PDF or image to markdown

Pandoc cannot read a scan. Use OCR first.

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')
result = ocr.ocr('scan.pdf', cls=True)

with open('scan.md', 'w', encoding='utf-8') as f:
    for page in result:
        for line in page:
            f.write(line[1][0] + '\n')
```

The output needs a cleanup pass. That is a job for the agent. Hand it the raw text and say: "Clean this OCR output. Preserve the structure. Fix obvious OCR errors like `rn` for `m`. Do not change meaning."

---

## Recipe 3: Voice memo to markdown

```bash
whisper memo.m4a --model base --output_format txt --output_dir ./transcripts
```

The `base` model is fine for English voice memos. Use `small` or `medium` if you want more accuracy at a time cost. The output lands in `./transcripts/memo.txt`. Rename to `.md`, drop in `00-Inbox/`, let the agent clean it.

For speed on a laptop, [whisper.cpp](https://github.com/ggerganov/whisper.cpp) runs the same models faster with no Python dependency.

---

## Recipe 4: Web article to markdown

Use a browser extension like MarkDownload, or:

```bash
pandoc -f html -t markdown https://example.com/article -o article.md
```

Either way, the article lands in markdown. Drop in `05-Resources/` with a `source:` field in frontmatter so you can find it again.

---

## Why not just screenshot everything?

Screenshots do not compound. A screenshot is a dead end. The agent cannot read it, you cannot `grep` it, and in five years you will not remember what it was. Text wins every time.

The one exception is diagrams. For those, save the image to `07-Attachments/` and write a markdown note next to it that describes what the diagram shows.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
