# KDCN Store Architecture

**System:** KDCN Commerce  
**Repository:** `KDCN-store`  
**Phase:** 2 — KDCN Commerce  
**Status:** Foundation and architecture  
**Authority:** This directory is the authoritative architecture documentation set for KDCN Store.

## Purpose

KDCN Store is the commerce and transaction layer of the KINGMAN DIGITAL ecosystem. It provides a controlled service-commerce platform for discovery, service selection, quote requests, orders, payments, customer information, fulfillment, and administrative operations.

## Architectural principles

1. Security-first
2. Server-side authority for commerce state
3. Single source of truth for service catalog data
4. Explicit separation of fixed-price and quote-based commerce
5. Least privilege
6. Auditable state transitions
7. Incremental delivery
8. Backward-compatible storefront evolution
9. No production secrets in source control
10. Documentation before irreversible architectural changes

## Documents

See `document-index.md` for the authoritative document inventory and status legend.
