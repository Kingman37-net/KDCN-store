# KDCN Store Order Lifecycle

**Status:** `AUTHORITATIVE`

## 1. Order states

Recommended initial states:

```text
DRAFT
  |
  v
PENDING_PAYMENT
  |
  +--> PAYMENT_FAILED
  |
  v
PAID
  |
  v
IN_PROGRESS
  |
  v
DELIVERED
  |
  v
COMPLETED
```

Cancellation/refund paths must be explicitly defined rather than inferred from arbitrary status changes.

## 2. Rules

- Only the backend creates authoritative orders.
- A client-submitted price is never trusted.
- Payment confirmation must be verified server-side.
- Order state transitions must be auditable.
- Administrative overrides require authorization.
- Completed orders should be immutable except through controlled correction/audit mechanisms.

## 3. Core relationships

```text
Customer
  |
  +--> Order
         |
         +--> Order Items
                 |
                 +--> Service
         |
         +--> Payment
         |
         +--> Fulfillment / Project
```
