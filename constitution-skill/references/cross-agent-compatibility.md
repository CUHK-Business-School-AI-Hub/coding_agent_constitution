# Cross-Agent Compatibility

Use this guide when making the generated governance assets work across Codex, Cursor, and Claude Code.

## Compatibility Principle

Keep one shared source of truth and create thin adapters for each tool:

- Shared canonical instructions: `AGENTS.md`
- Product/architecture/rules/contracts: `docs/SPEC.md`, `docs/ARCH.md`, `docs/RULES.md`, `docs/CONTRACTS/`
- Codex adapter: `AGENTS.md`
- Cursor: reads `AGENTS.md`; optional `.cursor/rules/project-governance.mdc` for tool-specific or scoped rules
- Claude Code adapter: `CLAUDE.md` importing `@AGENTS.md`, plus optional `.claude/rules/*.md`

Avoid copying long rules into three places. Duplicated rules drift.

Apply governance review consistently across tools:

- Implementers follow the bounded task file and report verification evidence.
- Reviewers check task compliance, architecture boundaries, contracts, tests, and governance drift.
- Assign either role to Codex, Cursor, or Claude Code according to the user's toolchain.
- All tools should separate `Spec Compliance` from `Implementation Quality` during review.

## Skill Installation Targets

For project-local installation, prefer the tool-native path the user is actually using:

- Codex: `.agents/skills/constitution-skill/SKILL.md` for a project, or `~/.agents/skills/constitution-skill/SKILL.md` for a user.
- Claude Code: `.claude/skills/constitution-skill/SKILL.md`
- Cursor: the same `.agents/skills/constitution-skill/SKILL.md` project copy, or `.cursor/skills/constitution-skill/SKILL.md`.

For open-source distribution, keep the package itself as a plain skill folder with `SKILL.md`, `references/`, and `assets/`. Users or installers can copy it into the right tool directory.

## Codex

Use `AGENTS.md` for repository instructions:

- Keep it concise and agent-focused.
- Include setup, test, coding, review, and approval rules.
- Reference durable docs instead of pasting large specs into `AGENTS.md`.
- Require command, exit status, and output summary before claiming done, fixed, passing, or complete.
- Ask implementers to report whether `SPEC.md`, `ARCH.md`, `CONTRACTS/`, `RULES.md`, or `AGENTS.md` changed or did not need to change.
- Use nested `AGENTS.md` files only when subdirectories need distinct rules.

## Cursor

Use Cursor Project Rules for persistent project behavior:

- Store rules under `.cursor/rules/`.
- Prefer `.mdc` files with YAML frontmatter.
- Use `alwaysApply: true` for governance rules that must be included every session.
- Use `globs` for path-scoped rules.
- Use Cursor skills under `.cursor/skills/<skill-name>/SKILL.md` for task-specific workflows.
- Current Cursor versions read root and nested `AGENTS.md` directly. Add Project Rules only when additional scope or tool-specific behavior is needed.
- Include implementation or review guidance according to the assigned role; neither role requires a particular tool.

Cursor is based on VS Code, but `.vscode/` is not the main agent-governance location. Use `.vscode/` only for editor settings, extensions, launch configs, or tasks.

## Claude Code

Use `CLAUDE.md` for project instructions:

- Keep root `CLAUDE.md` thin.
- Import shared instructions with `@AGENTS.md` when `AGENTS.md` already exists.
- Add Claude-specific guidance below the import only when necessary.
- Use `.claude/rules/*.md` for modular rules; rules without `paths` frontmatter are loaded broadly.
- Use path-scoped frontmatter when a rule only applies to certain files.
- Keep Claude rules thin and aligned with `AGENTS.md`; put Claude-specific behavior in `.claude/rules/` only when it cannot live in shared governance.

## File Map

This map shows available entrypoints. Create adapters only for tools in use; `.cursor/rules/` and `.claude/rules/` are optional. Preserve existing project-specific rules:

```text
project-root/
├─ AGENTS.md
├─ CLAUDE.md
├─ docs/
│  ├─ SPEC.md
│  ├─ ARCH.md
│  ├─ RULES.md
│  ├─ CONTRACTS/
│  │  └─ README.md
│  └─ TASKS/
│     └─ 001-<slug>.md
├─ .cursor/
│  └─ rules/
│     └─ project-governance.mdc
└─ .claude/
   └─ rules/
      └─ project-governance.md
```

If a repo needs the constitution skill itself to be project-local, add one of:

```text
.agents/skills/constitution-skill/SKILL.md  # Codex and current Cursor
.claude/skills/constitution-skill/SKILL.md  # Claude Code
```

Use one project-local skill copy rather than multiple duplicated copies when the user's toolchain can discover a shared location.

## Compatibility Check

Reviewed against official documentation on 2026-09-12:

- [Codex skills](https://learn.chatgpt.com/docs/build-skills)
- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Cursor rules](https://cursor.com/docs/rules) and [skills](https://cursor.com/docs/skills)
- [Claude Code memory and imports](https://code.claude.com/docs/en/memory)

These tools differ in when nested instructions load; do not assume identical discovery behavior. After installation, start a new session and confirm the skill appears and the expected project instructions are loaded. Older installations may use other paths, including `~/.codex/skills`; verify the actual client before moving or duplicating them.
