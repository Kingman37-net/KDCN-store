# KDCN Store Architecture Document Index

## Status legend

| Status | Meaning |
|---|---|
| `AUTHORITATIVE` | Approved source of truth for the subject |
| `DRAFT` | Proposed design; not yet approved as operational truth |
| `IMPLEMENTED` | Design is implemented and verified in code |
| `PARTIAL` | Some elements are implemented; remaining work exists |
| `DEPRECATED` | Retained for history; must not guide new implementation |
| `SUPERSEDED` | Replaced by a newer authoritative document |

> A document's status describes the document, not the maturity of the entire system.

## Index

| Document | Status | Scope |
|---|---|---|
| `README.md` | `AUTHORITATIVE` | Architecture set overview |
| `system-overview.md` | `AUTHORITATIVE` | System boundaries and major components |
| `commerce-model.md` | `AUTHORITATIVE` | Fixed-price and quote-based service commerce |
| `service-catalog.md` | `AUTHORITATIVE` | Service catalog ownership and data model |
| `order-lifecycle.md` | `AUTHORITATIVE` | Order states and transitions |
| `quote-lifecycle.md` | `AUTHORITATIVE` | Quote states and transitions |
| `payment-lifecycle.md` | `DRAFT` | Payment workflow and provider boundary |
| `admin-model.md` | `DRAFT` | Administrative roles and capabilities |

## Change rule

Architecture changes must update the affected authoritative document before or together with the implementation change.
