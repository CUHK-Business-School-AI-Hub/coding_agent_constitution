# Governance Review Rubrics

Use these rubrics after creating or changing governance assets. The goal is to catch ambiguity, contradictions, oversized scope, hidden chat context, and missing execution evidence before implementation starts.

## Severity

- Blocking: prevents a fresh agent from implementing or reviewing safely.
- Advisory: improves clarity or maintainability but does not block the next bounded task.

## Universal Checks

Blocking:
- Placeholder text remains outside explicit `Open Questions`: `TBD`, `TODO`, `<placeholder>`, `as discussed`, `implement later`.
- A requirement depends on hidden chat context instead of file content.
- Two governance files contradict each other on product behavior, module ownership, contracts, or approval boundaries.
- A risky decision affects data models, public APIs, auth, payments, destructive behavior, compliance, or production deployment without explicit human confirmation.

Advisory:
- The document repeats generic engineering advice instead of project-specific decisions.
- The same rule appears in multiple adapters instead of being canonical in `AGENTS.md` or durable docs.

## SPEC.md

Blocking:
- Primary users, goals, non-goals, or acceptance criteria are missing.
- Requirements describe implementation mechanics instead of product behavior.
- Acceptance criteria cannot be observed by a human or verified by an agent.
- Open product questions are hidden in prose instead of listed under `Open Questions`.

Advisory:
- Constraints are too broad to guide tradeoffs.
- Core workflows lack failure or edge-case behavior that matters to users.

## ARCH.md

Blocking:
- Product Shape is missing or does not name the selected base profile, modules, recipe, and deviations.
- Module boundaries omit ownership or `Must Not Own` constraints.
- Interfaces are named in prose but not captured in `CONTRACTS/` when another module, app, team, or agent depends on them.
- A non-obvious architecture, data, deployment, or module-boundary choice lacks considered approaches and a recommendation.

Advisory:
- Tradeoffs omit rejected alternatives.
- Operational concerns omit backups, migrations, failure handling, or security where relevant.

## RULES.md

Blocking:
- Approval-required surfaces are missing or weaker than `AGENTS.md`.
- Testing rules do not say which checks must pass before completion.
- Agents may claim completion without fresh verification evidence.

Advisory:
- Rules are generic rather than tied to this repo's stack, risks, and contracts.

## CONTRACTS/*

Blocking:
- A public API, database schema, event, file format, CLI, or tool interface is used by implementation tasks but has no contract.
- Contract shape is prose-only when a schema, example payload, SQL definition, or command example is needed.
- Validation and error behavior are unspecified for inputs that can fail.

Advisory:
- Examples do not cover the most common success and failure cases.

## TASKS/*.md

Blocking:
- The task has more than one goal or crosses multiple sizing limits without a `Size Justification`.
- Source Context does not point to durable governance files.
- Scope omits either `Touch` or `Do Not Touch`.
- Interfaces are missing for tasks that create or change APIs, schemas, events, files, CLI commands, or reusable functions.
- Verification lacks exact command(s) and expected evidence.
- Governance Drift Check is missing or does not explain why no durable docs changed.

Advisory:
- Acceptance criteria exceed six items, suggesting the task should be split.
- Handoff notes do not name what Cursor or the human should review.

## AGENTS.md And Tool Adapters

Blocking:
- `CLAUDE.md`, `.cursor/rules/`, or `.claude/rules/` exist without a canonical `AGENTS.md`.
- Adapter files duplicate long sections from canonical governance instead of pointing to them.
- Tool-specific behavior contradicts durable docs.

Advisory:
- Adapter files are long enough that future agents are unlikely to keep them aligned.
