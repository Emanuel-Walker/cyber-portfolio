# Install agent skills

## Goal

Install one `SKILL.md` folder so your agent can load it when the task matches.

You do not need all 15 skills.

Start with one.

## 1. Clone this portfolio

```bash
git clone https://github.com/Emanuel-Walker/cyber-portfolio.git
cd cyber-portfolio/05-ai-agent-skills
```

## 2. Pick one skill

Start with:

```text
skills/humanizer/
```

Every skill folder contains:

```text
SKILL.md
```

## 3. Copy it to your agent

### Claude Code

```bash
mkdir -p ~/.claude/skills
cp -r skills/humanizer ~/.claude/skills/
```

Verify:

```bash
test -f ~/.claude/skills/humanizer/SKILL.md && echo "PASS: skill installed"
```

### OpenAI Codex

```bash
mkdir -p ~/.codex/skills
cp -r skills/humanizer ~/.codex/skills/
```

Verify:

```bash
test -f ~/.codex/skills/humanizer/SKILL.md && echo "PASS: skill installed"
```

### GitHub Copilot

Personal skills commonly live under:

```text
~/.copilot/skills/
```

Project-specific skills can live under:

```text
.github/skills/
```

### Cursor

Project-level skills can live under:

```text
.cursor/skills/
```

If your Cursor version uses a different rules/skills path, use its current settings UI and point it at the same `SKILL.md` folder.

## 4. Test the install

Start a new agent session.

Ask:

```text
Use the humanizer skill.

Rewrite this:
"In today's rapidly evolving threat landscape, organizations must leverage robust and seamless AI solutions."
```

**PASS:** the output removes the inflated AI vocabulary and sounds more direct.

## Install several skills

Example:

```bash
for skill in humanizer docs-readability-audit repo-onboarding-audit builder-walkthrough; do
  cp -r "skills/$skill" ~/.claude/skills/
done
```

Change the destination for your agent.

## Recommended starter packs

### Writing

```text
humanizer
article-writing
brand-voice
docs-readability-audit
```

### Builder / coding agent

```text
repo-onboarding-audit
builder-walkthrough
web-ui-audit
prompt-optimizer
```

### Second brain / companion

```text
obsidian
companion-context
file-organizer
docs-readability-audit
```

## Adapt before trusting

Review every skill for:
- paths
- allowed tools
- voice preferences
- save destinations
- destructive actions
- external services

Do not install a skill you have not read.

## Troubleshooting

### Skill is not detected

Check:

```bash
find ~/.claude/skills -maxdepth 2 -name SKILL.md
```

Or use your agent's equivalent skills directory.

### Two skills conflict

Prefer the narrower skill.

Example:

```text
builder-walkthrough
```

should take precedence over a generic writing skill while authoring a technical setup guide.

### Skill runs but the result is wrong

The skill is guidance, not a proof system.

Add an acceptance test or review step instead of making the prompt longer.
