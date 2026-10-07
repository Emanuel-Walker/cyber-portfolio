# Quickstart - AI Agent Skills

> [!info] Plain English
> A "skill" is a small markdown file that teaches an AI assistant how to do one job well. You will install one skill (the humanizer, which rewrites AI-sounding text), then watch it transform a paragraph of corporate filler into something readable. Takes about 5 minutes.

## 5-minute demo

BLUF. You will install one skill (the humanizer), invoke it inside Claude Code, and watch it rewrite an AI-sounding paragraph into something that reads like a person wrote it. If the before and after differ in the expected ways, the skill works.

Prerequisites.

```bash
# Claude Code installed and logged in
claude --version
# Skills directory exists
mkdir -p ~/.claude/skills
ls ~/.claude/skills
```

Step 1 - setup. Install the humanizer skill.

```bash
cd 05-ai-agent-skills
bash scripts/install-skill.sh claude humanizer
```

On Windows PowerShell:

```powershell
Set-Location 05-ai-agent-skills
.\scripts\install-skill.ps1 -Agent claude -Item humanizer
```

What you see. The copy succeeds silently. `ls` prints `SKILL.md`. Claude Code auto-discovers skills in `~/.claude/skills/*/SKILL.md` on next launch.

Step 2 - invoke it on a sample.

Open Claude Code in any directory. Paste this prompt verbatim.

```
/humanizer

Rewrite this paragraph:

In today's rapidly evolving threat landscape, organizations must leverage
robust, scalable solutions to seamlessly integrate advanced detection
capabilities. Moreover, by utilizing cutting-edge AI, security teams can
delve into unprecedented insights that empower proactive defense.
```

What you see. Claude Code loads the humanizer SKILL.md, applies its rewrite rules, and returns a shortened paragraph with the AI vocabulary stripped. Something like:

```
Threats change fast. Security teams need detection tools that fit the stack
they already run, not a rip-and-replace. The AI piece is a force multiplier
when the schema and logging are already clean. When they are not, it is
just louder noise.
```

Step 3 - validate.

Confirm the rewrite drops these specific tells. Each one is called out in `SKILL.md`.

- "leverage," "robust," "seamlessly," "utilize," "delve," "moreover" all gone
- No em dashes
- No rule-of-three stacks
- Sentence length varies
- No vague attributions like "organizations must"

If any of those survive, the skill did not load. Confirm `~/.claude/skills/humanizer/SKILL.md` exists and is not empty, then restart Claude Code.

## What this proves

- Modular prompt engineering, scoped per skill with explicit trigger conditions and output contracts, instead of one bloated system prompt.
- A reusable library that ports between projects by copying one markdown file.
- Enforceable voice rules that catch AI tells automatically so the writer does not have to grep for them by hand.

## Add screenshots here

Capture these while running the demo and drop them in a `screenshots/` folder next to this file.

- `screenshots/01-skills-dir.png` - `~/.claude/skills/humanizer/` with `SKILL.md` present
- `screenshots/02-skill-md-open.png` - top of `SKILL.md` showing the trigger block
- `screenshots/03-before-paragraph.png` - the AI-flavored input pasted into Claude Code
- `screenshots/04-after-paragraph.png` - the humanized rewrite in the same session
- `screenshots/05-skill-logs.png` - Claude Code showing the skill was invoked (status line or tool call log)

## Common issues

- Claude Code does not recognize `/humanizer`. The file is in the wrong path. The directory name under `~/.claude/skills/` must match the skill name, and the file inside must be named `SKILL.md` exactly.
- Skill loads but the output still sounds like AI. The model received the input but ignored the rules. Add "apply the humanizer skill strictly, do not paraphrase" to the prompt and rerun.
- Windows path. On Windows, the skills directory lives at `%USERPROFILE%\.claude\skills\humanizer\SKILL.md`. Use PowerShell `Copy-Item` or Git Bash, not CMD.
