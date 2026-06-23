# Template: Linear Workflow Surface

Status: Latent asset
Use when mentioned, do not present as a new mode.

## Trigger Signals

Use this template when the user describes intake, approval, review, onboarding,
fulfillment, quoting, scheduling, handoff, queue, retry, step-by-step processing,
"move it through stages", "pipeline", or "workflow".

This template usually composes with:

- Base profile: `transactional-record-system` when each workflow instance is a
  durable business record
- Capability module: `deterministic-workflow` when the work can pause, retry,
  wait for approval, resume after failure, or create external side effects
- Capability module: `identity-access` when different actors own different steps
- Capability module: `llm-boundary` only for model-assisted steps, not for the
  workflow itself

## Quiet Use Rule

Do not ask the human to choose this template. Infer it from lifecycle language.
If the process fits in one synchronous request or one database transaction, use
record lifecycle states without selecting `deterministic-workflow`.

## MVP Defaults

- Start with a database-backed state machine before adding a workflow engine.
- Define the smallest state list that users must see.
- Make every transition explicit: actor, trigger, guard, side effect, result.
- Persist state before notifying users or external systems.
- Treat email, webhook, payment, calendar, and document generation as external
  side effects.
- Prefer manual recovery controls over invisible automatic repair in the first
  MVP.
- Add retries only where duplicate execution is safe or idempotency exists.

## SPEC Snippet

```markdown
### Workflow Experience

- Start condition:
- User-visible states:
- Who can move it forward:
- Waiting or approval states:
- Cancellation expectation:
- Failure message:
- Manual recovery expectation:
```

## ARCH Snippet

```markdown
### Workflow State

- Workflow owner:
- Persisted state table:
- Allowed transitions:
- Side-effecting steps:
- Idempotency strategy:
- Retry policy:
- Operator controls:
```

## CONTRACT Snippet

Create or update `docs/CONTRACTS/workflow.md` when the workflow is durable:

- states and transitions
- step inputs and outputs
- retryable and terminal failures
- idempotency keys
- cancellation rules
- operator actions and audit events

## Task Slicing

Good first slices:

- Add the workflow record and initial state.
- Implement one transition with authorization and tests.
- Add a visible status timeline.
- Add one retryable side-effect step behind an outbox.

Split when a task changes multiple transitions, multiple side effects, and UI
recovery behavior at once.

## Approval Triggers

Require explicit human approval for:

- skipping, replaying, or force-completing user-visible work
- side effects that send messages, spend money, create legal obligations, or
  change external systems
- changing the meaning of active states after users have live instances
- deleting execution history or operator audit logs
