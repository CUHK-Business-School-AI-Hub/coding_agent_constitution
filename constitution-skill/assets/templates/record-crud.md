# Template: Record CRUD Surface

Status: Latent asset
Use when mentioned, do not present as a new mode.

## Trigger Signals

Use this template when the user describes a product around customers, leads,
orders, inventory, bookings, documents, tickets, content, feedback, CRM, admin
screens, forms, lists, filters, dashboards, imports, exports, or "CRUD".

This template usually composes with:

- Base profile: `transactional-record-system`
- Capability modules: `identity-access` when users own private data or roles
  differ
- Capability modules: `llm-boundary` when AI summarizes, classifies, extracts,
  or drafts from records
- Technology recipe: existing stack first; otherwise the reviewed recipe that
  fits deployment and persistence needs

## Quiet Use Rule

Do not ask the human to choose this template. Infer it from the product language,
apply only the relevant defaults, and record the resulting product shape in
`ARCH.md`.

## MVP Defaults

- Start with one primary record and at most two supporting records.
- Ship list, create, detail, edit, archive, and export before bulk automation.
- Prefer archive over hard delete until retention expectations are explicit.
- Model important mutations as named actions instead of raw field updates.
- Add search and filters only for fields the first workflow actually uses.
- Require deterministic ordering and pagination before data volume grows.
- Treat CSV/JSONL import and export as contracts, not UI conveniences.
- Add server-side authorization before exposing private records to multiple
  users.

## SPEC Snippet

```markdown
### Record Workflow

- Primary record:
- Supporting records:
- Who creates records:
- Who can view or edit:
- Required lifecycle states:
- Archive/delete expectation:
- Import/export expectation:
- First useful dashboard or list:
```

## ARCH Snippet

```markdown
### Record Model

- Source of truth:
- Record owner:
- Immutable identifiers:
- Uniqueness rules:
- Named mutation commands:
- Transaction boundaries:
- Retention and export:
```

## CONTRACT Snippet

Create or update the relevant API, database, CLI, or file-format contract with:

- create input and validation errors
- update or named-action semantics
- list filters, sort order, and pagination
- record lifecycle transition table
- export/import schema and compatibility rules

## Task Slicing

Good first slices:

- Create the primary record with validation and persistence.
- Add list/detail views with deterministic ordering.
- Add one named lifecycle action.
- Add export for the primary record.

Split when a task touches schema, auth, UI, import/export, and background jobs
at the same time.

## Approval Triggers

Require explicit human approval for:

- destructive deletion or permanent purge
- schema changes that affect existing data
- ownership or authorization rule changes
- money, entitlement, legal status, inventory, or accounting semantics
- public API compatibility promises
