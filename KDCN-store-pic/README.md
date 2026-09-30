# KDCN Store Assets

Professional image pipeline for KINGMAN DIGITAL CYBER NETWORK.

## Structure

\`\`\`
source/    → original high-quality artwork
web/       → optimized WebP + AVIF for web
social/    → social-media-ready variants
\`\`\`

## Service ID Convention

\`SVC-XXX-slug.ext\` — e.g., \`SVC-001-business-startup.png\`

## Rebuild

\`\`\`bash
python build-kdcn-assets.py
\`\`\`

## Requirements

- \`cwebp\` (libwebp)
- \`avifenc\` (libavif)
- \`magick\` (imagemagick)

Install:
\`\`\`bash
pkg install libwebp libavif imagemagick
\`\`\`
