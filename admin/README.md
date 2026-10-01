# KDCN Store Administration

This directory contains administrative resources for KDCN Store.

## Purpose

The `admin/` directory defines and organizes resources used to operate,
manage, configure, and administer the KDCN Store system.

## Boundaries

- Application/server logic belongs in `backend/`.
- Database schemas and database resources belong in `database/`.
- Public and application assets belong in `assets/`.
- Project documentation belongs in `docs/`.
- Generated reports belong in `report/`.
- Automation and build tooling belong in `scripts/`.
- Tests belong in `tests/`.

## Security

Do not store secrets, credentials, API keys, private tokens, passwords,
or production environment secrets in this directory or anywhere else
in the Git repository.

Administrative configuration must use the appropriate environment or
secret-management mechanism where sensitive values are involved.
