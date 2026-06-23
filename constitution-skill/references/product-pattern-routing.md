# Product Pattern Routing

Use this guide after choosing Standard, Retrofit, or Minimal mode. Mode controls
the governance footprint; product pattern controls the content inside it.

## Contents

- Selection rule
- Latent template assets
- Base profiles
- Capability modules
- Technology recipes
- Composition examples
- Question budget

## Selection Rule

Select:

1. Zero or one base profile.
2. Zero or more capability modules.
3. At most one technology recipe.

Do not force a known profile onto a product that does not fit. Use the universal
templates and record `custom` when the product shape is genuinely different.

Record the selection in `ARCH.md`:

```markdown
## Product Shape

- Base profile: `transactional-record-system`
- Capability modules: `identity-access`, `llm-boundary`
- Technology recipe: `typescript-web-postgres`
- Deviations: None.
```

## Latent Template Assets

Templates under `assets/templates/` are hidden working assets, not modes,
profiles, or user-facing choices. Use them when the user's business language
matches their trigger signals. Do not ask the human to choose a template.

Scan the template directory when the user mentions concrete product surfaces
such as records, dashboards, forms, approvals, queues, pipelines, chatbots,
assistants, knowledge bases, or handoffs. Future templates may be added without
changing this routing file; prefer the template's own trigger signals over a
hard-coded list here.

Current latent templates:

| Template | Typical user language | Usually composes with |
| --- | --- | --- |
| `record-crud` | customers, leads, orders, inventory, documents, tickets, CRM, forms, lists, exports | `transactional-record-system`, optional `identity-access` |
| `linear-workflow` | approvals, review, queue, pipeline, onboarding, fulfillment, retry, handoff | record lifecycle or `deterministic-workflow` |
| `conversational-assistant` | chatbot, AI assistant, support bot, document Q&A, knowledge base, copilot | `llm-boundary`, optional records/workflow/auth |

Use templates to improve defaults, questions, contracts, and task slicing. Keep
the durable product shape recorded in `ARCH.md` as base profile + capability
modules + technology recipe.

## Base Profiles

### Transactional Record System

Choose `transactional-record-system` when the product primarily creates,
updates, queries, and transitions durable business records.

Common signals:

- ledger entries, bookings, orders, inventory, cases, tickets, content, or CRM
- lists, forms, filters, exports, dashboards, and administrative screens
- correctness depends on ownership, state transitions, and durable storage

Read `references/profile-transactional-record-system.md` and merge the relevant
parts of `assets/module-overlays/transactional-record-system.md`.

Do not use the label to imply that the product is only CRUD. Payments,
inventory, fulfillment, and accounting each require additional domain work.

### Custom

Use `custom` when no shipped profile describes the product. Fill the universal
templates without inventing a reusable profile. Capture candidate patterns in a
case retrospective after implementation.

## Capability Modules

### Identity And Access

Choose `identity-access` whenever people or services sign in, own private data,
or have different permissions. Read `references/module-identity-access.md` and
merge `assets/module-overlays/identity-access.md`.

### LLM Boundary

Choose `llm-boundary` whenever product behavior calls a third-party or locally
hosted language model. This includes extraction, classification, generation,
chat, retrieval, and tool selection. Read `references/module-llm-boundary.md` and
merge `assets/module-overlays/llm-boundary.md`.

Do not label every LLM feature an agent. An agent exists only when model output
selects tools or controls a multi-step loop.

### Deterministic Workflow

Choose `deterministic-workflow` when work crosses multiple durable steps, may
pause or retry, or must resume after process failure. Read
`references/module-deterministic-workflow.md` and merge
`assets/module-overlays/deterministic-workflow.md`.

Do not add a workflow engine for a request that can complete in one database
transaction or one short synchronous request.

## Technology Recipe

For a new, conventional web product with no stack constraints, read
`references/recipe-typescript-web-postgres.md`. Apply it only when its fit checks
pass. A recipe is a reviewed default, not a permanent governance principle.

For a single-user tool that runs on one device without deployment, read
`references/recipe-local-python-sqlite.md`. Prefer it when application code and
the database file stay on the same device, write concurrency is low, and local
backup/export is more important than shared remote access.

SQLite is an embedded relational database, not an embedding database. If the
product needs semantic retrieval, apply the SQLite recipe's search escalation
rules and treat any vector extension as derived infrastructure.

Preserve the existing stack in Retrofit mode unless changing it is the explicit
goal and the migration cost has human approval.

## Composition Examples

| Product | Base Profile | Modules | Recipe |
| --- | --- | --- | --- |
| Local personal expense tracker | transactional record system | none | local Python + SQLite |
| Hosted expense tracker | transactional record system | identity and access | TypeScript web + PostgreSQL |
| Appointment service | transactional record system | identity and access, deterministic workflow | TypeScript web + PostgreSQL |
| AI support assistant | transactional record system | identity and access, LLM boundary | TypeScript web + PostgreSQL |
| Local document classifier | custom | LLM boundary | local Python + SQLite |
| Internal approval system | transactional record system | identity and access, deterministic workflow | TypeScript web + PostgreSQL |

## Question Budget

Ask only questions that change a durable decision. Prefer these defaults:

- one deployable application before multiple services
- one relational source of truth before multiple databases
- embedded SQLite for single-device tools before a deployed database service
- server-enforced authorization before UI-only restrictions
- structured model output before prose parsing
- database-backed state before a workflow engine
- provider adapters at external boundaries

Require explicit confirmation for public APIs, data models with migration cost,
credential handling, authorization rules, destructive operations, model-driven
side effects, regulated data, payments, and production deployment.
