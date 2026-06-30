# Task: Bootstrap Feedback Inbox HTTP Skeleton

## Goal

Stand up the Fastify service with health check, request logging, env loading, and a working `POST /v1/feedback` endpoint that persists to Postgres according to the OpenAPI contract. No themes, no tags, no dashboard yet.

## Source Context

- `docs/SPEC.md` Workflow 1 (Customer Submits Feedback).
- `docs/ARCH.md` Module Boundaries (`api/http`, `api/feedback`, `api/persistence`).
- `docs/CONTRACTS/feedback-api.openapi.yaml` `POST /feedback` and `Feedback`, `FeedbackCreate`, `Error` schemas.
- `docs/CONTRACTS/db-schema.sql` `feedback` table only (do not create `tags`, `themes`, `feedback_events` yet).
- `docs/RULES.md` Coding Rules, Testing Rules, Security And Safety Rules.

## Scope

### Touch

- `package.json`, `pnpm-lock.yaml`, `tsconfig.json` (project setup).
- `src/api/http/server.ts` (Fastify bootstrap, request ID, JSON logging).
- `src/api/http/routes/feedback.ts` (POST handler only).
- `src/api/feedback/service.ts` (create-feedback domain function).
- `src/api/persistence/feedback-repo.ts` (insert query).
- `src/api/persistence/migrations/0001_init.sql` (only the `feedback` table).
- `src/config/env.ts` (env loader with zod).
- `tests/api/feedback-post.test.ts` (happy path + 400 validation).
- `tests/integration/feedback-repo.test.ts` (insert + read back).

### Do Not Touch

- Any file under `web/dashboard/`, `cli/`, or `integrations/`.
- Schema for `tags`, `themes`, or `feedback_events`.
- Authentication middleware (the POST endpoint is public per SPEC).
- Production deployment configuration.

### Public Contracts

- Allowed to change: `docs/CONTRACTS/db-schema.sql` only for the initial `feedback` table if the contract and migration stay aligned.
- Forbidden to change: `docs/CONTRACTS/feedback-api.openapi.yaml` endpoint paths, request body, response envelope, and error schema.

## Interfaces

- Consumes: `POST /v1/feedback` request and response schemas from `docs/CONTRACTS/feedback-api.openapi.yaml`; `feedback` table from `docs/CONTRACTS/db-schema.sql`.
- Produces: Fastify route handler, feedback domain service, feedback repository insert function, and initial migration.
- Public contracts touched: `docs/CONTRACTS/db-schema.sql`.
- Downstream tasks relying on this: dashboard list view, CLI list/export, and event outbox tasks.

## Requirements

- Server starts on `PORT` env var (default 3000).
- `GET /healthz` returns 200 with JSON `{"status":"ok"}`.
- `POST /v1/feedback` validates body against `FeedbackCreate` and either returns 201 with `Feedback`, or 400 with `Error` (code `validation_error`).
- Email is stored lowercased; raw email never appears in any log line.
- Request ID header `x-request-id` is propagated; if absent, generate a UUID.
- All logs are structured JSON to stdout.

## Acceptance Criteria

- `curl -fsS -X POST http://localhost:3000/v1/feedback -H 'content-type: application/json' -d '{"source":"web","message":"hello"}'` returns 201 with a JSON body matching `Feedback`.
- `curl -fsS -X POST http://localhost:3000/v1/feedback -H 'content-type: application/json' -d '{"source":"web"}'` returns 400 with `code: validation_error` and a `fields[*]` entry for `message`.
- Logging the same request shows the email field absent or hashed; never raw.
- Unit and integration tests added under the `tests/` paths above pass.

## Verification

- Command: `pnpm lint`
  - Expected evidence: exits 0 with no lint errors.
- Command: `pnpm typecheck`
  - Expected evidence: exits 0 with no TypeScript errors.
- Command: `pnpm test -- tests/api/feedback-post.test.ts tests/integration/feedback-repo.test.ts`
  - Expected evidence: exits 0; happy path, validation-error, and repository insert tests pass.

## Governance Drift Check

- SPEC changed? No; this task implements the existing Customer Submits Feedback workflow.
- ARCH changed? No; this task uses the existing `api/http`, `api/feedback`, and `api/persistence` boundaries.
- CONTRACTS changed? Only `docs/CONTRACTS/db-schema.sql` may be reconciled with the initial migration if needed.
- RULES/AGENTS changed? No expected change; promote any repeated setup/review rule only if discovered during implementation.
- If no durable docs changed, why is that safe? The task is the first implementation slice for already-authored contracts and architecture.

## Risks

- First-time scaffold; lint/test config may need iteration.
- Postgres testcontainer startup may be flaky in CI; fall back to a docker-compose dev DB if needed.

## Handoff Notes

- Cursor should review: that the handler does not call the repo directly, that no `any` types leak, and that error envelope matches `Error` schema exactly.
- Human should decide: choice of token-issuance approach (out of scope for this task but blocks Task 002).
