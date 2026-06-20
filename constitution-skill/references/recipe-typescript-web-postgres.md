# Recipe: TypeScript Web With PostgreSQL

Status: Recommended default for a conventional new web product
Last Reviewed: 2026-06-20

This is a replaceable implementation recipe, not a permanent architecture rule.
Use it only after the fit check passes.

## Fit Check

Use this recipe when:

- the project is a browser-based product or internal tool
- one deployable application is sufficient
- durable relational data is central
- the team has no existing stack to preserve
- the first release does not require native mobile, hard real-time processing,
  offline-first synchronization, or extreme compute workloads

Do not use it merely because it is the shipped default. Record deviations in
`ARCH.md`.

## Recommended Stack

| Concern | Default | Reason |
| --- | --- | --- |
| Language | TypeScript with strict checks | shared types and one primary language |
| Web application | Next.js App Router | integrated UI and server application |
| Database | PostgreSQL | relational constraints and transactions |
| Schema/migrations | Drizzle ORM and versioned SQL migrations | explicit schema and reviewable changes |
| Runtime validation | Zod | validate inputs and model outputs at runtime |
| Unit/integration tests | Vitest | fast application-level checks |
| Browser tests | Playwright | verify critical user workflows |
| API description | OpenAPI when external consumers exist | machine-readable public contract |
| Local environment | provider-independent environment variables | portable configuration |

Pin exact dependency versions in the generated project lockfile, not in this
recipe. Prefer current stable releases compatible with the chosen runtime.

## Application Shape

Start with one deployable application and one PostgreSQL database. Separate
presentation, application operations, domain rules, and persistence in code,
but do not create independent services without an operational reason.

Use server-side operations for trusted mutations. Validate all external input at
the boundary. Keep database access behind application-owned query and command
modules. Treat browser code as untrusted.

## Optional Modules

### Identity And Access

Prefer a maintained identity provider or Auth.js-compatible integration. Keep an
application-owned user record and authorization policy so provider replacement
does not rewrite domain ownership.

### LLM Boundary

Use the provider's maintained SDK behind an application-owned interface. Validate
structured output with Zod and persist normalized execution metadata in
PostgreSQL. Do not add an agent framework for a single bounded model call.

### Background Work

Begin with database-backed jobs and explicit status when work is modest. Adopt a
queue or durable workflow engine only after retries, throughput, timers, or
cross-service coordination justify it.

## Mandatory Architecture Decisions

Before implementation, record:

- hosting and database provider
- data region and backup expectations
- identity provider and session strategy, if applicable
- file/object storage provider, if applicable
- email/SMS provider status: planned, fake, or active
- LLM provider, data retention, and budget, if applicable
- migration and rollback ownership

## Escape Hatches

Reconsider the recipe when native device APIs, offline-first conflict handling,
strict regional deployment, sustained compute-heavy jobs, independent service
scaling, or an existing organizational stack dominates the design.

Review this recipe when a major framework lifecycle changes, a dependency enters
maintenance-only status, security guidance changes, or 180 days have elapsed.

