#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
AGENT="${1:-generic}"

cd "$ROOT"

mkdir -p \
  00-Inbox \
  01-Daily-Notes \
  02-People \
  03-Projects \
  04-Areas \
  05-Resources \
  06-Archive \
  07-Attachments \
  08-AI-History \
  09-Dreams \
  10-Study \
  99-MOC \
  99-System/templates \
  99-System/skills \
  99-System/companion \
  Legacy

if [ -d templates ]; then
  cp -R templates/. 99-System/templates/
fi

case "$AGENT" in
  claude)
    [ -f CLAUDE.md ] || cp vault-agent/templates/CLAUDE.md.template CLAUDE.md
    CHARTER="CLAUDE.md"
    ;;
  codex|generic|cursor)
    [ -f AGENTS.md ] || cp vault-agent/templates/AGENTS.md.template AGENTS.md
    CHARTER="AGENTS.md"
    ;;
  *)
    echo "Usage: bash vault-agent/scripts/bootstrap-vault.sh {claude|codex|generic|cursor}" >&2
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

Reusable public skills:
https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/05-ai-agent-skills
EOF
fi

for file in ABOUT-ME.md CURRENT-SEASON.md PROJECTS.md COMPANION-RULES.md; do
  if [ ! -f "99-System/companion/$file" ]; then
    name="${file%.md}"
    printf "# %s\n\n[FILL THIS IN]\n" "$name" > "99-System/companion/$file"
  fi
done

echo
echo "PASS: vault folders created."
echo "PASS: templates copied to 99-System/templates/."
echo "PASS: companion context folder created."
echo "PASS: Vault Agent charter ready at $CHARTER."
echo
echo "NEXT:"
echo "1. Open $CHARTER."
echo "2. Fill any placeholders you want to customize."
echo "3. Open start-here/README.md and continue at the Vault Agent validation step."
