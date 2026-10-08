# Cross-Agent Compatibility

Use this guide when configuring instruction discovery, installing the skill, or migrating tool adapters. Tool discovery and model behavior are separate concerns; an Opus model does not by itself determine which files Claude Code loads.

## One Canonical Source

Keep shared instructions in `AGENTS.md`, and product details in the relevant `docs/SPEC.md`, `docs/ARCH.md`, `docs/RULES.md`, and `docs/CONTRACTS/` entries. Prefer native discovery in supported Codex, Cursor, and Claude Code clients. Do not generate a second ruleset or add `CLAUDE.md` merely because Claude Code is used.

Preserve existing project-specific rules. Do not delete a working adapter from a user's repository until its unique guidance is preserved and the replacement loading path is verified. The bundled Feedback Inbox example demonstrates the native `AGENTS.md` layout; optional adapter templates remain available for other setups.

Either implementation or review can use any of the three tools. Both roles follow the same bounded task, interfaces, authorization, and verification evidence; reviews separate `Spec Compliance` from `Implementation Quality`.

## Skill Installation Is Separate

Use a supported discovery location for the actual tool:

- Codex: `.agents/skills/constitution-skill/SKILL.md` in a project, or `~/.agents/skills/constitution-skill/SKILL.md` for a user.
- Cursor: `.agents/skills/constitution-skill/SKILL.md` or `.cursor/skills/constitution-skill/SKILL.md`.
- Claude Code: `.claude/skills/constitution-skill/SKILL.md`.

Native `AGENTS.md` support does not imply Claude Code discovers skills in `.agents/skills/`. Keep the distributed package a plain skill folder; reuse one installation only when the clients actually discover that location. Do not move or duplicate an existing working install without checking it.

## Codex And Cursor

- Codex reads `AGENTS.md`; use nested files only for genuinely distinct directory rules.
- Current Cursor reads root and nested `AGENTS.md`. Add `.cursor/rules/*.mdc` only for necessary tool-specific or scoped behavior, using `globs` and `alwaysApply` appropriately.
- `.vscode/` contains editor configuration, not shared agent governance.
- Keep the instruction entry short: map to relevant task and source documents instead of importing every specification.

## Claude Code Native Discovery

Official documentation checked on 2026-10-08 documents native support via the built-in `agents-md` plugin, introduced in Claude Code 2.1.277. Later releases fixed early provider and telemetry-related limitations (2.1.281). Check the actual installed release and plugin state rather than assuming every installation has this support; an older-client upgrade can require another session before the plugin is available.

With the default plugin behavior:

- Root-to-working-directory `AGENTS.md` and `.claude/AGENTS.md` files load. Descendant instructions load when Claude reads files in those directories.
- A project or ancestor `CLAUDE.md`, `.claude/CLAUDE.md`, or `CLAUDE.local.md` suppresses native AGENTS discovery for that project. Descendants with their own Claude entries similarly use those entries.
- User-wide or managed Claude instructions and `.claude/rules/` do not by themselves trigger that project-level suppression.
- Do not assume Codex discovery semantics: `AGENTS.override.md`, `AGENTS.local.md`, or instruction files in `.agents/` are not native Claude instruction entrypoints. `--add-dir` loading and `InstructionsLoaded` hooks also differ; consult the current official guide for those cases.
- Imports outside the project may need the user's approval. Never bypass an import permission prompt.

### Optional Compatibility Adapter

When native discovery is unavailable, disabled, or an existing Claude-specific setup must remain, keep a thin root `CLAUDE.md`:

```markdown
@AGENTS.md
```

For an adapter in `.claude/CLAUDE.md`, the equivalent relative import is `@../AGENTS.md`. Add only unique Claude-specific guidance. A prose instruction saying "read AGENTS.md" is not the same as the supported import syntax. Do not create an adapter and then expect default native discovery to load additional AGENTS files: the adapter changes the discovery path. Verify needed nested rules as well as the root.

Use `.claude/rules/*.md` only for necessary Claude-specific modular or path-scoped behavior. Do not duplicate shared governance there. Custom plugin configuration may change coexistence behavior; inspect it instead of assuming the default.

## Installation And Migration Check

1. Inspect the actual tool version, project and ancestor entry files, and existing unique rules.
2. Choose one loading path: native discovery for a supported setup, or an explicit thin import where needed.
3. Start a fresh session and inspect actual loading evidence. In Claude Code, use `/context` to inspect launch context and available plugin/debug diagnostics to verify the intended AGENTS files were injected; `/memory` is not proof of native AGENTS loading. Read a file in each required nested scope and verify its rules load then, rather than expecting every descendant at startup. Also confirm the skill is available separately.
4. Only after verification, remove redundant adapters if that migration is authorized. If no live client is available, report discovery as unverified and leave existing working adapters intact.

The structural checker can flag local orphan adapters and common shadowing/import mistakes. It cannot establish plugin state, ancestor settings outside the checked root, custom coexistence configuration, approval of external imports, or actual runtime loading.

## References

- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) and [skills](https://learn.chatgpt.com/docs/build-skills)
- [Cursor rules](https://cursor.com/docs/rules) and [skills](https://cursor.com/docs/skills)
- [Claude Code AGENTS.md discovery](https://code.claude.com/docs/en/memory#agentsmd) and [differences from CLAUDE.md](https://code.claude.com/docs/en/memory#where-agentsmd-differs-from-claudemd)
- [Built-in agents-md plugin](https://github.com/anthropics/claude-code/blob/main/mods/agents-md/README.md)

For model-specific authoring considerations, load `frontier-model-guidance.md` only when relevant.
