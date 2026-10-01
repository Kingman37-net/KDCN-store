KDCN STORE — SYSTEM BLUEPRINT

System: KDCN Commerce
Organization: KINGMAN DIGITAL
Repository: "KDCN-store"
Version: 1.0
Status: "AUTHORITATIVE"
Purpose: Define the structure, responsibilities, workflows, data model, and implementation order of KDCN Store.

---

1. SYSTEM DEFINITION

KDCN Store is the digital service-commerce and transaction layer of the KINGMAN DIGITAL ecosystem.

It is designed to allow customers to:

DISCOVER
   ↓
UNDERSTAND
   ↓
SELECT
   ↓
REQUEST OR ORDER
   ↓
PAY
   ↓
TRACK
   ↓
RECEIVE

The system is not primarily a physical-product store.

The primary commercial unit is a digital service.

Therefore the core business relationship is:

SERVICE
   ↓
ORDER / QUOTE
   ↓
PAYMENT
   ↓
FULFILLMENT
   ↓
DELIVERABLE

---

2. CORE ARCHITECTURAL PRINCIPLES

These principles govern the whole project.

2.1 Security first

Security is part of the architecture, not an afterthought.

2.2 Backend authority

The browser is never authoritative for:

price
payment status
order status
quote status
permissions
fulfillment state

The backend validates and controls these.

2.3 Single source of truth

Service information should eventually have one authoritative source.

The system must avoid maintaining conflicting versions of:

service name
price
tier
pricing model
status
requirements

across multiple files.

2.4 Explicit commerce models

KDCN Store supports:

FIXED-PRICE SERVICES
QUOTE-BASED SERVICES

These are separate commercial workflows.

2.5 Least privilege

Every administrative or system action receives only the access required for its purpose.

2.6 Auditability

Important business events must be traceable.

2.7 Incremental implementation

The project is implemented in controlled phases.

No large rewrite is required unless architecture or security requires one.

2.8 Existing storefront preservation

The current "docs/" storefront is valuable working software.

The backend should be introduced behind it progressively rather than replacing the storefront unnecessarily.

---

3. REPOSITORY BLUEPRINT

The target repository structure is:

KDCN-store/
│
├── CNAME
├── README.md
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
│   ├── README.md
│   ├── service-catalog.csv
│   ├── source/
│   ├── _raw/
│   ├── web/
│   ├── social/
│   ├── dm-quote/
│   ├── fixed-price/
│   ├── build-kdcn-assets.py
│   ├── build-kdcn-assets.sh
│   └── conversion-report.txt
│
├── admin/
│
├── assets/
│
├── backend/
│
├── database/
│   ├── schema.sql
│   └── migrations/
│
├── docs/
│   ├── index.html
│   ├── faq.html
│   ├── privacy.html
│   ├── cookies.html
│   ├── terms.html
│   ├── robots.txt
│   ├── sitemap.xml
│   ├── css/
│   ├── js/
│   ├── assets/
│   └── services/
│
├── scripts/
│
├── tests/
│
├── package.json
├── tsconfig.json
└── wrangler.jsonc

---

4. RESPONSIBILITY OF EACH DIRECTORY

"architecture/"

The authoritative description of how KDCN Store is supposed to work.

Contains:

system architecture
business model
data model
state machines
security model
operational rules

This directory answers:

«"How is this system designed?"»

---

"docs/"

The public-facing customer storefront.

It answers:

«"What does the customer see?"»

Current implementation:

HTML
CSS
JavaScript
service pages
legal pages
SEO files
public assets

---

"admin/"

Internal administration interface.

It answers:

«"How do authorized KDCN personnel operate the store?"»

---

"backend/"

Application/API and business logic.

It answers:

«"What rules does the system enforce?"»

This is the trust boundary between the public client and the data layer.

---

"database/"

Persistent business data.

It answers:

«"What information does the system store?"»

---

"KDCN-store-pic/"

Asset production pipeline.

It answers:

«"How are service assets generated and prepared for publication?"»

It is a production/content pipeline, not the main runtime application.

---

"scripts/"

Developer and build automation.

---

"tests/"

Automated and manual verification.

---

"assets/"

Application-level/shared asset storage where appropriate.

---

5. SYSTEM BOUNDARIES

The architecture is divided into five major layers.

┌──────────────────────────────────────────┐
│ 1. PRESENTATION                          │
│    docs/ + customer-facing UI           │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│ 2. APPLICATION                           │
│    backend/ + API + business rules       │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│ 3. DATA                                  │
│    Cloudflare D1                         │
└────────────────────┬─────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────┐
│ 4. EXTERNAL SERVICES                     │
│    M-Pesa / messaging / email / etc.    │
└──────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ 5. OPERATIONS                            │
│    admin/ + auditing + monitoring        │
└──────────────────────────────────────────┘

---

6. CUSTOMER-FACING STRUCTURE

The storefront is centered around:

HOME
 ↓
SERVICE CATALOG
 ↓
SERVICE DETAIL
 ↓
BUY NOW / REQUEST QUOTE
 ↓
CHECKOUT / REQUIREMENTS
 ↓
PAYMENT
 ↓
CONFIRMATION
 ↓
ORDER STATUS

Current homepage sections remain:

Navigation
Hero
Service Tiers
Service Catalogue
Filter Controls
CTA
Footer

These should not be discarded simply because a backend is introduced.

---

7. SERVICE TIERS

The current storefront uses four tiers:

Essential
Professional
Business
Advanced

These are catalog classification levels.

They are not payment states.

They are not user roles.

They are not technical environments.

They describe the level/type of service offering.

---

8. SERVICE ENTITY

A service should conceptually have:

id
slug
name
tier
pricing_model
price
currency
status
description
requirements
delivery_information
image
created_at
updated_at

Example:

id: website-design
slug: website-design
name: Website Design
tier: professional
pricing_model: fixed
price: <authoritative price>
currency: KES
status: active

Quote-based example:

id: premium-brand-tech
slug: premium-brand-tech
name: Premium Brand & Tech
tier: advanced
pricing_model: quote
price: null
currency: KES
status: active

---

9. PRICING MODEL

Every service must explicitly declare one commercial model.

9.1 Fixed price

pricing_model = fixed

Flow:

Service
   ↓
Published price
   ↓
Buy Now
   ↓
Checkout
   ↓
Payment
   ↓
Order

The backend must resolve the authoritative price.

The client must never be trusted to determine what the customer owes.

---

9.2 Quote

pricing_model = quote

Flow:

Service
   ↓
Request Quote
   ↓
Requirements
   ↓
Quote Request
   ↓
Administrative Review
   ↓
Quote Issued
   ↓
Customer Acceptance
   ↓
Payment
   ↓
Order

---

10. SERVICE CATALOG SOURCE OF TRUTH

Current catalog-related sources include:

KDCN-store-pic/service-catalog.csv
docs/js/services.js
docs/services/*.html

These are currently implementation/content sources.

The target architecture is:

                 AUTHORITATIVE CATALOG
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
      Storefront       Admin         Asset Build
          │
          ▼
         API

The long-term objective is to prevent:

CSV price ≠ JavaScript price ≠ HTML price ≠ database price

There must be one authoritative production source.

---

11. CUSTOMER ENTITY

The customer domain represents the person or organization purchasing or requesting a service.

Conceptual attributes:

id
name
email
phone
account_status
created_at
updated_at

Additional customer information should only be stored where it serves a defined business purpose.

---

12. ORDER DOMAIN

The order represents a commercial transaction.

Core relationship:

CUSTOMER
   │
   ▼
ORDER
   │
   ├── ORDER ITEMS
   │      │
   │      └── SERVICE
   │
   ├── PAYMENT
   │
   └── FULFILLMENT / PROJECT

An order must retain enough historical information to reconstruct what was purchased.

---

13. ORDER LIFECYCLE

Recommended initial state model:

DRAFT
  ↓
PENDING_PAYMENT
  ↓
PAID
  ↓
IN_PROGRESS
  ↓
DELIVERED
  ↓
COMPLETED

Failure/cancellation branches:

PENDING_PAYMENT
      └──> PAYMENT_FAILED

PAID
      └──> CANCELLED / REFUNDED

Exact cancellation/refund rules must be implemented explicitly.

---

14. ORDER RULES

The backend owns order state.

The browser cannot directly perform:

order.status = "PAID"

or:

order.total = 250

Authoritative flow:

Customer request
     ↓
Backend validates
     ↓
Backend resolves service
     ↓
Backend calculates total
     ↓
Backend creates order

---

15. ORDER ITEMS

An order may contain one or multiple services.

Conceptual model:

ORDER
 │
 ├── ITEM
 │    └── SERVICE
 │
 ├── ITEM
 │    └── SERVICE
 │
 └── PAYMENT

Each order item should preserve the commercial details required to understand the transaction at the time it occurred.

This protects historical integrity when catalog information changes later.

---

16. QUOTE DOMAIN

A quote request represents a request for custom commercial pricing.

Core relationship:

CUSTOMER
   ↓
QUOTE REQUEST
   ↓
QUOTE
   ↓
ACCEPTANCE
   ↓
ORDER

---

17. QUOTE LIFECYCLE

Initial state model:

REQUESTED
    ↓
UNDER_REVIEW
    ↓
ISSUED
    ├──> DECLINED
    ├──> EXPIRED
    ↓
ACCEPTED
    ↓
PENDING_PAYMENT
    ↓
CONVERTED_TO_ORDER

Every accepted quote should retain its relationship to the resulting order.

---

18. PAYMENT DOMAIN

The payment provider is external to KDCN Store.

The architecture is:

CUSTOMER
   ↓
CHECKOUT
   ↓
KDCN BACKEND
   ↓
PAYMENT PROVIDER
   ↓
CALLBACK / WEBHOOK
   ↓
KDCN BACKEND
   ↓
VERIFY
   ↓
UPDATE PAYMENT
   ↓
UPDATE ORDER

For the planned implementation:

KDCN Store
    ↓
M-Pesa Daraja

Provider-specific implementation should remain isolated behind the payment integration layer.

---

19. PAYMENT RULES

Never trust a frontend success message as proof of payment.

The backend must verify provider-side confirmation.

Payment processing must support:

provider reference
payment amount
currency
payment status
timestamps
order reference
idempotency / duplicate protection
audit trail

Sensitive credentials must never be stored in Git.

---

20. FULFILLMENT / PROJECT DOMAIN

Because KDCN sells services, payment does not necessarily mean the service is immediately completed.

After payment:

ORDER
  ↓
FULFILLMENT
  ↓
PROJECT / WORK
  ↓
DELIVERABLE

For a simple service this may be lightweight.

For a larger engagement it may require:

requirements
assignment
work stages
deliverables
completion

The system should therefore be designed to support service fulfillment without forcing every service into a physical-shipping model.

---

21. ADMIN SYSTEM

The admin application operates against the backend.

Conceptual modules:

Dashboard
Services
Categories / Tiers
Customers
Orders
Quotes
Payments
Fulfillment
Audit Logs
Settings

Administrative controls must be enforced server-side.

The browser UI is not an authorization boundary.

---

22. ADMIN CAPABILITY MODEL

Access should eventually be divided by capability.

Conceptual capabilities:

catalog.read
catalog.write

orders.read
orders.write

quotes.read
quotes.write

payments.read

customers.read
customers.write

fulfillment.read
fulfillment.write

audit.read

system.admin

The exact role matrix will be finalized before production deployment.

---

23. BACKEND STRUCTURE

Target conceptual backend:

backend/
├── api/
├── auth/
├── catalog/
├── customers/
├── orders/
├── quotes/
├── payments/
├── fulfillment/
├── notifications/
├── validation/
└── index.ts

The exact file layout may evolve, but these responsibilities should remain separated.

---

24. API RESPONSIBILITY

The backend API should provide controlled access to:

services
customers
orders
quotes
payments
fulfillment
admin operations

Example conceptual endpoints:

GET    /api/services
GET    /api/services/:slug

POST   /api/orders
GET    /api/orders/:id

POST   /api/quotes
GET    /api/quotes/:id
POST   /api/quotes/:id/accept

POST   /api/payments
POST   /api/payments/webhook

GET    /api/customer/orders

Administrative APIs should be separated logically and protected by authorization.

---

25. DATABASE BLUEPRINT

The initial database domain should cover at least:

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

Additional tables should be added only when there is a defined requirement.

---

26. DATABASE RELATIONSHIP MAP

SERVICE
   │
   ├───────────────┐
   │               │
   ▼               ▼
ORDER ITEM       QUOTE ITEM
   │               │
   ▼               ▼
ORDER             QUOTE
   │               │
   ├──────┐        │
   │      │        │
   ▼      ▼        ▼
PAYMENT PROJECT  ACCEPTANCE
           │
           ▼
       DELIVERABLE

Customer relationship:

CUSTOMER
   ├── ORDER
   ├── QUOTE
   └── PROJECT

Audit relationship:

AUDIT LOG
   ├── actor
   ├── action
   ├── target
   ├── timestamp
   └── result/context

---

27. DATABASE IMPLEMENTATION RULES

Database design must follow these rules:

Primary keys are stable
Foreign keys are explicit
Constraints enforce invariants
Indexes support actual query patterns
Migrations are versioned
Schema changes are tracked
Sensitive data is minimized

The database must not become a dumping ground for arbitrary JSON without a defined purpose.

---

28. FRONTEND DATA FLOW

Current static implementation:

services.js
      ↓
browser
      ↓
service cards

Target implementation:

Backend API
      ↓
Service Catalog
      ↓
Storefront

The migration should happen progressively.

The current interface can continue functioning while the data source changes.

---

29. SERVICE DETAIL PAGE

Each service page should communicate:

Service name
Tier
Description
Benefits / scope
Requirements
Price or quote model
Expected delivery information
Purchase action
Quote action where applicable
Contact option

Primary action:

FIXED PRICE
    [BUY NOW]

QUOTE
    [REQUEST QUOTE]

---

30. CUSTOMER CHECKOUT

Fixed-price checkout should conceptually be:

Service
  ↓
Order summary
  ↓
Customer information
  ↓
Requirements
  ↓
Total
  ↓
Payment
  ↓
Confirmation

Before payment initiation:

backend validates:
- service exists
- service is active
- pricing model is fixed
- current price
- customer input
- order total

---

31. CUSTOMER ACCOUNT / TRACKING

The future customer area should support:

Profile
Orders
Payments
Quotes
Order status
Service progress

It does not need to be implemented before the core commerce flow is functional.

---

32. WHATSAPP

WhatsApp is a conversion and communication channel, not the primary source of commercial truth.

Use it for:

consultation
quote discussion
customer support
service clarification

But the canonical business state should still exist in KDCN Store.

Example:

WhatsApp conversation
        ↓
Quote request
        ↓
KDCN system record

rather than:

WhatsApp = database

---

33. EMAIL

Email can be used for:

order confirmation
payment confirmation
quote notification
status updates
delivery notification
support communication

Email sending should be backend-controlled.

---

34. ASSET PIPELINE

The existing asset structure is retained:

KDCN-store-pic/
│
├── source/
├── _raw/
├── web/
├── social/
├── dm-quote/
└── fixed-price/

The asset pipeline is:

SOURCE
   ↓
BUILD
   ↓
VALIDATE
   ↓
OUTPUT
   ↓
PUBLISH

The output should not become the authoritative source for service commercial data.

---

35. ASSET / CATALOG RELATIONSHIP

The service catalog should identify the asset associated with a service.

Example:

Service
   ↓
image_path
   ↓
docs/assets/services/...

This avoids random manual asset selection.

---

36. SECURITY ARCHITECTURE

Minimum controls:

HTTPS
Authentication
Authorization
Least privilege
Input validation
Parameterized SQL
Rate limiting
Secure headers
Secret management
Payment callback validation
Audit logging
Backup / recovery
Security testing

Security boundaries:

PUBLIC
  ↓
API
  ↓
AUTHORIZATION
  ↓
BUSINESS LOGIC
  ↓
DATABASE

---

37. SECRET MANAGEMENT

Never commit:

API keys
M-Pesa credentials
tokens
passwords
private keys
session secrets
production credentials

Use environment/secret-management mechanisms appropriate to the Cloudflare deployment.

---

38. AUDITING

Important events should be auditable.

Examples:

service created
service price changed
order created
payment confirmed
quote issued
quote accepted
order cancelled
admin login
admin action
fulfillment state changed

Audit records should preserve:

who
what
when
target
result

---

39. TESTING STRATEGY

Testing should be layered.

Unit tests

Test isolated business rules:

pricing
validation
state transitions
authorization

Integration tests

Test:

API + database
orders + payments
quotes + orders

Security tests

Test:

unauthorized admin access
input injection
invalid payment callbacks
tampered prices
tampered order IDs
rate limiting

End-to-end tests

Test customer journeys:

browse → order → pay → confirmation

browse → quote → accept → pay

---

40. ENVIRONMENTS

At minimum:

LOCAL
STAGING
PRODUCTION

Conceptually:

Developer
   ↓
Local
   ↓
Staging
   ↓
Production

Production data must not be casually used for local development.

---

41. DEPLOYMENT ARCHITECTURE

Planned deployment direction:

Customer
   ↓
KDCN Store domain
   ↓
Cloudflare
   ↓
Public storefront
   ↓
Cloudflare Worker
   ↓
Cloudflare D1

External payment:

Worker
   ↓
M-Pesa Daraja

---

42. "wrangler.jsonc"

"wrangler.jsonc" is the infrastructure/deployment configuration boundary.

It should eventually describe:

Worker
D1 binding
environment configuration
staging
production

Credentials must not be hardcoded in this file.

---

43. IMPLEMENTATION PHASES

Development proceeds in this exact sequence.

PHASE 1 — FOUNDATION

Current state:

Repository
Documentation
Architecture
Static storefront
Asset pipeline

Status:

FOUNDATION COMPLETE / IN PROGRESS

---

PHASE 2 — DATA MODEL

Build:

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

Then create:

database/schema.sql
database/migrations/*

---

PHASE 3 — SERVICE CATALOG

Create one authoritative service catalog.

Validate:

16 services
4 tiers
fixed-price / quote classification
prices
statuses
requirements
assets

Then synchronize:

backend
storefront
admin
asset pipeline

---

PHASE 4 — COMMERCE API

Build:

service API
customer API
order API
quote API

Add:

validation
authorization
error handling
logging

---

PHASE 5 — FIXED-PRICE CHECKOUT

Implement:

service
 ↓
cart/order
 ↓
checkout
 ↓
payment initiation
 ↓
payment verification
 ↓
paid order

---

PHASE 6 — QUOTE SYSTEM

Implement:

request
 ↓
review
 ↓
quote
 ↓
accept
 ↓
payment
 ↓
order

---

PHASE 7 — M-PESA

Implement provider integration.

Requirements:

secure credentials
server-side verification
callback handling
idempotency
transaction references
failure handling

---

PHASE 8 — ADMIN

Implement:

dashboard
catalog
orders
quotes
payments
fulfillment
audit

---

PHASE 9 — CUSTOMER OPERATIONS

Implement:

customer account
order history
status tracking
quote history
notifications

---

PHASE 10 — SECURITY / QA

Perform:

security review
database review
API review
authorization testing
payment testing
failure testing
backup testing

---

PHASE 11 — PRODUCTION

Only after the previous stages are verified:

production configuration
DNS
Cloudflare
D1
Worker
M-Pesa
monitoring
backup
recovery

---

44. DEFINITION OF DONE

A component is not considered complete merely because it runs.

It must satisfy:

FUNCTIONAL
SECURE
VALIDATED
TESTED
DOCUMENTED
RECOVERABLE

For production features:

Code
+
Tests
+
Documentation
+
Security validation
+
Deployment verification

---

45. CHANGE CONTROL

Before introducing a major architectural change:

1. Define the requirement
2. Check the architecture
3. Update affected architecture document
4. Implement
5. Test
6. Commit
7. Push

This prevents:

code evolves
architecture forgotten
documentation becomes fiction

---

46. GIT CHECKPOINT STRATEGY

Major milestones should create identifiable commits.

Example:

docs: establish KDCN Store architecture

feat: implement commerce database schema

feat: add service catalog API

feat: add fixed-price order workflow

feat: add quote workflow

feat: integrate M-Pesa payments

feat: add admin order management

test: add commerce security coverage

chore: prepare production deployment

---

47. WHAT SHOULD NOT BE BUILT YET

Do not add complexity merely because the system may need it someday.

Avoid prematurely building:

multi-vendor marketplace
physical shipping engine
complex warehouse inventory
mobile application
microservices
advanced recommendation engine
large analytics platform

The current business model does not require these for the core system.

---

48. THE CORE KDCN COMMERCE LOOP

Everything in the system should ultimately support this:

                    SERVICE CATALOG
                          │
              ┌───────────┴───────────┐
              │                       │
          FIXED PRICE               QUOTE
              │                       │
           BUY NOW              REQUEST QUOTE
              │                       │
              ▼                       ▼
          CHECKOUT              QUOTE REVIEW
              │                       │
              ▼                       ▼
           PAYMENT                 QUOTE
              │                       │
              │                    ACCEPT
              │                       │
              └───────────┬───────────┘
                          │
                          ▼
                        ORDER
                          │
                          ▼
                     FULFILLMENT
                          │
                          ▼
                      DELIVERABLE
                          │
                          ▼
                       COMPLETE

This is the heart of KDCN Store.

---

49. AUTHORITATIVE STRUCTURE

From this blueprint onward:

ARCHITECTURE
    = defines intended behavior

DATABASE
    = stores business state

BACKEND
    = enforces business rules

STOREFRONT
    = presents and collects customer input

ADMIN
    = operates the system

ASSET PIPELINE
    = produces marketing/store assets

TESTS
    = verify behavior

GIT
    = preserves controlled change history

No layer should silently take over another layer's responsibility.

---

50. FINAL OPERATING MODEL

The finished KDCN Store should conceptually look like this:

                         KDCN STORE
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
    STOREFRONT             ADMIN              ASSETS
      docs/               admin/          KDCN-store-pic/
        │                    │                    │
        └─────────────┬──────┴────────────┘       │
                      │                           │
                      ▼                           ▼
                 COMMERCE API                PUBLISHED
                  backend/                    ASSETS
                      │
          ┌───────────┼────────────┐
          │           │            │
          ▼           ▼            ▼
       CATALOG      ORDERS       QUOTES
          │           │            │
          └───────────┼────────────┘
                      │
                      ▼
                  PAYMENTS
                      │
                      ▼
                  FULFILLMENT
                      │
                      ▼
                  DELIVERABLES
                      │
                      ▼
                  CUSTOMER
                      │
                      ▼
                  COMPLETION

                 DATABASE
                    D1
                    │
                    ▼
               AUDIT RECORDS

51. BLUEPRINT LOCK

This blueprint establishes the working mental model for KDCN Store.

The project should now be developed from the architecture downward:

ARCHITECTURE
     ↓
DATA MODEL
     ↓
DATABASE
     ↓
BACKEND
     ↓
STOREFRONT INTEGRATION
     ↓
PAYMENTS
     ↓
ADMIN
     ↓
TESTING
     ↓
PRODUCTION

The rule is simple:

«No more guessing. Every new component must have a defined responsibility, location, data flow, and reason for existing.»

KDCN Store = service catalog + commerce workflows + payments + fulfillment + administration, implemented as a security-first system.

