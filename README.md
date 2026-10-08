<div align="center">

# Coding Agent Constitution

**Help your AI coding tool understand what you want before it builds, then check what it actually delivered.**

[简体中文](README_CN.md) · [繁體中文（香港）](README_HK.md)

[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-111827)](#)
[![Codex](https://img.shields.io/badge/Codex-compatible-10a37f)](#)
[![Cursor](https://img.shields.io/badge/Cursor-compatible-5b5bf7)](#)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-d97706)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

> Latest update, 2026-10-08: a new lightweight Flash mode, a rewritten beginner guide, and a new beginner glossary. Earlier changes are in the [update history](#update-history).

## What is this?

Coding Agent Constitution is a free, open-source skill for three AI coding tools: Codex (from OpenAI), Cursor (a code editor with AI built in) and Claude Code (from Anthropic). These tools can open the files in a folder on your computer, change them, run commands and write code. A skill is a folder of instructions that the tool reads when your request calls for it. Think of the handbook you'd give a new colleague on day one: "here's how we work on this team."

With this skill installed, the AI does some groundwork before it writes any code. It asks what you're trying to achieve, writes your answers into the project folder, and breaks the work into small steps that each come with a way to check them. When you come back next week, open a new chat or switch to another AI tool, the work picks up from those notes instead of from your memory.

You don't need to know how to code. Your part is to describe what you want, read what the AI writes back, and make the important calls.

## Why it helps

If you've ever asked an AI to "just build it", some of this may sound familiar:

- It builds a lot before the idea is clear, including features you never asked for.
- Every new chat starts from zero, so you explain the background all over again.
- It says "done", and you can't tell what it actually checked.
- A few weeks later, nobody (you included) remembers why something was built that way.

This skill keeps the plan and the important decisions in ordinary text files inside your project. You, a fresh chat, another AI tool, or an engineer who joins later can open those files and see where things stand.

## Pick how much structure you need

The skill has two ways of working, and it also knows when to stay out of the way.

| What you're asking for | What happens | Example request |
| --- | --- | --- |
| A small, clear change | The AI makes the change and runs the relevant checks. No planning session. | "Fix the typo on the sign-up page." |
| Flash: everyday work that needs a bit of clarity | The AI writes a short task agreement and adds only the structure this task needs. | "Compare three ways to collect customer feedback for our team." |
| Standard: a real software project | The AI clarifies the idea, writes a full set of project documents, then plans small tasks. | "I want a tool that helps a small team collect customer feedback, but I don't know where to start." |

You don't have to remember these names. Say what you want and how much help you'd like, and the AI should pick a way of working and tell you why in a sentence or two. If you already have a codebase without any of these documents, there is also a Retrofit mode. It adds the documents gradually, starting with the part of the code you're about to change.

### Flash in plain words

Flash is for daily tasks, research, documents, small pieces of software, and reusable capabilities such as skills. It starts with a short task agreement (the docs call it a task contract) that covers:

- the goal, and who the result is for
- the background, and any material to work from
- what's included and what isn't
- limits such as a deadline, a format or a budget
- how you'll both know it's finished
- open questions and assumptions

The agreement pins down what success looks like. The plan for getting there can change as the AI learns more, but it shouldn't quietly lower the bar or swap the goal to suit the method.

Depending on the task, the AI may add one or more kinds of detail:

- Behavior, for things that run more than once, like a script, an app feature or a skill: what goes in, what comes out, a few examples, and what happens with bad input.
- Evidence and judgment, for research and recommendations: the questions, the sources, how options are compared, and how confident the conclusion is.
- Content and structure, for documents, slides and messages: the reader, the main message, the outline and the format.
- Action, for changing something real, like moving a meeting, updating a record or sending a report: exactly what changes, what must be true first, the order of steps, and how to confirm it happened.

One task can combine several of these, and none of them needs its own file. Often the chat itself is enough. For ongoing project work, the usual starting point is an `AGENTS.md` file plus a short brief, often `docs/PLAN.md`.

To go deeper, read the [Flash guide](constitution-skill/references/flash-mode.md), the [component guide](constitution-skill/references/flash-components.md) and the [scenario examples](constitution-skill/references/flash-scenarios.md). Optional starter files: [AGENTS.md](constitution-skill/assets/flash-templates/AGENTS.md) and [PLAN.md](constitution-skill/assets/flash-templates/PLAN.md).

### Standard in plain words

Standard is the full workflow for a software project. The AI asks about the problem, the users and what the first version has to do. Then it writes files like these into your project, usually under `docs/`. You don't need to learn the names in advance.

| File | What it holds |
| --- | --- |
| `SPEC.md` | What to build, who it's for, and what to leave out for now |
| `ARCH.md` | How the parts fit together, and why the technology was chosen |
| `RULES.md` | Rules every change has to follow, including testing and safety |
| `CONTRACTS/` | Exact agreements about the data passed between parts, such as API and database shapes |
| `DECISIONS/` | Big decisions that are hard to undo, with the options that were considered |
| `TASKS/` | Small next steps, each with a way to check the result |
| `AGENTS.md` | Instructions for any AI tool that works on the project |

The exact set depends on the project. To see a finished example, open [Feedback Inbox](constitution-skill/assets/examples/feedback-inbox/), a sample project with every file filled in.

## Quick start

First, open your project folder in your AI coding tool. A project folder is just an ordinary folder on your computer that holds the project's files. If you're starting from nothing, create an empty one.

Then send the AI this message:

```text
Install the constitution-skill skill from this repository:
https://github.com/CUHK-Business-School-AI-Hub/coding_agent_constitution
Choose the installation location for the tool I am using and check that it can find the skill.
```

When it's done, start a new chat so the tool picks up the skill, and try one of the prompts in the next section. If the AI says it can't find the skill, ask it to check where the skill was installed.

## Your first prompt

For a real software project (Standard), swap the example for your own idea:

```text
I want a tool for small teams to collect customer feedback and summarize common requests.
I do not know how to choose the technology.
Use constitution-skill in Standard mode to explain what the first version should and should not do.
Save the plan in my project, then define the first small task and how to check it.
Explain decisions I need to make in plain language. Do not write application code yet.
```

The AI will ask you some questions. "I don't know" is a fine answer: it should suggest a sensible default and write it down as an assumption. At the end you'll have a plan you can read and edit, plus the first task.

Read the plan before going further. Two parts deserve the most attention: what the first version leaves out, and how it defines "done". If something is off, say so in your own words and ask the AI to fix the files.

For a lighter task (Flash), adapt this one:

```text
Use constitution-skill in Flash mode to help me compare three approaches to collecting customer feedback.
The audience is our small product team. Use the notes I provide and identify important missing evidence.
Define the scope and what a useful comparison must show, then choose the components needed for this task.
Keep the desired outcome separate from the steps you may revise as you work.
Use this conversation or an existing brief unless a project file would help us reuse the result.
```

## From plan to working software

Once you're happy with the plan, build it one task at a time. Send something like this:

```text
Find the first task in the plan and explain what it will deliver.
Complete it within the scope we have already agreed on, and run the relevant checks.
If a new important decision or a scope change is needed, explain why first.
When finished, tell me in plain language what changed, what checks passed,
and how I can try it myself.
```

When the AI reports back, look at three things:

1. Is this what you wanted? Did it add anything you didn't ask for?
2. What did it actually check, and what is still unchecked?
3. If it made a new important decision, did that get written back into the project files?

Before moving on, you can ask another AI tool or an engineer to review the change. Saying yes to building a task doesn't give permission to put it live or to delete real data. Those steps follow whatever permissions you've agreed on.

## Who does what

You decide what problem to solve, and you make the calls that would be expensive to undo. The AI asks questions, writes the plan, builds in small steps and tells you what it checked. The project files remember what was decided, so nothing important lives only in a chat window.

## New to the vocabulary?

Two pages are written for people without a technical background:

- The [beginner guide](constitution-skill/references/rookie-onboarding.md) walks through how a project goes, what each file is for, and what to say to the AI at each step.
- The [beginner glossary](constitution-skill/references/rookie-wiki.md) explains common app-building words, from API and database to deployment and Git, in a few sentences each.

When a word stops you, you can also just ask the AI: "Explain this as if I've never written code, and give me an everyday example."

## Sensible defaults for common products

You don't have to choose templates or technology. Tell the AI what you're making, whether that's a customer list, an approval process, a chat assistant, or a tool that only runs on your own computer, and the skill pulls in the matching guidance.

If your project already uses some technology, the AI starts from that. For a new project it has a few reviewed starting points, such as TypeScript and PostgreSQL for a website, or Python and SQLite for a personal tool that runs on your own machine. It explains why the suggestion fits you and writes down any adjustments. These are starting points; your requirements make the final call.

## Optional companion: Waymark

If you'd like to talk an idea through before planning any software, try [Waymark](https://github.com/CUHK-Business-School-AI-Hub/waymark), a skill developed by our team. It's a variant of `grill-me` that is friendlier to people without a technical background. You describe your work in everyday language, and it asks one question at a time: who does what, how the work actually happens, what to do when something goes wrong. Then it writes instructions people can follow.

If you then decide to turn that process into software, `constitution-skill` takes over and writes the project plan and development tasks. Waymark is optional; this skill works without it. To use the two together:

```text
Use waymark to help me clarify the real workflow and requirements.
Explain decisions I need to make in plain language.
If we decide to build software, use constitution-skill to turn the agreed details
into a project plan and the first small task.
```

## Which AI tool should I use?

The one you already have. You don't need all three, and any of them can build tasks or review changes.

| Tool | How it finds the project instructions |
| --- | --- |
| Codex | Reads `AGENTS.md` |
| Cursor | Current versions read `AGENTS.md`; add Cursor-specific rules only when needed |
| Claude Code | Current versions can find `AGENTS.md` on their own; check existing Claude-specific files before adding a fallback |

Shared rules live in a single `AGENTS.md`, so changing a rule doesn't leave an outdated copy somewhere else. New projects start with this shared file. Existing project-specific rules are kept, including Claude-specific guidance that is still useful. The [compatibility guide](constitution-skill/references/cross-agent-compatibility.md) has the setup details.

## Installing by hand

The Quick start prompt above is the easy way. If you'd rather do it yourself, download this repository and open a terminal (the window where you type commands) in its top folder. The steps below are for a fresh install. If you already have a copy, ask the AI to compare the versions first so your own changes don't get overwritten.

### Codex

Install for your user account:

```bash
mkdir -p ~/.agents/skills
cp -R constitution-skill ~/.agents/skills/constitution-skill
```

To use it in one project only, copy the skill into that project's `.agents/skills/constitution-skill/` folder instead.

### Cursor

Copy `constitution-skill/` into the target project's `.agents/skills/` folder. Current Cursor versions can share a Codex project copy in this location. `.cursor/skills/` also works.

### Claude Code

Copy `constitution-skill/` into the target project's `.claude/skills/` folder, and keep the shared project instructions in `AGENTS.md`. Current Claude Code can find `AGENTS.md` by itself, but an existing Claude entry file in the project or in a parent folder can switch that off. First check what your installed version actually loads in this project; see the [compatibility guide](constitution-skill/references/cross-agent-compatibility.md) and the [Claude Code documentation](https://code.claude.com/docs/en/memory#agentsmd).

Only if the project needs a fallback, add a short `CLAUDE.md` that imports the shared file, and keep any existing Claude-specific rules:

```markdown
@AGENTS.md
```

Afterwards, start a new chat and check that the skill is available. If an existing installation already works, check which locations your tool supports before moving it, and don't make extra copies you don't need.

## When can I stop using it?

Once the project has a clear plan and an engineer or a team can maintain it, you don't need to call the skill for every change. The files it created keep serving the project on their own. Bring the skill back when a new, fuzzy requirement needs thinking through.

## About the check script (ERROR, WARN, OK)

The skill includes a script that looks for missing pieces in Standard project documents, for example a task with no way to check it. It reports three kinds of results:

- `ERROR`: something needs fixing.
- `WARN`: something worth a look. You or the AI decide what to do about it.
- `OK`: this check of the document structure found no problems.

Passing this check does not mean the software works, has passed its tests, or is ready to go live. The script doesn't run the commands written in your tasks, and it can't judge whether a Flash task agreement or plan is any good. In Flash mode (`--mode flash`) it looks at the shared instruction files and references, and it always adds a WARN reminding you to review the task itself. If it finds no project files at all, it says so.

It may also warn when tool-specific files repeat the shared rules, or when a Claude-specific entry file stops Claude Code from finding `AGENTS.md`. Decide whether those files are still needed: keep the useful tool-specific rules, and use a short import if you need a fallback. The bundled example uses one shared `AGENTS.md`.

If commands aren't your thing, ask the AI to run the check and explain the result. Developers maintaining this skill can run:

```bash
bash constitution-skill/scripts/check-governance.sh constitution-skill/assets/examples/feedback-inbox
python3 constitution-skill/scripts/test_check_governance.py
```

## Update history

### 2026-10-08

- Added Flash, one lightweight entry point for daily work, research, documents, software and reusable capabilities. Standard keeps the full software-project workflow.
- Rewrote this README and the beginner guide for readers without a technical background, and added a beginner glossary in three languages.
- Updated Claude Code compatibility: start with the shared `AGENTS.md`, and add a thin fallback only after checking what the tool actually loads.
- File and line counts are now review signals and no longer force a task to be split. Related work can stay together when it's safer to check as one change.
- Kept the existing workflow: approved decisions are reused, you choose who builds and who reviews, and checks and safety limits stay explicit.

### 2026-09-14

- Small, well-defined edits no longer go through the planning workflow first.
- Fewer unnecessary questions: agreed decisions are reused, and alternatives are compared only when that helps.
- Clearer stopping points: a planning request stays a plan, and approved building work continues through its agreed checks. Unrelated old problems are reported separately.

### 2026-09-12

- More reliable checks: fixed cases where incomplete task documents could pass, and added regression tests.
- Smoother handoffs: approved tasks don't ask again for the same decision, and you can use your preferred AI tool to build or review.
- Updated installation guidance: shared rules live in one place, with tool-specific files only when needed.
- Clearer documentation, with less jargon and more prompts you can copy without a technical background.

### 2026-06-30

- Important technical choices now explain the options, the recommendation, and how easily the choice can be changed later.
- Generated documents are checked for unclear requirements, contradictions and missing information.
- Each task explains what to build, what may change, and how to check that it's done.

## Repository structure

<details>
<summary>Show files and developer references</summary>

```text
.
├─ README.md                          # this page
├─ README_CN.md                       # Simplified Chinese
├─ README_HK.md                       # Traditional Chinese (Hong Kong)
├─ LICENSE
├─ constitution.md                    # historical design note
├─ TODO_CASE_DERIVED_EVOLUTION.md     # ideas waiting for evidence from real projects
└─ constitution-skill/
   ├─ SKILL.md                        # the skill's main instructions
   ├─ agents/
   │  └─ openai.yaml
   ├─ references/
   │  ├─ rookie-onboarding.md          # beginner guide
   │  ├─ rookie-onboarding_CN.md
   │  ├─ rookie-onboarding_HK.md
   │  ├─ rookie-wiki.md                # beginner glossary
   │  ├─ rookie-wiki_CN.md
   │  ├─ rookie-wiki_HK.md
   │  ├─ flash-mode.md                 # lightweight entry across task types
   │  ├─ flash-components.md           # optional composable task components
   │  ├─ flash-scenarios.md            # examples of selecting components
   │  ├─ bootstrap-question-bank.md    # which questions to ask
   │  ├─ cross-agent-compatibility.md  # Codex / Cursor / Claude Code setup
   │  ├─ frontier-model-guidance.md    # portable Astra / Opus authoring guidance
   │  ├─ governance-asset-guide.md     # long-lived vs throwaway files, promotion rules
   │  ├─ governance-review-rubrics.md  # readiness checks for generated documents
   │  ├─ governance-evolution.md       # versioning, decision records, archiving
   │  ├─ anti-patterns.md              # common failure modes to avoid
   │  ├─ task-sizing.md                # review signals for coherent, checkable tasks
   │  ├─ task-review-contract.md       # how to review a finished task
   │  ├─ retrofit-mode.md              # adding governance to an existing codebase
   │  ├─ product-pattern-routing.md    # profile / module / recipe selection
   │  ├─ profile-transactional-record-system.md
   │  ├─ module-identity-access.md
   │  ├─ module-llm-boundary.md
   │  ├─ module-deterministic-workflow.md
   │  ├─ recipe-typescript-web-postgres.md
   │  ├─ recipe-local-python-sqlite.md
   │  ├─ wiki-record-crud-apps.md      # engineering notes for record apps
   │  ├─ wiki-linear-workflows.md      # engineering notes for step-by-step workflows
   │  └─ wiki-conversational-assistants.md # engineering notes for chat assistants
   ├─ assets/
   │  ├─ flash-templates/              # optional AGENTS.md and PLAN.md starters
   │  ├─ governance-templates/         # blank Standard starters
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
   │  ├─ module-overlays/              # add-on fragments for specific capabilities
   │  ├─ templates/                    # hidden starting points for common product types
   │  ├─ contracts-examples/           # filled OpenAPI / JSON Schema / event / SQL / CLI / file-format
   │  └─ examples/
   │     └─ feedback-inbox/            # fully filled worked example
   └─ scripts/
      ├─ check-governance.sh           # checks project documents for missing information
      └─ test_check_governance.py      # regression tests for the checker
```

</details>

## License

MIT License. Use it, fork it, remix it, and make your agents less chaotic.
