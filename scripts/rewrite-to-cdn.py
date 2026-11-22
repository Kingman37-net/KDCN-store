#!/usr/bin/env python3
"""
Ensure all KDCN-store assets are local, and fix old shop.* hostname.
Renamed concept: This script now maps CDN -> Local to prevent regressions.
Usage:
  python3 scripts/rewrite-to-cdn.py --dry-run
  python3 scripts/rewrite-to-cdn.py --apply
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
NEW_HOST = "https://store.kingmandigital.co.ke"

SVC_MAP = [
    ("online-cyber-services",        "SVC-001"),
    ("poster-flyer-design",          "SVC-002"),
    ("business-email-setup",         "SVC-003"),
    ("cv-cover-letter",              "SVC-004"),
    ("google-business-profile",      "SVC-005"),
    ("starter-digital-access",       "SVC-006"),
    ("digital-strategy-consultation","SVC-007"),
    ("professional-career",          "SVC-008"),
    ("logo-branding",                "SVC-009"),
    ("business-startup",             "SVC-010"),
    ("social-media-management",      "SVC-011"),
    ("website-design",               "SVC-012"),
    ("cross-platform-growth",        "SVC-013"),
    ("website-launch",               "SVC-014"),
    ("business-digital-presence",    "SVC-015"),
    ("premium-brand-tech",           "SVC-016"),
]

MAPPING = []

# -------- Service images: CDN -> Local absolute path --------
for slug, svc in SVC_MAP:
    MAPPING.append((
        f"https://media.kingmandigital.co.ke/store/services/{svc}/web/display.webp",
        f"/assets/services/{slug}.webp",
    ))
    # Catch any relative paths and force absolute
    MAPPING.append((
        f"assets/services/{slug}.webp",
        f"/assets/services/{slug}.webp",
    ))

# -------- Branding: CDN -> Local --------
MAPPING += [
    ("https://media.kingmandigital.co.ke/website/store/logo/kdcn-logo-500.webp", "/assets/images/logo.webp"),
    ("https://media.kingmandigital.co.ke/website/store/logo/kdcn-logo.svg", "/assets/images/logo.webp"),
    ("https://media.kingmandigital.co.ke/website/store/logo/kdcn-web-logo-500.webp", "/assets/images/logo.webp"),
    ("https://media.kingmandigital.co.ke/website/store/logo/kdcn-web-logo.svg", "/assets/images/logo.webp"),
]

# -------- Generic hostname fix (og:url, canonical) --------
MAPPING.append(("https://shop.kingmandigital.co.ke", NEW_HOST))


def main():
    dry = "--dry-run" in sys.argv
    apply = "--apply" in sys.argv
    if not (dry or apply):
        print("Usage: rewrite-to-cdn.py [--dry-run | --apply]")
        return 1

    targets = sorted(
        list((REPO / "docs").rglob("*.html")) +
        list((REPO / "docs").rglob("*.js"))
    )
    print(f"▶ Scanning {len(targets)} files to ensure local assets")
    print()

    total = 0
    per_file = {}

    for path in targets:
        original = path.read_text(encoding="utf-8")
        content = original
        hits = 0
        for old, new in MAPPING:
            c = content.count(old)
            if c:
                content = content.replace(old, new)
                hits += c
        if hits:
            per_file[path] = hits
            total += hits
            rel = path.relative_to(REPO)
            print(f"  {hits:>3}  {rel}")
            if apply:
                path.write_text(content, encoding="utf-8")

    print()
    print(f"▶ Files changed:      {len(per_file)}")
    print(f"▶ Total replacements: {total}")
    print()
    print("✅ Dry run — no files written" if dry else "✅ Changes applied")
    return 0

if __name__ == "__main__":
    sys.exit(main())
