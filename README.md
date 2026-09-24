# KDCN Store

**KDCN Commerce — KINGMAN DIGITAL**

A security-first digital commerce system for KINGMAN DIGITAL, designed to manage digital service packages, customer orders, payments, and transaction workflows.

> **No data left unguarded. No system left unsafe.**

## Purpose

KDCN Store is the commerce layer of the KINGMAN DIGITAL ecosystem.

It is being developed to provide a controlled digital environment where customers can:

- Discover available services
- Review service requirements
- Select service packages
- Submit orders
- Provide required information
- Make payments
- Track order status

The internal system will provide authorized administrators with controlled management of:

- Services
- Categories
- Orders
- Customers
- Payments
- Service requirements
- Audit records

## Architecture

```text

Customer
   ↓
KDCN Store
   ↓
Secure API
   ↓
Cloudflare Worker
   ↓
Cloudflare D1
   ↓
Orders / Customers / Payments
   ↓
M-Pesa Integration

Technology
TypeScript
Cloudflare Workers
Cloudflare D1
Wrangler
HTML / CSS / JavaScript
M-Pesa Daraja API
Git / GitHub


---


## Security
Security is treated as a core system requirement rather than an optional feature.
Planned controls include:

**HTTPS**
- Authentication and authorization
- Secure credential handling
- Input validation
- Parameterized database queries
- Rate limiting
- Security headers
- Payment callback validation
- Audit logging
- Access control
- Backup and recovery procedures
- Security testing
- Least-privilege design

No production secrets, API credentials, access tokens, customer payment information, or other sensitive data should be committed to this repository.

## Project Status

**Phase 2**— KDCN Commerce
**Current stage:** Foundation and architecture

**Development will proceed incrementally:**
1. Project foundation
2. Database architecture
3. Commerce API
4. Storefront
5. Order management
6. Payment integration
7. Administration
8. Security testing
9. Production deployment
10. Ecosystem integration

**Relationship to the KDCN Ecosystem**
```text
KINGMAN DIGITAL ECOSYSTEM

├── Website
├── KDCN Store       ← This project
├── KDCN Platform
├── KDCN Admin
├── KDCN CRM
├── KDCN Analytics
└── KDCN Automation

KDCN Store is the commerce and transaction layer of the wider 
**KINGMAN DIGITAL ecosystem.**
Backup & Recovery
**Development follows a backup-first approach.**
Important milestones should be committed to version control before 
**major architectural changes.**
Production data and secrets must use appropriate secure backup and secret-management systems rather than being stored directly in Git.

# License

See LICENSE.

---
KINGMAN DIGITAL
Global IT & Cybersecurity Services
**System:** KDCN Commerce
**Phase:** 2
**Status:** Development
