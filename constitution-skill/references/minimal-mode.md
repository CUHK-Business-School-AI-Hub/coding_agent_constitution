# Minimal Mode

Use this guide when full governance is overkill: solo projects, weekend prototypes, single-person scripts, throwaway research code. Producing nine governance files for a 200-line CLI is wasteful and signals to future readers that the project is heavier than it is.

This mode keeps the same principles (document before implementation, bounded tasks, cross-agent compatibility) at the smallest possible footprint.

## When To Use Minimal Mode

Minimal mode is eligible only when all of these safety exclusions are satisfied:

- No real or persistent user data.
- No authentication, payments, money handling, or destructive operations.
- No public API consumers or externally consumed webhook contracts.
- No production deployment or traffic.

Then assess fit: a single contributor, one active coding agent, short lifespan, and a small reversible scope are useful signals. They never override the exclusions. A local script with synthetic data may fit; a solo weekend app collecting customer data does not.

If an excluded surface appears later, upgrade before implementing it. Also reassess the footprint when collaborators or multiple active agents need a durable handoff.

## The Minimal File Set

Produce exactly two files:

```text
AGENTS.md
docs/PLAN.md
```

Optionally, one more only when the installed client needs a compatibility adapter (see `cross-agent-compatibility.md`):

```text
CLAUDE.md
```

Skip everything else. Specifically, do not create:

- `SPEC.md`, `ARCH.md`, `RULES.md`, `CONTRACTS/` as separate files.
- `.cursor/rules/`, `.claude/rules/`.
- `TASKS/` folder.
- `DECISIONS/`.

The reduction is intentional. Each file you add has a maintenance tax.

## AGENTS.md In Minimal Mode

Keep under ~60 lines. Suggested shape:

```markdown
# AGENTS

## Project
One paragraph: what this is, who uses it, why it exists.

## Stack
- Language / runtime:
- Key dependencies:
- How to run:
- How to test:

## Conventions
- <2-5 repo-specific rules>

## Sensitive
- <files or behaviors that need human confirmation, if any>

## Workflow
- Read `docs/PLAN.md` for current task scope.
- After each change, summarize files touched, checks run, residual risk.
```

## docs/PLAN.md In Minimal Mode

`docs/PLAN.md` plays the role of SPEC + TASKS combined.

```markdown
# Plan

## Intent
What problem this codebase solves. Update when product direction shifts.

## Product Shape
- Base profile: custom
- Capability modules: none
- Technology recipe: none
- Deviations and rationale: state the actual stack choice and why it fits.

## Current Slice
The single thing being worked on right now. Replace as work progresses.

### Goal
One outcome.

### Scope
- Touch:
- Do not touch:

### Interfaces
- Consumes: name the local inputs and formats, or None.
- Produces: name the local outputs and formats, or None.
- Public contracts touched: None (promote before adding an external interface).

### Acceptance
- Observable result.

### Verification
- Command: exact command.
  - Expected evidence: exit status and observable result.

### Governance Drift
- Update this plan or AGENTS.md for changed intent, decisions, interfaces, or recurring rules; otherwise state why no update is needed.

## Backlog
- Short bulleted list of next things, no detail until they become the current slice.

## Decisions Log
- 2026-05-01: chose SQLite over Postgres for simplicity. Revisit if multi-user.
- 2026-05-12: skipping auth for now. Add before any deploy.
```

The `Decisions Log` is the minimal-mode ADR. One line per decision is enough at this scale.

## Promotion Triggers

Promote before crossing a safety exclusion. For growth signals, reassess how much durable context the next contributor or task needs.

| Trigger | Promotion |
| --- | --- |
| You hire a contributor or invite reviewers | Reassess handoff needs; split product and architecture context into SPEC/ARCH/RULES when useful |
| You add real or persistent user data | Promote; add `RULES.md` with data rules and `CONTRACTS/` for storage schemas |
| You add auth, money handling, or destructive operations | Promote before implementation; record approval and safety boundaries |
| You add a public API or webhook | Add `docs/CONTRACTS/` |
| You add a second active coding agent | Reassess shared context and split durable docs as needed; add adapters only if discovery or tool-specific behavior requires them |
| `docs/PLAN.md` becomes hard to navigate (around 200 lines is a signal) | Split into `SPEC.md` + `docs/TASKS/` when that improves use and maintenance |
| You deploy to production | Add `ARCH.md` with operational concerns |

Promotion is a one-task job: file `docs/TASKS/001-promote-governance.md`, split, retire `docs/PLAN.md` into specific files.

## Minimal Mode Workflow

The flow is identical in shape to standard mode, just shorter:

1. Update the `Current Slice` section of `docs/PLAN.md`.
2. Ask the agent to implement only that slice.
3. After implementation, append to `Decisions Log` if anything irreversible happened.
4. Move next item up from `Backlog` into `Current Slice`.

The skill's standard approval rules still apply. An explicitly approved task covers its stated implementation scope; ask about new or expanded decisions, not the same decision again. Production deployment and destructive production operations still need the agreed execution permissions.

## What You Lose

Be honest about the tradeoff. Minimal mode gives up:

- Separate long-lived task and review records (native instruction discovery remains available).
- Long-term historical clarity (no ADR chain).
- Explicit module boundaries (single-file project assumed).
- Drift detection scripts (too little surface to be worth running).

This is acceptable for the target use cases. Do not use minimal mode for anything that handles real user data, money, or production traffic.
