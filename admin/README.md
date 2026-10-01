# KDCN Store — Admin Control Plane

**Owner:** KINGMAN DIGITAL
**Status:** Phase A — shell only

## Purpose

Internal operator interface for the KDCN Commerce system.
Admin is NOT the backend, NOT the database, and NOT the public storefront.

## Boundary rule

    Admin UI  →  backend API  →  authorization  →  business rule  →  database

The admin browser NEVER talks to the database directly.
The admin browser NEVER decides authorization.
The admin browser NEVER confirms payments.

## Phase status

- [x] Folder reserved
- [x] README
- [x] Application shell (index.html + css + js)
- [ ] Auth wiring          (blocked on backend auth endpoints)
- [ ] Dashboard page       (blocked on backend metrics endpoints)
- [ ] Services page        (blocked on catalog API)
- [ ] Customers page       (blocked on customer API)
- [ ] Orders page          (blocked on order API)
- [ ] Quotes page          (blocked on quote API)
- [ ] Payments page        (blocked on payment API)
- [ ] Fulfillment page     (blocked on fulfillment API)
- [ ] Audit page           (blocked on audit API)
- [ ] Settings page        (blocked on settings API)

## Forbidden in this directory

- M-Pesa / payment credentials
- API tokens, signing keys, JWT secrets
- Server-side business logic
- Direct database access code
- Customer PII written to disk
- "admin because the button is hidden" authorization
