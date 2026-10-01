KDCN STORE

MASTER DEVELOPMENT ROADMAP & PHASE PLAN

System: KDCN Commerce
Organization: KINGMAN DIGITAL
Repository: "KDCN-store"
Version: 1.0
Status: "AUTHORITATIVE"
Development Model: Sequential, checkpoint-driven, security-first

---

1. PURPOSE OF THIS ROADMAP

This roadmap defines exactly how KDCN Store will be developed.

It exists to prevent:

random coding
↓
unfinished dependencies
↓
architecture drift
↓
broken integrations
↓
confusion

The project will instead follow:

PLAN
 ↓
DESIGN
 ↓
IMPLEMENT
 ↓
TEST
 ↓
VERIFY
 ↓
COMMIT
 ↓
PROCEED

A later phase must not become the foundation for an earlier unfinished phase.

---

2. THE GOLDEN DEVELOPMENT RULE

ONE PHASE AT A TIME

We do not move forward merely because something is partially working.

We move forward when the current phase satisfies its:

Entry Criteria
Implementation Requirements
Testing Requirements
Security Requirements
Exit Criteria
Git Checkpoint

Only then does the next phase begin.

---

3. CURRENT PROJECT POSITION

The repository currently contains:

KDCN-store/
├── architecture/
├── KDCN-store-pic/
├── admin/
├── assets/
├── backend/
├── database/
├── docs/
├── scripts/
├── tests/
├── package.json
├── tsconfig.json
└── wrangler.jsonc

The architecture documentation has already been established and committed.

Current checkpoint:

Commit:
ca8cea8

Message:
docs: establish KDCN Store architecture

Working tree:

CLEAN

Therefore:

PHASE 0 = COMPLETE
PHASE 1 = READY

---

4. MASTER ROADMAP

The project will use these phases:

PHASE 0  — Repository Baseline
PHASE 1  — Architecture Lock
PHASE 2  — Catalog & Business Rules
PHASE 3  — Database Foundation
PHASE 4  — Backend/API Foundation
PHASE 5  — Service Catalog Integration
PHASE 6  — Customer & Order System
PHASE 7  — Quote System
PHASE 8  — Checkout & Payment
PHASE 9  — Fulfillment & Customer Tracking
PHASE 10 — Admin Operations
PHASE 11 — Notifications & Communications
PHASE 12 — Security Hardening
PHASE 13 — Testing & Quality Assurance
PHASE 14 — Deployment & Infrastructure
PHASE 15 — Production Readiness
PHASE 16 — Operations & Continuous Improvement

---

5. DEVELOPMENT FLOW

The dependency chain is:

ARCHITECTURE
     ↓
BUSINESS MODEL
     ↓
DATABASE
     ↓
BACKEND
     ↓
CATALOG API
     ↓
ORDERS / QUOTES
     ↓
PAYMENTS
     ↓
FULFILLMENT
     ↓
ADMIN
     ↓
SECURITY / QA
     ↓
DEPLOYMENT
     ↓
OPERATIONS

This is the main road we follow.

---

6. PHASE 0 — REPOSITORY BASELINE

Objective

Establish a clean and recoverable starting point.

Tasks

Verify:

Git repository
main branch
remote origin
working tree
existing storefront
database directory
backend directory
admin directory
tests directory
deployment configuration

Required commands

git status
git branch
git remote -v
tree -L 2

Exit criteria

Repository accessible
Remote configured
Working tree clean
Existing application identified
No unknown architectural assumptions

Status

COMPLETE

---

7. PHASE 1 — ARCHITECTURE LOCK

Objective

Define exactly what KDCN Store is before writing commerce code.

Deliverables

architecture/
├── README.md
├── document-index.md
├── system-overview.md
├── commerce-model.md
├── service-catalog.md
├── order-lifecycle.md
├── quote-lifecycle.md
├── payment-lifecycle.md
├── admin-model.md
└── kdcn-store-blueprint.md

Questions this phase answers

What is the system?
Who uses it?
What does it sell?
How does a customer buy?
How does a quote work?
Where is payment handled?
Who is allowed to administer it?
Where does data live?

Exit criteria

Architecture is:

documented
reviewed
internally consistent
committed
pushed

Status

COMPLETE

---

8. PHASE 2 — CATALOG & BUSINESS RULES

Objective

Define the actual KDCN commercial catalogue before designing the database around it.

This is where we stop talking about generic products and work with the real 16 KDCN services.

Tasks

Inspect:

KDCN-store-pic/service-catalog.csv
docs/js/services.js
docs/services/*.html

Determine for every service:

service ID
slug
name
tier
pricing model
price
currency
status
requirements
delivery information
asset

Required classification

Every service must be:

FIXED PRICE

or:

QUOTE

No ambiguous services.

Deliverable

Canonical service catalogue specification.

Exit criteria

We can answer:

How many services?
Which tier?
Which price?
Which pricing model?
Which requirements?
Which image?
Which status?

without checking five different files.

Git checkpoint

git add .
git commit -m "docs: define KDCN service catalog model"
git push origin main

---

9. PHASE 3 — DATABASE FOUNDATION

Objective

Turn the business model into a controlled persistence model.

Main entities

Initial target:

services
service_requirements

customers

orders
order_items

quotes
quote_items

payments

projects
deliverables

audit_logs

Tasks

Design:

primary keys
foreign keys
constraints
indexes
timestamps
status fields
money representation
relationships

Deliverables

database/schema.sql
database/migrations/001_initial.sql

Potential additional migrations follow only when justified.

Validation

We verify:

service uniqueness
order integrity
quote integrity
payment relationships
customer relationships
valid state values

Exit criteria

Database can represent:

service
customer
order
quote
payment
project
audit event

without hacks.

Git checkpoint

git add database/
git commit -m "feat: establish KDCN commerce database schema"
git push origin main

---

10. PHASE 4 — BACKEND/API FOUNDATION

Objective

Create the secure application layer between the frontend and database.

Responsibilities

routing
validation
database access
business rules
error handling
authentication
authorization
logging

Target conceptual structure

backend/
├── api/
├── auth/
├── catalog/
├── customers/
├── orders/
├── quotes/
├── payments/
├── fulfillment/
├── notifications/
└── index.ts

First API capability

Start with:

GET /api/services
GET /api/services/:slug

Then expand.

Exit criteria

The backend can:

connect to D1
query safely
return valid responses
reject invalid requests
handle errors

without exposing database internals.

Git checkpoint

git add backend/
git commit -m "feat: establish KDCN commerce API foundation"
git push origin main

---

11. PHASE 5 — SERVICE CATALOG INTEGRATION

Objective

Connect the real service catalogue to the storefront.

Current architecture

services.js
   ↓
browser

Target architecture

D1
 ↓
Backend API
 ↓
Storefront

Implementation strategy

Do not destroy the working storefront.

Instead:

existing UI
   ↓
API-backed data

The visual structure may remain largely unchanged.

Tasks

Connect:

service listing
service filtering
service details
pricing
tier information
availability/status

Exit criteria

The storefront successfully consumes authoritative catalog data.

Git checkpoint

feat: connect storefront to service catalog API

---

12. PHASE 6 — CUSTOMER & ORDER SYSTEM

Objective

Implement the first real commerce workflow.

Customer flow

Customer
 ↓
Select service
 ↓
Checkout
 ↓
Customer information
 ↓
Order creation

API capabilities

Conceptually:

POST /api/orders
GET  /api/orders/:id
GET  /api/customer/orders

Order validation

Backend must verify:

service exists
service is active
service is fixed-price
price is authoritative
customer data valid
order total correct

Exit criteria

A valid customer can create an order without payment yet being involved.

Git checkpoint

feat: implement KDCN order workflow

---

13. PHASE 7 — QUOTE SYSTEM

Objective

Implement the second commercial workflow.

Quote process

Customer
 ↓
Request Quote
 ↓
Requirements
 ↓
Quote Request
 ↓
Admin Review
 ↓
Quote Issued
 ↓
Customer Accepts

API capabilities

Conceptually:

POST /api/quotes
GET  /api/quotes/:id
POST /api/quotes/:id/accept

Exit criteria

A quote can be:

requested
reviewed
issued
accepted
declined
expired

and accepted quotes can later become orders.

Git checkpoint

feat: implement KDCN quote workflow

---

14. PHASE 8 — CHECKOUT & PAYMENT

Objective

Connect commerce transactions to payment processing.

Primary planned provider

M-Pesa Daraja

Architecture

Customer
 ↓
Checkout
 ↓
Backend
 ↓
M-Pesa
 ↓
Callback
 ↓
Backend verification
 ↓
Payment confirmed
 ↓
Order marked PAID

Critical rule

Never implement:

browser says paid
↓
order = paid

Instead:

provider confirmation
↓
server verification
↓
payment record
↓
order update

Required controls

callback validation
idempotency
duplicate prevention
payment reference
failure handling
logging

Exit criteria

Test payments work correctly in the intended non-production environment.

Git checkpoint

feat: integrate M-Pesa payment workflow

---

15. PHASE 9 — FULFILLMENT & CUSTOMER TRACKING

Objective

Connect paid orders to actual service delivery.

Flow

PAID
 ↓
IN_PROGRESS
 ↓
DELIVERED
 ↓
COMPLETED

Project relationship

Order
 ↓
Project
 ↓
Work
 ↓
Deliverable

Customer visibility

Customer should eventually see:

order number
service
payment status
order status
progress
delivery information

Exit criteria

The system can track a service after payment through completion.

---

16. PHASE 10 — ADMIN OPERATIONS

Objective

Build the internal operating console.

Admin modules

Dashboard
Services
Customers
Orders
Quotes
Payments
Fulfillment
Audit Logs
Settings

Admin operations

Authorized personnel can:

manage services
review orders
review quote requests
issue quotes
monitor payments
manage fulfillment
inspect audit records

Security principle

Frontend restrictions are not authorization.

The API must enforce permissions.

Exit criteria

An authorized administrator can operate the core commerce lifecycle without database-level manual intervention.

---

17. PHASE 11 — NOTIFICATIONS & COMMUNICATIONS

Objective

Automate customer communication around important business events.

Notifications

Potential events:

order created
payment received
payment failed
quote issued
quote accepted
work started
service completed
delivery available

Channels

Email
WhatsApp
Other approved channels

Communication remains separate from authoritative transaction state.

---

18. PHASE 12 — SECURITY HARDENING

Objective

Attack the system before attackers do.

Review areas

authentication
authorization
input validation
SQL safety
rate limiting
CSRF where applicable
secure cookies
headers
secret management
payment callbacks
admin access
logging

Attack scenarios

Test:

tampered price
tampered order ID
unauthorized admin request
fake payment callback
replayed callback
invalid quote acceptance
invalid status transition
malicious input
excessive requests

Exit criteria

Known security controls are implemented and verified.

Git checkpoint

test: harden KDCN commerce security controls

---

19. PHASE 13 — TESTING & QUALITY ASSURANCE

Objective

Verify the whole system before production.

Testing levels

Unit

pricing
validation
state transitions
authorization

Integration

API + D1
orders + payments
quotes + orders

End-to-end

browse
 ↓
order
 ↓
checkout
 ↓
payment
 ↓
confirmation

and:

browse
 ↓
quote
 ↓
review
 ↓
accept
 ↓
payment
 ↓
order

Quality checks

Also test:

mobile
desktop
navigation
forms
SEO
broken links
performance
accessibility
error handling

Exit criteria

Critical customer and admin journeys pass.

---

20. PHASE 14 — DEPLOYMENT & INFRASTRUCTURE

Objective

Prepare the system for controlled deployment.

Environment model

LOCAL
   ↓
STAGING
   ↓
PRODUCTION

Infrastructure

Cloudflare
Cloudflare Workers
Cloudflare D1
DNS
Secrets
Logging

"wrangler.jsonc"

Must correctly represent the deployment architecture without embedding production secrets.

Exit criteria

Staging environment works independently and predictably.

---

21. PHASE 15 — PRODUCTION READINESS

Objective

Prove that the system is safe to operate in production.

Checklist

DNS verified
HTTPS verified
Worker deployed
D1 production database ready
secrets configured
payment integration verified
logging enabled
backups defined
recovery procedure documented
monitoring available
legal pages available
robots.txt verified
sitemap verified
error pages verified
security review completed

Operational test

Simulate:

normal order
failed payment
duplicate callback
quote request
quote acceptance
service completion
administrator action

Final gate

No production release without passing the production-readiness checklist.

---

22. PHASE 16 — OPERATIONS & CONTINUOUS IMPROVEMENT

Objective

Move from development to sustainable operation.

Ongoing responsibilities

monitoring
backups
security reviews
dependency updates
database maintenance
performance review
customer support
incident response
feature planning

Change cycle

Observe
 ↓
Identify problem
 ↓
Document
 ↓
Design change
 ↓
Implement
 ↓
Test
 ↓
Deploy
 ↓
Monitor

---

23. PHASE DEPENDENCY RULE

Every phase depends on the previous foundation.

P0 ─→ P1 ─→ P2 ─→ P3 ─→ P4 ─→ P5
                         │
                         ├─→ P6
                         │
                         └─→ P7
                                │
                                ▼
                               P8
                                │
                                ▼
                               P9
                                │
                                ▼
                               P10
                                │
                                ▼
                               P11
                                │
                                ▼
                         P12 ─→ P13
                                │
                                ▼
                               P14
                                │
                                ▼
                               P15
                                │
                                ▼
                               P16

A dependency may not be bypassed merely to make a demo appear complete.

---

24. PHASE GATE SYSTEM

Every phase receives one of these statuses:

NOT STARTED
IN PROGRESS
BLOCKED
READY FOR REVIEW
VERIFIED
COMPLETE

Only:

VERIFIED

or:

COMPLETE

allows the project to move to the next phase.

---

25. STANDARD WORKFLOW FOR EVERY PHASE

For every phase we follow:

STEP 1
Read architecture

STEP 2
Inspect current code

STEP 3
Identify what already exists

STEP 4
Define exact change

STEP 5
Implement smallest correct unit

STEP 6
Test it

STEP 7
Review security implications

STEP 8
Update documentation

STEP 9
Run Git diff/status

STEP 10
Commit

STEP 11
Push

STEP 12
Verify clean working tree

STEP 13
Move to next phase

---

26. STANDARD GIT CHECKPOINT

After a completed phase:

git status
git diff
git add <files>
git commit -m "<type>: <description>"
git push origin main
git status

Expected final state:

working tree clean
branch synchronized with origin

---

27. HOW WE WILL WORK TOGETHER

The development process will be:

ROADMAP
   ↓
CURRENT PHASE
   ↓
TASK
   ↓
COMMAND
   ↓
RESULT
   ↓
ANALYSIS
   ↓
FIX / IMPLEMENT
   ↓
TEST
   ↓
COMMIT
   ↓
NEXT TASK

We do not randomly jump ahead.

For example:

Current Phase = Database

We finish the database foundation first.

We do not simultaneously begin:

M-Pesa
Admin Dashboard
Notifications
Customer Portal

just because those are exciting.

Those depend on earlier foundations.

---

28. JUNIOR-DEVELOPER OPERATING RULE

While developing KDCN Store, every implementation should be understandable.

For every new file, we should be able to answer:

Why does this file exist?
Who uses it?
What does it own?
What does it depend on?
What depends on it?

For every database table:

Why does this table exist?
What entity does it represent?
What references it?
What references does it contain?

For every API endpoint:

Who calls it?
What input does it accept?
What does it return?
What can fail?
Who is authorized?

For every feature:

What business problem does it solve?

This keeps the project teachable as well as production-oriented.

---

29. ANTI-CONFUSION RULE

Never leave multiple unfinished architectures competing.

There must be one current answer.

Architecture document
        ↓
Current implementation
        ↓
Tests
        ↓
Git history

If implementation differs from documented architecture:

STOP
 ↓
determine which is correct
 ↓
update architecture OR implementation
 ↓
test
 ↓
commit

Never silently let both versions coexist.

---

30. FEATURE REQUEST RULE

Every new feature goes through:

REQUEST
 ↓
IMPACT CHECK
 ↓
ARCHITECTURE CHECK
 ↓
DEPENDENCY CHECK
 ↓
IMPLEMENT
 ↓
TEST
 ↓
DOCUMENT
 ↓
COMMIT

Example:

"Add discount codes"

We do not immediately start coding.

First determine:

Does the commerce model support discounts?
Does the database need a new entity?
Does pricing logic change?
Does checkout change?
Does admin need management?
Does auditing need updates?
Does payment calculation change?

Then implement.

---

31. CURRENT WORK QUEUE

Immediately after the architecture lock, the project queue is:

[1] Inspect existing catalog sources
    ↓
[2] Define canonical 16-service catalog
    ↓
[3] Resolve fixed-price vs quote services
    ↓
[4] Design database entities
    ↓
[5] Create schema.sql
    ↓
[6] Create first migration
    ↓
[7] Validate schema

Only after these are completed do we proceed to the API.

---

32. WHAT "DONE" MEANS

A feature is not done because:

the page loads

or:

the API responds

or:

the code compiles

Done means:

FUNCTIONAL
+
CORRECT
+
SECURE
+
TESTED
+
DOCUMENTED
+
COMMITTED

---

33. RELEASE LEVELS

We will use three conceptual release levels.

Development

Code is being built.

Staging

System is integrated and testable.

Production

System is approved for real customers and transactions.

Never confuse:

"works on my phone"

with:

"production ready"

---

34. ARCHITECTURAL NORTH STAR

The finished system is:

                    KDCN STORE
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
    STOREFRONT        ADMIN           ASSETS
      docs/           admin/        asset pipeline
        │               │
        └───────┬───────┘
                │
                ▼
           COMMERCE API
             backend/
                │
       ┌────────┼────────┐
       │        │        │
       ▼        ▼        ▼
    Catalog   Orders    Quotes
       │        │        │
       └────────┼────────┘
                │
                ▼
             Payments
                │
                ▼
           Fulfillment
                │
                ▼
            Deliverables
                │
                ▼
             Customer

                │
                ▼
           Cloudflare D1

                │
                ▼
            Audit Trail

---

35. THE RULE FROM THIS POINT FORWARD

The project is no longer:

"Let's see what we can build."

It is:

"Let's implement the defined system."

The roadmap is the navigation map.

The architecture is the engineering contract.

The code is the implementation.

The tests are the proof.

Git is the checkpoint.

---

36. CURRENT STATUS BOARD

PHASE 0   Repository Baseline          ✅ COMPLETE
PHASE 1   Architecture Lock            ✅ COMPLETE
PHASE 2   Catalog & Business Rules     ⏳ NEXT
PHASE 3   Database Foundation          ⏳
PHASE 4   Backend/API                  ⏳
PHASE 5   Catalog Integration          ⏳
PHASE 6   Customer & Orders            ⏳
PHASE 7   Quote System                 ⏳
PHASE 8   Checkout & Payment           ⏳
PHASE 9   Fulfillment & Tracking       ⏳
PHASE 10  Admin Operations             ⏳
PHASE 11  Notifications                ⏳
PHASE 12  Security Hardening           ⏳
PHASE 13  Testing & QA                 ⏳
PHASE 14  Deployment                   ⏳
PHASE 15  Production Readiness         ⏳
PHASE 16  Operations                   ⏳

---

37. FIRST NEXT STEP

The next phase is:

PHASE 2 — CATALOG & BUSINESS RULES
Objective

Define the actual KDCN commercial catalogue before designing the database around it.

This is where we stop talking about generic products and work with the real 16 KDCN services.

Tasks

Inspect:

KDCN-store-pic/service-catalog.csv
docs/js/services.js
docs/services/*.html

Determine for every service:

service ID
slug
name
tier
pricing model
price
currency
status
requirements
delivery information
asset

Required classification

Every service must be:

FIXED PRICE

or:

QUOTE

No ambiguous services.

Deliverable

Canonical service catalogue specification.

Exit criteria

We can answer:

How many services?
Which tier?
Which price?
Which pricing model?
Which requirements?
Which image?
Which status?

without checking five different files.

Git checkpoint

git add .
git commit -m "docs: define KDCN service catalog model"
git push origin main

---

9. PHASE 3 — DATABASE FOUNDATION

Objective

Turn the business model into a controlled persistence model.

Main entities

Initial target:

services
service_requirements

customers

orders
order_items

quotes
quote_items

payments

projects
deliverables

audit_logs

Tasks

Design:

primary keys
foreign keys
constraints
indexes
timestamps
status fields
money representation
relationships

Deliverables

database/schema.sql
database/migrations/001_initial.sql

Potential additional migrations follow only when justified.

Validation

We verify:

service uniqueness
order integrity
quote integrity
payment relationships
customer relationships
valid state values

Exit criteria

Database can represent:

service
customer
order
quote
payment
project
audit event

without hacks.

Git checkpoint

git add database/
git commit -m "feat: establish KDCN commerce database schema"
git push origin main

---

10. PHASE 4 — BACKEND/API FOUNDATION

Objective

Create the secure application layer between the frontend and database.

Responsibilities

routing
validation
database access
business rules
error handling
authentication
authorization
logging

Target conceptual structure

backend/
├── api/
├── auth/
├── catalog/
├── customers/
├── orders/
├── quotes/
├── payments/
├── fulfillment/
├── notifications/
└── index.ts

First API capability

Start with:

GET /api/services
GET /api/services/:slug

Then expand.

Exit criteria

The backend can:

connect to D1
query safely
return valid responses
reject invalid requests
handle errors

without exposing database internals.

Git checkpoint

git add backend/
git commit -m "feat: establish KDCN commerce API foundation"
git push origin main

---

11. PHASE 5 — SERVICE CATALOG INTEGRATION

Objective

Connect the real service catalogue to the storefront.

Current architecture

services.js
   ↓
browser

Target architecture

D1
 ↓
Backend API
 ↓
Storefront

Implementation strategy

Do not destroy the working storefront.

Instead:

existing UI
   ↓
API-backed data

The visual structure may remain largely unchanged.

Tasks

Connect:

service listing
service filtering
service details
pricing
tier information
availability/status

Exit criteria

The storefront successfully consumes authoritative catalog data.

Git checkpoint

feat: connect storefront to service catalog API

---

12. PHASE 6 — CUSTOMER & ORDER SYSTEM

Objective

Implement the first real commerce workflow.

Customer flow

Customer
 ↓
Select service
 ↓
Checkout
 ↓
Customer information
 ↓
Order creation

API capabilities

Conceptually:

POST /api/orders
GET  /api/orders/:id
GET  /api/customer/orders

Order validation

Backend must verify:

service exists
service is active
service is fixed-price
price is authoritative
customer data valid
order total correct

Exit criteria

A valid customer can create an order without payment yet being involved.

Git checkpoint

feat: implement KDCN order workflow

---

13. PHASE 7 — QUOTE SYSTEM

Objective

Implement the second commercial workflow.

Quote process

Customer
 ↓
Request Quote
 ↓
Requirements
 ↓
Quote Request
 ↓
Admin Review
 ↓
Quote Issued
 ↓
Customer Accepts

API capabilities

Conceptually:

POST /api/quotes
GET  /api/quotes/:id
POST /api/quotes/:id/accept

Exit criteria

A quote can be:

requested
reviewed
issued
accepted
declined
expired

and accepted quotes can later become orders.

Git checkpoint

feat: implement KDCN quote workflow

---

14. PHASE 8 — CHECKOUT & PAYMENT

Objective

Connect commerce transactions to payment processing.

Primary planned provider

M-Pesa Daraja

Architecture

Customer
 ↓
Checkout
 ↓
Backend
 ↓
M-Pesa
 ↓
Callback
 ↓
Backend verification
 ↓
Payment confirmed
 ↓
Order marked PAID

Critical rule

Never implement:

browser says paid
↓
order = paid

Instead:

provider confirmation
↓
server verification
↓
payment record
↓
order update

Required controls

callback validation
idempotency
duplicate prevention
payment reference
failure handling
logging

Exit criteria

Test payments work correctly in the intended non-production environment.

Git checkpoint

feat: integrate M-Pesa payment workflow

---

15. PHASE 9 — FULFILLMENT & CUSTOMER TRACKING

Objective

Connect paid orders to actual service delivery.

Flow

PAID
 ↓
IN_PROGRESS
 ↓
DELIVERED
 ↓
COMPLETED

Project relationship

Order
 ↓
Project
 ↓
Work
 ↓
Deliverable

Customer visibility

Customer should eventually see:

order number
service
payment status
order status
progress
delivery information

Exit criteria

The system can track a service after payment through completion.

---

16. PHASE 10 — ADMIN OPERATIONS

Objective

Build the internal operating console.

Admin modules

Dashboard
Services
Customers
Orders
Quotes
Payments
Fulfillment
Audit Logs
Settings

Admin operations

Authorized personnel can:

manage services
review orders
review quote requests
issue quotes
monitor payments
manage fulfillment
inspect audit records

Security principle

Frontend restrictions are not authorization.

The API must enforce permissions.

Exit criteria

An authorized administrator can operate the core commerce lifecycle without database-level manual intervention.

---

17. PHASE 11 — NOTIFICATIONS & COMMUNICATIONS

Objective

Automate customer communication around important business events.

Notifications

Potential events:

order created
payment received
payment failed
quote issued
quote accepted
work started
service completed
delivery available

Channels

Email
WhatsApp
Other approved channels

Communication remains separate from authoritative transaction state.

---

18. PHASE 12 — SECURITY HARDENING

Objective

Attack the system before attackers do.

Review areas

authentication
authorization
input validation
SQL safety
rate limiting
CSRF where applicable
secure cookies
headers
secret management
payment callbacks
admin access
logging

Attack scenarios

Test:

tampered price
tampered order ID
unauthorized admin request
fake payment callback
replayed callback
invalid quote acceptance
invalid status transition
malicious input
excessive requests

Exit criteria

Known security controls are implemented and verified.

Git checkpoint

test: harden KDCN commerce security controls

---

19. PHASE 13 — TESTING & QUALITY ASSURANCE

Objective

Verify the whole system before production.

Testing levels

Unit

pricing
validation
state transitions
authorization

Integration

API + D1
orders + payments
quotes + orders

End-to-end

browse
 ↓
order
 ↓
checkout
 ↓
payment
 ↓
confirmation

and:

browse
 ↓
quote
 ↓
review
 ↓
accept
 ↓
payment
 ↓
order

Quality checks

Also test:

mobile
desktop
navigation
forms
SEO
broken links
performance
accessibility
error handling

Exit criteria

Critical customer and admin journeys pass.

---

20. PHASE 14 — DEPLOYMENT & INFRASTRUCTURE

Objective

Prepare the system for controlled deployment.

Environment model

LOCAL
   ↓
STAGING
   ↓
PRODUCTION

Infrastructure

Cloudflare
Cloudflare Workers
Cloudflare D1
DNS
Secrets
Logging

"wrangler.jsonc"

Must correctly represent the deployment architecture without embedding production secrets.

Exit criteria

Staging environment works independently and predictably.

---

21. PHASE 15 — PRODUCTION READINESS

Objective

Prove that the system is safe to operate in production.

Checklist

DNS verified
HTTPS verified
Worker deployed
D1 production database ready
secrets configured
payment integration verified
logging enabled
backups defined
recovery procedure documented
monitoring available
legal pages available
robots.txt verified
sitemap verified
error pages verified
security review completed

Operational test

Simulate:

normal order
failed payment
duplicate callback
quote request
quote acceptance
service completion
administrator action

Final gate

No production release without passing the production-readiness checklist.

---

22. PHASE 16 — OPERATIONS & CONTINUOUS IMPROVEMENT

Objective

Move from development to sustainable operation.

Ongoing responsibilities

monitoring
backups
security reviews
dependency updates
database maintenance
performance review
customer support
incident response
feature planning

Change cycle

Observe
 ↓
Identify problem
 ↓
Document
 ↓
Design change
 ↓
Implement
 ↓
Test
 ↓
Deploy
 ↓
Monitor

---

23. PHASE DEPENDENCY RULE

Every phase depends on the previous foundation.

P0 ─→ P1 ─→ P2 ─→ P3 ─→ P4 ─→ P5
                         │
                         ├─→ P6
                         │
                         └─→ P7
                                │
                                ▼
                               P8
                                │
                                ▼
                               P9
                                │
                                ▼
                               P10
                                │
                                ▼
                               P11
                                │
                                ▼
                         P12 ─→ P13
                                │
                                ▼
                               P14
                                │
                                ▼
                               P15
                                │
                                ▼
                               P16

A dependency may not be bypassed merely to make a demo appear complete.

---

24. PHASE GATE SYSTEM

Every phase receives one of these statuses:

NOT STARTED
IN PROGRESS
BLOCKED
READY FOR REVIEW
VERIFIED
COMPLETE

Only:

VERIFIED

or:

COMPLETE

allows the project to move to the next phase.

---

25. STANDARD WORKFLOW FOR EVERY PHASE

For every phase we follow:

STEP 1
Read architecture

STEP 2
Inspect current code

STEP 3
Identify what already exists

STEP 4
Define exact change

STEP 5
Implement smallest correct unit

STEP 6
Test it

STEP 7
Review security implications

STEP 8
Update documentation

STEP 9
Run Git diff/status

STEP 10
Commit

STEP 11
Push

STEP 12
Verify clean working tree

STEP 13
Move to next phase

---

26. STANDARD GIT CHECKPOINT

After a completed phase:

git status
git diff
git add <files>
git commit -m "<type>: <description>"
git push origin main
git status

Expected final state:

working tree clean
branch synchronized with origin

---

27. HOW WE WILL WORK TOGETHER

The development process will be:

ROADMAP
   ↓
CURRENT PHASE
   ↓
TASK
   ↓
COMMAND
   ↓
RESULT
   ↓
ANALYSIS
   ↓
FIX / IMPLEMENT
   ↓
TEST
   ↓
COMMIT
   ↓
NEXT TASK

We do not randomly jump ahead.

For example:

Current Phase = Database

We finish the database foundation first.

We do not simultaneously begin:

M-Pesa
Admin Dashboard
Notifications
Customer Portal

just because those are exciting.

Those depend on earlier foundations.

---

28. JUNIOR-DEVELOPER OPERATING RULE

While developing KDCN Store, every implementation should be understandable.

For every new file, we should be able to answer:

Why does this file exist?
Who uses it?
What does it own?
What does it depend on?
What depends on it?

For every database table:

Why does this table exist?
What entity does it represent?
What references it?
What references does it contain?

For every API endpoint:

Who calls it?
What input does it accept?
What does it return?
What can fail?
Who is authorized?

For every feature:

What business problem does it solve?

This keeps the project teachable as well as production-oriented.

---

29. ANTI-CONFUSION RULE

Never leave multiple unfinished architectures competing.

There must be one current answer.

Architecture document
        ↓
Current implementation
        ↓
Tests
        ↓
Git history

If implementation differs from documented architecture:

STOP
 ↓
determine which is correct
 ↓
update architecture OR implementation
 ↓
test
 ↓
commit

Never silently let both versions coexist.

---

30. FEATURE REQUEST RULE

Every new feature goes through:

REQUEST
 ↓
IMPACT CHECK
 ↓
ARCHITECTURE CHECK
 ↓
DEPENDENCY CHECK
 ↓
IMPLEMENT
 ↓
TEST
 ↓
DOCUMENT
 ↓
COMMIT

Example:

"Add discount codes"

We do not immediately start coding.

First determine:

Does the commerce model support discounts?
Does the database need a new entity?
Does pricing logic change?
Does checkout change?
Does admin need management?
Does auditing need updates?
Does payment calculation change?

Then implement.

---

31. CURRENT WORK QUEUE

Immediately after the architecture lock, the project queue is:

[1] Inspect existing catalog sources
    ↓
[2] Define canonical 16-service catalog
    ↓
[3] Resolve fixed-price vs quote services
    ↓
[4] Design database entities
    ↓
[5] Create schema.sql
    ↓
[6] Create first migration
    ↓
[7] Validate schema

Only after these are completed do we proceed to the API.

---

32. WHAT "DONE" MEANS

A feature is not done because:

the page loads

or:

the API responds

or:

the code compiles

Done means:

FUNCTIONAL
+
CORRECT
+
SECURE
+
TESTED
+
DOCUMENTED
+
COMMITTED

---

33. RELEASE LEVELS

We will use three conceptual release levels.

Development

Code is being built.

Staging

System is integrated and testable.

Production

System is approved for real customers and transactions.

Never confuse:

"works on my phone"

with:

"production ready"

---

34. ARCHITECTURAL NORTH STAR

The finished system is:

                    KDCN STORE
                        │
        ┌───────────────┼────────────────┐
        │               │                │
        ▼               ▼                ▼
    STOREFRONT        ADMIN           ASSETS
      docs/           admin/        asset pipeline
        │               │
        └───────┬───────┘
                │
                ▼
           COMMERCE API
             backend/
                │
       ┌────────┼────────┐
       │        │        │
       ▼        ▼        ▼
    Catalog   Orders    Quotes
       │        │        │
       └────────┼────────┘
                │
                ▼
             Payments
                │
                ▼
           Fulfillment
                │
                ▼
            Deliverables
                │
                ▼
             Customer

                │
                ▼
           Cloudflare D1

                │
                ▼
            Audit Trail

---

35. THE RULE FROM THIS POINT FORWARD

The project is no longer:

"Let's see what we can build."

It is:

"Let's implement the defined system."

The roadmap is the navigation map.

The architecture is the engineering contract.

The code is the implementation.

The tests are the proof.

Git is the checkpoint.

---

36. CURRENT STATUS BOARD

PHASE 0   Repository Baseline          ✅ COMPLETE
PHASE 1   Architecture Lock            ✅ COMPLETE
PHASE 2   Catalog & Business Rules     ⏳ NEXT
PHASE 3   Database Foundation          ⏳
PHASE 4   Backend/API                  ⏳
PHASE 5   Catalog Integration          ⏳
PHASE 6   Customer & Orders            ⏳
PHASE 7   Quote System                 ⏳
PHASE 8   Checkout & Payment           ⏳
PHASE 9   Fulfillment & Tracking       ⏳
PHASE 10  Admin Operations             ⏳
PHASE 11  Notifications                ⏳
PHASE 12  Security Hardening           ⏳
PHASE 13  Testing & QA                 ⏳
PHASE 14  Deployment                   ⏳
PHASE 15  Production Readiness         ⏳
PHASE 16  Operations                   ⏳

---

37. FIRST NEXT STEP

The next phase is:

PHASE 2 — CATALOG & BUSINESS RULES

The first job inside that phase is:

Inspect the existing KDCN service catalogue

Sources:

KDCN-store-pic/service-catalog.csv
docs/js/services.js
docs/services/*.html

From those sources we will establish the canonical:

16 SERVICES
4 TIERS
FIXED-PRICE SERVICES
QUOTE SERVICES
PRICES
REQUIREMENTS
STATUSES
ASSET REFERENCES

That catalogue becomes the foundation for the database schema.

---

38. ROADMAP LOCK

This roadmap is the governing development sequence for KDCN Store v1.

Changes to the sequence should occur only when:

new technical information
security requirements
business requirements
or implementation constraints

justify the change.

When the sequence changes, the roadmap should be updated before the project silently drifts.

END OF KDCN-STORE MASTER DEVELOPMENT ROADMAP v1.0
