# Writeup: what these skills are and why they are organized this way

## What a "skill" is in this sense

A skill is a single instruction module that an AI assistant can load on demand. In Claude Code it lives at `~/.claude/skills/<name>/SKILL.md`. It has YAML front matter with a `name` and `description` field. The description is the trigger. When your prompt matches the description, the assistant reads the body of the file and applies the rules inside.

That is it. No code. No runtime. No plugin install. The whole mechanism is the assistant deciding "this instruction block is relevant to the current request" and reading the file.

Cursor does something similar through its rules file, though less dynamically. Any skill-aware assistant can be adapted to the pattern. The point is modular, loadable instructions instead of one giant system prompt that tries to cover everything.

## Why modular beats monolithic

I started where most people start. One system prompt. One file called `instructions.md` that tried to cover every situation I cared about. Voice rules, folder paths, canonical quote handling, what to never fabricate, how to format a long-form draft, how to open a file in Obsidian from PowerShell. All of it in one place.

The problem showed up fast. The system prompt got long. The assistant lost focus. Rules that mattered for one task would bleed into tasks where they did not apply. Humanizer rules written for personal essays would quietly strip em dashes out of an academic paper where em dashes were fine. Content-engine rules written for short-form video would show up when I was drafting a technical post. The signal-to-noise ratio collapsed.

Modular instructions fix that. The humanizer skill loads only when I ask for humanizer work. The content-engine skill loads only when I touch content. The obsidian skill loads only when I touch the vault. When I draft a paper, three skills chain in order (brand-voice, article-writing, humanizer) and each one does its narrow job. No cross-contamination.

There is a second benefit. Each skill is readable on its own. I can open the humanizer file and know exactly what it does. If I want to change how I handle rule-of-three, I change one file. If I want to retire a skill, I delete one folder. Nothing is tangled.

## Three patterns I used across these ten

### 1. Trigger clarity

Every skill opens with a `description` field that reads like a trigger. "Remove AI-writing tells from text." "Build a durable VOICE PROFILE from real source material." "Create and edit draw.io diagrams in XML format." The description tells the assistant what the skill is for. If the description is vague, the assistant loads the wrong skill or loads nothing. If the description is sharp, routing is clean.

I also encoded "when to use" and "when NOT to use" sections inside each skill body. The negative cases matter as much as the positive ones. The prompt-optimizer skill explicitly says "if the user says 'just do it', do not run this skill. Execute instead." Without that, the skill would catch requests it should ignore.

### 2. Scope boundary

Each skill declares what it owns and what it does not own. The content-engine skill writes exclusively to `<your-content-root>/`. The obsidian skill handles general vault ops but defers to specialized vault-local skills for things like dream interpretation or extracting signals from daily notes. The smart-ocr skill never overwrites source files. It writes to a sidecar.

Scope boundaries prevent collisions. Two skills with overlapping scope will fight. Two skills with clean boundaries will chain. The write-zone rule in content-engine is the sharpest version of this pattern. Everything outside that folder is read-only to the skill. The assistant cannot accidentally rewrite a reference file.

### 3. Output contract

Each skill specifies what its output looks like. Humanizer delivers a draft, a bullet list of remaining tells, a final rewrite, and an optional changelog. Prompt-optimizer delivers five numbered sections in a specific order. Ship-learn-next delivers a saved markdown file with a defined frontmatter block and a Rep 1 block highlighted in chat.

Output contracts matter because downstream skills depend on them. The content-engine skill saves a draft with `status: needs-review` in frontmatter. The humanizer skill knows that `needs-review` means "touch this." If one skill broke the contract, every downstream skill would break too. Making the contract explicit in the skill file keeps the chain intact.

## Honest limits

These are personal. The humanizer skill reflects my own preferences. No em dashes in operational voice. No AI vocabulary I happen to notice. Rule-of-three when I think it is padding. Someone else's humanizer would ban different words, treat em dashes differently, let different cliches through.

The folder paths are placeholders. Everywhere a path appears, I replaced my own path with `<your-vault-root>` or `<your-content-root>` or `<your-system-folder>`. If you fork and keep the placeholders, nothing runs. You have to decide what your folder structure looks like and fill them in.

The platform assumptions are mine. Content-engine assumes short-form vertical video and long-form social. If you ship a podcast or a newsletter or a GitHub project, the format spec needs rewriting. Smart-ocr assumes PaddleOCR 3.6 on Windows. On Linux the oneDNN workaround is unnecessary. On a Mac the install path differs.

None of that is a problem if you treat these as reference. The logic generalizes. The specifics do not.

## What a reader can steal

If you are building your own skill set, the patterns transfer.

- Write a trigger description that says exactly what the skill does and what it does not do. Vague descriptions lose routing precision.
- Draw a scope boundary around what the skill writes to. Anything outside that boundary should be read-only.
- Specify the output shape. Downstream chains need a contract.
- Encode negative examples. "When NOT to use this skill" is as useful as "when to use."
- Keep each skill short enough to re-read in one sitting. If it does not fit in a scroll or two, split it.
- Reference other skills by name instead of inlining their rules. Cross-skill chains are the point.

The ten here are a starting set. Mine. If any one of them clicks for your workflow, keep that one, discard the rest, and build your own with the same pattern.

That is how I think about these. A tool is only as sharp as the instructions behind it, and modular instructions stay sharp longer than monolithic ones. Fork what works. Replace what does not.
