#!/usr/bin/env python3
"""
KDCN ASSET BUILDER — pipeline only.
Reads:  assets/services/raw/{fixed-price,dm-quote}/
Writes: assets/services/{source,web,social}/
Emits:  assets/services/asset-manifest.csv
No pricing. Pricing lives in assets/services/catalog.csv.
"""

import shutil, subprocess, sys
from pathlib import Path
from datetime import datetime

BASE = (Path(__file__).parent.parent / "assets" / "services").resolve()
RAW_FIXED   = BASE / "raw" / "fixed-price"
RAW_DM      = BASE / "raw" / "dm-quote"
SRC_FIXED   = BASE / "source" / "fixed-price"
SRC_DM      = BASE / "source" / "dm-quote"
WEB_FIXED   = BASE / "web" / "fixed-price"
WEB_DM      = BASE / "web" / "dm-quote"
SOCIAL_FIXED = BASE / "social" / "fixed-price"
SOCIAL_DM    = BASE / "social" / "dm-quote"
MANIFEST = BASE / "asset-manifest.csv"
REPORT   = (Path(__file__).parent.parent / "report" / "asset-build-report.txt").resolve()

SERVICES = [
    ("SVC-001", "online-cyber-services",        "online-services-price.png",        "DM-online_services.png"),
    ("SVC-002", "poster-flyer-design",          "poster-flyer-price.jpg",           "DM-poster_flyer.png"),
    ("SVC-003", "business-email-setup",         "business_email_price.png",         "DM-business_email.png"),
    ("SVC-004", "cv-cover-letter",              "cv-&-cover-letter-price.png",      "DM-cv_&_cover_letter.png"),
    ("SVC-005", "google-business-profile",      "google_my_business_price.png",     "DM-google_my_business.png"),
    ("SVC-006", "starter-digital-access",       "starter_digital_access_price.png", "DM-starter_digital_access.png"),
    ("SVC-007", "digital-strategy-consultation","strategy_consultation_price.png",  "DM-strategy_consultation.png"),
    ("SVC-008", "professional-career",          "professional-career-price.png",    "DM-professional_career.png"),
    ("SVC-009", "logo-branding",                "logo-&-branding-price.jpg",        "DM-logo_&_branding.png"),
    ("SVC-010", "business-startup",             "business-startup-price.png",       "DM-business_startup.png"),
    ("SVC-011", "social-media-management",      "social-media-management-price.jpg","DM-social_media_management.png"),
    ("SVC-012", "website-design",               "website-design-price.jpg",         "DM-website_design.png"),
    ("SVC-013", "cross-platform-growth",        "cross_platform_bundle-price.png",  "DM-cross_platform_bundle.png"),
    ("SVC-014", "website-launch",               "website_promo_price.png",          "DM-website_promo.png"),
    ("SVC-015", "business-digital-presence",    "business_presence_price.png",      "DM-business-presence.png"),
    ("SVC-016", "premium-brand-tech",           "premium_brand_tech_price.png",     "DM-premium_brand_tech.png"),
]

SOCIAL_SIZES = [("square", 1080, 1080), ("story", 1080, 1920), ("landscape", 1200, 630)]

def run(cmd):
    return subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL,
                          stderr=subprocess.DEVNULL, text=True).returncode == 0

def log(msg):
    print(msg)
    with open(REPORT, "a") as f: f.write(msg + "\n")

def check_tools():
    missing = [t for t in ["magick", "cwebp", "avifenc"] if not shutil.which(t)]
    if missing:
        print(f"ERROR missing tools: {', '.join(missing)}")
        print("pkg install imagemagick libwebp libavif")
        sys.exit(1)

def main():
    print("=" * 60); print(" KDCN ASSET BUILDER (pipeline only)"); print("=" * 60)
    check_tools()
    for d in [SRC_FIXED, SRC_DM, WEB_FIXED, WEB_DM, SOCIAL_FIXED, SOCIAL_DM]:
        d.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(f"KDCN ASSET BUILD REPORT\nGenerated: {datetime.now()}\n\n")

    MANIFEST.write_text(
        "svc_id,slug,"
        "source_fixed,source_dm,"
        "web_fixed_webp,web_fixed_avif,"
        "web_dm_webp,web_dm_avif,"
        "social_fixed_square,social_fixed_story,social_fixed_landscape,"
        "social_dm_square,social_dm_story,social_dm_landscape\n"
    )

    rows = []
    for svc_id, slug, raw_fixed, raw_dm in SERVICES:
        log(f"── {svc_id} | {slug}")
        fixed_src = RAW_FIXED / raw_fixed
        dm_src    = RAW_DM / raw_dm
        fixed_ok, dm_ok = fixed_src.exists(), dm_src.exists()
        if not fixed_ok: log(f"   ⚠ missing fixed: {raw_fixed}")
        if not dm_ok:    log(f"   ⚠ missing dm:    {raw_dm}")

        fixed_ext = raw_fixed.rsplit(".", 1)[-1].lower() if fixed_ok else "png"
        dm_ext    = raw_dm.rsplit(".", 1)[-1].lower()    if dm_ok    else "png"
        fixed_name = f"{svc_id}-{slug}.{fixed_ext}"
        dm_name    = f"{svc_id}-{slug}.{dm_ext}"

        if fixed_ok: shutil.copy2(fixed_src, SRC_FIXED / fixed_name)
        if dm_ok:    shutil.copy2(dm_src,    SRC_DM / dm_name)

        wf_w = wf_a = wd_w = wd_a = ""
        if fixed_ok:
            wf_w, wf_a = f"{svc_id}-{slug}.webp", f"{svc_id}-{slug}.avif"
            run(f"magick '{fixed_src}' -resize '1200x1200>' -quality 85 '{WEB_FIXED}/{wf_w}'")
            run(f"magick '{fixed_src}' -resize '1200x1200>' -quality 65 '{WEB_FIXED}/{wf_a}'")
        if dm_ok:
            wd_w, wd_a = f"{svc_id}-{slug}.webp", f"{svc_id}-{slug}.avif"
            run(f"magick '{dm_src}' -resize '1200x1200>' -quality 85 '{WEB_DM}/{wd_w}'")
            run(f"magick '{dm_src}' -resize '1200x1200>' -quality 65 '{WEB_DM}/{wd_a}'")

        for ok, src, out_dir in [(fixed_ok, fixed_src, SOCIAL_FIXED), (dm_ok, dm_src, SOCIAL_DM)]:
            if not ok: continue
            for name, w, h in SOCIAL_SIZES:
                out = f"{svc_id}-{slug}-{name}.webp"
                run(f"magick '{src}' -resize '{w}x{h}^' -gravity center -extent '{w}x{h}' "
                    f"-quality 85 '{out_dir}/{out}'")

        rows.append([
            svc_id, slug,
            f"source/fixed-price/{fixed_name}" if fixed_ok else "",
            f"source/dm-quote/{dm_name}"       if dm_ok    else "",
            f"web/fixed-price/{wf_w}" if wf_w else "",
            f"web/fixed-price/{wf_a}" if wf_a else "",
            f"web/dm-quote/{wd_w}"    if wd_w else "",
            f"web/dm-quote/{wd_a}"    if wd_a else "",
            f"social/fixed-price/{svc_id}-{slug}-square.webp"    if fixed_ok else "",
            f"social/fixed-price/{svc_id}-{slug}-story.webp"     if fixed_ok else "",
            f"social/fixed-price/{svc_id}-{slug}-landscape.webp" if fixed_ok else "",
            f"social/dm-quote/{svc_id}-{slug}-square.webp"       if dm_ok    else "",
            f"social/dm-quote/{svc_id}-{slug}-story.webp"        if dm_ok    else "",
            f"social/dm-quote/{svc_id}-{slug}-landscape.webp"    if dm_ok    else "",
        ])

    with open(MANIFEST, "a") as f:
        for row in rows:
            f.write(",".join(f'"{c}"' for c in row) + "\n")

    log(""); log("=" * 60); log(" BUILD COMPLETE"); log("=" * 60)
    log(f"  Manifest: {MANIFEST}")

if __name__ == "__main__":
    main()
