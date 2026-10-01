# KDCN Store Service Catalog

**Status:** `AUTHORITATIVE`

## 1. Current presentation model

The storefront currently presents 16 services across four tiers:

```text
Essential
Professional
Business
Advanced
```

The existing storefront and asset pipeline should be preserved while the catalog is progressively moved toward a single authoritative data source.

## 2. Single-source-of-truth target

```text
Authoritative catalog
        |
        +--> Storefront
        +--> Admin
        +--> Asset generation
        +--> API
        +--> Service pages
```

No independently maintained price or pricing-model copies should become authoritative.

## 3. Recommended service entity

```text
service
- id
- slug
- name
- tier
- pricing_model
- price_minor
- currency
- status
- description
- requirements
- delivery_description
- image_path
- created_at
- updated_at
```

`price_minor` is optional for quote-based services.

## 4. Pricing rule

Currency values should be represented in the smallest supported unit for transactional arithmetic rather than floating-point values.

For KES, a project may choose the smallest practical unit consistently across the payment integration and database.

## 5. Existing source material

The repository already contains:

- `docs/js/services.js`
- `KDCN-store-pic/service-catalog.csv`
- individual `docs/services/*.html` pages

These should be treated as migration inputs until the authoritative production catalog is established.
