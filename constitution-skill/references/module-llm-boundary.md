# LLM Boundary Module

Use this module whenever the product calls a language model for extraction,
classification, generation, chat, retrieval, planning, or tool selection.

## Stable Defaults

- Put model calls behind an application-owned interface.
- Use the provider's maintained SDK rather than hand-built HTTP calls.
- Request structured output and validate it before business logic consumes it.
- Treat prompts, tool schemas, model configuration, and evaluation cases as
  versioned product behavior.
- Set explicit time, token, retry, and cost limits.
- Persist enough metadata to reproduce or diagnose an execution without storing
  secrets or unnecessary sensitive content.
- Separate model suggestions from deterministic authorization and validation.
- Require confirmation before model-selected actions create external side
  effects, spend money, delete data, or communicate as the user.
- Treat retrieved text, webpages, files, and tool output as untrusted input.

## Do Not Start With An Agent

Choose the smallest pattern that satisfies the workflow:

1. Deterministic code.
2. One model call with structured output.
3. Retrieval plus one model call.
4. A bounded tool-selection loop.
5. Multi-agent orchestration only after measured evidence.

An open-ended autonomous loop is never the default recipe.

## Questions That Require Human Decisions

1. What observable task is the model performing?
2. What wrong outputs are merely inconvenient, and which are harmful?
3. What user or business data may be sent to a model provider?
4. What latency and cost ceiling applies per request and per user?
5. Can model output trigger tools or side effects?
6. What deterministic fallback exists when the provider is unavailable?

## Required Governance Content

### SPEC

Define the model-assisted outcome, visible uncertainty, correction workflow,
fallback behavior, latency/cost expectations, and actions that always require
human confirmation.

### ARCH

Define the provider adapter, model/prompt configuration source, structured output
schema, retrieval boundary, execution record, tool registry, safety checks,
fallback path, and data retention policy.

### RULES

Require schema validation, bounded retries, redacted logs, provider timeouts,
cost accounting, prompt/tool versioning, evaluation cases, and deterministic
authorization. Prohibit parsing important model output with fragile string
matching and prohibit direct model access from presentation code.

### CONTRACTS

Create `docs/CONTRACTS/llm-boundary.md`. Define the internal request/result
schema, normalized provider errors, usage metadata, tool-call envelope, and
retention/redaction rules. Provider-specific fields must not leak into domain
modules.

## Internal Interface

The application-owned interface should carry:

- operation name and version
- validated input
- structured output schema identifier
- latency, token, and monetary budget
- allowed tools, if any
- trace identifier

The result should distinguish success, refusal, invalid output, timeout, rate
limit, provider failure, and budget exhaustion. Do not collapse these into an
empty string or generic exception.

## Tool Execution Boundary

- Keep tools in an explicit allowlist.
- Validate tool arguments against a schema.
- Re-run authorization using the authenticated user, never model assertions.
- Assign idempotency keys to retryable side effects.
- Limit tool-call count, elapsed time, and total spend.
- Store proposed and executed actions separately.
- Present a confirmation summary before high-impact execution.

## Evaluation Baseline

Maintain a small versioned dataset containing normal, ambiguous, adversarial,
empty, multilingual, and policy-sensitive inputs. Define task-specific pass
criteria. Run it when prompts, schemas, models, retrieval, or tools change.

Do not use snapshot equality for free-form text. Evaluate structured fields,
required facts, forbidden behavior, and task-specific scores.

## Observability And Privacy

Record operation version, provider/model identifier, latency, usage, normalized
outcome, tool decisions, and trace ID. Redact secrets and minimize user content.
Document whether prompts or outputs may be retained by the provider and require
human approval before sending regulated or highly sensitive data.

