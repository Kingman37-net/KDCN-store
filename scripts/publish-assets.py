#!/usr/bin/env python3
"""
KDCN PUBLISH — canonical webp → docs/assets/services/ (slug-named).

Reads:  assets/services/catalog.csv          (svc_id → slug)
        assets/services/web/fixed-price/     (canonical webp)
Writes: docs/assets/services/{slug}.webp

Never edits docs/ content. Only mirrors files.
"""

import csv, shutil
from pathlib import Path

ROOT   = Path(__file__).parent.parent.resolve()
ASSETS = ROOT / "assets" / "services"
DOCS   = ROOT / "docs" / "assets" / "services"
SRC_WEB = ASSETS / "web" / "fixed-price"
CATALOG = ASSETS / "catalog.csv"

def main():
    DOCS.mkdir(parents=True, exist_ok=True)

    with open(CATALOG, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    published, missing = 0, []
    for r in rows:
        svc_id, slug = r["svc_id"], r["slug"]
        src = SRC_WEB / f"{svc_id}-{slug}.webp"
        dst = DOCS / f"{slug}.webp"
        if not src.exists():
            missing.append(src.name)
            continue
        shutil.copy2(src, dst)
        published += 1

    print(f"✅ Published {published} files to {DOCS}")
    if missing:
        print(f"⚠ {len(missing)} canonical files missing:")
        for m in missing:
            print(f"   - {m}")

if __name__ == "__main__":
    main()
