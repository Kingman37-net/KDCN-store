# KDCN Store Payment Lifecycle

**Status:** `DRAFT`

## 1. Payment boundary

The payment provider is an external system. KDCN Store must treat provider responses as untrusted input until the backend validates them.

Target flow:

```text
Customer
  -> Checkout
  -> KDCN Backend
  -> Payment Provider
  -> Provider Callback/Webhook
  -> KDCN Backend validation
  -> Payment state update
  -> Order state update
```

## 2. Payment principles

- Never store payment-card secrets or sensitive provider credentials in the repository.
- Never trust a browser-only success response.
- Validate callback authenticity according to the provider's documented mechanism.
- Make callbacks idempotent.
- Record provider transaction references.
- Maintain an audit trail for payment state changes.

## 3. M-Pesa

The repository identifies M-Pesa Daraja as the intended payment integration. Provider-specific implementation details should be documented only after the exact API contract and deployment configuration are finalized.
