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

- Read durable project docs before implementation.
- Keep implementation tasks bounded.
- Do not change public APIs, database schemas, auth, billing, or destructive behavior without explicit approval.
- Add or update tests for changed behavior.
- Do not claim done, fixed, passing, or complete without fresh verification evidence: command, exit status, and relevant output summary.
- Summarize checks run, governance docs changed or not changed, and residual risk after each change.

## Review Rules

- Review agents should separately assess Spec Compliance and Implementation Quality.
- Review agents should check architecture boundaries, hidden coupling, contract drift, missing tests, and missing verification evidence.
- Cursor-specific review rules belong in `.cursor/rules/project-governance.mdc`.
- Claude-specific review rules belong in `.claude/rules/project-governance.md`.
- Human approval is required for risky surfaces and merge decisions.
