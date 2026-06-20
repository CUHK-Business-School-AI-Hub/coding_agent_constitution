# Overlay: Identity And Access

Merge applicable sections into `SPEC.md`, `ARCH.md`, and `RULES.md`. Create the
contract section as `docs/CONTRACTS/identity-access.md`.

## SPEC Additions

```markdown
### Account Lifecycle

- Registration model: `<public | invitation | administrator-created>`
- Verification:
- Sign-in methods:
- Recovery:
- Suspension:
- Account deletion and owned data:

### Access Matrix

| Actor | Resource | Action | Condition | Result When Denied |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
```

## ARCH Additions

```markdown
### Identity And Access

- Identity provider:
- Application user mapping:
- Session strategy and lifetime:
- Authorization enforcement point:
- Email provider status: `<planned | fake | active>`
- SMS provider status: `<planned | fake | active>`
- Audit events:
- Secret owner and rotation path:
```

## RULES Additions

```markdown
## Identity And Access Rules

- Enforce authorization on the server for every protected read and mutation.
- Default to deny when identity, role, tenant, or ownership is ambiguous.
- Never log credentials, tokens, authorization headers, or one-time codes.
- Use generic responses for sign-in, reset, and verification failures.
- Rate-limit abuse-sensitive endpoints.
- Rotate or revoke sessions after credential and privilege changes.
- Test every protected action as owner, non-owner, and unauthenticated user.
```

## Contract Template

```markdown
# Identity And Access Contract

Status: Active
Last Reviewed: YYYY-MM-DD
Owner: `<module/team>`

## Identity Mapping

| Field | Meaning | Authority |
| --- | --- | --- |
| Application user ID | Immutable internal identity | Application database |
| Provider subject | Identity at one provider | Identity provider |

## Session Contract

- Transport:
- Idle/absolute expiry:
- Rotation triggers:
- Revocation behavior:

## Account Flows

| Flow | Input | Success | Stable Errors | Rate Limit |
| --- | --- | --- | --- | --- |
| Register |  |  |  |  |
| Sign in |  |  |  |  |
| Sign out |  |  |  |  |
| Recover |  |  |  |  |
| Delete |  |  |  |  |

## Authorization

| Actor | Action | Resource Predicate | Decision |
| --- | --- | --- | --- |
|  |  |  |  |

## Notification Providers

`send(templateId, recipient, variables) -> deliveryId | normalized error`

- Email adapter status:
- SMS adapter status:
- Webhook authentication and deduplication:

## Audit Events

- Sign-in success/failure without secret material
- Recovery requested/completed
- Session revoked
- Role or ownership changed
- Account suspended/deleted
```

