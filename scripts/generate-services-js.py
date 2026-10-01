#!/usr/bin/env python3
"""
KDCN — regenerate docs/js/services.js from catalog.csv + tiers.csv.
The services.js file is a GENERATED artifact. Do not edit by hand.
"""

import csv
from pathlib import Path

ROOT     = Path(__file__).parent.parent.resolve()
CATALOG  = ROOT / "assets" / "services" / "catalog.csv"
TIERS    = ROOT / "assets" / "services" / "tiers.csv"
OUT      = ROOT / "docs" / "js" / "services.js"

def esc(s):
    return str(s).replace("\\", "\\\\").replace('"', '\\"')

def main():
    with open(TIERS, newline="", encoding="utf-8") as f:
        tiers = list(csv.DictReader(f))
    with open(CATALOG, newline="", encoding="utf-8") as f:
        services = list(csv.DictReader(f))

    lines = []
    lines.append("/* =========================================================")
    lines.append("   KDCN SERVICE CATALOGUE — AUTO-GENERATED")
    lines.append("   Source of truth: assets/services/catalog.csv")
    lines.append("   Regenerate:      python scripts/generate-services-js.py")
    lines.append("   DO NOT EDIT BY HAND.")
    lines.append("   ========================================================= */")
    lines.append("")
    lines.append("const KDCN_TIERS = [")
    for t in tiers:
        lines.append("  {")
        lines.append(f'    id: "{esc(t["id"])}",')
        lines.append(f'    name: "{esc(t["name"])}",')
        lines.append(f'    icon: "{esc(t["icon"])}",')
        lines.append(f'    tagline: "{esc(t["tagline"])}",')
        lines.append(f'    description: "{esc(t["description"])}",')
        lines.append(f'    idealFor: "{esc(t["ideal_for"])}",')
        lines.append(f'    priceRange: "{esc(t["price_range"])}",')
        lines.append(f'    color: "{esc(t["color"])}"')
        lines.append("  },")
    lines.append("];")
    lines.append("")
    lines.append("const KDCN_SERVICES = [")
    for r in services:
        includes = [i for i in r["includes"].split("|") if i.strip()]
        lines.append("  {")
        lines.append(f'    id: "{esc(r["slug"])}",')
        lines.append(f'    code: "{esc(r["code"])}",')
        lines.append(f'    tier: "{esc(r["tier"])}",')
        lines.append(f'    name: "{esc(r["name"])}",')
        lines.append(f'    tagline: "{esc(r["tagline"])}",')
        lines.append(f'    fee: "{esc(r["price_display"])}",')
        lines.append(f'    feeMin: {int(r["price_min"]) if r["price_min"] else 0},')
        lines.append(f'    pricingType: "{esc(r["pricing_type"])}",')
        lines.append(f'    idealFor: "{esc(r["ideal_for"])}",')
        lines.append(f'    objective: "{esc(r["objective"])}",')
        lines.append("    includes: [")
        for inc in includes:
            lines.append(f'      "{esc(inc)}",')
        if includes:
            lines[-1] = lines[-1].rstrip(",")
        lines.append("    ],")
        lines.append(f'    image: "{esc(r["image"])}",')
        lines.append(f'    whatsapp: "{esc(r["whatsapp"])}"')
        if r["badge"]:
            lines[-1] += ","
            lines.append(f'    badge: "{esc(r["badge"])}"')
        lines.append("  },")
    lines.append("];")
    lines.append("")
    lines.append("/* -------- helpers -------- */")
    lines.append("function getServiceById(id) { return KDCN_SERVICES.find(s => s.id === id); }")
    lines.append("function getServicesByTier(tier) { return KDCN_SERVICES.filter(s => s.tier === tier); }")
    lines.append("function getAllServices() { return KDCN_SERVICES; }")
    lines.append("function getTierById(id) { return KDCN_TIERS.find(t => t.id === id); }")
    lines.append("")
    lines.append("if (typeof module !== 'undefined' && module.exports) {")
    lines.append("  module.exports = { KDCN_SERVICES, KDCN_TIERS, getServiceById, getServicesByTier, getAllServices, getTierById };")
    lines.append("}")
    lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"✅ {OUT} ({len(services)} services, {len(tiers)} tiers)")

if __name__ == "__main__":
    main()
