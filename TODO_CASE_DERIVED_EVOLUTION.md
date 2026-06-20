# Case-Derived Evolution TODO

This file tracks work that should not be presented as settled guidance inside
`constitution-skill` yet. Promote an item only after evidence from real projects
or an appropriate domain review.

## Promotion Rule

- One case: keep the lesson in that case retrospective.
- Two similar cases: mark it as a candidate profile or module rule.
- Three independent cases: consider promotion into a shipped reference or
  overlay.
- Cross-product repetition: consider promotion into the universal templates.
- Mechanically checkable rule: consider adding it to `check-governance.sh`.

Before promotion, distinguish a stable principle from a framework, vendor, or
project-specific preference.

## P0: Collect Real Cases

- [ ] Run the transactional record system profile on at least three products:
  one personal tool, one multi-user business tool, and one order/booking system.
- [ ] Run the identity/access module on invitation-only, public-registration,
  and organization-owned products.
- [ ] Run the LLM boundary module on one extraction/classification feature, one
  retrieval/chat feature, and one tool-executing workflow.
- [ ] Run the deterministic workflow module on one database-backed job and one
  genuinely long-running or approval-based workflow.
- [ ] For every case, capture initial omissions, governance changes, rework,
  useful defaults, rejected defaults, and project-specific decisions.
- [ ] Measure whether a fresh coding agent can implement the first task without
  hidden chat context.

## P0: Validate The Golden Recipe

- [ ] Build at least two small projects from the TypeScript/PostgreSQL recipe and
  record setup time, generated governance quality, migration experience, and
  deployment friction.
- [ ] Review current official documentation and security advisories for every
  named framework before each recipe review date.
- [ ] Decide whether Next.js remains the best zero-background default after
  comparing a simpler server-rendered stack and a backend-first stack.
- [ ] Test whether Drizzle migrations remain understandable to non-technical
  owners during a real schema change and rollback.
- [ ] Define a documented recipe replacement process before adding another
  framework recipe.
- [ ] Build at least three local SQLite tools: one CLI, one local browser UI,
  and one LLM-assisted document tool.
- [ ] Test backup/restore with rollback journal and WAL mode, including an
  interrupted migration and a corrupt-copy recovery drill.
- [ ] Compare FTS5-only retrieval with a SQLite vector extension on a real local
  document corpus before recommending any vector extension by name.
- [ ] Test packaging and application-data paths on macOS, Windows, and Linux.

## P1: Provider And Region Decisions

These choices vary by geography, budget, regulation, and procurement. Keep them
out of the stable module guidance until the project context is known.

- [ ] Create a decision matrix for managed identity providers versus Auth.js,
  including data region, exportability, account linking, MFA, pricing, and local
  development.
- [ ] Create separate email and SMS provider matrices for global and mainland
  China deployments.
- [ ] Compare PostgreSQL hosting options by region, backup, point-in-time
  recovery, connection limits, and exit path.
- [ ] Define LLM provider selection criteria for data retention, supported
  regions, structured output, tool calling, cost, latency, and fallback.
- [ ] Validate hosting recipes in the target region instead of declaring one
  universal provider.

## P1: Candidate Modules Requiring More Evidence

- [ ] Multi-tenant SaaS: tenant isolation, organization lifecycle, invitations,
  role inheritance, tenant-scoped uniqueness, and tenant export/deletion.
- [ ] Notifications: email/SMS/push preferences, templates, delivery state,
  retries, suppression, and webhook normalization.
- [ ] File/object storage: upload authorization, content type validation,
  scanning, retention, signed access, and orphan cleanup.
- [ ] Search/RAG: indexing ownership, freshness, citations, access filtering,
  deletion propagation, and evaluation.
- [ ] Audit log: event taxonomy, actor identity, tamper resistance, retention,
  export, and privacy boundaries.
- [ ] Offline/local-first: conflict resolution, sync protocol, device identity,
  encryption, migration, and recovery.

## P2: Domain-Specific Packs

Do not call these industry best practices without qualified domain review.

- [ ] Payments and refunds.
- [ ] Inventory reservation and fulfillment.
- [ ] Double-entry accounting and financial reporting.
- [ ] Healthcare or other regulated personal data.
- [ ] Tax, invoicing, employment, or legal records.
- [ ] Safety-critical or high-stakes automated decisions.

Each pack needs a domain owner, explicit jurisdiction, failure analysis, and
review schedule.

## Keep Outside The Skill Core

- Exact dependency versions; keep them in generated lockfiles.
- Universal cloud, identity, SMS, email, database, or LLM vendor endorsements.
- Claims of legal or regulatory compliance.
- A default autonomous multi-agent framework.
- A default durable workflow engine before scale and recovery needs are known.
- Product-specific schemas, roles, pricing, tax rules, or lifecycle semantics.
- Generated application boilerplate until repeated cases show that governance
  templates alone are insufficient.

## Evaluation And Maintenance

- [ ] Add case-retrospective fixtures that can be reviewed without leaking the
  intended answer to the evaluating agent.
- [ ] Add forward tests for profile/module selection and over-engineering
  avoidance.
- [ ] Add a recipe staleness check based on `Last Reviewed`.
- [ ] Review false positives from Product Shape and contract warnings after real
  adoption.
- [ ] Promote only evidence-backed changes and record why each rule entered the
  skill.
