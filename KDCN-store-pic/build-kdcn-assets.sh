#!/data/data/com.termux/files/usr/bin/bash

set -Eeuo pipefail

BASE="/storage/emulated/0/kdcn-store-pic"

DM_DIR="$BASE/DM"
PRICE_DIR="$BASE/services"

SOURCE_FIXED="$BASE/source/fixed-price"
SOURCE_DM="$BASE/source/dm-quote"

WEB_FIXED="$BASE/web/fixed-price"
WEB_DM="$BASE/web/dm-quote"

SOCIAL_FIXED="$BASE/social/fixed-price"
SOCIAL_DM="$BASE/social/dm-quote"

CSV="$BASE/service-catalog.csv"
REPORT="$BASE/conversion-report.txt"

echo "=============================================="
echo " KDCN STORE ASSET BUILDER"
echo "=============================================="
echo
echo "Base: $BASE"
echo

# ------------------------------------------------
# 1. Check required tools
# ------------------------------------------------

for cmd in cwebp avifenc magick; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "ERROR: '$cmd' is not installed."
        echo
        echo "Install required packages with:"
        echo "pkg update"
        echo "pkg install libwebp libavif imagemagick"
        exit 1
    fi
done

# ------------------------------------------------
# 2. Check source folders
# ------------------------------------------------

if [[ ! -d "$DM_DIR" ]]; then
    echo "ERROR: Missing folder:"
    echo "$DM_DIR"
    exit 1
fi

if [[ ! -d "$PRICE_DIR" ]]; then
    echo "ERROR: Missing folder:"
    echo "$PRICE_DIR"
    exit 1
fi

# ------------------------------------------------
# 3. Create production directories
# ------------------------------------------------

mkdir -p \
    "$SOURCE_FIXED" \
    "$SOURCE_DM" \
    "$WEB_FIXED" \
    "$WEB_DM" \
    "$SOCIAL_FIXED" \
    "$SOCIAL_DM"

# ------------------------------------------------
# 4. Backup before processing
# ------------------------------------------------

TIMESTAMP="$(date '+%Y%m%d-%H%M%S')"
BACKUP="$BASE-backup-$TIMESTAMP"

echo "Creating safety backup..."
cp -a "$BASE" "$BACKUP"

echo "Backup created:"
echo "$BACKUP"
echo

# ------------------------------------------------
# 5. Service mapping
# ------------------------------------------------

declare -a SERVICES=(
    "business-startup"
    "business-email"
    "business-presence"
    "cross-platform-bundle"
    "cv-cover-letter"
    "google-business-profile"
    "logo-branding"
    "online-services"
    "poster-flyer"
    "premium-brand-tech"
    "professional-career"
    "social-media-management"
    "starter-digital-access"
    "strategy-consultation"
    "website-design"
    "website-promo"
)

declare -a DISPLAY_NAMES=(
    "Business Startup"
    "Business Email"
    "Business Presence"
    "Cross-Platform Bundle"
    "CV & Cover Letter"
    "Google Business Profile"
    "Logo & Branding"
    "Online Services"
    "Poster & Flyer Design"
    "Premium Brand & Tech"
    "Professional Career"
    "Social Media Management"
    "Starter Digital Access"
    "Strategy Consultation"
    "Website Design"
    "Website Promo"
)

# ------------------------------------------------
# 6. CSV header
# ------------------------------------------------

cat > "$CSV" <<'EOF'
svc_id,slug,name,pricing_type,currency,price,source_fixed,source_dm,web_fixed_webp,web_fixed_avif,web_dm_webp,web_dm_avif
EOF

# ------------------------------------------------
# 7. Report header
# ------------------------------------------------

cat > "$REPORT" <<EOF
KDCN STORE ASSET CONVERSION REPORT
Generated: $(date)
Base: $BASE

Original assets were preserved.
EOF

# ------------------------------------------------
# 8. Find source file helper
# ------------------------------------------------

find_source_file() {
    local directory="$1"
    local slug="$2"

    find "$directory" -maxdepth 1 -type f \
        \( -iname "$slug.png" \
        -o -iname "$slug.jpg" \
        -o -iname "$slug.jpeg" \
        -o -iname "$slug.webp" \
        \) \
        -print -quit
}

# ------------------------------------------------
# 9. Process all 16 services
# ------------------------------------------------

for i in "${!SERVICES[@]}"; do

    NUM=$((i + 1))
    SVC_ID=$(printf "SVC-%03d" "$NUM")

    SLUG="${SERVICES[$i]}"
    NAME="${DISPLAY_NAMES[$i]}"

    echo "----------------------------------------------"
    echo "$SVC_ID | $NAME"
    echo "----------------------------------------------"

    PRICE_SOURCE="$(find_source_file "$PRICE_DIR" "$SLUG" || true)"
    DM_SOURCE="$(find_source_file "$DM_DIR" "DM-$SLUG" || true)"

    # ------------------------------------------------
    # Fixed-price source
    # ------------------------------------------------

    FIXED_SOURCE_NAME=""

    if [[ -n "$PRICE_SOURCE" ]]; then

        EXT="${PRICE_SOURCE##*.}"
        EXT="${EXT,,}"

        FIXED_SOURCE_NAME="$SVC_ID-$SLUG.$EXT"

        cp "$PRICE_SOURCE" \
            "$SOURCE_FIXED/$FIXED_SOURCE_NAME"

        echo "Fixed source: $FIXED_SOURCE_NAME"

        # WebP
        cwebp -quiet -q 85 \
            "$PRICE_SOURCE" \
            -o "$WEB_FIXED/$SVC_ID-$SLUG.webp"

        # AVIF
        avifenc \
            --min 20 \
            --max 35 \
            --speed 6 \
            "$PRICE_SOURCE" \
            "$WEB_FIXED/$SVC_ID-$SLUG.avif" \
            >/dev/null 2>&1

    else

        echo "WARNING: Fixed-price source not found."

    fi

    # ------------------------------------------------
    # DM source
    # ------------------------------------------------

    DM_SOURCE_NAME=""

    if [[ -n "$DM_SOURCE" ]]; then

        EXT="${DM_SOURCE##*.}"
        EXT="${EXT,,}"

        DM_SOURCE_NAME="$SVC_ID-$SLUG.$EXT"

        cp "$DM_SOURCE" \
            "$SOURCE_DM/$DM_SOURCE_NAME"

        echo "DM source: $DM_SOURCE_NAME"

        # WebP
        cwebp -quiet -q 85 \
            "$DM_SOURCE" \
            -o "$WEB_DM/$SVC_ID-$SLUG.webp"

        # AVIF
        avifenc \
            --min 20 \
            --max 35 \
            --speed 6 \
            "$DM_SOURCE" \
            "$WEB_DM/$SVC_ID-$SLUG.avif" \
            >/dev/null 2>&1

    else

        echo "WARNING: DM source not found."

    fi

    # ------------------------------------------------
    # CSV paths
    # ------------------------------------------------

    if [[ -n "$PRICE_SOURCE" ]]; then
        SOURCE_FIXED_CSV="source/fixed-price/$FIXED_SOURCE_NAME"
        WEB_FIXED_WEBP_CSV="web/fixed-price/$SVC_ID-$SLUG.webp"
        WEB_FIXED_AVIF_CSV="web/fixed-price/$SVC_ID-$SLUG.avif"
    else
        SOURCE_FIXED_CSV=""
        WEB_FIXED_WEBP_CSV=""
        WEB_FIXED_AVIF_CSV=""
    fi

    if [[ -n "$DM_SOURCE" ]]; then
        SOURCE_DM_CSV="source/dm-quote/$DM_SOURCE_NAME"
        WEB_DM_WEBP_CSV="web/dm-quote/$SVC_ID-$SLUG.webp"
        WEB_DM_AVIF_CSV="web/dm-quote/$SVC_ID-$SLUG.avif"
    else
        SOURCE_DM_CSV=""
        WEB_DM_WEBP_CSV=""
        WEB_DM_AVIF_CSV=""
    fi

    # ------------------------------------------------
    # Pricing
    # ------------------------------------------------

    if [[ "$SLUG" == "poster-flyer" ]]; then
        PRICING_TYPE="FIXED"
        CURRENCY="KES"
        PRICE="2500"
    else
        PRICING_TYPE="DM_QUOTE"
        CURRENCY="KES"
        PRICE=""
    fi

    printf '"%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s"\n' \
        "$SVC_ID" \
        "$SLUG" \
        "$NAME" \
        "$PRICING_TYPE" \
        "$CURRENCY" \
        "$PRICE" \
        "$SOURCE_FIXED_CSV" \
        "$SOURCE_DM_CSV" \
        "$WEB_FIXED_WEBP_CSV" \
        "$WEB_FIXED_AVIF_CSV" \
        "$WEB_DM_WEBP_CSV" \
        "$WEB_DM_AVIF_CSV" \
        >> "$CSV"

done

# ------------------------------------------------
# 10. Social directories
# ------------------------------------------------
# Social folders are intentionally created but not
# automatically populated. Social graphics may need
# different dimensions/resolution from storefront assets.

# ------------------------------------------------
# 11. Generate report
# ------------------------------------------------

{
    echo
    echo "DIRECTORY SIZES"
    echo "---------------"
    du -sh "$SOURCE_FIXED" 2>/dev/null || true
    du -sh "$SOURCE_DM" 2>/dev/null || true
    du -sh "$WEB_FIXED" 2>/dev/null || true
    du -sh "$WEB_DM" 2>/dev/null || true
    echo
    echo "FILE COUNTS"
    echo "-----------"
    printf "Fixed source: "
    find "$SOURCE_FIXED" -type f | wc -l

    printf "DM source: "
    find "$SOURCE_DM" -type f | wc -l

    printf "Fixed WebP: "
    find "$WEB_FIXED" -type f -name "*.webp" | wc -l

    printf "Fixed AVIF: "
    find "$WEB_FIXED" -type f -name "*.avif" | wc -l

    printf "DM WebP: "
    find "$WEB_DM" -type f -name "*.webp" | wc -l

    printf "DM AVIF: "
    find "$WEB_DM" -type f -name "*.avif" | wc -l
} >> "$REPORT"

# ------------------------------------------------
# 12. Final output
# ------------------------------------------------

echo
echo "=============================================="
echo " BUILD COMPLETE"
echo "=============================================="
echo
echo "Production assets:"
echo "$BASE"
echo
echo "CSV catalog:"
echo "$CSV"
echo
echo "Conversion report:"
echo "$REPORT"
echo
echo "Backup:"
echo "$BACKUP"
echo
echo "Run:"
echo "tree -L 3 \"$BASE\""
echo
