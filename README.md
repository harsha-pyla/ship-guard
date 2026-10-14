<div align="center">

# 🛡️ ship-guard

**Zero-Token Pre-Launch Security, Secret-Leak & SEO Readiness Skill for AI Coding Agents**

[![GitHub Stars](https://img.shields.io/github/stars/harsha-pyla/ship-guard?style=for-the-badge&logo=github&color=yellow)](https://github.com/harsha-pyla/ship-guard/stargazers)
[![Agent Skill Standard](https://img.shields.io/badge/Skill_Spec-SKILL.md-blue?style=for-the-badge)](https://skills.sh)
[![Zero Token Scanner](https://img.shields.io/badge/Scanner-Zero_LLM_Tokens-success?style=for-the-badge)](#-why-deterministic--prompt-only-skills)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

<p align="center">
  Works seamlessly with <b>Claude Code</b> • <b>Cursor</b> • <b>Cline</b> • <b>Windsurf</b> • <b>OpenClaw</b>
</p>

[⚡ Quick Install](#-quick-install-download) • [🎬 Terminal Demo](#-what-it-looks-like-in-action) • [🔍 What It Catches](#-what-it-catches) • [🧠 Why Zero-Token?](#-why-deterministic--prompt-only-skills)

</div>

---

## 🚨 The Problem

Vibe-coding a micro-SaaS or web app is fast—until you accidentally push a live Stripe key to GitHub, forget `.env` in your `.gitignore`, or launch on Product Hunt/X with broken OpenGraph previews.

Asking an AI agent to *"check my repo for security and SEO issues"* forces the LLM to read dozens of files manually, **burning 25,000+ tokens** while still missing regex patterns.

## 💡 The Solution: `ship-guard`

`ship-guard` combines a strict `SKILL.md` workflow with a **deterministic local Python scanner (`audit.py`)**. 
1. It scans your entire codebase locally in **<150ms** using **0 LLM tokens**.
2. It feeds a compact JSON report of exact `file:line` vulnerabilities to your coding agent.
3. Your agent automatically patches `.gitignore`, moves hardcoded secrets to `.env`, and injects missing OpenGraph metadata.

---

## ⚡ Quick Install (`/download`)

### Option 1: Via Skills CLI *(Recommended for Claude Code, Cursor, Windsurf, OpenClaw)*
```bash
npx skills add harsha-pyla/ship-guard
```

### Option 2: One-Liner Bash Installer (Direct to ~/.claude/skills)
```bash
curl -fsSL https://raw.githubusercontent.com/harsha-pyla/ship-guard/main/install.sh | bash
```

### Option 3: Project-Local Install (For team repositories)
```bash
mkdir -p .claude/skills/ship-guard/scripts && \
curl -fsSL https://raw.githubusercontent.com/harsha-pyla/ship-guard/main/skills/ship-guard/SKILL.md -o .claude/skills/ship-guard/SKILL.md && \
curl -fsSL https://raw.githubusercontent.com/harsha-pyla/ship-guard/main/skills/ship-guard/scripts/audit.py -o .claude/skills/ship-guard/scripts/audit.py
```

---

## 🎬 What It Looks Like In Action

Open your coding agent terminal or chat and run `/ship-guard`:

```text
> /ship-guard

⏺ Running local deterministic scanner: python3 ~/.claude/skills/ship-guard/scripts/audit.py .
  ⎿  Scan completed in 42ms (0 LLM tokens used for file traversal)

🛡️ Ship-Guard Pre-Launch Audit Report:
┌────────────────────┬──────────────────────────────┬────────────────────────────────────────────┐
│ Severity           │ Location                     │ Finding                                    │
├────────────────────┼──────────────────────────────┼────────────────────────────────────────────┤
│ 🔴 CRITICAL SECRET │ src/lib/stripe.ts:14         │ Exposed Stripe Live Key (sk_live_...)      │
│ 🟠 CONFIG WARNING  │ .gitignore                   │ Missing '.env' entry in .gitignore         │
│ 🟡 SEO GAP         │ src/app/layout.tsx           │ Missing OpenGraph (og:title, og:image)     │
└────────────────────┴──────────────────────────────┴────────────────────────────────────────────┘

🔧 Applying automated fixes...
  ✔ Added `.env` and `.env.*` to `.gitignore`
  ✔ Extracted Stripe key in `src/lib/stripe.ts:14` -> `process.env.STRIPE_SECRET_KEY`
  ✔ Added OpenGraph metadata block to `src/app/layout.tsx`
  ✔ Re-ran `audit.py` -> 0 critical issues remaining. Ready to ship! 🚀
```

---

## 🔍 What It Catches

| Category | Checks Performed Locally (`audit.py`) | Automated Agent Fix (`SKILL.md`) |
| :--- | :--- | :--- |
| **🔑 Hardcoded Secrets** | Stripe Live Keys (`sk_live_`), OpenAI Keys (`sk-proj-`), AWS Access Keys (`AKIA...`), RSA/SSH Private Keys | Moves keys to `.env.example` & replaces strings with `process.env` / `os.getenv` |
| **🛡️ Git Hygiene** | Verifies `.gitignore` exists and explicitly blocks `.env` files | Creates or patches `.gitignore` before `git push` |
| **📈 Launch SEO** | Scans `index.html`, `layout.tsx`, and `layout.jsx` for OpenGraph tags | Generates clean `og:title`, `og:description`, and `og:image` tags |

---

## 🧠 Why Deterministic > Prompt-Only Skills

| Metric | Standard Prompt ("Audit my repo") | ship-guard (`SKILL.md` + `audit.py`) |
| :--- | :--- | :--- |
| **Token Cost per Run** | ~15,000 – 40,000 tokens | **~350 tokens** (JSON output only) |
| **Scan Speed** | 20 – 45 seconds | **< 0.1 seconds** |
| **False Negatives** | High (skips files to save context) | **Zero** (walks 100% of non-ignored files) |
| **Works Offline** | ❌ No | **✅ Scanner runs 100% locally** |

---

## 📂 Repository Architecture

```text
ship-guard/
├── skills/
│   └── ship-guard/
│       ├── SKILL.md            # Agent routing rules & remediation workflow
│       └── scripts/
│           └── audit.py        # Zero-dependency Python secret & SEO scanner
├── install.sh                  # One-line curl installer for ~/.claude/skills
└── README.md                   # Documentation
```

---

## 🛠️ Standalone CLI Usage (Without an AI Agent)

You can also run the scanner directly in any CI/CD pipeline or terminal:

```bash
python3 ~/.claude/skills/ship-guard/scripts/audit.py /path/to/your/project
```

---

## 🤝 Contributing

Want to add more secret regex patterns (Supabase, Firebase, Clerk, Resend) or framework SEO checks (Astro, Nuxt, SvelteKit)?

1. Fork the repository
2. Add your pattern to `skills/ship-guard/scripts/audit.py`
3. Submit a Pull Request!
