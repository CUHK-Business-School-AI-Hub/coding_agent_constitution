# Project Governance Rules

- Treat `AGENTS.md` as the shared project instruction source.
- Check changes against `docs/SPEC.md`, `docs/ARCH.md`, and `docs/RULES.md`.
- Read the relevant `docs/TASKS/*.md` before implementation.
- Check task interfaces, public contract boundaries, verification evidence, and governance drift expectations.
- Flag changes that cross module boundaries without updating `docs/ARCH.md`.
- Flag public API, schema, event, or file format changes without a matching `docs/CONTRACTS/` update.
- Flag new behavior without acceptance criteria or tests.
- Flag completion claims without command, exit status, and relevant output summary.
- During review, separate Spec Compliance from Implementation Quality.
- Ask before changing public APIs, database schemas, auth, billing, destructive operations, or production deployment architecture.
