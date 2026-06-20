# Deterministic Workflow Module

Use this module when work crosses durable steps, may pause, retry, wait for human
approval, or resume after a process failure.

## Fit Check

Do not introduce a workflow abstraction when the operation can finish safely in
one short request or database transaction.

Use a database-backed state machine first when:

- steps are few and owned by one application
- throughput is moderate
- delays and retries are simple
- operators can recover work through an admin action

Evaluate a durable workflow engine only when workflows are long-running,
high-volume, cross-service, timer-heavy, or difficult to recover correctly with
the database approach.

## Stable Defaults

- Give every workflow instance a durable identifier and explicit version.
- Define states and allowed transitions before implementation.
- Make each retryable step idempotent.
- Persist state before acknowledging completion.
- Distinguish retryable, terminal, cancelled, and manual-review failures.
- Use bounded retries with backoff and a terminal recovery path.
- Record attempts and operator actions in an execution log.
- Pin an instance to the workflow definition version it started with.
- Model compensation explicitly; do not imply that distributed rollback exists.

## Questions That Require Human Decisions

1. Which step begins the workflow and what proves it completed?
2. Which steps have external side effects?
3. How long may an instance wait or run?
4. Which failures retry, stop, compensate, or require human review?
5. Can an operator cancel, resume, replay, or skip a step?
6. What happens to active instances when the workflow definition changes?

## Required Governance Content

### SPEC

Define the user-visible lifecycle, waiting states, cancellation, progress,
failure messaging, manual approval, and recovery expectations.

### ARCH

Define the workflow owner, persisted state, queue or scheduler boundary,
idempotency strategy, retry policy, timers, execution log, compensation,
versioning, and operator controls.

### RULES

Require explicit transitions, idempotent steps, bounded retries, durable attempt
records, authenticated operator actions, and tests that resume after failure.
Prohibit unbounded polling and in-memory-only state for durable work.

### CONTRACTS

Create `docs/CONTRACTS/workflow.md`. Define states, events, step input/output,
failure classes, retry policy, idempotency keys, cancellation, and versioning.

## Outbox Rule

When a database change and an event publication must appear atomic, store the
event in an outbox in the same transaction, then publish asynchronously. Make
consumers idempotent because delivery may occur more than once.

## Verification Baseline

At minimum verify:

- every allowed and forbidden transition
- duplicate delivery or repeated execution
- process failure between state persistence and acknowledgement
- retry exhaustion and manual recovery
- cancellation while waiting and while executing
- old instances continuing under their original workflow version
- authorization of operator actions

