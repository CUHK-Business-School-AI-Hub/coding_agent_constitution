# Flash Scenarios

These are illustrative task-contract walkthroughs for reviewing the shipped guidance. They do not report live actions, implemented products, or model-behavior evaluations. Each scenario starts from one shared contract and adds only useful component detail. The concrete choices below are example assumptions, not defaults to impose on another user's task.

## 1. usage_monitor: A Continuing Software Tool

**Request:** Build a local `usage_monitor` that reads an existing usage export and reports remaining quota.

**Common contract:** The user wants a usable report for their own planning. Reference the existing export schema and project run instructions. Read the export and calculate usage for its stated period; changing provider accounts or purchasing capacity is outside scope. Preserve the existing runtime and units. Completion means representative exports produce the expected totals and the user can invoke the tool. Unknown: whether missing quota means unknown or unlimited; clarify or expose it as unknown rather than guessing a number.

**Components:** Behavioral contract. Reuse the export schema, define command inputs and report outputs, and distinguish source data from derived totals. Examples cover an ordinary record, an empty period, missing quota, and malformed data. Add evidence/judgment only if the request also asks for forecasts or advice; reading a known export does not itself need a research framework.

**Footprint:** Existing `AGENTS.md` and a brief/`docs/PLAN.md` can hold project conventions and the contract. Link the real schema and tests rather than copy them. Software product modules are optional when they resolve an actual design question.

**Revisable plan:** Inspect schema and current code, implement parsing and reporting, exercise examples, then check invocation instructions. A different parser is an implementation change; changing what the quota figure means is an outcome change.

**Outcome checks:** Run the project's relevant tests and the actual command on representative fixtures, inspect units and totals, and distinguish fixture results from live provider data. Static documentation review cannot establish that this tool works.

## 2. A Reusable Skill

**Request:** Create a skill that converts supplied meeting notes into an action summary.

**Common contract:** The user wants a reusable capability for colleagues who supply notes. Use the existing skill format and example notes. Produce the skill and representative examples; sending summaries or creating tasks elsewhere is outside scope. Preserve only commitments supported by the notes. Completion means a fresh caller can identify when to invoke it, what to supply, and what output to expect. Unknown: preferred output format; use the user's existing template when available.

**Components:** Behavioral contract for invocation, inputs, outputs, and absent owner/deadline behavior; content blueprint for concise decisions and actions. No separate evidence framework is needed when the skill only transforms supplied text and makes no researched claims.

**Footprint:** Keep canonical behavior in `SKILL.md` and examples. Use a temporary brief only if construction needs one; do not generate parallel project contracts duplicating the skill.

**Revisable plan:** Draft the transformation instructions, work through ordinary and ambiguous notes, and revise examples where the instruction is unclear.

**Outcome checks:** Inspect installation structure and invocation guidance. Run representative cases if an execution environment is available; otherwise label them reviewed examples, not proof of model compliance. A note without an owner must not turn into an invented assignment.

## 3. Research Plus Slides

**Request:** Compare three packaging options and prepare a short decision deck for a purchasing team.

**Common contract:** The team needs a sourced comparison suited to its stated budget and delivery window. Use their existing constraints and product specifications. Deliver research findings and the requested deck; ordering products is outside scope. Completion means the comparison covers the agreed criteria and the rendered slides make the recommendation and uncertainty understandable. Unknown: a vendor's current lead time; flag the gap if it cannot be verified.

**Components:** Evidence/judgment for questions, dated sources, comparison criteria, and uncertain claims; content/structure for the takeaway, slide sequence, and presentation. Record the audience and constraints once. A citation/source map connects the two components.

**Footprint:** One brief and the requested deck are enough unless reusable source records already exist. No `ARCH.md`, database choice, or Product Shape section is needed.

**Revisable plan:** Gather comparable facts, assess options against the criteria, draft the story, and render and inspect the deck. Revise the recommendation if sources contradict an assumption; do not silently omit an unfavorable comparison criterion.

**Outcome checks:** Check material claims against sources and dates; identify inferred conclusions. Inspect the deck's rendered pages, requested coverage, legibility, and source attribution. Source checking and rendering are distinct checks.

## 4. A One-Off Document Edit

**Request:** Shorten this memo to one page for the leadership team, keeping its recommendation and figures.

**Common contract:** The supplied memo, audience, length, and preservation constraints already define the task. Completion is a readable one-page memo with the same recommendation and figures. Ask only about a material conflict, such as required content that cannot fit legibly.

**Components:** The content blueprint is already implicit in the request and source. Use it while editing; no component-selection interview or separate blueprint file is needed.

**Footprint:** Proceed directly and return the edited artifact. Do not bootstrap `AGENTS.md` or a plan for this isolated edit.

**Revisable plan:** Edit and check the rendered result; no written plan is necessary.

**Outcome checks:** Compare recommendation and figures with the source and inspect the one-page rendering. Do not claim page fit from text length alone.

## 5. Reschedule And Notify

**Request:** Move a specified team meeting to the agreed new time and notify the named participants.

**Common contract:** The user wants the selected meeting moved and its participants informed. Use the exact meeting reference, date, time zone, and participant list from the request and current calendar. Other events are outside scope. Completion means the event reflects the new time and the requested notification has a confirmed outcome. Unknowns such as duplicate meeting names or an ambiguous date must be resolved before changing the wrong event.

**Components:** Action contract: inspect the current meeting, identify the desired time, check relevant availability/preconditions, make the requested update, then notify against the resulting state. A short content blueprint is useful only if the notification's message needs composition beyond the supplied wording. Do not add a behavioral contract merely because a calendar tool is used.

**Footprint:** An in-conversation contract is sufficient; use an existing task record if the work spans a handoff.

**Revisable plan:** Resolve the target and applicable scheduling constraints, update, inspect the result, and complete the requested notification. If the event update succeeds but notification fails, preserve that distinction and inspect delivery state before repeating it.

**Outcome checks:** Check the returned event time and participants and the notification's actual status. An accepted send is not proof everyone read it. This walkthrough does not execute a calendar change or send a message.

## 6. A Weekly Analysis And Report Agent

**Request:** Build a reusable agent that analyzes a weekly support export and prepares the agreed team report; include the specifically requested scheduled delivery.

**Common contract:** The team wants a reliable weekly view of volume, themes, and unresolved issues. Reference the existing export schema, reporting definitions, audience, and agreed delivery destination and timing. Build the capability and requested delivery path; unrelated outreach or changing support records is outside scope. Completion requires the reusable behavior, report artifact, and specified run/delivery behavior to be checked. Unknowns include the reporting time zone and how partial weeks should be handled; settle what affects calculations before relying on them.

**Components:**

- Behavioral contract: invocation, export inputs, report outputs, period state, and repeated or missing-data examples.
- Evidence/judgment: metric definitions, aggregation criteria, source provenance, and uncertainty in theme classification.
- Content/structure: a concise report outline, comparison period, important changes, and limitations.
- Action contract: the requested schedule/run/delivery target, dependencies, resulting state, and confirmation of each operation.

These share one goal and context. The behavioral output feeds the report; its facts are checked against the analysis; delivery depends on a completed report. Do not create four modes or four copies of the project description.

**Footprint:** Link the canonical `SKILL.md` or implementation entry, export schema, and existing report template from a compact project brief. Add a separate interface or run record only when a consumer or later run needs it.

**Revisable plan:** Define the reporting behavior, exercise historical and incomplete exports, inspect the report, then check the requested schedule and delivery path. Building a reusable agent and performing its first live run are distinct requested outcomes; report them separately if one remains pending.

**Outcome checks:** Reconcile totals and reporting periods with source exports, review theme evidence and uncertainty, inspect rendered output where relevant, and inspect the actual configured schedule and delivery status when those actions are performed. Mocks or dry runs cannot establish a successful scheduled delivery. This walkthrough performs none of those external actions.

## What These Walkthroughs Check

Use these cases to inspect whether routing and documentation support:

- Direct execution for a clear small task.
- Behavioral detail for reusable software or capabilities without a mandatory full app file set.
- Mixed-task composition with one shared goal and context.
- Artifact, source, executable, and state checks matched to actual outcomes.
- Explicit differences between a plan, a static check, a simulated case, and a completed live result.

Automated assertions can check that these structures and links remain in the repository. They cannot demonstrate how a model selects components or performs these tasks. A later behavior evaluation would need actual task runs and inspected results.
