# 🛡️ ship-guard (Agent Skill)

Zero-token pre-launch security, secret-leak, and SEO readiness skill for **Claude Code**, **Cursor**, **Cline**, and **OpenClaw**.

Instead of burning thousands of LLM tokens reading files, `ship-guard` runs a fast local Python AST/regex scanner first, then directs your coding agent to patch exposed keys, `.gitignore` gaps, and missing OpenGraph tags automatically.

## ⚡ Quick Install (`/download`)

**Option 1: via Skills CLI (Claude Code, Cursor, Windsurf, OpenClaw)**

```bash
npx skills add harsha-pyla/ship-guard
```

**Option 2: One-liner Bash Install**

```bash
curl -fsSL https://raw.githubusercontent.com/harsha-pyla/ship-guard/main/install.sh | bash
```

## 🚀 Usage

Inside your coding agent terminal or chat, type:

```text
/ship-guard
```
