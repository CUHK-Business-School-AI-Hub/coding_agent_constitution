# RULES

## Coding Rules

- 

## Testing Rules

- Required checks:
- Minimum coverage expectations:
- Test data rules:

## Architecture Rules

- 

## Contract Rules

- 

## Security And Safety Rules

- 

## Dependency Rules

- 

## Agent Rules

- Read the task and its relevant source documents before implementation.
- Keep implementation tasks bounded.
- Follow the approval boundaries in `AGENTS.md`. Existing task approval covers its stated scope; ask about new or expanded decisions.
- Add or update tests for changed behavior.
- Follow the verification and baseline-finding rules in `AGENTS.md`; report actual evidence and never describe a failing check as passing.
- Summarize checks run, governance docs changed or not changed, and residual risk after each change.

## Review Rules

- Review agents should separately assess Spec Compliance and Implementation Quality.
- Review agents should check architecture boundaries, hidden coupling, contract drift, missing tests, and missing verification evidence.
- Cursor-specific review rules belong in `.cursor/rules/project-governance.mdc`.
- Claude-specific review rules belong in `.claude/rules/project-governance.md`.
- Human approval is required for risky surfaces and merge decisions.
