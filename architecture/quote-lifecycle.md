# KDCN Store Quote Lifecycle

**Status:** `AUTHORITATIVE`

## 1. Quote states

```text
REQUESTED
   |
   v
UNDER_REVIEW
   |
   v
ISSUED
   |
   +--> DECLINED
   |
   +--> EXPIRED
   |
   v
ACCEPTED
   |
   v
PENDING_PAYMENT
   |
   v
CONVERTED_TO_ORDER
```

## 2. Quote contents

A quote should contain:

- quote identifier
- customer
- requested service
- scope/requirements
- quoted amount
- currency
- validity period
- terms
- status
- issued timestamp
- acceptance timestamp where applicable

## 3. Conversion rule

An accepted quote may create an order. The order must retain a reference to the originating quote so the commercial history remains auditable.
