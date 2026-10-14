#!/usr/bin/env bash
set -e

DEST="${HOME}/.claude/skills/ship-guard"
mkdir -p "$DEST/scripts"

REPO_URL="https://raw.githubusercontent.com/harsha-pyla/ship-guard/main/skills/ship-guard"

curl -fsSL "$REPO_URL/SKILL.md" -o "$DEST/SKILL.md"
curl -fsSL "$REPO_URL/scripts/audit.py" -o "$DEST/scripts/audit.py"
chmod +x "$DEST/scripts/audit.py"

echo "✅ ship-guard installed! Type /ship-guard inside Claude Code or Cursor to run."
