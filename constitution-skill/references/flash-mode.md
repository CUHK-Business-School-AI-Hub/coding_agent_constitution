# Flash Mode

Flash turns unclear intent into a compact, usable task contract. Use it for daily work, research, documents, software, and reusable capabilities when a full project-governance set would add little value. A continuing tool or service can also use Flash when its context remains understandable in this form.

## Start With The Task

A clear small task can proceed directly: fix a known typo, answer a well-specified question, or make a scoped edit using existing context. Do not bootstrap files or ask the user to select components merely because Flash is available.

For unclear or multi-part work:

1. Read the user's request and the relevant existing context. Load further sources only as the task needs them.
2. State the common task contract at the level of detail needed to work and check the result. Reuse settled answers; fill routine reversible gaps with explicit assumptions. Ask only when an unresolved choice materially changes the outcome, scope, or correctness.
3. Select the useful components below. Omit a component when it adds no decision or check. Link an existing source that already supplies it.
4. Do the requested work, revising the implementation plan as evidence changes. Keep coupled changes together when that produces a coherent result; split independently useful outcomes when doing so makes execution or review clearer.
5. Check the observable outcome, address relevant failures, and report the result with actual evidence and remaining uncertainty.

This is one entry path, not a sequence of required documents or separate planning sessions. If the contract is already clear, proceed with the requested implementation. If the request is planning-only, stop with a usable plan rather than building the result it describes.

## Common Task Contract

Capture these ideas once, in natural language or a brief structured note. Do not turn every label into a mandatory heading.

- **Goal:** What result is wanted, and why?
- **User or audience:** Who will use, receive, or judge the result?
- **Context:** Relevant source material, existing work, decisions, and current situation. Reference canonical files, schemas, `SKILL.md`, or task records rather than reproducing them.
- **Scope:** Requested deliverables and actions, plus important non-goals.
- **Constraints:** Facts that shape the result, such as timing, format, compatibility, available resources, or user preferences.
- **Observable completion:** What will be true when finished, how it will be checked, and where this task ends.
- **Unknowns:** Material open questions and assumptions. Distinguish those blocking a dependent step from those that can remain open.

A small task may express the entire contract in a few sentences in the conversation. Persistent or handed-off work needs enough recorded context for the next person or agent to continue without reconstructing chat.

### Outcome Versus Implementation Plan

The outcome contract says what counts as success. The implementation plan says how to try to achieve it: approach, steps, dependencies, and current status. Revise the plan when an approach fails or better evidence appears; do not silently lower the outcome, change the audience, or expand the deliverable to fit the attempted method. Record a material change to the agreed outcome explicitly.

For multi-part work, track unfinished deliverables and checks. A first draft, progress update, or started background job is not completion. Await task-critical work already started, or report its blocked or pending state and what is needed to continue.

## Select Components By Need

Use [the component guide](flash-components.md) only for the parts the task needs:

| Component | Trigger | Useful structure |
| --- | --- | --- |
| Behavioral contract | Building or changing something with repeatable behavior, including a script, service, skill, or agent | Inputs, outputs, state, examples, failure behavior |
| Evidence and judgment framework | The result depends on research, comparison, interpretation, or a recommendation | Questions, sources, criteria, uncertainty |
| Content and structure blueprint | A document, slide deck, message, or other composed deliverable must serve an audience | Audience, message, outline, presentation |
| Action contract | Work changes an external or local state, or coordinates a sequence of operations | Target, current-to-desired state, preconditions, sequence, result confirmation |

These are provisional useful structures, not four exclusive modes or four compulsory files. Combine them when needed and adapt or extend a structure if it fails to describe the real task. State the shared goal and context once; components add only their distinct details. Explain a selection briefly when it helps the user understand the approach, without asking them to choose a taxonomy.

For example, researching a market and preparing slides shares one contract, with evidence/judgment feeding the content blueprint. A recurring analysis-and-report agent can combine all four components: reusable behavior, analytical criteria, report structure, and the requested run or delivery actions.

## Keep The Footprint Useful

For continuing project work, start with existing context. If files would help, a useful default is:

- `AGENTS.md`: stable project context, canonical references, recurring conventions, and how to check work.
- `docs/PLAN.md` or an existing brief: the outcome contract, selected component details or references, current implementation plan, and evidence/status.

See [optional starters](../assets/flash-templates/). This is not an exact file set. A one-off document may need only the conversation and requested artifact; a reusable skill may keep behavior in its `SKILL.md` and examples; an established project may already have a suitable task and schemas. Do not create empty component files or parallel copies of those sources.

Keep stable conventions in the canonical entry point; keep temporary steps and run results in the task or brief. Add a separate schema, reference, example, or decision record when another consumer actually needs it. Use tool-specific adapters only when discovery or scoped behavior needs them; see [cross-agent compatibility](cross-agent-compatibility.md).

Choose a larger footprint when distinct concerns become hard to navigate, multiple consumers need stable interfaces, or handoffs require independent durable records. Standard supplies the full project-governance workflow; Retrofit helps establish it incrementally in an existing codebase. Growth is judged by information and coordination needs, not file counts, line counts, or elapsed sessions.

## Software-Specific Detail

For software, the behavioral component can reference existing APIs, data schemas, CLI contracts, and tests. Use [product pattern routing](product-pattern-routing.md) when a product shape, capability module, or technology recipe helps a concrete design decision. Those modules describe software architecture; they are not Flash's task components. Record only applicable selections in the existing brief or architecture source. Research, documents, and routine actions do not need an app stack, product profile, database, or Product Shape section.

## Review And Completion

Review the contract and result proportionately:

- Does the result answer the actual goal for the intended user or audience, within the requested scope and constraints?
- Can each important completion claim be tied to observed evidence? Use commands and results for executable behavior, inspected artifacts for presentation, checked sources for research, and observed state for actions.
- Do selected components cover the meaningful normal, edge, and failure cases? Are their dependencies and any mismatches visible?
- Are material unknowns, assumptions, incomplete steps, and checks not run explicit?
- Have changed reusable behavior or recurring conventions been updated in their canonical source, without duplicating it elsewhere?

Do not force a command onto a task whose outcome is best checked by reading or inspecting it. Do not present structural lint, a dry run, or a drafted artifact as evidence of successful live execution.

For persistent project files, run `bash <installed-skill-directory>/scripts/check-governance.sh --mode flash <project-root>` using the actual skill path when structural checks are useful. It checks shared adapters, recognized contract references, and dated metadata, without imposing Standard sections or interpreting free-form unknowns, and reports its coverage. It does not semantically validate a flexible Flash contract or prove completion; use this review against the actual deliverable. [Representative scenarios](flash-scenarios.md) illustrate component selection and suitable evidence, not measured model performance.
