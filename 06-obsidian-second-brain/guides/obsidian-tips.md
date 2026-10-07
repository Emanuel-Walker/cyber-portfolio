# Obsidian Tips - Make the Vault Actually Work For You

Obsidian out of the box is a markdown editor. Obsidian with the right habits and plugins is a thinking system. Here is the short list of what to turn on, what to install, and what shortcuts actually matter.

> [!info] Plain English
> This is a cheat sheet. Pick the three or four tips that fit how you work. Ignore the rest until you need them.

---

## Callouts (the thing that makes notes readable)

Callouts are colored boxes you can drop into any note. They work like this:

```markdown
> [!info] This is an info callout
> Your explanation here. Multiple lines are fine.
```

The default callout types:

| Type | Use it for |
|------|-----------|
| `info` | Background context, definitions, "plain English" explanations |
| `tip` | A trick or shortcut the reader will thank you for |
| `warning` | "Be careful" moments. Yellow box. |
| `danger` | "Do not do this" moments. Red box. |
| `question` | Open questions you want to come back to |
| `quote` | Direct quotes from people or sources |
| `example` | A worked example |
| `success` | What worked |
| `failure` | What did not work |
| `note` | General note. Blue box. |
| `todo` | Tasks you have not done yet |
| `abstract` | Summary at the top of a long note |

### Why callouts matter

Your future self scans. Callouts give the scan something to land on. Also, when your AI agent reads your notes, `[!question]` and `[!todo]` callouts are easy for it to find and surface in a review.

### Tricks

- Add a plus sign to make a callout collapsible: `> [!info]+ Click to open`
- Add a minus sign to make it collapsed by default: `> [!info]- Click to open`
- Nest callouts by indenting with another `>` character

---

## Core plugins to enable right now

Core plugins ship with Obsidian. You just turn them on. Settings → Core plugins.

- **Templates** - lets you have a template file and insert it into any note with a hotkey. Set your template folder to `99-System/templates/`.
- **Daily notes** - creates one note per day using your daily note template. Set it to open your today note on launch so your first click is always your day.
- **Graph view** - the visual map of how your notes connect. Open it from the left sidebar. See the growth over time.
- **Backlinks** - shows every note that links to the note you are reading. Live context.
- **Outline** - the heading map of the current note. Good for long notes.
- **Tags** - the tag pane. Click a tag, see every note that uses it.
- **File recovery** - keeps auto-snapshots of your notes. Saves you when you accidentally delete.
- **Command palette** - press `Ctrl+P` and type what you want. The fastest way to use Obsidian.
- **Quick switcher** - press `Ctrl+O` and start typing a note name. Teleport.
- **Unique note creator** - creates new notes with a timestamp in the name. Great for atomic captures.
- **Workspaces** - save a window layout and switch between them. One layout for daily note writing, another for research.

---

## Community plugins worth installing

Community plugins are third-party. Install via Settings → Community plugins → Browse. Always read what a plugin wants permission to do before installing.

| Plugin | Why you want it |
|--------|----------------|
| **Templater** | Smarter templates with variables, prompts, and scripting. The daily note template in this repo expects Templater. |
| **Dataview** | Query your vault like a database. "Show me every note tagged `#project` with `status: active`." Powerful. |
| **Kanban** | A real Kanban board inside a note. Great for personal workflow and small team tracking. |
| **Excalidraw** | Hand-drawn diagrams and sketches inside your notes. Pairs with Draw.io if you need both. |
| **Advanced Tables** | Keyboard navigation and auto-formatting for markdown tables. Life saver. |
| **Natural Language Dates** | Type `@today` or `@next thursday` and it inserts the real date. |
| **Tasks** | Due dates, recurring tasks, filters. If you want a task manager inside your vault. |
| **Calendar** | A monthly calendar in the sidebar. Click a day, jump to that daily note. |
| **Periodic Notes** | Weekly, monthly, quarterly, yearly notes with templates. For reviews. |
| **Smart Connections** | AI-powered semantic search over your vault. Free with a local model, paid for the convenient one. |
| **Omnisearch** | Full-text search that is way better than the default. |
| **Mind Map** | Convert any note into a mind map view. |
| **Minimal Theme** | Clean, calming visual theme. Taste varies, worth trying. |

> [!tip] Resist plugin creep
> Install three. Use them for a week. Only add a fourth if you hit a wall. More plugins = more startup time and more things that can break.

---

## Keyboard shortcuts that save hours

Most of these also work on macOS with Cmd instead of Ctrl.

| Shortcut | What it does |
|----------|-------------|
| `Ctrl+P` | Command palette. If you learn ONE shortcut, make it this one. |
| `Ctrl+O` | Quick switcher. Jump to any note by name. |
| `Ctrl+N` | New note in the current folder. |
| `Ctrl+E` | Toggle between edit mode and reading mode. |
| `Ctrl+K` | Insert a link. Then type to search for the note. |
| `Ctrl+Shift+F` | Search across the whole vault. |
| `Ctrl+click` on a link | Open that note in a new tab. |
| `Ctrl+Alt+click` on a link | Open that note in a split pane. |
| `Ctrl+Shift+click` on a link | Open in new window. |
| `Alt+Enter` on a link | Follow the link. |
| `Ctrl+/` | Toggle comment on current line. |
| `Ctrl+D` | Duplicate the current line. |
| `Ctrl+L` | Make the current line a task (adds `- [ ]`). |

### Custom hotkeys

Settings → Hotkeys. You can bind any command to any key. The two most useful customs:

- Bind `Templater: Insert template` to `Ctrl+T`
- Bind `Daily notes: Open today's note` to `Ctrl+D` (or whatever you prefer)

---

## Wikilinks and the graph

Wikilinks are the glue of your second brain. Any time you type `[[` Obsidian suggests notes to link to.

```markdown
Yesterday I had coffee with [[Jamie Chen]]. We talked about [[Cloud Security Projects]] and the [[AWS IR Lab]].
```

Every one of those becomes a clickable link. Open the graph view and you will see Jamie connected to coffee notes, Jamie connected to Cloud Security Projects, and so on. That is your second brain forming.

### Alias tricks

Pipe syntax lets you link to a note but display different text:

```markdown
I met with [[Jamie Chen|Jamie]] this morning.
```

Shows as "Jamie" in the note, still links to the Jamie Chen file.

### Block links

Link to a specific paragraph:

```markdown
See [[2026-10-03#^important-block]] for details.
```

The `^important-block` is a block id Obsidian can generate for you.

---

## Tags vs folders

Both work. Here is the rule of thumb.

- **Folders** are for files that logically live together. A project folder holds its project notes. A people folder holds people notes.
- **Tags** are for themes that cut across folders. `#faith`, `#reading`, `#health`, `#career` can show up anywhere.

A single note can live in one folder and have many tags. Use folders for structure, tags for lenses.

---

## Properties (frontmatter) and why they matter

The top of every good note has a YAML block like this:

```markdown
---
title: Weekly review 2026-10-03
tags: [review, weekly]
status: draft
mood: focused
---
```

This is **frontmatter**. Obsidian treats these fields as **properties** you can filter, query, and sort on with Dataview. Your AI agent also reads them. A note with `status: draft` can be routed differently than one with `status: published`.

### Common properties worth standardizing

| Property | Values |
|----------|--------|
| `status` | draft, needs-review, published, archived |
| `tags` | array of topic tags |
| `created` | ISO date |
| `updated` | ISO date |
| `type` | daily, project, person, meeting, book, idea |
| `priority` | 1-5 |
| `related` | array of wikilinks to other notes |

---

## Canvas (visual thinking space)

Canvas is Obsidian's whiteboard. Right-click in the file tree → New canvas.

- Drag any note onto a canvas. The canvas card shows the note live. Edit it right there.
- Draw arrows between cards. Group them. Zoom in and out.
- Great for: brainstorming, project planning, concept mapping, visual outlines, meeting prep.
- Export the canvas as PNG for sharing.

If Excalidraw is your sketchpad, Canvas is your whiteboard. Different tools, different jobs.

---

## Templater snippets that pay for themselves

Templater lets your templates run code. Three snippets that get a lot of mileage:

### Today's date

```markdown
<% tp.date.now("YYYY-MM-DD") %>
```

### Prompt the user for a title

```markdown
<% tp.system.prompt("What is this note about?") %>
```

### Insert the current filename as the title

```markdown
# <% tp.file.title %>
```

Combine them in a daily note template so your new day file auto-fills with date, mood prompt, and today's priority prompt.

---

## Graph view - what to look for

Open the graph. Left click a node to highlight its connections. What matters:

- **Hub nodes** (lots of lines coming in and out) are your main topics. These are probably your Maps of Content.
- **Islands** (small clusters disconnected from the main mass) are notes that need linking. Open one, add a wikilink or two.
- **Orphans** (single nodes floating alone) are either unfinished thoughts or things that should be archived.

Doing a 5-minute graph review once a month tells you what your brain has been working on without you having to remember.

---

## Mobile tips

Obsidian has a mobile app (iOS and Android, free). To sync without paying:

- Use a cloud folder service (iCloud Drive, Google Drive, Dropbox) and point the mobile app at it.
- Or use the Obsidian Git plugin to sync via a private GitHub repo.
- Or pay for Obsidian Sync ($5/month, end-to-end encrypted).

On mobile, the thing you really want to tune is **Quick Capture**. Bind a widget or shortcut that opens Obsidian straight to a new note in your Inbox. Capture latency matters more than editing power on mobile.

---

## The ten-minute weekly habit

Once a week, do this:

1. Open the graph. Scan for orphans. Link or archive each one.
2. Open your Inbox folder. Route anything older than 7 days to its real home.
3. Open your daily notes folder. Scroll last week's days. Any pattern you want to turn into a project? Any person you keep mentioning? Any question that still has no answer?
4. Ask your agent: `Read my daily notes from the past 7 days. Give me one page: what I built, what I avoided, what deserves a project note next week.`
5. Act on exactly one thing from that review.

This is where the second brain stops being a journal and starts being a system.

---

## Things to avoid

- **Plugin hoarding.** Three plugins used daily beat twenty gathering dust.
- **Over-nesting folders.** More than three levels deep and you will never find anything.
- **Treating the vault as perfect.** Messy notes are better than no notes. Clean later.
- **Sharing your vault with people who should not see your journal.** Legacy folder is for after-you-go. Not for sharing while you are around.
- **Encrypting the whole vault and losing the password.** Keep your password manager current. Keep a sealed paper copy somewhere safe for your family.

---

## Further reading

- **Core docs:** help.obsidian.md
- **Plugin registry:** obsidian.md/plugins
- **Dataview docs:** blacksmithgu.github.io/obsidian-dataview
- **Templater docs:** silentvoid13.github.io/Templater

---

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template inside [cyber-portfolio](https://github.com/Emanuel-Walker/cyber-portfolio). Credit appreciated, not required._
