#!/usr/bin/env python3
import os
import re
import json
import sys

SECRET_PATTERNS = {
    "Stripe Live Key": r"sk_live_[0-9a-zA-Z]{24,}",
    "OpenAI API Key": r"sk-[a-zA-Z0-9]{20}T3BlbkFJ[a-zA-Z0-9]{20}|sk-proj-[a-zA-Z0-9_-]{40,}",
    "AWS Access Key": r"AKIA[0-9A-Z]{16}",
    "Generic Private Key": r"-----BEGIN (RSA|EC|OPENSSH) PRIVATE KEY-----"
}

IGNORE_DIRS = {".git", "node_modules", ".next", "dist", "build", "__pycache__", ".venv"}


def scan_repo(root="."):
    report = {"critical_secrets": [], "config_warnings": [], "seo_gaps": []}

    # 1. Check .gitignore for .env
    gitignore_path = os.path.join(root, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", errors="ignore") as f:
            if ".env" not in f.read():
                report["config_warnings"].append(".gitignore is missing '.env' entry")
    else:
        report["config_warnings"].append("Missing .gitignore file in project root")

    # 2. Walk files for secrets and SEO tags
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for fname in filenames:
            fpath = os.path.join(dirpath, fname)
            if fname.endswith((".py", ".js", ".ts", ".tsx", ".jsx", ".env", ".json", ".html")):
                try:
                    with open(fpath, "r", errors="ignore") as f:
                        content = f.read()

                    for label, pattern in SECRET_PATTERNS.items():
                        for match in re.finditer(pattern, content):
                            line_no = content[:match.start()].count("\n") + 1
                            report["critical_secrets"].append(f"{fpath}:{line_no} -> {label}")

                    if fname in ("index.html", "layout.tsx", "layout.jsx"):
                        if "og:title" not in content and "openGraph" not in content:
                            report["seo_gaps"].append(f"{fpath} -> Missing OpenGraph (og:title) metadata")
                except Exception:
                    pass

    return report


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    print(json.dumps(scan_repo(target), indent=2))
