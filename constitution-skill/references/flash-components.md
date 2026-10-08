# Flash Components

Use this guide after [Flash's common task contract](flash-mode.md). These structures help interpret and carry out a task; select only useful details. They may be paragraphs, a sketch, an existing schema, examples, or sections of one brief. They are not separate modes or required files. Extend them when another structure describes the task better.

## Behavioral Contract

**Use when:** the deliverable has repeatable behavior: software, scripts, reusable skills, agent capabilities, data transformations, or a repeatable workflow.

Clarify:

- Inputs and invocation: accepted data, parameters, context, and how work begins.
- Outputs: observable results, formats, and consumers.
- State: what persists, what changes, and what is derived or transient, if any.
- Examples: meaningful normal, boundary, and failure cases with expected results.
- Failure behavior: what an absent, invalid, or unavailable input means for the result.

Reference an existing API/schema, `SKILL.md`, command usage, tests, or examples when they already define these details. Add only the missing agreement. A reusable capability needs a clear invocation, input/output behavior, and representative checks; it does not automatically need an application's architecture file set.

**Completion evidence:** exercise representative inputs and inspect outputs and state. Label mocked, simulated, dry-run, and live results accurately.

## Evidence And Judgment Framework

**Use when:** research, comparison, diagnosis, analysis, or a recommendation determines the result.

Clarify:

- Questions: what must be learned or decided, and what is outside the inquiry.
- Sources: where evidence will come from, relevant dates or versions, and access limits.
- Criteria: how sources or options will be compared and what would change the conclusion.
- Uncertainty: missing evidence, conflicts, assumptions, and confidence limits.

Distinguish observations from interpretations. Connect material claims to sources and preserve enough source context to check them. For analysis, state units, time windows, definitions, and transformations when they affect the result. Avoid gathering more material once the requested conclusion has sufficient evidence unless an unresolved concern requires it.

**Completion evidence:** the requested questions are answered against the criteria, material claims are supported, and unresolved or conflicting evidence is visible.

## Content And Structure Blueprint

**Use when:** writing or arranging a document, report, slides, message, lesson, or other audience-facing artifact.

Clarify:

- Audience: use the common contract's audience, adding only distinct needs of a section or variant.
- Message: main takeaway, purpose, and what the reader should understand or do.
- Outline: necessary sections, narrative order, and supporting evidence.
- Presentation: format, tone, length, visual structure, and delivery destination when relevant.

Use an existing template or style guide rather than duplicating it. Connect claims to the evidence component when research is involved. A blueprint should guide the artifact without becoming a second artifact of equal size.

**Completion evidence:** inspect the finished content and, when layout matters, the rendered artifact. Check audience fit, requested coverage, consistency, source attribution, and readable presentation.

## Action Contract

**Use when:** performing or coordinating operations that change a state, such as organizing files, rescheduling an event, updating a record, or delivering an agreed report.

Clarify:

- Target: the exact object, record, system, or recipient involved.
- Current-to-desired state: what exists now and what should be true afterward.
- Preconditions: required inputs, current-state facts, and dependencies that make the action applicable.
- Sequence: ordering that matters; distinguish independent steps from steps that depend on prior success.
- Result confirmation: how to observe the resulting state and recognize partial completion.

Check the actual target and current state before relying on an assumed state. If a step fails or has an uncertain result, inspect what happened before repeating it; record completed and pending parts separately. Do not equate initiating an operation with observing its result.

**Completion evidence:** inspect the relevant resulting state or returned receipt/status. For a multi-action task, verify each requested outcome and report any incomplete dependent action.

## Composing Components

Write the common goal, audience, scope, and constraints once. Connect component details through references or adjacent sections:

- Evidence supports the content's claims.
- Behavioral output supplies an action's input.
- An action's resulting state supplies evidence that a workflow completed.
- Content requirements shape the output examples for a reusable reporting capability.

A component can be satisfied by an existing source. Do not copy its full contents into a brief or add fields with no bearing on the result. For a quick one-off rewrite, the user's text and requested edit may already supply all needed structure; proceed directly.
