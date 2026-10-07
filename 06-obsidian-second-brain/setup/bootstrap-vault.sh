#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT="${1:-generic}"

cd "$ROOT"

mkdir -p   00-Inbox   01-Daily-Notes   02-People   03-Projects   04-Areas   05-Resources   06-Archive   07-Attachments   08-AI-History   09-Dreams   10-Study   99-MOC   99-System/templates   99-System/skills   Legacy

if [ -d templates ]; then
  cp -R templates/. 99-System/templates/
fi

case "$AGENT" in
  claude)
    [ -f CLAUDE.md ] || cp agent-setup/CLAUDE.md.template CLAUDE.md
    CHARTER="CLAUDE.md"
    ;;
  codex)
    [ -f CODEX.md ] || cp agent-setup/CODEX.md.template CODEX.md
    CHARTER="CODEX.md"
    ;;
  generic|cursor)
    [ -f AGENTS.md ] || cp agent-setup/AGENTS.md.template AGENTS.md
    CHARTER="AGENTS.md"
    ;;
  *)
    echo "Usage: bash setup/bootstrap-vault.sh {claude|codex|generic|cursor}" >&2
    exit 2
    ;;
esac

if [ ! -f 99-System/skills/INDEX.md ]; then
  cat > 99-System/skills/INDEX.md <<'EOF'
# Local skills

Put vault-specific agent skills here.

Good first skills:
- weekly-review
- brain-dump-cleanup
- project-kickoff
- meeting-prep

For a larger reusable skill library:
https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/05-ai-agent-skills
EOF
fi

echo
echo "PASS: vault folders created."
echo "PASS: templates copied to 99-System/templates/."
echo "PASS: agent charter ready at $CHARTER."
echo
echo "NEXT:"
echo "1. Open $CHARTER."
echo "2. Replace every <ANGLE_BRACKET> placeholder."
echo "3. Open this folder as an Obsidian vault."
