# Identity And Access Module

Use this module whenever users or services authenticate, own non-public data, or
have different permissions.

## Stable Defaults

- Prefer a maintained authentication library or managed identity provider over
  custom credential and token code.
- Keep provider identity separate from the application's user record.
- Enforce authorization on the server for every protected read and mutation.
- Default to deny when identity, tenant, role, or ownership is ambiguous.
- Use secure, HTTP-only, same-site cookies for browser sessions unless a
  documented client constraint requires bearer tokens.
- Store password hashes only. When password authentication is owned locally, use
  a memory-hard password hashing implementation with maintained defaults.
- Return non-enumerating responses for sign-in, reset, and verification flows.
- Make sessions revocable and rotate them after privilege or credential changes.
- Put email and SMS behind provider interfaces; use fake providers in tests.

## Separate The Concepts

- Authentication establishes an identity.
- Authorization decides whether that identity may perform one action on one
  resource.
- Account lifecycle covers registration, verification, recovery, suspension,
  provider linking, and deletion.

Do not use a single `isAdmin` check as a substitute for an authorization model.

## Questions That Require Human Decisions

1. Is access public, invitation-only, organization-based, or administrator-made?
2. Which resources are private, shared, organization-owned, or public?
3. Are passwords required, or can the first release use magic link or OAuth?
4. Must sessions be revoked immediately after password reset or suspension?
5. Is multi-factor authentication required by risk or regulation?
6. What must happen to owned data when an account is deleted?

## Required Governance Content

### SPEC

Define registration, verification, sign-in, sign-out, recovery, suspension,
deletion, and access-denied behavior. Name roles only after listing the actions
each role can perform.

### ARCH

Define the identity provider boundary, application user mapping, session model,
authorization enforcement point, email/SMS interfaces, audit events, and secret
ownership.

### RULES

Require server-side authorization, generic recovery responses, secret redaction,
rate limiting on abuse-sensitive endpoints, session rotation, and negative
authorization tests. Prohibit logging passwords, reset tokens, session tokens,
authorization headers, or one-time codes.

### CONTRACTS

Create `docs/CONTRACTS/identity-access.md` using the shipped overlay. Include
flow inputs/outputs, stable error codes, session behavior, authorization rules,
provider interfaces, audit events, and deletion behavior.

## Authorization Pattern

Express authorization as an action on a resource:

```text
can(identity, action, resource) -> allow | deny
```

Keep ownership or tenant predicates close to data access so callers cannot
forget them. Administrative bypasses must be explicit and audited.

## Provider Boundary

Email and SMS interfaces should accept a template identifier and structured
variables, not arbitrary provider-specific payloads. Return an internal delivery
identifier and normalized status. Provider webhooks must be authenticated,
deduplicated, and mapped to internal events.

Do not claim that an interface is implemented merely because it is reserved in
the architecture. Mark adapters as planned, fake, or active.

## Verification Baseline

At minimum verify:

- successful and failed sign-in without account enumeration
- session expiry, logout, revocation, and rotation
- recovery token single use and expiry
- every protected action for owner, non-owner, and unauthenticated user
- role or tenant boundary changes
- suspended and deleted accounts
- provider failures without leaking secrets

## Approval Boundary

Require human approval before selecting the production identity provider,
enabling password authentication, defining roles, changing session lifetime,
adding administrator bypasses, or deciding account deletion semantics.

