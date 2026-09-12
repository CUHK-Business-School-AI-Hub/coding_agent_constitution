# AGENTS

This is the shared project instruction file for coding agents. Codex can read this directly. Current Cursor versions can read it directly; use `.cursor/rules/` only for additional tool-specific or scoped behavior. Claude Code should read it through `CLAUDE.md` using `@AGENTS.md`.

## Project Context

Before implementation, read the relevant task and the documents it depends on. Use this map to load only the context needed for the change:

- `docs/SPEC.md`
- `docs/ARCH.md`
- `docs/RULES.md`
- `docs/CONTRACTS/`
- the relevant file in `docs/TASKS/`
- `constitution-skill/references/task-review-contract.md` when reviewing completed work, if available.

## Agent Roles

- Implementer: edit bounded tasks, run checks, and produce reviewable diffs.
- Reviewer: check task compliance, architecture, contracts, and verification evidence.
- Codex, Cursor, or Claude Code can fill either role; use the user's chosen tools.
- Human: define intent, approve risky decisions, and decide what merges.

## Work Rules

- Keep one main editor per change.
- Prefer small vertical slices over broad rewrites.
- Preserve existing code style and project conventions.
- Do not overwrite durable docs without understanding existing decisions.
- Promote repeated instructions into durable files.
- Follow task interfaces, public contract boundaries, verification evidence, and governance drift expectations.
- Do not claim done, fixed, passing, or complete without command, exit status, and relevant output summary.

## Approval Required

An explicitly approved task authorizes its stated implementation scope. Do not ask again for the same decision. Ask before introducing new or expanded changes to:

- public APIs
- database schemas or migrations
- authentication or authorization
- billing, payments, legal, privacy, or compliance behavior
- destructive data operations
- production deployment architecture

Implementation approval does not by itself authorize production deployment or destructive production operations. Follow the agreed execution permissions. These instructions do not replace permissions, sandbox controls, or required CI checks.

## Handoff Format

After implementation, report:

- files changed
- behavior changed
- checks run
- verification evidence
- governance docs changed or why no durable docs changed
- known risks or skipped checks
- what the reviewer should check
- what the human should decide

## Review Expectations

- Separate Spec Compliance from Implementation Quality.
- Flag missing verification evidence, contract drift, architecture drift, and task scope violations.
