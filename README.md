<div align="center">

# Coding Agent Constitution

**Turn vague software ideas into durable project governance before any agent starts coding.**

[Simplified Chinese](README_CN.md) · [Traditional Chinese (Hong Kong)](README_HK.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## What Is This?

Coding Agent Constitution is an open-source Agent Skill for **Codex, Cursor, and Claude Code**.

It helps coding agents slow down before implementation and turn unclear software intent into durable repo-native governance files.

Instead of jumping from:

> I have an idea. Please build it.

straight into code, this skill creates:

```text
docs/SPEC.md                  product goals, boundaries, non-goals
docs/ARCH.md                  architecture, module boundaries, technical choices
docs/RULES.md                 coding, testing, and safety rules
docs/CONTRACTS/README.md      APIs, schemas, events, interfaces
docs/TASKS/001-*.md           small executable implementation tasks
AGENTS.md                     shared instructions for Codex and other agents
CLAUDE.md                     Claude Code entrypoint
.cursor/rules/*.mdc           Cursor Project Rules
.claude/rules/*.md            Claude Code modular rules
```

In one sentence:

> It turns chat-only intent into reusable repository assets.

If most of the filenames above are unfamiliar, that is expected. Start with [`constitution-skill/references/rookie-onboarding.md`](constitution-skill/references/rookie-onboarding.md) for a short concept primer, then come back.

## Why Does This Exist?

Coding agents are powerful, but starting with code too early creates drift:

- requirements live only in chat
- architecture decisions disappear between sessions
- interfaces are implemented before they are agreed on
- tests and review rules are inconsistent
- Codex, Cursor, and Claude Code each see different context
- humans cannot easily review what the agent was following

This skill creates a safer flow:

```text
vague intent
-> governance assets
-> bounded tasks
-> agent implementation
-> Cursor / Claude / human review
-> durable decisions go back into files
```

## Who This Is For

This is a stage-specific tool, useful in the window between "I have an idea for a software product" and "I have an engineer who has fully taken over the project". It is meant to be sharp, not exhaustive.

Likely useful if you are:

- a product manager starting a new project and want the docs to outlive the kickoff chat
- someone building a side project and planning to bring in collaborators later
- a domain expert (designer, analyst, operator) shipping a first software product
- a non-technical founder who is willing to learn a little engineering so the work is portable
- an engineer who wants to set a clean baseline before letting agents touch the repo

If you are new to the engineering vocabulary in the generated files, read [`constitution-skill/references/rookie-onboarding.md`](constitution-skill/references/rookie-onboarding.md) first. It is a short concept primer aimed at first-time product builders and does not assume coding skill.

## When Should I Use It?

Use it when:

- the product idea is still fuzzy
- the tech stack is undecided
- architecture boundaries are unclear
- APIs or data contracts are missing
- you want Codex, Cursor, and Claude Code to share one project context
- you want to create `SPEC.md`, `ARCH.md`, `RULES.md`, or `AGENTS.md`
- a big request needs to become smaller reviewable tasks

Do not use it for:

- tiny already-scoped bug fixes
- single-function edits
- pure formatting
- replacing human product or architecture decisions
- avoiding the need to understand any engineering at all (it is a learning scaffold, not a no-code platform)

## When To Stop Using It

This skill is designed to step out of the way once a project has stabilized. Reasonable graduation signals:

- a full-time engineer has taken over maintenance of `docs/SPEC.md`, `docs/ARCH.md`, and `docs/RULES.md`
- code review by humans is happening regularly on every change
- the team has its own onboarding doc that supersedes the rookie primer

After that point, the durable files keep working, but the skill itself is no longer the daily entrypoint.

## Compatibility

| Agent | Recommended entrypoint | Best role |
| --- | --- | --- |
| Codex | `AGENTS.md` + `constitution-skill/SKILL.md` | Implement bounded tasks and run checks |
| Cursor | `.cursor/rules/*.mdc` + optional `.cursor/skills/` | Review diffs and enforce project rules |
| Claude Code | `CLAUDE.md` + `.claude/rules/*.md` + optional `.claude/skills/` | Implement or review bounded tasks with Claude project memory |

Important note:

Cursor is based on VS Code, but agent governance does not primarily live in `.vscode/`. Use `.cursor/rules/` for Cursor rules and `.cursor/skills/` for Cursor Agent Skills.

## Quick Start (Recommended)

Just enter this prompt below to your coding agent (Codex/Claude Code/Cursor):

```
Install the skill in this repo: https://github.com/UbicusMyron/coding_agent_constitution. Make sure you always call it when I mention `constitution-skill`.
```
Then you can have a cup of coffee and wait for your agent to finish everything.

## If you want to install this by yourself...

### Codex

```bash
mkdir -p ~/.codex/skills
cp -R constitution-skill ~/.codex/skills/constitution-skill
```

Then ask:

```text
Use constitution-skill to turn this software idea into governance docs before coding.
```

### Cursor

Project-local installation:

```bash
mkdir -p .cursor/skills
cp -R constitution-skill .cursor/skills/constitution-skill
```

Recommended generated Cursor rule:

```text
.cursor/rules/project-governance.mdc
```

### Claude Code

Project-local installation:

```bash
mkdir -p .claude/skills
cp -R constitution-skill .claude/skills/constitution-skill
```

Recommended Claude Code entrypoint:

```text
CLAUDE.md
```

Example:

```markdown
@AGENTS.md

## Claude Code

- Read governance docs before implementation.
- Ask before changing risky surfaces.
```

## The Simplest Prompt

```text
I want to build a SaaS tool for small teams to collect customer feedback,
summarize feature requests, and generate development tasks.
I do not know the stack, architecture, database, or API design yet.
Use constitution-skill to create governance assets before coding.
```

Expected output:

```text
docs/SPEC.md
docs/ARCH.md
docs/RULES.md
docs/CONTRACTS/README.md
docs/TASKS/001-bootstrap-feedback-inbox.md
AGENTS.md
CLAUDE.md
.cursor/rules/project-governance.mdc
.claude/rules/project-governance.md
```

## After The Docs Exist, How Do I Actually Build The Thing?

Once the governance files exist, do not ask the agent to "build the whole app". That is how projects get messy again. Instead, use the first task file as the bridge from planning to implementation.

1. Open the first task.

   Start with something like:

   ```text
   docs/TASKS/001-bootstrap-feedback-inbox.md
   ```

   This file should describe one small, reviewable implementation slice.

2. Ask one coding agent to implement only that task.

   Example prompt:

   ```text
   Read AGENTS.md, docs/SPEC.md, docs/ARCH.md, docs/RULES.md,
   and docs/TASKS/001-bootstrap-feedback-inbox.md.

   Implement only this task.
   Do not change public APIs, database schemas, auth, billing,
   or destructive behavior unless the task explicitly says so.

   Run the listed verification checks.
   Then summarize files changed, checks run, risks, and what needs review.
   ```

3. Review the change before doing the next task.

   Use Cursor, Claude Code, Codex review mode, or a human reviewer to check:

   - does the diff match the task?
   - did the agent change files outside the allowed scope?
   - are tests or verification steps present?
   - did any architecture, contract, or product decision change?

4. Promote durable discoveries back into files.

   If implementation reveals a rule, contract, architecture choice, or product clarification that should matter later, update:

   ```text
   docs/SPEC.md
   docs/ARCH.md
   docs/RULES.md
   docs/CONTRACTS/
   AGENTS.md
   CLAUDE.md
   .cursor/rules/
   .claude/rules/
   ```

5. Repeat with the next small task.

   The loop is simple:

   ```text
   pick one task
   -> implement it
   -> run checks
   -> review the diff
   -> update durable docs if needed
   -> pick the next task
   ```

For beginners, the safest rule is:

> One task, one agent implementation pass, one review pass, then move on.

## Product-Aware Defaults

The skill now composes governance instead of forcing every product through one
blank template:

```text
project mode
+ base profile (for example, transactional record system)
+ capability modules (identity/access, LLM boundary, durable workflow)
+ optional reviewed technology recipe
-> project-specific SPEC / ARCH / RULES / CONTRACTS / TASKS
```

The shipped recipes recommend TypeScript/PostgreSQL for a deployed web product
or Python/SQLite for a single-device local tool. They are reviewed defaults,
not permanent rules; the generated `ARCH.md` records the recipe and every
deviation. SQLite starts with relational queries and FTS5; vector search is an
optional escalation, not part of the default stack.

## Mental Model

```text
Human owns intent.
Agents implement bounded work.
Review layers inspect diffs.
Durable knowledge belongs in files.
Disposable plans can be replaced.
```

## Repository Structure

```text
.
├─ README.md
├─ README_CN.md
├─ README_HK.md
├─ LICENSE
├─ constitution.md
└─ constitution-skill/
   ├─ SKILL.md
   ├─ agents/
   │  └─ openai.yaml
   ├─ references/
   │  ├─ rookie-onboarding.md          # concept primer for first-time product builders
   │  ├─ bootstrap-question-bank.md    # which questions to ask
   │  ├─ cross-agent-compatibility.md  # Codex / Cursor / Claude Code adapter mapping
   │  ├─ governance-asset-guide.md     # durable vs disposable, promotion rules
   │  ├─ anti-patterns.md              # common failure modes to avoid
   │  ├─ task-sizing.md                # quantifiable bounded-task rules
   │  ├─ retrofit-mode.md              # applying governance to a legacy repo
   │  ├─ governance-evolution.md       # versioning, ADRs, archival
   │  ├─ minimal-mode.md               # solo or throwaway lightweight setup
   │  ├─ product-pattern-routing.md    # profile/module/recipe selection
   │  ├─ profile-transactional-record-system.md
   │  ├─ module-identity-access.md
   │  ├─ module-llm-boundary.md
   │  ├─ module-deterministic-workflow.md
   │  ├─ recipe-typescript-web-postgres.md
   │  └─ recipe-local-python-sqlite.md
   ├─ assets/
   │  ├─ governance-templates/
   │  │  ├─ AGENTS.md
   │  │  ├─ CLAUDE.md
   │  │  ├─ SPEC.md
   │  │  ├─ ARCH.md
   │  │  ├─ RULES.md
   │  │  ├─ TASK.md
   │  │  ├─ DECISION.md
   │  │  ├─ CONTRACTS_README.md
   │  │  ├─ cursor-project-governance.mdc
   │  │  └─ claude-project-governance.md
   │  ├─ module-overlays/               # composable governance and contract fragments
   │  ├─ contracts-examples/           # filled OpenAPI / JSON Schema / event / SQL / CLI / file-format
   │  └─ examples/
   │     └─ feedback-inbox/            # fully filled worked example
   └─ scripts/
      └─ check-governance.sh           # drift and missing-section detector
```

## About the Validation Warning

The skill ships a small validation script, `constitution-skill/scripts/check-governance.sh`, that scans a project's governance files for common problems. It prints three kinds of lines:

- `ERROR` — something is actually broken (for example, a task file is missing its `## Verification` section). This blocks "done".
- `WARN` — a friendly heads-up worth a look, but not a blocker.
- `OK` — passed.

When you run it on the bundled example (or on your own project), you will likely see one `WARN` like this:

```text
WARN   Repeated lines across adapter files (top 5). Consider keeping AGENTS.md canonical:
```

**This is expected, and we keep it on purpose.** In plain language:

Cursor and Claude Code each read their *own* rules file — Cursor reads `.cursor/rules/*.mdc`, Claude Code reads `.claude/rules/*.md`. They are two different files for two different tools, so a few important safety rules (for example "never log a raw email address" or "ask a human before changing the database schema, auth, or billing") end up written in both. The script notices the repeated lines and gives you a nudge.

We deliberately do *not* remove these repeats, because:

- Putting the safety rules directly in each tool's file guarantees that whichever agent you use, the rule is reliably in front of it.
- "De-duplicating" them would mean each tool only points to `AGENTS.md` and has to load it to see the rule. Not every tool or version loads `AGENTS.md` automatically, so a critical safety rule could silently go missing — a worse outcome than a little repetition.

So treat this particular `WARN` as accepted by design. The only thing to remember: if you edit one copy of a repeated rule, update the other copy too, so they do not drift apart.

> Rule of thumb: `ERROR` must be fixed before you call a task done. `WARN` is advice — read it, then decide. This duplication `WARN` is one we have already decided to accept.

## License

MIT License. Use it, fork it, remix it, and make your agents less chaotic.
