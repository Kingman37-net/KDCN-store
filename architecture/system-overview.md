# KDCN Store System Overview

**Status:** `AUTHORITATIVE`

## 1. System purpose

KDCN Store is a digital service-commerce system for KINGMAN DIGITAL. It supports service discovery, service requirements, fixed-price purchases, quote-based engagements, payments, order management, customer records, fulfillment, and controlled administration.

## 2. Current repository boundaries

```text
KDCN-store/
├── KDCN-store-pic/   # Asset production pipeline
├── admin/            # Internal administration surface
├── backend/          # API and business logic
├── database/         # Database schema and migrations
├── docs/             # Public storefront
├── scripts/          # Developer/build automation
├── tests/            # Verification
└── architecture/     # Authoritative architecture documentation
```

## 3. Logical architecture

```text
Customer
   |
   v
Public Storefront (`docs/`)
   |
   v
Commerce API (`backend/`)
   |
   +--------------------+
   |                    |
   v                    v
Service Catalog      Commerce Workflows
                        |
              +---------+---------+
              |         |         |
              v         v         v
            Orders    Quotes   Payments
              |         |         |
              +---------+---------+
                        |
                        v
                 Cloudflare D1
                   (`database/`)

Administrator
   |
   v
Admin Surface (`admin/`)
   |
   v
Commerce API
```

## 4. Asset pipeline

`KDCN-store-pic/` is treated as a production pipeline rather than an application runtime directory.

```text
Source
  -> Build
  -> Validate
  -> Web / Social / DM outputs
  -> Published storefront assets
```

## 5. Runtime authority

The browser is not authoritative for:

- price
- payment status
- order status
- quote status
- customer authorization
- fulfillment state

Those values must be validated and enforced by the backend.
