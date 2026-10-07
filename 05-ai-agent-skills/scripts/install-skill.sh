#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT="${1:-}"
ITEM="${2:-}"

usage() {
  cat <<'EOF'
Usage:
  bash scripts/install-skill.sh claude humanizer
  bash scripts/install-skill.sh codex builder-pack
  bash scripts/install-skill.sh copilot writing-pack
  bash scripts/install-skill.sh cursor second-brain-pack

Agents:
  claude  -> ~/.claude/skills
  codex   -> ~/.codex/skills
  copilot -> ~/.copilot/skills
  cursor  -> ./.cursor/skills

Packs:
  writing-pack
  builder-pack
  second-brain-pack
EOF
}

[ -n "$AGENT" ] && [ -n "$ITEM" ] || { usage; exit 2; }

case "$AGENT" in
  claude) DEST="$HOME/.claude/skills" ;;
  codex) DEST="$HOME/.codex/skills" ;;
  copilot) DEST="$HOME/.copilot/skills" ;;
  cursor) DEST="$PWD/.cursor/skills" ;;
  *) usage; exit 2 ;;
esac

skills_for_item() {
  case "$1" in
    writing-pack)
      printf '%s
' humanizer article-writing brand-voice docs-readability-audit
      ;;
    builder-pack)
      printf '%s
' repo-onboarding-audit builder-walkthrough web-ui-audit prompt-optimizer
      ;;
    second-brain-pack)
      printf '%s
' obsidian companion-context file-organizer docs-readability-audit
      ;;
    *)
      printf '%s
' "$1"
      ;;
  esac
}

mkdir -p "$DEST"

while IFS= read -r skill; do
  src="$ROOT/skills/$skill"
  dst="$DEST/$skill"

  if [ ! -f "$src/SKILL.md" ]; then
    echo "STOP: skill not found: $skill" >&2
    exit 3
  fi

  if [ -e "$dst" ]; then
    echo "STOP: $dst already exists. Review or remove it before reinstalling." >&2
    exit 4
  fi

  cp -R "$src" "$dst"
  echo "INSTALLED: $skill -> $dst"
done < <(skills_for_item "$ITEM")

echo
echo "PASS: install complete."
echo "Start a new agent session before testing skill discovery."
