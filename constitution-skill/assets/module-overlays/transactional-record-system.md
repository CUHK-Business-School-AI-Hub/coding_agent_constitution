# Overlay: Transactional Record System

Merge only applicable material into the standard governance files. Do not copy
this file into the generated repository.

## SPEC Additions

```markdown
### Record Lifecycle

| Record | Owner | Created By | States | Archive/Delete Behavior |
| --- | --- | --- | --- | --- |
| `<record>` | `<user/org/system>` | `<actor>` | `<states>` | `<behavior>` |

### Query And Bulk Behavior

- Default ordering:
- Filters and search:
- Pagination:
- Import/export:
- Duplicate handling:
- Concurrent update behavior:
```

## ARCH Additions

```markdown
### Transaction And Lifecycle Rules

- Source of truth:
- Transaction boundaries:
- Identifiers and uniqueness:
- Allowed state transitions:
- Concurrency control:
- Retention/deletion:
- Backup and restore:
```

## RULES Additions

```markdown
## Record System Rules

- Apply schema changes through reviewed migrations.
- Enforce ownership and authorization on every server-side read and mutation.
- Put durable invariants in database constraints where expressible.
- Make retryable create and effectful operations idempotent.
- Reject invalid state transitions with stable error codes.
- Test cross-owner access, invalid transitions, and transaction rollback.
```

## Contract Checklist

- Database schema and constraints
- API/command input, output, and errors
- Lifecycle transition table
- Import/export schema
- Events consumed outside the owning module

