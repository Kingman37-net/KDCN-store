#!/usr/bin/env python3
"""
KDCN Store — Service Detail Page Generator
Reads services.js and generates 16 individual service pages.
"""

import os
import re
import json

# Paths
SERVICES_JS = "js/services.js"
OUTPUT_DIR = "services"
USD_RATE = 130

# Service slug → filename mapping (matches services.js IDs)
SERVICE_IDS = [
    "online-cyber-services",
    "poster-flyer-design",
    "business-email-setup",
    "cv-cover-letter",
    "google-business-profile",
    "starter-digital-access",
    "digital-strategy-consultation",
    "professional-career",
    "logo-branding",
    "business-startup",
    "social-media-management",
    "website-design",
    "cross-platform-growth",
    "website-launch",
    "business-digital-presence",
    "premium-brand-tech",
]

# Note: services.js has "google-my-business" and "website-promo" as IDs
# but the requested filenames are different — we'll map them.
ID_TO_FILE = {
    "google-my-business": "google-business-profile",
    "website-promo": "website-launch",
}

TIER_META = {
    "essential":     {"name": "Essential Digital Services",     "icon": "🟢", "color": "#22c55e"},
    "professional":  {"name": "Professional Digital Services",  "icon": "🟡", "color": "#fbbf24"},
    "business":      {"name": "Business & Growth Solutions",    "icon": "🔵", "color": "#00d1ff"},
    "advanced":      {"name": "Advanced Digital Solutions",     "icon": "🟣", "color": "#a855f7"},
}

def parse_services_js():
    """Parse the KDCN_SERVICES array from services.js"""
    with open(SERVICES_JS, "r", encoding="utf-8") as f:
        content = f.read()

    # Find all service objects
    services = []
    # Match from `{ id:` up to the closing `}` of each object
    pattern = re.compile(r'\{\s*\n\s*id:\s*"([^"]+)",.*?\n\s*\}', re.DOTALL)
    for match in pattern.finditer(content):
        block = match.group(0)
        svc = {}

        def get_field(field, pattern=r'([^"]+)'):
            m = re.search(rf'{field}:\s*"{pattern}"', block)
            return m.group(1) if m else ""

        def get_array(field):
            m = re.search(rf'{field}:\s*\[(.*?)\]', block, re.DOTALL)
            if not m:
                return []
            items = re.findall(r'"([^"]+)"', m.group(1))
            return items

        svc["id"] = get_field("id")
        svc["code"] = get_field("code")
        svc["tier"] = get_field("tier")
        svc["name"] = get_field("name")
        svc["tagline"] = get_field("tagline")
        svc["fee"] = get_field("fee")
        svc["feeMin"] = int(re.search(r'feeMin:\s*(\d+)', block).group(1)) if re.search(r'feeMin:\s*(\d+)', block) else 0
        svc["idealFor"] = get_field("idealFor")
        svc["objective"] = get_field("objective")
        svc["includes"] = get_array("includes")
        svc["image"] = get_field("image")
        svc["whatsapp"] = get_field("whatsapp")
        svc["badge"] = get_field("badge") or ""

        services.append(svc)

    return services

def build_page(svc):
    tier = TIER_META.get(svc["tier"], {"name": "Service", "icon": "⚪", "color": "#888"})
    usd = round(svc["feeMin"] / USD_RATE)
    file_id = ID_TO_FILE.get(svc["id"], svc["id"])
    canonical = f"https://shop.kingmandigital.co.ke/services/{file_id}.html"

    includes_html = "\n".join(f'            <li>{item}</li>' for item in svc["includes"])

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{svc["name"]} | KDCN Store</title>
  <meta name="description" content="{svc["objective"]}">
  <meta name="author" content="Kingman Digital Cyber Network">
  <meta name="theme-color" content="#0a0f14">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">

  <meta property="og:type" content="website">
  <meta property="og:title" content="{svc["name"]} | KDCN Store">
  <meta property="og:description" content="{svc["objective"]}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="https://shop.kingmandigital.co.ke/{svc["image"]}">
  <meta property="og:site_name" content="KDCN Store">
  <meta property="og:locale" content="en_KE">

  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{svc["name"]} | KDCN Store">
  <meta name="twitter:description" content="{svc["objective"]}">
  <meta name="twitter:image" content="https://shop.kingmandigital.co.ke/{svc["image"]}">
  <meta name="twitter:site" content="@KDCN_OFFICIAL">

  <link rel="icon" href="../assets/branding/kdcn-logo-500.webp" type="image/webp">
  <link rel="stylesheet" href="../css/style.css">
</head>
<body>

  <nav class="site-nav" id="site-nav">
    <div class="nav-container">
      <a href="../index.html" class="brand" aria-label="KDCN Store Home">
        <img src="../assets/branding/kdcn-web-logo-500.webp" alt="KDCN Store" class="brand-logo" width="40" height="40">
        <span class="brand-text">KDCN Store</span>
      </a>
      <ul class="nav-menu" id="nav-menu">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../index.html#essential">Essential</a></li>
        <li><a href="../index.html#professional">Professional</a></li>
        <li><a href="../index.html#business">Business</a></li>
        <li><a href="../index.html#advanced">Advanced</a></li>
        <li><a href="../faq.html">FAQ</a></li>
      </ul>
      <div class="nav-actions">
        <button class="theme-toggle" id="theme-toggle" type="button" aria-label="Toggle theme">🌙</button>
        <a href="https://wa.me/254111843716?text={svc["whatsapp"]}" class="btn btn-whatsapp-nav" target="_blank" rel="noopener">💬 WhatsApp</a>
        <button class="hamburger" id="hamburger" type="button" aria-label="Menu" aria-expanded="false">
          <span class="bar"></span><span class="bar"></span><span class="bar"></span>
        </button>
      </div>
    </div>
  </nav>

  <header class="service-hero">
    <a href="../index.html" class="back-link">← Back to All Services</a>
    <div>
      <span class="service-tier-badge" style="background: {tier["color"]}20; color: {tier["color"]}; border: 1px solid {tier["color"]}40;">
        {tier["icon"]} {tier["name"]}
      </span>
    </div>
    <h1>{svc["name"]}</h1>
    <p class="service-tagline">{svc["tagline"]}</p>
    <span class="service-code">Service Code: {svc["code"]}</span>
  </header>

  <main class="service-detail">
    <div class="service-detail-grid">

      <div class="service-detail-content">
        <div class="service-detail-image">
          <img src="../{svc["image"]}" alt="{svc["name"]}" loading="eager" decoding="async">
        </div>

        <h2>About This Service</h2>
        <p>{svc["objective"]}</p>

        <h2>What's Included</h2>
        <ul class="service-includes">
{includes_html}
        </ul>

        <h2>Who This Is For</h2>
        <p>{svc["idealFor"]}</p>

        <h2>How It Works</h2>
        <p>Reach out to KDCN via WhatsApp with your project details. We'll confirm scope, timeline, and any specific requirements. Once agreed, we'll proceed with delivery and keep you updated throughout the process.</p>

      </div>

      <aside class="service-sidebar">
        <span class="sidebar-label">Service Fee</span>
        <span class="sidebar-price">{svc["fee"]}</span>
        <span class="sidebar-usd">≈ ${usd} USD</span>

        <div class="sidebar-info">
          <div>
            <strong>Service Code</strong>
            <span>{svc["code"]}</span>
          </div>
          <div>
            <strong>Ideal For</strong>
            <span>{svc["idealFor"]}</span>
          </div>
        </div>

        <a href="https://wa.me/254111843716?text={svc["whatsapp"]}"
           class="btn btn-primary" target="_blank" rel="noopener">
          💬 Inquire on WhatsApp
        </a>
        <a href="mailto:info@kingmandigital.co.ke?subject=Inquiry: {svc["name"]}"
           class="btn btn-secondary">
          ✉️ Email Inquiry
        </a>
      </aside>

    </div>
  </main>

  <footer class="site-footer">
    <div class="footer-container">
      <div class="footer-top">
        <div class="footer-column">
          <h4>Services</h4>
          <a href="../index.html#essential">Essential Digital Services</a>
          <a href="../index.html#professional">Professional Digital Services</a>
          <a href="../index.html#business">Business &amp; Growth Solutions</a>
          <a href="../index.html#advanced">Advanced Digital Solutions</a>
        </div>
        <div class="footer-column">
          <h4>KDCN</h4>
          <a href="https://www.kingmandigital.co.ke" target="_blank" rel="noopener">Main Website</a>
          <a href="https://cto.kingmandigital.co.ke" target="_blank" rel="noopener">Leadership</a>
          <a href="../faq.html">FAQ</a>
          <a href="../terms.html">Terms of Service</a>
          <a href="../privacy.html">Privacy Policy</a>
          <a href="../cookies.html">Cookie Policy</a>
        </div>
        <div class="footer-column">
          <h4>Connect</h4>
          <a href="mailto:info@kingmandigital.co.ke">✉️ Email</a>
          <a href="https://wa.me/254111843716" target="_blank" rel="noopener">💬 WhatsApp</a>
          <a href="tel:+254111843716">📞 Phone</a>
        </div>
      </div>
      <hr class="footer-divider">
      <div class="footer-bottom">
        <div class="footer-identity">
          <img src="../assets/branding/kdcn-logo-500.webp" alt="KDCN" class="footer-logo" width="48" height="48">
          <h3>KDCN STORE</h3>
          <p>Powered by Kingman Digital</p>
          <p class="footer-motto">"No data left unguarded. No system left unsafe."</p>
          <p class="footer-location">📍 Manyatta, Embu, Kenya 🇰🇪</p>
        </div>
        <div class="footer-legal">
          <p>© 2026 KINGMAN DIGITAL</p>
          <span>Shop Subdomain — Secure Commerce</span>
        </div>
      </div>
    </div>
  </footer>

  <script src="../js/app.js"></script>
</body>
</html>
'''

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("📖 Parsing services.js...")
    services = parse_services_js()
    print(f"   Found {len(services)} services")

    print("\n🔧 Generating service pages...")
    count = 0
    for svc in services:
        file_id = ID_TO_FILE.get(svc["id"], svc["id"])
        filename = f"{file_id}.html"
        path = os.path.join(OUTPUT_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(build_page(svc))

        print(f"   ✅ {filename}")
        count += 1

    print(f"\n🎯 Generated {count} service pages in {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
