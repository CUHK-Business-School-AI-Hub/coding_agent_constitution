# Anti-Patterns

Use this guide to recognize and avoid the common ways governance assets fail. For every anti-pattern, the structure is: what it looks like, why it fails, what to do instead.

## SPEC.md Anti-Patterns

### SPEC As Sprint Plan
- Looks like: numbered backlog with deadlines, story points, or sprint markers.
- Fails because: sprint plans expire; SPEC must remain stable across sessions.
- Do instead: keep SPEC about durable product intent. Move sprint detail into `docs/TASKS/` or an external tracker.

### SPEC As Implementation Manual
- Looks like: SPEC describes function names, libraries, database tables, or code structure.
- Fails because: leaks reversible decisions into the most-quoted file. Implementation changes will silently invalidate SPEC.
- Do instead: keep implementation choices in `ARCH.md`. SPEC describes observable behavior and outcomes.

### Vague Goals Without Boundaries
- Looks like: "users can manage feedback" with no acceptance criteria, no non-goals.
- Fails because: every agent invents different scope.
- Do instead: list explicit non-goals and acceptance criteria. Prefer "must reject X" and "must produce Y" sentences.

### Marketing Copy
- Looks like: aspirational paragraphs about "transforming how teams work".
- Fails because: agents cannot act on adjectives.
- Do instead: replace with workflows, users, and constraints. If a phrase cannot be checked against code or behavior, cut it.

## ARCH.md Anti-Patterns

### Architecture Restated As Features
- Looks like: ARCH repeats the feature list from SPEC.
- Fails because: doubles the maintenance load, drift between files is inevitable.
- Do instead: ARCH describes structure, boundaries, and tradeoffs. Reference SPEC sections, do not paste them.

### "We Will Decide Later" Everywhere
- Looks like: every section says TBD or "to be determined".
- Fails because: agents will pick defaults silently, locking in decisions through code.
- Do instead: mark explicit `Assumptions` and `Open Technical Questions`. Commit to a reversible default for everything else.

### Hidden Dependency Choices
- Looks like: ARCH mentions a database or framework only in a code example.
- Fails because: choice is buried; reviewers miss it.
- Do instead: surface every major dependency in `Technology Stack` and `Dependency Rules`.

### Boundary Tables With No "Must Not Own"
- Looks like: module table lists `Responsibility` only.
- Fails because: agents have no signal about forbidden coupling.
- Do instead: always include `Must Not Own` columns. This is what prevents leak-through.

## RULES.md Anti-Patterns

### Generic Programming Advice
- Looks like: "write clean code", "follow SOLID", "use meaningful names".
- Fails because: every model already knows this; it dilutes repo-specific rules.
- Do instead: write rules only when they are non-obvious, specific to this repo, or repeatedly violated.

### Rules Without Enforcement Path
- Looks like: "all code must be tested" with no command, no path scope, no review hook.
- Fails because: agents cannot prove compliance.
- Do instead: pair each rule with a check command, file glob, or review prompt.

### Rule Inflation
- Looks like: hundreds of rules accumulated over months.
- Fails because: agents stop reading or only pattern-match the start.
- Do instead: keep RULES.md under ~150 lines. Move topic-specific rules into `.cursor/rules/*.mdc` or `.claude/rules/*.md` with `globs:` scoping.

## CONTRACTS Anti-Patterns

### Contract As Prose
- Looks like: "the API returns a user object with name and email".
- Fails because: agents will invent field names, types, and error shapes.
- Do instead: write an OpenAPI, JSON Schema, SQL DDL, or typed event schema. Add at least one example payload.

### No Error Contract
- Looks like: only happy-path schema.
- Fails because: error handling diverges between implementations.
- Do instead: define error envelope and at least three failure cases per endpoint or event.

### Contract Drift From Code
- Looks like: contract file untouched for months while handlers change.
- Fails because: durable doc becomes a lie. New agents trust the wrong source.
- Do instead: require contract update in the same task that changes the interface. Use `scripts/check-governance.sh` to flag missing updates.

## TASKS Anti-Patterns

### Task As Whole Feature
- Looks like: `001-implement-auth.md`, `002-build-dashboard.md`.
- Fails because: too large for one agent pass; review surface is unmanageable.
- Do instead: split by vertical slice. See `references/task-sizing.md`.

### Task Without `Do Not Touch`
- Looks like: `Scope` only lists files to change.
- Fails because: agents wander into adjacent modules, schemas, or APIs.
- Do instead: always enumerate forbidden files, APIs, schemas, and behaviors.

### Task Without Verification
- Looks like: acceptance criteria exist, but no command shows how to verify.
- Fails because: agents claim done without proof.
- Do instead: include exact commands (`npm test path/to/file`, `curl ...`, `pytest -k ...`).

### Task Referencing Hidden Chat Context
- Looks like: "as we discussed", "the user wants…".
- Fails because: a fresh agent has no access to that chat.
- Do instead: copy relevant decisions into the task, or link to a durable doc.

## AGENTS.md / CLAUDE.md / Cursor Rules Anti-Patterns

### Three Copies Of The Same Rules
- Looks like: nearly identical content in `AGENTS.md`, `CLAUDE.md`, and `.cursor/rules/project-governance.mdc`.
- Fails because: edits land in one file, others drift.
- Do instead: keep `AGENTS.md` canonical. `CLAUDE.md` imports via `@AGENTS.md`. Cursor rule is short and Cursor-specific.

### Tool-Agnostic Bloat In Tool-Specific File
- Looks like: long generic project description in `.cursor/rules/`.
- Fails because: every Cursor session re-reads the same content; should have been in `AGENTS.md`.
- Do instead: keep `.cursor/rules/` focused on review heuristics, scoping, and Cursor-only behaviors.

### Project Marketing In AGENTS.md
- Looks like: "Welcome to FooApp, the next-gen platform for…".
- Fails because: wastes context window; not actionable.
- Do instead: agents need entrypoints, commands, sensitive files, approval boundaries.

## Cross-Cutting Anti-Patterns

### Recipe As Constitution
- Looks like: a framework or hosting provider is declared permanently mandatory because it appears in a shipped recipe.
- Fails because: implementation ecosystems change faster than product and data boundaries.
- Do instead: record the recipe, review date, fit, and deviations in ARCH. Keep stable principles separate from replaceable tools.

### Every Capability Enabled By Default
- Looks like: auth, LLM, workflow engine, queue, and multiple services appear in every new project.
- Fails because: unused infrastructure adds failure modes and decisions without delivering product behavior.
- Do instead: select one base profile and only capabilities proved necessary by product workflows.

### Authentication Without Authorization
- Looks like: users can sign in, but protected queries do not enforce resource ownership or tenant boundaries.
- Fails because: authentication answers who the user is, not what the user may access.
- Do instead: define action/resource rules and test owner, non-owner, and unauthenticated access.

### Model Output As Authority
- Looks like: model output directly selects records, grants access, or executes high-impact tools.
- Fails because: model output is probabilistic and may be manipulated by untrusted content.
- Do instead: validate structured output, re-run deterministic authorization, bound tool use, and require confirmation for high-impact side effects.

### SQLite As A Shared Network Database
- Looks like: multiple computers directly open one SQLite file from a network or synchronized drive.
- Fails because: SQLite is an application-embedded database with one writer at a time; network filesystem locking and partial file synchronization can make correctness unreliable.
- Do instead: keep application code and the SQLite file on one device, or put an application server in front of the file. Move to a client/server database when shared direct access or concurrent server writes are required.

### Vector Search Before Search Requirements
- Looks like: an embedding model and vector extension are added before ordinary filters and lexical search are evaluated.
- Fails because: derived indexes, model lifecycle, platform extensions, and relevance evaluation add complexity that many local tools do not need.
- Do instead: start with relational indexes and FTS5. Add vector search only with a representative evaluation set and a documented rebuild path.

### Chat-Only Decisions
- Looks like: the human said "use Postgres" but no file mentions it.
- Fails because: next session starts blind.
- Do instead: promote spoken decisions into `ARCH.md`, `RULES.md`, or a `DECISIONS/` entry the same day.

### Promote-Once, Never Update
- Looks like: governance files are created at project bootstrap and never touched.
- Fails because: reality drifts; docs become fiction.
- Do instead: add governance updates to the same PR that changes behavior. The `Handoff Notes` of every task should ask: "what should change in durable docs?"

### Over-Documentation Of Trivia
- Looks like: 50-line RULES.md entry for a one-line lint rule.
- Fails because: drowns important rules in noise.
- Do instead: prefer machine-enforced lint/format rules. Put only what cannot be linted into RULES.md.

### Mixing Durable And Disposable In One File
- Looks like: `SPEC.md` contains a migration checklist.
- Fails because: durable file gets edited every sprint; signal-to-noise collapses.
- Do instead: route checklists to `TASKS/*.md` or `docs/notes/`.

## Promotion Inversion

When in doubt, ask: "will a new agent six months from now need this?"

- Yes -> durable file.
- Only this week -> disposable file.
- Both -> split it. The durable extract goes upstream; the disposable rest stays in the task.
