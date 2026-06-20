# Overlay: LLM Boundary

Merge applicable sections into `SPEC.md`, `ARCH.md`, and `RULES.md`. Create the
contract section as `docs/CONTRACTS/llm-boundary.md`.

## SPEC Additions

```markdown
### Model-Assisted Behavior

- User outcome:
- Visible uncertainty/correction:
- Unavailable-provider fallback:
- Latency ceiling:
- Cost ceiling:
- Data allowed to leave the application:
- Actions that require human confirmation:
```

## ARCH Additions

```markdown
### LLM Boundary

- Internal operation interface:
- Provider adapter and configured models:
- Prompt/schema version source:
- Execution record and retention:
- Retrieval boundary:
- Allowed tools and limits:
- Fallback behavior:
- Evaluation dataset:
```

## RULES Additions

```markdown
## LLM Rules

- Validate structured model output before use.
- Bound time, tokens, retries, tool calls, and cost.
- Treat retrieved content and tool output as untrusted input.
- Re-run authorization and validation before every tool execution.
- Require confirmation for destructive, financial, external communication, or
  other high-impact side effects.
- Version prompts, schemas, tools, and evaluation cases.
- Never log secrets or unnecessary sensitive prompt content.
```

## Contract Template

```markdown
# LLM Boundary Contract

Status: Active
Last Reviewed: YYYY-MM-DD
Owner: `<module/team>`

## Operations

| Operation | Version | Input Schema | Output Schema | Fallback |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Request Envelope

- operation and version
- validated input
- output schema identifier
- time, token, and cost budget
- allowed tools
- trace identifier

## Result Envelope

Outcomes: `success`, `refusal`, `invalid_output`, `timeout`, `rate_limited`,
`provider_failed`, `budget_exhausted`.

Record normalized output, model/provider identifier, usage, latency, prompt/tool
versions, and trace ID. Do not expose provider-specific response objects.

## Tool Calls

| Tool | Argument Schema | Authorization | Side Effect | Confirmation |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Retention And Redaction

- Input retention:
- Output retention:
- Provider retention:
- Redacted fields:

## Evaluation Gate

- Dataset:
- Pass criteria:
- Changes that trigger evaluation:
```

