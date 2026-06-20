# Transactional Record System Profile

Use this profile when durable business records are the product's source of
truth. Examples include ledgers, bookings, orders, inventory items, support
cases, documents, and administrative tools.

## Stable Defaults

- Use a relational database as the authoritative store.
- Model business actions as named commands, not unrestricted field updates.
- Define lifecycle states and allowed transitions before implementation.
- Enforce invariants in the database when the database can express them.
- Use transactions for changes that must succeed or fail together.
- Keep timestamps in UTC and define the business timezone separately.
- Prefer immutable identifiers; do not expose sequential IDs when enumeration is
  a risk.
- Use soft deletion only when restore, retention, or audit requirements justify
  its permanent complexity.
- Make list endpoints paginated and deterministically ordered.
- Treat imports, exports, and bulk edits as contracts, not incidental UI code.

## Questions That Change The Design

Ask only what is not discoverable:

1. What is the primary record, and who owns it?
2. Which actions change its lifecycle state?
3. Which fields or relationships must never become inconsistent?
4. Can two users update the same record concurrently?
5. Which records must be retained, exported, restored, or permanently erased?
6. Which operations affect money, inventory, entitlement, or legal status?

## Required Governance Content

### SPEC

Define:

- primary records and user-visible lifecycle
- ownership and sharing behavior
- create, view, update, archive, restore, and delete semantics
- empty, invalid, duplicate, stale, and concurrent-update behavior
- list, search, filter, sort, pagination, import, and export requirements
- retention and deletion expectations

### ARCH

Define:

- source of truth and data ownership
- transaction boundaries
- identifiers and uniqueness rules
- lifecycle state machine
- concurrency strategy: last-write-wins, optimistic version, or serialized update
- migration, backup, restore, and export strategy
- boundary between HTTP/UI handlers and domain operations

### RULES

Require:

- schema changes through reviewed migrations
- authorization on every server-side read and mutation
- database constraints for durable invariants
- idempotency for retryable create or effectful operations
- no direct database access from presentation modules
- tests for invalid transitions and cross-owner access
- explicit approval for destructive migrations or changed financial meaning

### CONTRACTS

Create contracts for:

- API or command inputs and outputs
- database schema and constraints
- lifecycle transitions and transition errors
- import/export file formats
- emitted events when another component consumes them

## Default Architecture Shape

Start with one deployable application split into presentation, application,
domain, and persistence responsibilities. These may be folders rather than
separate packages. Split services only when deployment, scaling, security, or
team ownership requires independent operation.

Handlers may authenticate, validate, and translate transport data. Domain or
application operations own business transitions. Persistence code owns queries
and transactions. UI code must not encode the only copy of an invariant.

## Data And API Rules

- Distinguish omitted fields from explicit `null`.
- Define whether update commands are replace, patch, or named action semantics.
- Return stable error codes separately from human-readable messages.
- Reject unknown lifecycle transitions rather than silently coercing them.
- Use optimistic concurrency for records where lost updates matter.
- Never use floating-point values for money; store integer minor units or an
  exact decimal with an explicit currency.
- Recompute derived totals from authoritative inputs or document when a cached
  value becomes authoritative.

## Verification Baseline

At minimum verify:

- happy-path creation and retrieval
- validation and uniqueness rejection
- cross-owner read and mutation rejection
- every lifecycle transition, including forbidden transitions
- transaction rollback after a mid-operation failure
- pagination stability
- migration forward path and backup/restore procedure when real data exists

## Do Not Generalize

This profile does not provide accounting, inventory, payment, tax, medical, or
legal domain rules. Those require domain-specific contracts and human review.

