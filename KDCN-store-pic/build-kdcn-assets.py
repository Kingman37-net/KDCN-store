#!/usr/bin/env python3
"""
KDCN STORE ASSET BUILDER
Professional Image Pipeline
Maintainer: KENNEDY KITANGA (KINGMAN KE)
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

BASE = Path(__file__).parent.resolve()

# Source (raw originals)
RAW_FIXED = BASE / "_raw" / "fixed-price"
RAW_DM    = BASE / "_raw" / "dm-quote"

# Normalized source (renamed originals)
SRC_FIXED = BASE / "source" / "fixed-price"
SRC_DM    = BASE / "source" / "dm-quote"

# Web output
WEB_FIXED = BASE / "web" / "fixed-price"
WEB_DM    = BASE / "web" / "dm-quote"

# Social output
SOCIAL_FIXED = BASE / "social" / "fixed-price"
SOCIAL_DM    = BASE / "social" / "dm-quote"

# Reports
CSV    = BASE / "service-catalog.csv"
REPORT = BASE / "conversion-report.txt"

# ============================================================
# SERVICE CATALOG
# Format: (ID, slug, display_name, raw_fixed_filename, raw_dm_filename, pricing)
# ============================================================
SERVICES = [
    ("SVC-001", "business-startup",        "Business Startup",         "business-startup-price.png",      "DM-business_startup.png",        "DM_QUOTE"),
    ("SVC-002", "business-email",          "Business Email",           "business_email_price.png",        "DM-business_email.png",          "DM_QUOTE"),
    ("SVC-003", "business-presence",       "Business Presence",        "business_presence_price.png",     "DM-business-presence.png",       "DM_QUOTE"),
    ("SVC-004", "cross-platform-bundle",   "Cross-Platform Bundle",    "cross_platform_bundle-price.png", "DM-cross_platform_bundle.png",   "DM_QUOTE"),
    ("SVC-005", "cv-cover-letter",         "CV & Cover Letter",        "cv-&-cover-letter-price.png",     "DM-cv_&_cover_letter.png",       "DM_QUOTE"),
    ("SVC-006", "google-business-profile", "Google Business Profile",  "google_my_business_price.png",    "DM-google_my_business.png",      "DM_QUOTE"),
    ("SVC-007", "logo-branding",           "Logo & Branding",          "logo-&-branding-price.jpg",       "DM-logo_&_branding.png",         "DM_QUOTE"),
    ("SVC-008", "online-services",         "Online Services",          "online-services-price.png",       "DM-online_services.png",         "DM_QUOTE"),
    ("SVC-009", "poster-flyer",            "Poster & Flyer Design",    "poster-flyer-price.jpg",          "DM-poster_flyer.png",            "FIXED"),
    ("SVC-010", "premium-brand-tech",      "Premium Brand & Tech",     "premium_brand_tech_price.png",    "DM-premium_brand_tech.png",      "DM_QUOTE"),
    ("SVC-011", "professional-career",     "Professional Career",      "professional-career-price.png",   "DM-professional_career.png",     "DM_QUOTE"),
    ("SVC-012", "social-media-management", "Social Media Management",  "social-media-management-price.jpg","DM-social_media_management.png", "DM_QUOTE"),
    ("SVC-013", "starter-digital-access",  "Starter Digital Access",   "starter_digital_access_price.png","DM-starter_digital_access.png",  "DM_QUOTE"),
    ("SVC-014", "strategy-consultation",   "Strategy Consultation",    "strategy_consultation_price.png", "DM-strategy_consultation.png",   "DM_QUOTE"),
    ("SVC-015", "website-design",          "Website Design",           "website-design-price.jpg",        "DM-website_design.png",          "DM_QUOTE"),
    ("SVC-016", "website-promo",           "Website Promo",            "website_promo_price.png",         "DM-website_promo.png",           "DM_QUOTE"),
]

# Social media sizes (name, width, height)
SOCIAL_SIZES = [
    ("square",    1080, 1080),
    ("story",     1080, 1920),
    ("landscape", 1200, 630),
]

# ============================================================
# HELPERS
# ============================================================

def run(cmd, quiet=False):
    """Run a shell command, return success bool."""
    try:
        result = subprocess.run(
            cmd, shell=True,
            stdout=subprocess.DEVNULL if quiet else None,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.returncode == 0
    except Exception:
        return False

def log(msg):
    print(msg)
    with open(REPORT, "a") as f:
        f.write(msg + "\n")

def check_tools():
    """Verify required tools are installed."""
    missing = []
    for tool in ["cwebp", "avifenc", "magick"]:
        if not shutil.which(tool):
            missing.append(tool)
    if missing:
        print(f"ERROR: Missing tools: {', '.join(missing)}")
        print("Install with: pkg install libwebp libavif imagemagick")
        sys.exit(1)

# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print(" KDCN STORE ASSET BUILDER")
    print("=" * 60)
    print()

    check_tools()

    # Ensure all directories exist
    for d in [SRC_FIXED, SRC_DM, WEB_FIXED, WEB_DM, SOCIAL_FIXED, SOCIAL_DM]:
        d.mkdir(parents=True, exist_ok=True)

    # Reset report
    REPORT.write_text(
        "KDCN STORE ASSET CONVERSION REPORT\n"
        f"Generated: {datetime.now()}\n"
        f"Base: {BASE}\n\n"
    )

    # CSV header
    CSV.write_text(
        "svc_id,slug,name,pricing_type,currency,price,"
        "source_fixed,source_dm,"
        "web_fixed_webp,web_fixed_avif,"
        "web_dm_webp,web_dm_avif,"
        "social_fixed_square,social_fixed_story,social_fixed_landscape,"
        "social_dm_square,social_dm_story,social_dm_landscape\n"
    )

    csv_rows = []

    for svc_id, slug, name, raw_fixed, raw_dm, pricing in SERVICES:
        log(f"─────────────────────────────────────────────")
        log(f"{svc_id} | {name}")
        log(f"─────────────────────────────────────────────")

        fixed_src = RAW_FIXED / raw_fixed
        dm_src    = RAW_DM / raw_dm

        fixed_exists = fixed_src.exists()
        dm_exists    = dm_src.exists()

        if not fixed_exists:
            log(f"  ⚠️  Missing fixed-price source: {raw_fixed}")
        if not dm_exists:
            log(f"  ⚠️  Missing DM source: {raw_dm}")

        # ---------------------------------------------------------
        # 1. Normalize source files
        # ---------------------------------------------------------
        fixed_ext = raw_fixed.split(".")[-1].lower() if fixed_exists else "png"
        dm_ext    = raw_dm.split(".")[-1].lower()    if dm_exists    else "png"

        fixed_target = SRC_FIXED / f"{svc_id}-{slug}.{fixed_ext}"
        dm_target    = SRC_DM    / f"{svc_id}-{slug}.{dm_ext}"

        if fixed_exists:
            shutil.copy2(fixed_src, fixed_target)
            log(f"  ✅ Source: source/fixed-price/{fixed_target.name}")

        if dm_exists:
            shutil.copy2(dm_src, dm_target)
            log(f"  ✅ Source: source/dm-quote/{dm_target.name}")

        # ---------------------------------------------------------
        # 2. Web: WebP + AVIF (max 1200px wide)
        # ---------------------------------------------------------
        web_fixed_webp = web_fixed_avif = ""
        web_dm_webp    = web_dm_avif    = ""

        if fixed_exists:
            web_fixed_webp = f"{svc_id}-{slug}.webp"
            web_fixed_avif = f"{svc_id}-{slug}.avif"

            run(f"magick '{fixed_src}' -resize '1200x1200>' -quality 85 '{WEB_FIXED}/{web_fixed_webp}'", quiet=True)
            run(f"magick '{fixed_src}' -resize '1200x1200>' -quality 65 '{WEB_FIXED}/{web_fixed_avif}'", quiet=True)
            log(f"  🌐 Web: {web_fixed_webp} + {web_fixed_avif}")

        if dm_exists:
            web_dm_webp = f"{svc_id}-{slug}.webp"
            web_dm_avif = f"{svc_id}-{slug}.avif"

            run(f"magick '{dm_src}' -resize '1200x1200>' -quality 85 '{WEB_DM}/{web_dm_webp}'", quiet=True)
            run(f"magick '{dm_src}' -resize '1200x1200>' -quality 65 '{WEB_DM}/{web_dm_avif}'", quiet=True)
            log(f"  🌐 Web: {web_dm_webp} + {web_dm_avif}")

        # ---------------------------------------------------------
        # 3. Social: multi-size variants
        # ---------------------------------------------------------
        social_fixed_names = []
        social_dm_names    = []

        if fixed_exists:
            for size_name, w, h in SOCIAL_SIZES:
                out = f"{svc_id}-{slug}-{size_name}.webp"
                run(
                    f"magick '{fixed_src}' "
                    f"-resize '{w}x{h}^' -gravity center -extent '{w}x{h}' "
                    f"-quality 85 '{SOCIAL_FIXED}/{out}'",
                    quiet=True,
                )
                social_fixed_names.append(out)
            log(f"  📱 Social: {len(social_fixed_names)} variants")

        if dm_exists:
            for size_name, w, h in SOCIAL_SIZES:
                out = f"{svc_id}-{slug}-{size_name}.webp"
                run(
                    f"magick '{dm_src}' "
                    f"-resize '{w}x{h}^' -gravity center -extent '{w}x{h}' "
                    f"-quality 85 '{SOCIAL_DM}/{out}'",
                    quiet=True,
                )
                social_dm_names.append(out)
            log(f"  📱 Social: {len(social_dm_names)} variants")

        # ---------------------------------------------------------
        # 4. Pricing
        # ---------------------------------------------------------
        if pricing == "FIXED":
            price_type = "FIXED"
            price      = "2500"
        else:
            price_type = "DM_QUOTE"
            price      = ""

        # ---------------------------------------------------------
        # 5. CSV row
        # ---------------------------------------------------------
        csv_rows.append([
            svc_id, slug, name, price_type, "KES", price,
            f"source/fixed-price/{fixed_target.name}" if fixed_exists else "",
            f"source/dm-quote/{dm_target.name}"       if dm_exists    else "",
            f"web/fixed-price/{web_fixed_webp}"       if fixed_exists else "",
            f"web/fixed-price/{web_fixed_avif}"       if fixed_exists else "",
            f"web/dm-quote/{web_dm_webp}"             if dm_exists    else "",
            f"web/dm-quote/{web_dm_avif}"             if dm_exists    else "",
            f"social/fixed-price/{svc_id}-{slug}-square.webp"    if fixed_exists else "",
            f"social/fixed-price/{svc_id}-{slug}-story.webp"     if fixed_exists else "",
            f"social/fixed-price/{svc_id}-{slug}-landscape.webp" if fixed_exists else "",
            f"social/dm-quote/{svc_id}-{slug}-square.webp"       if dm_exists    else "",
            f"social/dm-quote/{svc_id}-{slug}-story.webp"        if dm_exists    else "",
            f"social/dm-quote/{svc_id}-{slug}-landscape.webp"    if dm_exists    else "",
        ])

        log("")

    # Write CSV
    with open(CSV, "a") as f:
        for row in csv_rows:
            f.write(",".join(f'"{cell}"' for cell in row) + "\n")

    # Summary
    log("=" * 60)
    log(" BUILD COMPLETE")
    log("=" * 60)
    log(f"  Base:              {BASE}")
    log(f"  Source files:      {SRC_FIXED} + {SRC_DM}")
    log(f"  Web files:         {WEB_FIXED} + {WEB_DM}")
    log(f"  Social files:      {SOCIAL_FIXED} + {SOCIAL_DM}")
    log(f"  Catalog CSV:       {CSV}")
    log(f"  Report:            {REPORT}")
    log("")

    print()
    print("=" * 60)
    print(" BUILD COMPLETE")
    print("=" * 60)
    print()
    print(f"  📁 Source:  {SRC_FIXED}")
    print(f"  🌐 Web:     {WEB_FIXED}")
    print(f"  📱 Social:  {SOCIAL_FIXED}")
    print(f"  📊 Catalog: {CSV}")
    print(f"  📄 Report:  {REPORT}")
    print()

if __name__ == "__main__":
    main()
