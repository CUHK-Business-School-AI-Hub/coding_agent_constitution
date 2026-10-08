# Task Sizing

Use this guide to keep bounded tasks small enough for one agent pass and one review pass. A "task" here means one `docs/TASKS/NNN-*.md` file.

## Sizing Signals

Use these signals to estimate review effort. They are starting points, not hard limits.

| Signal | Review threshold |
| --- | --- |
| Files touched | > 5 production files |
| Diff size | > ~300 changed lines (excluding generated files, lockfiles, fixtures) |
| New top-level modules introduced | > 1 |
| Public API endpoints added or changed | > 2 |
| Database tables created or altered | > 1 |
| Verification commands | > 3 distinct commands |
| Distinct review concerns | > 1 (e.g., auth AND payments) |

Use these signals together with risk, independent outcomes, reviewability, and atomicity. Several signals warrant a closer look, not an automatic stop or split. Split independently useful changes when that reduces risk; keep coupled contract, implementation, test, and documentation updates together when splitting would leave an invalid intermediate state. Document why an unusually large task is still one coherent change. Run all checks required by the change even when there are more than three commands.

## Soft Limits

A task is on the edge if any of these are true. Consider splitting; if not, document the reason in `Risks`.

- Adds a new dependency that affects deployment, security, or licensing.
- Touches both UI and backend in the same task.
- Requires a data migration.
- Introduces a new external service integration.
- Crosses two `ARCH.md` module boundaries.

## Sizing Anchors

Useful mental anchors when scoping the next task.

| Task Type | Typical Size |
| --- | --- |
| Schema-aligned endpoint implementation | 1-3 files, ~80-200 lines, 2-3 tests |
| Add one form to existing UI | 2-4 files, ~100-250 lines, 1-2 tests |
| Wire one external service adapter | 2-3 files, ~100-200 lines, contract test + integration test |
| Refactor with no behavior change | 3-5 files, ~100-300 lines, regression coverage as needed, must pass required checks |
| Bug fix with regression test | 1-2 production files, 1 test file, ~30-80 lines |

These anchors are examples, not a mandatory taxonomy. A task outside them can still be bounded if its outcome, risk, rollback boundary, and verification are clear.

## Splitting Patterns

### Pattern 1: Slice By Layer

Too broad when each layer can deliver an independently useful result: `001-add-feedback-feature.md` (DB + API + UI + tests + docs). Do not split a small atomic vertical slice merely because it crosses layers.

Possible split when these intermediate states are valid:
- `001-add-feedback-db-schema.md`
- `002-add-feedback-api-endpoints.md`
- `003-add-feedback-list-ui.md`
- `004-add-feedback-submit-form.md`

Each task ends with a working, reviewable slice. Earlier tasks must not depend on later ones for correctness.

### Pattern 2: Slice By Vertical

Bad: `001-implement-auth.md` (signup + login + reset + 2FA + session + middleware).

Good:
- `001-bootstrap-auth-session-model.md` (only data + middleware + one login endpoint)
- `002-add-auth-signup-endpoint.md`
- `003-add-auth-password-reset.md`
- `004-add-auth-2fa.md`

Each task delivers a complete vertical feature, end to end, but small.

### Pattern 3: Slice Out The Risky Decision

Bad: `001-refactor-payments-and-add-stripe.md`.

Good:
- `001-stabilize-payments-tests.md` (no behavior change)
- `002-introduce-payment-provider-interface.md` (contract only, no provider yet)
- `003-implement-stripe-adapter.md` (one provider, behind feature flag)
- `004-cutover-default-provider-to-stripe.md`

Risky decisions become their own task with explicit acceptance criteria.

### Pattern 4: Carve Out The Migration

Bad: `001-move-from-rest-to-graphql.md`.

Good:
- `001-introduce-graphql-gateway-alongside-rest.md`
- `002-migrate-resource-foo-to-graphql.md`
- ... one task per resource ...
- `NNN-remove-rest-endpoints.md`

Long-running migrations become a series of small, reversible tasks.

## When You Cannot Split Further

Some tasks legitimately exceed these signals. Acceptable reasons:

- Generated code, schema diff, or vendored file.
- Single mechanical rename across many files.
- An API, schema, and implementation change that must remain atomic to preserve correctness.
- One large fixture or seed dataset.

In those cases:

- Add a `## Size Justification` section to the task.
- Name the review signals crossed and why the change should stay atomic.
- Ask the reviewer to verify the invariant and rollback boundary; mechanical or generated changes may be spot-checked.

## Interface Clarity

Tasks that create or change a reusable surface must state the interface before implementation:

- APIs and schemas
- events and queues
- file formats
- CLI commands
- tool inputs/outputs
- reusable functions or modules consumed by downstream tasks

If no interface is created or changed, write `None`. Do not leave names, payload shapes, or compatibility promises for the implementer to invent.

## Acceptance Criteria Sizing

Usually 2-6 acceptance criteria are enough. The count is a review signal: one precise criterion may cover a simple task, and more than six may be needed for one atomic change. Split for independent outcomes, not to reach a count. Every criterion should name an observable result.

## Verification Sizing

Aim for 1-3 verification commands; include more when needed for correctness. Examples of good verification commands:

- `npm test -- src/feedback/api.test.ts`
- `pytest tests/test_feedback_repo.py -x`
- `curl -fsS http://localhost:3000/api/feedback -d '@fixtures/sample.json'`

Bad verification: "manually click around" or "make sure it works".

Each verification entry should include the command and expected evidence. "Expected evidence" can be an exit code, assertion name, API response, generated file, log line, or other observable proof.

## Governance Drift

Every task should say whether implementation is expected to change durable governance:

- `SPEC.md` for changed product behavior.
- `ARCH.md` for changed module boundaries, data ownership, deployment assumptions, or tradeoffs.
- `CONTRACTS/` for changed APIs, schemas, events, file formats, CLI behavior, or tool interfaces.
- `RULES.md` or `AGENTS.md` for repeated engineering, safety, testing, or agent behavior.

If no durable docs should change, the task should say why that is safe.

## Smell Tests

Run these checks before handing the task to an agent.

1. Can a fresh agent execute this task without re-reading chat? If no, copy missing context into the task.
2. Could two reviewers reach the same conclusion about whether the task is done? If no, the criteria are too vague.
3. Could the task be reverted with a single `git revert`? If no, it is too entangled.
4. Does the task name describe one action? "Implement feedback list endpoint" is good. "Improve feedback system" is bad.
5. Are produced interfaces and governance drift expectations explicit? If no, the task is not ready for agent execution.
