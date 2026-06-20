# Overlay: Deterministic Workflow

Merge applicable sections into `SPEC.md`, `ARCH.md`, and `RULES.md`. Create the
contract section as `docs/CONTRACTS/workflow.md`.

## SPEC Additions

```markdown
### Workflow Lifecycle

- Start condition:
- User-visible states:
- Progress visibility:
- Cancellation:
- Manual approval:
- Failure and recovery experience:
```

## ARCH Additions

```markdown
### Durable Workflow

- Workflow owner:
- Persisted state:
- Queue/scheduler:
- Idempotency key:
- Retry and terminal failure policy:
- Timers and maximum duration:
- Execution log:
- Compensation:
- Versioning of active instances:
- Operator controls:
```

## RULES Additions

```markdown
## Workflow Rules

- Define states and transitions explicitly.
- Make every retryable step idempotent.
- Bound retries and provide a terminal recovery path.
- Persist durable state before acknowledging completion.
- Authenticate and audit operator actions.
- Keep active instances pinned to their starting workflow version.
- Never rely on in-memory-only state for durable work.
```

## Contract Template

```markdown
# Workflow Contract

Status: Active
Last Reviewed: YYYY-MM-DD
Owner: `<module/team>`
Workflow Version: `1`

## States And Transitions

| From | Trigger | To | Guard | Side Effect |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Steps

| Step | Input | Output | Idempotency Key | Timeout |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Failure Policy

| Failure Class | Retry | Backoff | Terminal State | Recovery Owner |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Cancellation And Compensation

- Cancellable states:
- In-flight behavior:
- Compensation steps:

## Versioning

- Active-instance compatibility:
- Migration or drain policy:
- Replay policy:
```

