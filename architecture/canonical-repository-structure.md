KDCN STORE — CANONICAL REPOSITORY STRUCTURE

System: KDCN Commerce
Version: 1.0
Status: "AUTHORITATIVE"

---

1. ROOT STRUCTURE

KDCN-store/
│
├── CNAME
├── README.md
│
├── architecture/
│
├── KDCN-store-pic/
│
├── assets/
│
├── frontend/
│
├── admin/
│
├── backend/
│
├── database/
│
├── docs/
│
├── scripts/
│
├── tests/
│
├── package.json
├── tsconfig.json
└── wrangler.jsonc

---

2. ROOT RESPONSIBILITY MAP

architecture/
    ↓
Defines how the system works.

KDCN-store-pic/
    ↓
Produces marketing/service assets.

assets/
    ↓
Stores canonical/master application assets.

frontend/
    ↓
Contains storefront source/application code.

docs/
    ↓
Contains the GitHub Pages public deployment.

admin/
    ↓
Contains internal administration application.

backend/
    ↓
Contains API and business logic.

database/
    ↓
Contains schema, migrations and database tooling.

scripts/
    ↓
Contains automation/build utilities.

tests/
    ↓
Contains verification and quality assurance.

---

3. "architecture/"

This is the system's documentation authority.

architecture/
├── README.md
├── document-index.md
├── system-overview.md
├── commerce-model.md
├── service-catalog.md
├── order-lifecycle.md
├── quote-lifecycle.md
├── payment-lifecycle.md
├── admin-model.md
└── kdcn-store-blueprint.md

Rule:

Architecture decides what the system is supposed to do.

---

4. "KDCN-store-pic/"

This remains the asset-production pipeline.

KDCN-store-pic/
├── README.md
├── service-catalog.csv
│
├── source/
│   ├── fixed-price/
│   └── dm-quote/
│
├── _raw/
│   ├── fixed-price/
│   └── dm-quote/
│
├── web/
│   ├── fixed-price/
│   └── dm-quote/
│
├── social/
│   ├── fixed-price/
│   └── dm-quote/
│
├── fixed-price/
├── dm-quote/
│
├── build-kdcn-assets.py
├── build-kdcn-assets.sh
└── conversion-report.txt

Its responsibility is:

SOURCE
  ↓
GENERATE
  ↓
VALIDATE
  ↓
PUBLISH

It does not own the runtime commerce system.

---

5. "assets/"

This becomes the canonical application asset library.

Target:

assets/
├── README.md
│
├── branding/
│   ├── kdcn-logo.svg
│   ├── kdcn-logo.webp
│   ├── kdcn-web-logo.svg
│   └── kdcn-web-logo.webp
│
├── services/
│   ├── business-digital-presence/
│   ├── business-email-setup/
│   ├── business-startup/
│   ├── cross-platform-growth/
│   ├── cv-cover-letter/
│   ├── digital-strategy-consultation/
│   ├── google-business-profile/
│   ├── logo-branding/
│   ├── online-cyber-services/
│   ├── poster-flyer-design/
│   ├── premium-brand-tech/
│   ├── professional-career/
│   ├── social-media-management/
│   ├── starter-digital-access/
│   ├── website-design/
│   └── website-launch/
│
└── icons/

Important distinction

Your existing:

docs/assets/

is the published web copy.

Your future:

assets/

is the canonical/master source.

Therefore:

assets/
   ↓
build/copy
   ↓
docs/assets/

We should not move the current live files blindly.

The live website must remain working while we reorganize.

---

6. "frontend/"

This is optional for the current static implementation but gives us a clean future application boundary.

frontend/
├── README.md
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── api/
│   ├── state/
│   ├── utils/
│   └── styles/
│
└── public/

The key distinction is:

frontend/
    = source/application

docs/
    = public GitHub Pages output

For the current phase, we can keep the existing HTML site in "docs/" and introduce "frontend/" only when the storefront build architecture requires it.

---

7. "docs/"

This is the public production storefront.

Keep the current working site here.

docs/
├── CNAME
│
├── index.html
├── faq.html
├── privacy.html
├── cookies.html
├── terms.html
│
├── assets/
│   ├── branding/
│   ├── icons/
│   └── services/
│
├── css/
│   └── style.css
│
├── js/
│   ├── app.js
│   └── services.js
│
├── services/
│   ├── business-digital-presence.html
│   ├── business-email-setup.html
│   ├── business-startup.html
│   ├── cross-platform-growth.html
│   ├── cv-cover-letter.html
│   ├── digital-strategy-consultation.html
│   ├── google-business-profile.html
│   ├── logo-branding.html
│   ├── online-cyber-services.html
│   ├── poster-flyer-design.html
│   ├── premium-brand-tech.html
│   ├── professional-career.html
│   ├── social-media-management.html
│   ├── starter-digital-access.html
│   ├── website-design.html
│   └── website-launch.html
│
├── robots.txt
└── sitemap.xml

"docs/" rule

Allowed:

HTML
CSS
browser JavaScript
public images
public fonts
SEO files
public legal pages

Not allowed:

API secrets
database credentials
M-Pesa credentials
private keys
admin secrets
server-only code
internal audit information
private customer data

---

8. "admin/"

This is the internal operations application.

Target:

admin/
├── README.md
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── api/
│   ├── auth/
│   ├── state/
│   ├── services/
│   └── utils/
│
└── public/

Conceptual pages:

admin/
├── dashboard
├── services
├── customers
├── orders
├── quotes
├── payments
├── fulfillment
├── audit
└── settings

The admin application talks to:

admin
  ↓
backend API

Not directly:

admin
  ↓
D1

The backend remains the enforcement layer.

---

9. "backend/"

This is the heart of KDCN Commerce.

Target:

backend/
├── README.md
│
├── src/
│   ├── index.ts
│   │
│   ├── config/
│   │
│   ├── middleware/
│   │
│   ├── auth/
│   │
│   ├── routes/
│   │   ├── public/
│   │   ├── customer/
│   │   ├── admin/
│   │   └── webhooks/
│   │
│   ├── modules/
│   │   ├── catalog/
│   │   ├── customers/
│   │   ├── orders/
│   │   ├── quotes/
│   │   ├── payments/
│   │   ├── fulfillment/
│   │   └── notifications/
│   │
│   ├── database/
│   │
│   ├── validation/
│   │
│   ├── security/
│   │
│   ├── logging/
│   │
│   └── types/
│
└── tests/

The backend owns:

validation
authorization
pricing
orders
quotes
payment processing
business rules
database access
audit operations

---

10. BACKEND DOMAIN STRUCTURE

The main business domains are:

catalog
customers
orders
quotes
payments
fulfillment
notifications

Conceptually:

CATALOG
   ↓
ORDER / QUOTE
   ↓
PAYMENT
   ↓
FULFILLMENT
   ↓
DELIVERABLE

---

11. "database/"

Database responsibility is isolated here.

Target:

database/
├── README.md
├── schema.sql
│
├── migrations/
│   ├── 001_initial.sql
│   ├── 002_catalog.sql
│   ├── 003_customers.sql
│   ├── 004_orders.sql
│   ├── 005_quotes.sql
│   ├── 006_payments.sql
│   ├── 007_fulfillment.sql
│   └── 008_audit.sql
│
└── seeds/
    ├── README.md
    └── development/

The database eventually contains:

services
service_requirements

customers

orders
order_items

quotes
quote_items

payments

projects
deliverables

audit_logs

---

12. "scripts/"

Development automation:

scripts/
├── README.md
├── generate_service_pages.py
├── validate_catalog.py
├── validate_assets.py
├── db-check.sh
├── test.sh
└── build.sh

Scripts should automate repetitive work instead of becoming undocumented magic.

---

13. "tests/"

Testing should be divided by purpose.

tests/
├── README.md
│
├── unit/
│   ├── catalog/
│   ├── pricing/
│   ├── orders/
│   ├── quotes/
│   └── validation/
│
├── integration/
│   ├── api/
│   ├── database/
│   ├── orders/
│   ├── quotes/
│   └── payments/
│
├── e2e/
│   ├── customer-order/
│   ├── customer-quote/
│   └── admin/
│
├── security/
│   ├── authorization/
│   ├── input-validation/
│   ├── payment-callback/
│   └── abuse/
│
└── fixtures/

---

14. DATA FLOW

The complete system becomes:

                         CUSTOMER
                            │
                            ▼
                    PUBLIC STOREFRONT
                         docs/
                            │
                            ▼
                       COMMERCE API
                       backend/src
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
       CATALOG            ORDERS            QUOTES
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ▼
                         PAYMENTS
                            │
                            ▼
                       FULFILLMENT
                            │
                            ▼
                        DELIVERABLE
                            │
                            ▼
                         CUSTOMER


ADMIN
  │
  ▼
admin/
  │
  ▼
Commerce API

Database:

backend
   ↓
Cloudflare D1

External provider:

backend
   ↓
M-Pesa Daraja

---

15. PUBLIC VS PRIVATE BOUNDARY

This is one of the most important rules in the project.

PUBLIC
│
└── docs/
      │
      ├── HTML
      ├── CSS
      ├── JS
      └── public assets


PRIVATE / SERVER
│
├── backend/
├── database/
├── admin/
└── secrets/configuration


BUILD / SOURCE
│
├── architecture/
├── assets/
├── KDCN-store-pic/
└── scripts/

GitHub Pages exposes the public layer.

Cloudflare Workers operate the backend layer.

Cloudflare D1 stores the data layer.

---

16. CURRENT LIVE WEBSITE PRESERVATION RULE

Your current live site uses:

docs/assets/branding/
docs/assets/services/

Therefore:

Do not move those files right now.

We first establish:

assets/

as the canonical source.

Later:

assets/
    ↓
build
    ↓
docs/assets/

That way the public website does not suddenly break because of a cleanup operation.

---

17. LOGICAL ASSET OWNERSHIP

Use this model:

KDCN-store-pic/
    = marketing generation

assets/
    = master/canonical application assets

docs/assets/
    = public published assets

admin/
    = admin-specific UI assets where required

Do not make:

docs/assets

the long-term master source.

---

18. SERVICE INFORMATION OWNERSHIP

Eventually:

DATABASE / CANONICAL CATALOG
            │
      ┌─────┼─────┐
      │     │     │
      ▼     ▼     ▼
   STORE   ADMIN ASSETS

Current migration inputs:

KDCN-store-pic/service-catalog.csv
docs/js/services.js
docs/services/*.html

These will be normalized rather than independently edited forever.

---

19. WHAT EACH LAYER MUST NOT DO

"docs/"

Must not:

calculate authoritative prices
confirm payments
write directly to D1
authorize admin users
contain secrets

"admin/"

Must not:

bypass backend authorization
directly mutate database
trust browser state

"backend/"

Must not:

depend on browser-provided authority
trust client prices
expose secrets

"database/"

Must not:

contain application UI
contain secrets
be edited manually in production without controlled process

---

20. DEVELOPMENT ORDER

The repository structure does not mean all directories are developed simultaneously.

We still follow:

01 Architecture
      ↓
02 Catalog
      ↓
03 Database
      ↓
04 Backend
      ↓
05 Storefront Integration
      ↓
06 Orders
      ↓
07 Quotes
      ↓
08 Payments
      ↓
09 Fulfillment
      ↓
10 Admin
      ↓
11 Notifications
      ↓
12 Security
      ↓
13 Testing
      ↓
14 Deployment
      ↓
15 Production

---

21. THE IMPORTANT CHANGE NOW

We already have:

architecture/
KDCN-store-pic/
admin/
assets/
backend/
database/
docs/
scripts/
tests/

Therefore we do not need to create random new top-level folders just to make the tree look bigger.

We only create subdirectories when the corresponding implementation requires them.

---

22. FIRST STRUCTURAL TARGET

Before database coding, our immediate repository target is:

KDCN-store/
│
├── architecture/
│
├── KDCN-store-pic/
│
├── assets/
│   ├── branding/
│   ├── services/
│   └── icons/
│
├── admin/
│   └── README.md
│
├── backend/
│   └── README.md
│
├── database/
│   ├── schema.sql
│   ├── migrations/
│   └── README.md
│
├── docs/
│   └── CURRENT LIVE STOREFRONT
│
├── scripts/
│   └── generate_service_pages.py
│
├── tests/
│   └── README.md
│
├── README.md
├── package.json
├── tsconfig.json
└── wrangler.jsonc

That is enough structure for the current stage.

---

23. STRUCTURAL RULE

We build downward, not outward.

Bad:

new folder
new framework
new app
new service
new abstraction

every time we need something.

Good:

existing domain
    ↓
existing boundary
    ↓
correct file
    ↓
correct responsibility

---

24. GOLDEN MAP

When deciding where something belongs, use this:

"How does it work?"
        ↓
architecture/

"What does the customer see?"
        ↓
docs/ / frontend/

"How is it generated?"
        ↓
KDCN-store-pic/ / scripts/

"What data does it store?"
        ↓
database/

"What rules does it enforce?"
        ↓
backend/

"How does staff operate it?"
        ↓
admin/

"How do we prove it works?"
        ↓
tests/

---

25. FINAL TARGET

The mature KDCN Store repository should eventually resemble:

KDCN-store/
│
├── architecture/
│   ├── README.md
│   ├── document-index.md
│   ├── system-overview.md
│   ├── commerce-model.md
│   ├── service-catalog.md
│   ├── order-lifecycle.md
│   ├── quote-lifecycle.md
│   ├── payment-lifecycle.md
│   ├── admin-model.md
│   └── kdcn-store-blueprint.md
│
├── KDCN-store-pic/
│   ├── source/
│   ├── _raw/
│   ├── web/
│   ├── social/
│   ├── dm-quote/
│   └── fixed-price/
│
├── assets/
│   ├── branding/
│   ├── services/
│   └── icons/
│
├── frontend/
│
├── admin/
│   └── src/
│
├── backend/
│   └── src/
│       ├── auth/
│       ├── routes/
│       ├── modules/
│       ├── validation/
│       ├── security/
│       ├── logging/
│       └── types/
│
├── database/
│   ├── schema.sql
│   ├── migrations/
│   └── seeds/
│
├── docs/
│   ├── index.html
│   ├── services/
│   ├── assets/
│   ├── css/
│   ├── js/
│   └── legal / SEO files
│
├── scripts/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   ├── security/
│   └── fixtures/
│
├── README.md
├── package.json
├── tsconfig.json
└── wrangler.jsonc
