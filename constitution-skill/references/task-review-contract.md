# Task Review Contract

Use this contract after a bounded task is implemented. Reviewers should separate "did it do the requested thing?" from "is it well built?" so that passing tests do not hide spec drift, and spec compliance does not hide fragile implementation.

## Inputs

- The task file.
- Source Context named by the task: `SPEC.md`, `ARCH.md`, `RULES.md`, `CONTRACTS/*`, `AGENTS.md`, and adapters as applicable.
- The implementation diff or changed files.
- Verification evidence from the implementer: command, exit status, and relevant output summary.
- Any implementation notes or handoff notes.

## Required Verdicts

### Spec Compliance

Answer: `pass`, `pass with minor notes`, or `fail`.

Check:
- The implementation satisfies every acceptance criterion in the task.
- The implementation stays inside `Touch` and `Do Not Touch`.
- Produced interfaces match the task and any referenced contracts.
- Public contracts were changed only when the task allowed it.
- Human-confirmation surfaces were not changed without approval.

### Implementation Quality

Answer: `pass`, `pass with minor notes`, or `fail`.

Check:
- The implementation follows local architecture and dependency rules.
- Tests or equivalent checks cover changed behavior and likely failure paths.
- Error handling, migration behavior, and security-sensitive behavior are appropriate for the task.
- The implementation is not broader than needed for the task.

## Governance Drift Review

Reviewers must answer:

- Did the code change product behavior that belongs in `SPEC.md`?
- Did it change module boundaries, data ownership, deployment assumptions, or tradeoffs that belong in `ARCH.md`?
- Did it change APIs, schemas, events, file formats, CLI behavior, or tool interfaces that belong in `CONTRACTS/`?
- Did it reveal a repeated coding, testing, security, or agent rule that belongs in `RULES.md` or `AGENTS.md`?
- If no durable docs changed, does the handoff explain why that is safe?

## Verification Evidence

Blocking:
- The implementer claims done, fixed, passing, or complete without a fresh command, exit status, and output summary.
- The verification command cannot exercise the acceptance criteria.
- A command failed and the failure is not explained as unrelated.

Advisory:
- Verification is broad enough to pass but not focused enough to prove the task-local behavior.

## Severity

- Critical: data loss, security issue, broken core behavior, contract violation, unauthorized destructive action, or unapproved risky surface change.
- Important: missed requirement, fragile implementation, missing regression test, architecture-boundary violation, or unverifiable acceptance criterion.
- Minor: naming, small duplication, documentation clarity, or polish that does not change correctness.

Critical and Important findings block task completion. Minor findings may be recorded for later unless they accumulate into real risk.

## Review Output Shape

```markdown
## Spec Compliance
Verdict: <pass | pass with minor notes | fail>
- <finding with file/line evidence or "No findings">

## Implementation Quality
Verdict: <pass | pass with minor notes | fail>
- <finding with file/line evidence or "No findings">

## Governance Drift
- SPEC:
- ARCH:
- CONTRACTS:
- RULES/AGENTS:

## Verification
- Evidence reviewed:
- Gaps:

## Required Fixes
- <Critical/Important fixes only>
```
