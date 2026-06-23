# Wiki: Record CRUD Apps

This page explains the engineering shape behind products that manage business
objects: customers, leads, orders, bookings, inventory, documents, tickets,
content, feedback, and CRM-style workflows.

For the skill, this is usually the `transactional-record-system` profile. For
the founder, it often feels like "a simple app with forms and lists." The
important lesson is that forms and lists become durable business memory. Once
real users depend on that memory, schema, ownership, deletion, and export rules
matter.

## What The Founder Sees

- A form creates an item.
- A list helps people find items.
- A detail page shows one item.
- A status or tag tells people what to do next.
- An export gets data out when the product is not enough yet.

## What The System Must Know

- Which record is the source of truth.
- Who owns each record.
- Which fields are required and why.
- Which actions are allowed at each lifecycle state.
- Which data can be edited, archived, restored, exported, or permanently erased.
- Which users can read or mutate which records.
- Which invariants belong in the database, not only in UI code.

## MVP Shape

Start with one primary record. Add only the supporting records needed for the
first workflow.

A useful first slice is:

1. create the record
2. validate required fields
3. persist it
4. list it with deterministic ordering
5. view one detail page
6. export the data

This is not "just CRUD" once ownership, validation, lifecycle, and export are
defined. It is the smallest durable product core.

## Common Mistakes

- Treating update as "any field can change any time".
- Hiding the only business rule in frontend code.
- Adding hard delete before retention and restore expectations are clear.
- Shipping search and dashboards before the record model is stable.
- Changing schema without migration discipline.
- Adding AI summary over records before deciding what data may leave the app.

## Engineering Concepts To Learn

- **Schema**: the shape of stored data.
- **Migration**: the forward-only change to that shape.
- **Invariant**: something that must never become false.
- **Lifecycle**: allowed states and transitions.
- **Authorization**: who may read or change each record.
- **Pagination**: predictable list retrieval as data grows.
- **Import/export contract**: stable file shape that lets data move safely.

## When To Upgrade

Upgrade the architecture when:

- more than one actor edits the same record concurrently
- records affect money, entitlement, inventory, or legal status
- customers need API access
- imports or exports become central workflows
- data retention or deletion becomes a promise
- the product needs audit history

Do not upgrade just because the UI has many screens. Upgrade when data
correctness, ownership, or external dependency pressure increases.

## Skill Assets

- `references/profile-transactional-record-system.md`
- `assets/module-overlays/transactional-record-system.md`
- `assets/templates/record-crud.md`
- `assets/contracts-examples/openapi-rest.yaml`
- `assets/contracts-examples/db-schema.sql`
- `assets/contracts-examples/file-format.md`

## Research Anchors

- Twenty models CRM-like products as objects, fields, views, workflows, and
  versioned app code: https://github.com/twentyhq/twenty
- Supabase centers MVP backends on Postgres, auth, storage, and generated APIs:
  https://github.com/supabase/supabase
