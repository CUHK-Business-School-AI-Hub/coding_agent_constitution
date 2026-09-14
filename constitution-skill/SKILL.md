---
name: constitution-skill
description: >-
  Turn unclear software requirements into reusable project docs and a bounded
  next task. Use when the user needs to clarify product scope, architecture,
  or interface agreements before implementation, or explicitly requests project
  governance files. Skip already-scoped code changes unless governance updates
  are requested.
---

# Constitution Skill

## Purpose

Turn ambiguous software intent into durable project files before implementation. Treat specs, architecture, contracts, and rules as reusable assets; treat task plans, implementation notes, and one-off agent prompts as consumables.

This skill follows the portable `SKILL.md` shape so it can be installed as a Codex skill, Claude Code skill, or Cursor Agent Skill. The governance assets it creates should also work when different agents rotate through the same repository.

## Applicability And User Intent

Check whether this workflow is needed before choosing a mode or loading references. An already-scoped code change can proceed normally without generating governance files. Merely mentioning a database, API, or coding agent does not require this skill.

The user's explicit instructions take precedence over this skill's workflow guidelines and templates. Preserve the requested scope and existing project conventions; this does not override system/tool permissions or authorize unrelated actions. If the user only requests planning, produce the requested documents and stop before implementation. If implementation is also authorized, continue through its agreed verification and fixes rather than stopping at a first draft.

If a skill instruction makes you pause, request confirmation, or leave authorized work unfinished, identify and link the exact file and quote the relevant rule. Explain what decision is missing, distinguish a requirement from your interpretation, and continue independent authorized work where possible.

## Modes

Once the request needs governance work, choose the matching mode. For a bounded update to existing governance, preserve its structure and edit only the relevant files rather than recreating a full set.

| Mode | When | Output Footprint | Reference |
| --- | --- | --- | --- |
| Standard | Greenfield or growing project, multiple agents, real users expected | Full file set (~9 files) | This document, sections below |
| Retrofit | Existing codebase with no governance, mixed conventions, legacy code | Incremental, seam-first | `references/retrofit-mode.md` |
| Minimal | Solo, weekend, throwaway, no production traffic | 1-3 files | `references/minimal-mode.md` |

Default to Standard. Drop to Minimal only when at least three of these are true: single contributor, lifespan under 3 months, one coding agent, no external API, no auth, no persistent user data. Switch to Retrofit when the repo already has substantial code without governance assets.

## Operating Model

Assign these roles using the tools the user already has:

- Human owns product intent, boundaries, architecture decisions, risk approval, and merge decisions.
- An implementer edits bounded units, runs checks, and produces reviewable changes.
- A reviewer checks the task, architecture, contracts, and verification evidence.
- Codex, Cursor, or Claude Code can fill either role using the same project context.

Keep one main editor per change, then hand off a clean review surface to the reviewer and the human.

## Workflow

Use the steps relevant to the request; this is not a requirement to complete every phase on every invocation.

1. Discover relevant context.
   - Follow applicable agent instructions. Read `SPEC.md` for product scope, `ARCH.md` for architecture choices, `RULES.md` for project conventions, and the relevant `CONTRACTS/` entries for interfaces (using root or `docs/` paths as the repo does). Do not load every document or adapter just because it exists.
   - Identify disposable assets if present: `TASKS/`, `docs/TASKS/`, implementation notes, migration checklists, experiment logs.
   - Preserve existing project conventions and avoid overwriting durable assets without first understanding them.

2. Set the requested outcome.
   - Identify which decisions the requested work actually needs. Fill routine reversible gaps with stated assumptions; ask about unresolved choices that materially change scope, risk, or correctness.
   - Record consequential decisions before the implementation that depends on them. Unrelated open questions need not block useful work.
   - For planning-only requests, completion means the requested documents are usable and material unresolved decisions are visible; it does not include building the application.

3. Select the product pattern.
   - Read `references/product-pattern-routing.md` after selecting the mode.
   - Select zero or one base profile, zero or more capability modules, and at most one technology recipe.
   - When the user's business language matches a common MVP surface, scan `assets/templates/` and apply relevant latent templates quietly. Do not present templates as modes or ask the user to choose them.
   - Record the selection and deviations in the `Product Shape` section of `ARCH.md`, or `docs/PLAN.md` in Minimal mode.
   - Load only the selected profile/module references and merge only applicable overlay sections.
   - In Retrofit mode, preserve the existing stack unless stack migration is the explicit approved goal.

4. Convert vague intent into bounded project context.
   - Capture product goals, users, non-goals, constraints, risks, and acceptance criteria in `SPEC.md`.
   - Capture architecture, module boundaries, data ownership, dependency choices, deployment assumptions, considered approaches, and tradeoffs in `ARCH.md`.
   - For non-obvious architecture, data, deployment, or module-boundary decisions, record the rationale and compare genuinely viable alternatives when they help the decision. Do not invent options to reach a count; an already-chosen or straightforward approach only needs its relevant rationale.
   - Capture coding rules, testing expectations, security/safety rails, and agent behavior in `RULES.md` and `AGENTS.md`.
   - Use `AGENTS.md` as the shared cross-agent instruction source when possible.
   - Use `CLAUDE.md` as the Claude Code adapter, usually importing `@AGENTS.md` and adding Claude-specific guidance.
   - Use `.cursor/rules/*.mdc` as the Cursor adapter for always-on or scoped project rules.
   - Use `.claude/rules/*.md` as the Claude Code adapter for modular or path-scoped rules.
   - Capture APIs, schemas, events, database rules, and external integrations in `CONTRACTS/` when interfaces matter.
   - Capture implementation slices in `TASKS/*.md`; keep them disposable and specific.
   - Use `references/governance-asset-guide.md` when deciding whether information belongs in a durable asset or a disposable task artifact.
   - Use `references/cross-agent-compatibility.md` when creating tool-specific adapters.
   - Use `references/anti-patterns.md` to avoid common failure modes in each governance file.
   - Use `references/governance-evolution.md` for versioning, ADR superseded chains, and archival.
   - Point first-time product builders to `references/rookie-onboarding.md` so the engineering vocabulary in the generated files is approachable.
   - Point learning-minded solo founders to the relevant `references/wiki-*.md` pages after templates are applied. The wiki is for engineering understanding; it is not a substitute for bounded tasks or governance assets.

5. Ask only the questions needed to remove dangerous ambiguity.
   - Ask only unanswered questions that could materially change the result; there is no minimum count. Reuse answers already in the conversation or project files.
   - Offer reasonable defaults when the user is unsure.
   - If a decision is reversible, choose a conservative default and mark it as an assumption.
   - Require explicit human confirmation for new or changed decisions affecting data models, public APIs, auth, payments, destructive operations, compliance, production deployment, or another expensive-to-change surface. An explicitly approved task already authorizes its stated implementation scope: do not ask again for the same decision. Ask when the scope or risk changes; approval to implement does not by itself authorize production deployment or destructive production operations.
   - Use `docs/DECISIONS/` for irreversible or expensive-to-change decisions discovered during bootstrap or task slicing.
   - Use `references/bootstrap-question-bank.md` for optional question prompts.
   - Ask the selected profile/module questions only when the answer changes architecture, contracts, risk, or scope.

6. Produce a governance asset set.
   - Prefer `docs/` for new projects unless the repo already uses root-level docs.
   - Use the templates in `assets/governance-templates/` when creating new files.
   - Keep `AGENTS.md` canonical. Add `CLAUDE.md` when Claude Code is used; generate `.cursor/rules/*.mdc` or `.claude/rules/*.md` only for needed tool-specific or scoped behavior. Preserve existing adapters and their project-specific rules.
   - Write concise, decision-oriented files. Avoid turning governance docs into generic essays.
   - Mark unresolved items as `Open Questions` or `Assumptions`, not hidden prose.
   - Treat shipped technology recipes as versioned defaults. Copy decisions into `ARCH.md`; do not make a project depend on this skill at runtime.
   - Before declaring governance complete, use `references/governance-review-rubrics.md` to self-review the generated or changed assets.

7. Create bounded implementation tasks.
   - Each task must have one clear goal, explicit constraints, limited touched surface area, acceptance criteria, interface expectations, verification commands, and governance drift checks.
   - Apply the quantifiable sizing rules in `references/task-sizing.md`:
     - touched files <= 5, diff <= ~300 lines, new top-level modules <= 1, public API changes <= 2, schema changes <= 1, verification commands <= 3.
     - Treat these as review signals: one may be acceptable, two suggest splitting, and three require splitting or a documented atomicity/size justification. Never omit necessary checks or break an atomic change merely to meet a number.
   - Acceptance criteria: 2-6 items. Verification: usually 1-3 exact commands (not "manually verify") plus expected evidence; include all necessary checks.
   - Do not create broad tasks like "clean up the codebase" or "improve reliability everywhere".
   - Use `references/task-review-contract.md` when preparing review handoff for a bounded task.

8. Handoff for implementation and review.
   - Before coding, name the governance files that define the task.
   - After coding, summarize what changed, checks run, residual risks, and what the reviewer/human should review.
   - Promote repeated review feedback into `RULES.md`, `.cursor/rules/`, or `AGENTS.md`.

9. Validate before declaring done.
   - Run `bash <installed-skill-directory>/scripts/check-governance.sh <project-root>` using the actual skill path; do not assume the script was copied into the generated project.
   - The script lints adapter orphans, required sections in TASKS/SPEC/ARCH/RULES, contract references, product pattern declarations, adapter duplication, and `Last Reviewed` staleness. It does not execute task commands or prove project readiness; review Minimal `docs/PLAN.md` separately. Open Questions may remain, but tasks depending on unresolved decisions are not ready for implementation.
   - Fix findings introduced by this change and findings that prevent the current deliverable or its dependencies from being correct or verifiable. A pre-existing problem is not exempt if the current task depends on it.
   - For pre-existing, unrelated findings, record the file, evidence that the issue predates the change, and why it does not affect the current task. Do not expand scope or suppress the checker result. Report completion of the scoped task separately from repository-wide status; a nonzero checker exit remains nonzero. `WARN` items need judgment, not automatic new work.
   - Run verification appropriate to the change and required project checks. After they pass, broaden or repeat only for new changes, failures, or unresolved concerns.

## Output Contract

The file set depends on mode.

### Standard Mode (default)

- `docs/SPEC.md`
- `docs/ARCH.md`
- `docs/RULES.md`
- `docs/CONTRACTS/README.md` plus one file per real interface (see `assets/contracts-examples/` for format choices)
- `docs/TASKS/001-<slug>.md`
- `docs/DECISIONS/001-<slug>.md` for any irreversible decision discovered during bootstrap
- `AGENTS.md`
- `CLAUDE.md` when Claude Code is used
- `.cursor/rules/project-governance.mdc` only for needed Cursor-specific or scoped rules
- `.claude/rules/project-governance.md` only for needed Claude-specific or scoped rules

In Standard and Retrofit modes, `docs/ARCH.md` must record the selected base profile, capability modules,
technology recipe, and deviations. A product may use `custom` and no recipe.

A fully filled example of this set lives in `assets/examples/feedback-inbox/`. Use it as a reference for what good looks like, not as a starter template.

### Retrofit Mode

Follow `references/retrofit-mode.md`. Produce, in order:

1. `AGENTS.md` at root (under 100 lines).
2. `docs/CONTRACTS/<seam>.md` for the next module about to change.
3. `docs/ARCH.md` with a single-module entry.
4. `docs/RULES.md` with only the rules relevant to the seam.
5. `docs/SPEC.md` scoped to the seam (mark `## Scope`).
6. `docs/TASKS/001-<slug>.md` referencing all of the above.

Do not try to document the whole legacy repo at once.

### Minimal Mode

Follow `references/minimal-mode.md`. Produce only:

- `AGENTS.md` (under ~60 lines).
- `docs/PLAN.md` (combined SPEC + TASKS + decisions log).
- Optionally `CLAUDE.md` if Claude Code is the active agent.

Promote out of Minimal Mode immediately when any of these happen: new contributor, real user data, public API, second active coding agent, deployment to production.

### Location Note

Do not use `.vscode/` as the primary place for agent governance. Cursor is VS Code-based, but Cursor agent rules live in Cursor-specific locations such as `.cursor/rules/` and `.cursor/skills/`.

## Asset Hierarchy

Durable assets:

- `SPEC.md` or `docs/SPEC.md`: product goals, boundaries, non-goals.
- `ARCH.md` or `docs/ARCH.md`: architecture, module boundaries, design constraints.
- `CONTRACTS/` or `docs/CONTRACTS/`: API schemas, database rules, event formats, interfaces.
- `RULES.md` or `docs/RULES.md`: coding rules, testing rules, safety rails.
- `AGENTS.md`: shared cross-agent instructions.
- `CLAUDE.md` and `.claude/rules/`: Claude Code persistent instructions and modular rules.
- `.cursor/rules/`: Cursor persistent project rules.

Disposable assets:

- `TASKS/*.md` or `docs/TASKS/*.md`
- implementation notes
- one-off plans
- temporary migration checklists
- experiment logs

## Bounded Task Format

Use [the task template](assets/governance-templates/TASK.md) when creating a task. Fill its goal, source context, allowed scope, consumed/produced interfaces, acceptance criteria, verification commands and expected evidence, governance drift, and handoff notes. Use `None` for genuinely absent interfaces.

## Quality Bar

The skill succeeds when a fresh coding agent can implement the next task by reading files in the repo instead of relying on hidden chat context.

Before finishing, check:

- Major requirements are written in files, not only in chat.
- Product shape, selected modules, recipe, and deviations are explicit in `ARCH.md` (or `docs/PLAN.md` in Minimal mode).
- Non-obvious architecture or deployment choices include their rationale and any alternatives needed for an informed decision.
- Every bounded task points to durable source context.
- Every bounded task states interfaces, verification evidence, and governance drift expectations.
- Risky decisions are explicit and assigned to the human.
- Contracts exist before implementation when interfaces matter.
- Repeated standards are promoted into persistent rules.
- Codex, Cursor, and Claude Code each have a readable entrypoint into the same governance source of truth.
- No unresolved findings introduced by this change or affecting its deliverable remain. Report any unrelated baseline findings separately with evidence; do not describe a failing repository check as passing.

## Anti-Patterns To Avoid

Read `references/anti-patterns.md` for the full catalog. The most common pitfalls:

- SPEC written as sprint backlog or implementation manual.
- ARCH module table with no `Must Not Own` column.
- RULES file full of generic programming advice rather than repo-specific rules.
- CONTRACTS expressed as prose instead of schemas; no error envelope defined.
- Tasks named after whole features, with no `Do Not Touch` and no verification command.
- Tasks that leave interface names, contract changes, or verification evidence for the implementer to invent.
- Governance files with placeholders, "as discussed", or requirements that rely on hidden chat context.
- Three near-identical copies of the same rules in `AGENTS.md`, `CLAUDE.md`, and `.cursor/rules/`.
- Governance files created at bootstrap and never updated again.

## File Map

This skill ships:

```text
constitution-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── bootstrap-question-bank.md       # which questions to ask the user
│   ├── cross-agent-compatibility.md     # Codex/Cursor/Claude adapter mapping
│   ├── governance-asset-guide.md        # durable vs disposable, promotion rules
│   ├── anti-patterns.md                 # common failure modes to avoid
│   ├── governance-review-rubrics.md     # readiness checks for generated governance
│   ├── task-review-contract.md          # review contract for bounded task execution
│   ├── task-sizing.md                   # quantifiable bounded-task rules
│   ├── retrofit-mode.md                 # applying governance to legacy repos
│   ├── governance-evolution.md          # versioning, ADRs, archival
│   ├── minimal-mode.md                  # solo/throwaway lightweight setup
│   ├── rookie-onboarding.md             # concept primer for first-time product builders
│   ├── wiki-record-crud-apps.md         # engineering wiki for record apps
│   ├── wiki-linear-workflows.md         # engineering wiki for workflows
│   ├── wiki-conversational-assistants.md # engineering wiki for chat assistants
│   ├── product-pattern-routing.md       # base profile/module/recipe selection
│   ├── profile-transactional-record-system.md
│   ├── module-identity-access.md
│   ├── module-llm-boundary.md
│   ├── module-deterministic-workflow.md
│   ├── recipe-typescript-web-postgres.md
│   └── recipe-local-python-sqlite.md
├── assets/
│   ├── governance-templates/            # blank starters for each file
│   ├── module-overlays/                  # composable governance fragments and contracts
│   ├── templates/                        # latent MVP-surface templates, used on mention
│   ├── contracts-examples/              # filled OpenAPI / JSON Schema / event / SQL / CLI / file-format
│   └── examples/
│       └── feedback-inbox/              # fully filled worked example
└── scripts/
    └── check-governance.sh              # drift and missing-section detector
```
