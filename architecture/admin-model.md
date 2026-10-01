# KDCN Store Administration Model

**Status:** `DRAFT`

## 1. Administrative responsibilities

The admin system should manage:

- services
- pricing
- service requirements
- customers
- orders
- quote requests
- quotes
- payments
- fulfillment/projects
- audit records

## 2. Access model

Administrative access should follow least privilege.

Recommended capability groups:

```text
Catalog Management
Order Management
Quote Management
Payment Visibility
Customer Management
Fulfillment Management
Audit / Security
System Administration
```

The exact role matrix should be approved before production deployment.

## 3. Security rule

Administrative authorization must be enforced by the backend/API. Hiding an admin button in the browser is not an authorization control.
