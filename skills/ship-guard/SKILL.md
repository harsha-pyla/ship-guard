---
name: ship-guard
description: Pre-launch security, secret-leak, and SEO readiness auditor. Trigger when the user types /ship-guard or asks to audit, secure, or prepare a repository for production launch.
---

# Ship-Guard Workflow

When triggered, NEVER guess security or SEO issues by reading random files manually. Follow this exact sequence:

## Step 1: Run Deterministic Audit
Execute the bundled zero-token scanner from the repository root:

```bash
python3 ~/.claude/skills/ship-guard/scripts/audit.py . || python3 .claude/skills/ship-guard/scripts/audit.py . || python skills/ship-guard/scripts/audit.py .
```

## Step 2: Triage & Fix
Read the JSON output from the script and present a clean markdown table of findings:

1. **Critical Secrets (`critical_secrets`):** Immediately offer to move hardcoded keys to `.env.example` and replace code references with environment variables (`process.env` or `os.getenv`).
2. **Config Warnings (`config_warnings`):** Automatically patch `.gitignore` so `.env` files are never committed.
3. **SEO Gaps (`seo_gaps`):** Generate missing OpenGraph (`og:title`, `og:description`, `og:image`) and canonical tags in the main layout file.

## Step 3: Verification
Re-run `audit.py` after applying fixes to confirm zero critical findings remain.
