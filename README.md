<div align="center">

# Coding Agent Constitution

**Turn your software idea into a clear plan, then let AI build it one step at a time.**

[Simplified Chinese](README_CN.md) · [Traditional Chinese (Hong Kong)](README_HK.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## Recent Updates - 2026-09-14

- Clearer skill selection: small, well-defined edits no longer enter the planning workflow first.
- Fewer unnecessary questions: reuse agreed decisions and compare alternatives only when useful.
- Clearer stopping points: planning stays planning; authorized implementation continues through its agreed checks. Unrelated old issues are reported separately.

## Recent Updates - 2026-09-12

- More reliable checks: fixed cases where incomplete task documents could pass, and added regression tests.
- Smoother handoffs: approved tasks do not need repeated approval for the same decision; use your preferred AI tool to implement or review.
- Updated installation guidance: keep shared rules in one place and add tool-specific files only when needed.
- Clearer documentation: less jargon and more prompts you can copy without a technical background.

## Recent Updates - 2026-06-30

- Important technical choices now explain the options, the recommendation, and how easily the choice can be changed later.
- Generated documents are checked for unclear requirements, contradictions, and missing information.
- Each task explains what to build, what may change, and how to check that it is done.

## What Is This?

Coding Agent Constitution is a free, open-source skill for **Codex, Cursor, and Claude Code**. Think of it as a working guide for your AI assistant.

For example, you might say:

> I want a tool that helps a small team collect customer feedback, but I do not know where to start.

The skill helps you answer three questions: **who is it for, what should come first, and how will we know it works?** It saves the answers in your project folder so a new conversation, another AI tool, or an engineer can pick up the work.

You will usually get these files. You do not need to learn the names first:

| File | What it means |
| --- | --- |
| `SPEC.md` | What to build, and what to leave out for now |
| `ARCH.md` | How the parts fit together and why the technology was chosen |
| `RULES.md` | Rules to follow during development |
| `CONTRACTS/` | Agreements about the data and behavior shared between parts |
| `TASKS/` | Small next steps with a way to check each result |
| `AGENTS.md` | Project instructions for AI tools |

The number of files depends on the project. A small personal project can use just two main files. Instructions for specific tools are added when needed.

Read the [beginner guide](constitution-skill/references/rookie-onboarding.md) if you want to learn the terms, or go straight to Quick Start below.

## Why Does This Exist?

Asking AI to start coding immediately can lead to a few familiar problems:

- Features get built before the requirements are clear.
- A new conversation or tool needs everything explained again.
- You cannot tell what instructions the AI followed or how to check its work.

This skill writes down the requirements and important decisions first, then breaks the work into small tasks. After each step, check the result and save useful discoveries back into the project.

## Who This Is For

For people who have a software idea and want AI help while keeping the work understandable:

- Product managers starting a new project.
- People building a personal project who may bring in collaborators later.
- Designers, analysts, or operators turning their experience into a tool.
- Founders who do not write code but want to understand and adjust the plan.
- Engineers who want AI to work from clear requirements.

You explain the need, check the result, and make important tradeoffs. The AI helps write the plan and break it into tasks.

## When Should I Use It?

Use it when your idea is unclear, you do not know what to build first, or you are preparing to hand the project to someone else.

For a typo or a small, well-understood bug, ask the AI to make the change directly. You do not need to plan the whole project again. Important product decisions remain yours.

## When To Stop Using It

Once the project has a clear plan and an engineer or team can maintain it, you do not need to invoke this skill for every change. The files you created can keep serving the project.

Use it again when a new, unclear requirement needs working through.

## Compatibility

**Use the tool you already have. You do not need all three.** Each can implement tasks or review changes.

| Tool | How it reads project instructions |
| --- | --- |
| Codex | Reads `AGENTS.md` |
| Cursor | Current versions read `AGENTS.md`; add dedicated rules only when needed |
| Claude Code | Reads shared instructions through `CLAUDE.md` |

Keep common rules in one place so a change does not leave another copy out of date. Preserve existing project-specific rules. See the [compatibility guide](constitution-skill/references/cross-agent-compatibility.md) for configuration details.

## Quick Start (Recommended)

Open your project folder in your AI coding tool and send this:

```text
Install the constitution-skill skill from this repository:
https://github.com/CUHK-Business-School-AI-Hub/coding_agent_constitution
Choose the installation location for the tool I am using and check that it can find the skill.
```

After installation, start a new conversation and try the prompt under “The Simplest Prompt” below. If the skill is not found, ask the AI to check its installation location.

## Optional Companion Skill: `waymark`

To clarify your idea through a question-and-answer conversation first, try [Waymark](https://github.com/CUHK-Business-School-AI-Hub/waymark), developed by our team. It is a variant of `grill-me` designed to be friendlier to people without a technical background. Describe your work in everyday language; Waymark asks one question at a time to clarify who does what, how it works, and how to handle exceptions, then writes instructions people can follow.

If you then want to turn that process into software, use `constitution-skill` to create the project plan and development tasks. Waymark is an optional companion, not a required dependency.

To combine them:

```text
Use waymark to help me clarify the real workflow and requirements.
Explain decisions I need to make in plain language.
If we decide to build software, use constitution-skill to turn the agreed details
into a project plan and the first small task.
```

## If you want to install this by yourself...

These commands assume you have downloaded this repository and opened a terminal in its root folder. They are for a fresh installation; if a copy already exists, ask the AI to compare it before updating.

### Codex

Install for your user account:

```bash
mkdir -p ~/.agents/skills
cp -R constitution-skill ~/.agents/skills/constitution-skill
```

For project-only use, copy the skill into the target project's `.agents/skills/constitution-skill/` folder instead.

### Cursor

Copy `constitution-skill/` into the target project's `.agents/skills/` folder. A Codex project copy in this location can be shared with current Cursor versions. `.cursor/skills/` also remains an option.

### Claude Code

Copy `constitution-skill/` into the target project's `.claude/skills/` folder. For shared project instructions, `CLAUDE.md` can import them with:

```markdown
@AGENTS.md
```

Start a new conversation and check that the skill is available. Keep existing working installations until you have checked your tool's supported paths; do not create extra copies unnecessarily.

## The Simplest Prompt

Replace this example with your idea:

```text
I want a tool for small teams to collect customer feedback and summarize common requests.
I do not know how to choose the technology.
Use constitution-skill to explain what the first version should and should not do.
Save the plan in my project, then define the first small task and how to check it.
Explain decisions I need to make in plain language. Do not write application code yet.
```

You will get a project plan you can read and change, plus the next task. Files for a standard project usually live under `docs/`; a small personal project may only need `AGENTS.md` and `docs/PLAN.md`.

Check whether the plan matches your intent, especially what it leaves out and how it defines success. Ask the AI to correct anything it misunderstood.

## After The Docs Exist, How Do I Actually Build The Thing?

Once you agree with the plan, start with the first small task:

```text
Find the first task in the plan and explain what it will deliver.
Complete it within the scope we have already agreed on, and run the relevant checks.
If a new important decision or a scope change is needed, explain why first.
When finished, tell me in plain language what changed, what checks passed,
and how I can try it myself.
```

After each task, check three things:

1. Is the result what you wanted? Did the AI add features you did not need?
2. What did it actually check, and what remains unchecked?
3. Were important new decisions saved back into the project files?

Another AI or an engineer can review the changes before the next task. Permission to implement does not automatically authorize deployment or deleting production data; those actions follow your agreed permissions.

## Product-Aware Defaults

You do not need to choose internal templates. Describe whether you need customer records, an approval process, a chat assistant, or a tool that runs only on your computer. The skill selects the relevant guidance.

For an existing project, it starts with the technology already in use. For a new project, its suggestions include TypeScript/PostgreSQL for a website and Python/SQLite for a local personal tool. It explains the fit and records any adjustments.

These are starting points. Your requirements determine the choice.

## Mental Model

You decide what problem to solve. The AI works within the agreed scope. Check each result, and keep important instructions in the project so they can be used again.

## Repository Structure

<details>
<summary>Show files and developer references</summary>

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
   │  ├─ wiki-record-crud-apps.md      # engineering wiki for record apps
   │  ├─ wiki-linear-workflows.md      # engineering wiki for workflows
   │  ├─ wiki-conversational-assistants.md # engineering wiki for chat assistants
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
   │  ├─ templates/                     # latent MVP-surface templates, used on mention
   │  ├─ contracts-examples/           # filled OpenAPI / JSON Schema / event / SQL / CLI / file-format
   │  └─ examples/
   │     └─ feedback-inbox/            # fully filled worked example
   └─ scripts/
      ├─ check-governance.sh           # checks project documents for missing information
      └─ test_check_governance.py       # regression tests for the checker
```

</details>

## About the Validation Warning

The skill includes a script that looks for missing information in project documents:

- `ERROR`: something needs fixing, such as a task without a verification section.
- `WARN`: something deserves attention; you or the AI should decide how to handle it.
- `OK`: this document structure check found no errors.

**Passing this check does not mean the software has passed its tests or is ready to deploy.** The script does not execute task commands or check the lightweight `docs/PLAN.md`; review those separately. It reports when there are no files to check.

The example's “repeated rules” warning means some instructions appear in more than one tool file. Existing projects may retain copies that serve a purpose, but keep them consistent when editing. New projects should share `AGENTS.md` where possible.

If you are unfamiliar with commands, ask the AI to run the check and explain the result. Developers maintaining this skill can run:

```bash
bash constitution-skill/scripts/check-governance.sh constitution-skill/assets/examples/feedback-inbox
python3 constitution-skill/scripts/test_check_governance.py
```

## License

MIT License. Use it, fork it, remix it, and make your agents less chaotic.
