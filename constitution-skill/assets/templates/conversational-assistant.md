# Template: Conversational Assistant Surface

Status: Latent asset
Use when mentioned, do not present as a new mode.

## Trigger Signals

Use this template when the user describes a chatbot, AI assistant, support bot,
sales assistant, document Q&A, knowledge base assistant, internal helper,
copilot, chat interface, human handoff, or conversation memory.

This template usually composes with:

- Capability module: `llm-boundary`
- Base profile: `transactional-record-system` when conversations, tickets,
  sources, or handoffs are durable records
- Capability module: `identity-access` when private data or role-specific
  answers are involved
- Capability module: `deterministic-workflow` only when the assistant starts a
  durable process that can pause, retry, or require approval

## Quiet Use Rule

Do not ask the human to choose this template. Infer it from chat and assistant
language. Keep the visible product discussion in user outcomes; record the
engineering boundaries in `ARCH.md`, `RULES.md`, and contracts.

## MVP Defaults

- Start with answer drafting or retrieval-grounded Q&A before autonomous action.
- Keep conversation state separate from source-of-truth business records.
- Show uncertainty, citations, or "I do not know" behavior when grounding is
  required.
- Provide a human correction or handoff path before expanding automation.
- Use structured output for decisions the application consumes.
- Keep tools on an allowlist and require confirmation for high-impact actions.
- Log enough metadata to debug failures without storing unnecessary sensitive
  content.
- Maintain a small evaluation set before changing prompts, retrieval, models, or
  tool schemas.

## SPEC Snippet

```markdown
### Conversation Experience

- Assistant job:
- Users and channels:
- Source material it may use:
- What it must not answer:
- Visible uncertainty or citation behavior:
- Correction or handoff path:
- Memory and retention expectation:
- Actions requiring confirmation:
```

## ARCH Snippet

```markdown
### Conversational Boundary

- Conversation/session store:
- Source retrieval boundary:
- Prompt and tool version source:
- Structured output schemas:
- Tool allowlist:
- Human confirmation path:
- Evaluation dataset:
- Retention and redaction policy:
```

## CONTRACT Snippet

Create or update `docs/CONTRACTS/llm-boundary.md` and add conversation-specific
fields:

- conversation/session identifier
- message roles and persisted metadata
- retrieval source identifiers and citation requirements
- normalized refusal, unknown, timeout, and provider failure outcomes
- tool proposal vs executed action records
- retention and redaction rules for messages and retrieved content

## Task Slicing

Good first slices:

- Add a chat UI that calls a single model operation with no tools.
- Add retrieval with citations from one approved source.
- Add structured output for one business decision.
- Add a human-confirmed tool proposal without automatic execution.

Split when a task adds chat UI, retrieval, tools, persistence, and external
actions at the same time.

## Approval Triggers

Require explicit human approval for:

- sending private, regulated, or highly sensitive content to a model provider
- enabling tools that send messages, spend money, delete data, or act as a user
- retaining conversation content beyond the documented policy
- letting model output decide authorization, ownership, pricing, or eligibility
