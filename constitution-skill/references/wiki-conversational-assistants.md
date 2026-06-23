# Wiki: Conversational Assistants

This page explains the engineering shape behind chatbots, support assistants,
sales assistants, document Q&A, internal copilots, and AI helpers.

For the skill, this starts with the `llm-boundary` module. A conversational
assistant is not automatically an "agent". Most MVPs should begin with a bounded
model call, retrieval-grounded answer, or draft suggestion before allowing tool
execution.

## What The Founder Sees

- A user asks a question in chat.
- The assistant answers, cites sources, or says it does not know.
- The assistant may draft a reply, summarize a document, or suggest an action.
- A human can correct it or take over.
- Later, the assistant may propose actions in other systems.

## What The System Must Know

- What job the assistant is allowed to perform.
- Which sources it may read.
- Which user data may be sent to a provider.
- Whether conversation content is retained.
- Which answers require citations or visible uncertainty.
- Which outputs are suggestions vs executable decisions.
- Which tools exist, who may use them, and what requires confirmation.
- How prompt, retrieval, model, and tool changes are evaluated.

## MVP Shape

Start with the smallest useful pattern:

1. deterministic code when no model is needed
2. one model call with structured output
3. retrieval plus one model call
4. bounded tool proposal with human confirmation
5. tool execution only after the authorization and audit boundaries exist

A useful first slice is a chat UI connected to one model operation with no
tools. Add retrieval, citations, memory, and tool proposals as separate slices.

## Common Mistakes

- Letting the model decide authorization.
- Treating prompt text as a hidden implementation detail instead of versioned
  product behavior.
- Parsing important model output from free-form prose.
- Giving the assistant tools before confirmation, audit, and idempotency exist.
- Saving all conversation content forever by default.
- Mixing conversation memory with source-of-truth business records.
- Calling every chatbot an autonomous agent.

## Engineering Concepts To Learn

- **LLM boundary**: the application-owned interface around model calls.
- **Structured output**: schema-constrained data the application can validate.
- **Retrieval boundary**: what content the model may use as context.
- **Tool allowlist**: the explicit list of actions a model may propose.
- **Human confirmation**: a required review before high-impact execution.
- **Evaluation set**: examples used to detect prompt, model, or retrieval
  regressions.
- **Retention policy**: what conversation data is stored and for how long.

## When To Upgrade

Upgrade the architecture when:

- the assistant touches private or regulated data
- users rely on citations for decisions
- conversation history affects future answers
- the assistant proposes or executes tools
- support handoff becomes a core workflow
- cost, latency, refusal, or provider failure affects user trust
- prompt/model changes need repeatable evaluation

Do not upgrade because the product has a chat UI. Upgrade when the assistant can
affect records, users, external systems, money, privacy, or trust.

## Skill Assets

- `references/module-llm-boundary.md`
- `assets/module-overlays/llm-boundary.md`
- `assets/templates/conversational-assistant.md`
- `assets/contracts-examples/json-schema-validation.json`
- `assets/contracts-examples/event-payload.md`

## Research Anchors

- OpenAI Structured Outputs emphasize schema adherence and explicit refusal
  handling: https://openai.com/index/introducing-structured-outputs-in-the-api/
- OpenAI function calling treats tool arguments as schemas, not prose:
  https://developers.openai.com/api/docs/guides/function-calling
- Anthropic recommends choosing simple workflows before open-ended agentic
  systems: https://www.anthropic.com/engineering/building-effective-agents
