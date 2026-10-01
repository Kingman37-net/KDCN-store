# KDCN Store Commerce Model

**Status:** `AUTHORITATIVE`

## 1. Service commerce, not inventory commerce

KDCN Store primarily sells professional digital services. The core fulfillment unit is therefore a service engagement rather than a physical inventory item.

Primary flow:

```text
Service
  -> Order or Quote
  -> Payment
  -> Fulfillment / Project
  -> Deliverable
```

## 2. Commercial models

### Fixed-price service

```text
Service
  -> Buy
  -> Checkout
  -> Payment
  -> Order
  -> Fulfillment
```

A fixed-price service has a published price and may proceed through automated checkout.

### Quote-based service

```text
Service
  -> Requirements
  -> Quote request
  -> Administrative review
  -> Quote
  -> Customer acceptance
  -> Payment
  -> Order / Project
```

A quote-based service does not expose a final transactional price until the quote is issued and accepted.

## 3. Catalog attributes

Each service should have, at minimum:

- stable identifier
- slug
- display name
- tier
- description
- pricing model
- published price when applicable
- currency
- active/inactive status
- service requirements
- expected delivery information
- public asset reference

## 4. Business rule

The frontend may display a price, but the backend must re-resolve the current authoritative service and price before creating a payable order.
