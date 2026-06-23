# Wiki: Linear Workflows

This page explains the engineering shape behind products that move work through
steps: intake, qualification, approval, review, quoting, fulfillment, scheduling,
onboarding, handoff, and recovery.

For the skill, this may be simple record lifecycle modeling or the
`deterministic-workflow` module. The distinction matters. A workflow is not a UI
wizard. It is durable work that may wait, retry, fail, be cancelled, or require a
person to recover it.

## What The Founder Sees

- A request enters a pipeline.
- Someone reviews or approves it.
- The system sends something, generates something, or notifies someone.
- A status tells everyone where the work is.
- An operator fixes the case when automation fails.

## What The System Must Know

- What starts the workflow.
- Which state proves each step completed.
- Which actor or system can trigger each transition.
- Which steps have external side effects.
- Which failures should retry, stop, cancel, or wait for a human.
- Which actions must be audited.
- What happens to active work when the workflow changes.

## MVP Shape

Start with a database-backed state machine. Do not add a workflow engine until
the process is long-running, high-volume, cross-service, timer-heavy, or hard to
recover with database state.

A useful first slice is:

1. create the workflow record
2. persist the initial state
3. implement one transition
4. enforce who can trigger it
5. show a simple status timeline
6. test allowed and forbidden transitions

Only then add retries, outbox publication, timers, or operator controls.

## Common Mistakes

- Treating state as a label instead of a contract.
- Letting any user move any item to any state.
- Sending emails or webhooks before state is persisted.
- Retrying side effects without idempotency.
- Adding a queue or workflow engine before the state model is understood.
- Changing state meaning while live items are still in old states.

## Engineering Concepts To Learn

- **State machine**: allowed states and transitions.
- **Idempotency**: safe repeated execution of the same operation.
- **Retry policy**: when and how failed work is attempted again.
- **Terminal failure**: a final failed state that needs a recovery path.
- **Outbox**: storing a message in the same transaction as the database change,
  then publishing it later.
- **Compensation**: an explicit follow-up action when external rollback is not
  possible.

## When To Upgrade

Upgrade the architecture when:

- workflow instances run for hours or days
- multiple external services are involved
- timers and retries dominate the behavior
- operators need replay, skip, resume, or force-complete controls
- duplicate side effects are expensive
- volume makes polling or manual recovery unreliable

Do not upgrade because the business process has several steps. Upgrade when
durability, recovery, and side effects become hard to reason about.

## Skill Assets

- `references/module-deterministic-workflow.md`
- `assets/module-overlays/deterministic-workflow.md`
- `assets/templates/linear-workflow.md`
- `assets/contracts-examples/event-payload.md`

## Research Anchors

- Anthropic separates predictable workflows from more open-ended agent behavior:
  https://www.anthropic.com/engineering/building-effective-agents
- The transactional outbox pattern keeps database changes and message
  publication recoverable: https://microservices.io/patterns/data/transactional-outbox.html
