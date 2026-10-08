#!/usr/bin/env python3
"""
Rewrite KDCN-store image references to CDN + fix old shop.* hostname.
Usage:
  python3 scripts/rewrite-to-cdn.py --dry-run
  python3 scripts/rewrite-to-cdn.py --apply
"""

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CDN = "https://media.kingmandigital.co.ke"
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

# -------- Service images: absolute URL form (og:image/twitter:image) --------
for slug, svc in SVC_MAP:
    MAPPING.append((
        f"https://shop.kingmandigital.co.ke/assets/services/{slug}.webp",
        f"{CDN}/store/services/{svc}/web/display.webp",
    ))

# -------- Service images: relative path form in subpages --------
for slug, svc in SVC_MAP:
    MAPPING.append((
        f'src="../assets/services/{slug}.webp"',
        f'src="{CDN}/store/services/{svc}/web/display.webp"',
    ))

# -------- Service images: services.js form --------
for slug, svc in SVC_MAP:
    MAPPING.append((
        f'"assets/services/{slug}.webp"',
        f'"{CDN}/store/services/{svc}/web/display.webp"',
    ))

# -------- Branding: absolute URL form --------
MAPPING += [
    ("https://shop.kingmandigital.co.ke/assets/branding/kdcn-logo-500.webp",
     f"{CDN}/website/store/logo/kdcn-logo-500.webp"),
    ("https://shop.kingmandigital.co.ke/assets/branding/kdcn-logo.svg",
     f"{CDN}/website/store/logo/kdcn-logo.svg"),
    ("https://shop.kingmandigital.co.ke/assets/branding/kdcn-web-logo-500.webp",
     f"{CDN}/website/store/logo/kdcn-web-logo-500.webp"),
    ("https://shop.kingmandigital.co.ke/assets/branding/kdcn-web-logo.svg",
     f"{CDN}/website/store/logo/kdcn-web-logo.svg"),
]

# -------- Branding: relative paths in root pages --------
MAPPING += [
    ('src="assets/branding/kdcn-logo-500.webp"',
     f'src="{CDN}/website/store/logo/kdcn-logo-500.webp"'),
    ('src="assets/branding/kdcn-web-logo-500.webp"',
     f'src="{CDN}/website/store/logo/kdcn-web-logo-500.webp"'),
    ('href="assets/branding/kdcn-logo-500.webp"',
     f'href="{CDN}/website/store/logo/kdcn-logo-500.webp"'),
    ('href="assets/branding/kdcn-web-logo-500.webp"',
     f'href="{CDN}/website/store/logo/kdcn-web-logo-500.webp"'),
]

# -------- Branding: relative paths in subpages --------
MAPPING += [
    ('src="../assets/branding/kdcn-logo-500.webp"',
     f'src="{CDN}/website/store/logo/kdcn-logo-500.webp"'),
    ('href="../assets/branding/kdcn-logo-500.webp"',
     f'href="{CDN}/website/store/logo/kdcn-logo-500.webp"'),
    ('src="../assets/branding/kdcn-web-logo-500.webp"',
     f'src="{CDN}/website/store/logo/kdcn-web-logo-500.webp"'),
]

# -------- Admin panel --------
MAPPING += [
    ('src="../docs/assets/branding/kdcn-web-logo-500.webp"',
     f'src="{CDN}/website/store/logo/kdcn-web-logo-500.webp"'),
]

# -------- Generic hostname fix (og:url, canonical, anything else) --------
MAPPING.append(("https://shop.kingmandigital.co.ke", NEW_HOST))


def main():
    dry = "--dry-run" in sys.argv
    apply = "--apply" in sys.argv
    if not (dry or apply):
        print("Usage: rewrite-to-cdn.py [--dry-run | --apply]")
        return 1

    targets = sorted(
        list((REPO / "docs").rglob("*.html")) +
        list((REPO / "docs").rglob("*.js")) +
        list((REPO / "admin").rglob("*.html")) +
        list((REPO / "admin").rglob("*.js"))
    )
    print(f"▶ Scanning {len(targets)} files (HTML + JS)")
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
