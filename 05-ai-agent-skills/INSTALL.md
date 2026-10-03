# Install

Three paths depending on which assistant you use.

## Claude Code

Claude Code loads skills from `~/.claude/skills/<skill-name>/SKILL.md`. The front-matter `name` and `description` fields let the assistant decide when to load the file.

```
cp -r skills/humanizer ~/.claude/skills/
cp -r skills/article-writing ~/.claude/skills/
cp -r skills/brand-voice ~/.claude/skills/
```

Then start a new Claude Code session. The next time your prompt matches a skill's description, the assistant will load that skill before responding.

Verify an install:

```
ls ~/.claude/skills/humanizer/SKILL.md
```

## Cursor

Cursor uses a single rules file at `.cursorrules` (project root) or Settings → Rules for AI (global). It does not load skills on demand the way Claude Code does, so you have two options:

**Option 1 - pick one skill and paste it in.** If you want Cursor to always apply the humanizer rules while you write, open `skills/humanizer/SKILL.md`, strip the YAML front matter, and paste the body into `.cursorrules`.

**Option 2 - index multiple skills by description.** Build a `.cursorrules` that lists each skill name and description with a one-liner that says "when the user asks for X, apply the rules in `skills/X/SKILL.md`." Then keep this repo as a sibling folder so Cursor can read the files when needed.

Example `.cursorrules` header:

```
When the user asks to clean up AI writing tells, apply the rules in
skills/humanizer/SKILL.md. When the user asks to draft a long-form
piece, apply skills/article-writing/SKILL.md. When unsure which skill
applies, ask.
```

## Any skill-aware assistant

The pattern is universal.

1. Each `SKILL.md` is a self-contained instruction module.
2. Front matter declares `name` and `description`. The description is the trigger signal.
3. Body is the ruleset.

If your assistant supports a "load this file as context when the user asks about X" pattern, point it at `SKILL.md` using the description as the match condition. If it only supports a single system prompt, concatenate the skills you use most into one file and keep the rest as reference.

## Adaptation checklist before you ship

- [ ] Replace `<your-vault-root>` with your actual notes path.
- [ ] Replace `<your-content-root>` with your actual content folder, or remove the skill if you do not run a content engine.
- [ ] Replace `<your-system-folder>` with the folder you use for templates and automation.
- [ ] Review the voice rules in `humanizer` and `brand-voice`. Mine are specific. Keep what applies, drop what does not.
- [ ] Review the save-routing tables in `smart-ocr`, `file-organizer`, and `ship-learn-next`. Point them at your folders.
- [ ] Check platform specifics in `content-engine`. Short-form vertical video is my lane. Yours may be a newsletter or a blog.

## Troubleshooting

**Skill does not load.** Check that the `name` field matches the folder name and that the file is at `~/.claude/skills/<name>/SKILL.md`, not nested one level deeper.

**Skill loads but does not fire the right behavior.** Read the front-matter description. The assistant uses that to decide whether to load the skill. If the description does not clearly match the user's intent, tighten it.

**Two skills try to run at once.** Add a precedence note at the top of one. The `obsidian` skill in this set shows the pattern - it defers to more specialized skills when they apply.
