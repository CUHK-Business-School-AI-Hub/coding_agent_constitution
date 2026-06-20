# Recipe: Local Python Tool With SQLite

Status: Recommended default for a single-user local tool
Last Reviewed: 2026-06-20

This is a replaceable implementation recipe for software that runs on one
device and does not need a deployed database or application server.

SQLite is an embedded relational database. It is not itself an embedding or
vector database. Use its built-in relational and full-text capabilities first;
add a reviewed vector extension only when semantic retrieval is a measured
product requirement.

## Contents

- Fit check and recommended stack
- Application shape and SQLite rules
- Backup, export, and recovery
- Search and embeddings
- Local security and migration triggers
- Mandatory architecture decisions

## Fit Check

Use this recipe when:

- one user or one local process owns the data
- application code and the database file run on the same device
- offline operation and simple installation matter
- write concurrency is low
- the product is a CLI, personal utility, local automation, desktop companion,
  analysis tool, or prototype with durable data

Do not use this recipe when many computers directly access one database file,
multiple application servers need concurrent writes, remote clients issue SQL,
or centralized access control and operations are primary requirements.

## Recommended Stack

| Concern | Default | Reason |
| --- | --- | --- |
| Language | Python with type checks | mature local tooling and broad portability |
| Database | SQLite through Python `sqlite3` | embedded, transactional, no service to operate |
| Schema changes | numbered SQL migrations | explicit and reviewable evolution |
| Validation | Pydantic at external boundaries | typed parsing for files, CLI, and model output |
| CLI | Typer when a CLI is needed | typed commands and generated help |
| Local HTTP/UI | FastAPI only when a browser UI is needed | keep UI optional, not foundational |
| Tests | pytest with temporary database files | isolate real SQLite behavior |
| Text search | SQLite FTS5 | built-in lexical search before vector search |

Use the standard library before adding an ORM. Add SQLAlchemy only when model
mapping or multi-database support removes demonstrated complexity. Test against
SQLite itself rather than replacing database behavior with mocks.

Verify the SQLite library version and required compile-time features in every
packaged target. Do not assume FTS5 or a loadable extension is available merely
because it works on the development machine.

## Application Shape

Start with one process, one application-owned data directory, and one database
file. Keep commands/use cases separate from SQL access so a later storage
migration does not rewrite product behavior.

Store the database in the operating system's application-data location, not the
source tree, install directory, current working directory, temporary directory,
network filesystem, or actively synchronized cloud-drive folder.

Keep user documents and large replaceable binaries outside the database unless
atomic packaging is an explicit product requirement. Store stable references
and integrity metadata when files live separately.

## SQLite Rules

- Enable foreign-key enforcement on every connection.
- Set a bounded busy timeout and keep write transactions short.
- Use explicit transactions for multi-statement invariants.
- Expect many readers but only one writer at a time.
- Add indexes from observed query paths, not every column.
- Apply numbered migrations in order and record each applied migration.
- Run `PRAGMA integrity_check` as part of recovery diagnostics, not every normal
  startup.
- Do not edit generated tables, indexes, or FTS shadow tables manually.
- Treat database paths and imported database files as untrusted input.

WAL mode may improve read/write overlap for a database used on one device, but
it is a recorded choice, not an unconditional default. A WAL database includes
related `-wal` and `-shm` files while open. Backup and transfer procedures must
account for the active journal mode.

## Backup, Export, And Recovery

Provide user-visible backup and restore before real data accumulates.

- Use SQLite's backup API or `VACUUM INTO` for a consistent live copy.
- Do not copy only the main database file while a WAL database is active.
- Create a pre-migration backup before a destructive or hard-to-reverse change.
- Restore into a separate path first, run an integrity check, then switch over.
- Keep a portable export format when long-term access outside the application
  matters.
- Document where the live database and backups are stored.

SQLite does not provide application-level encrypted storage by default. Use
operating-system disk protection for ordinary local tools. Require a separate
review before adding a database encryption extension or storing high-risk data.

## Search And Embeddings

Use this escalation order:

1. Indexed relational queries.
2. FTS5 lexical search with explicit tokenizer and ranking behavior.
3. Application-side reranking for a small candidate set.
4. A SQLite vector extension only after semantic retrieval is required and
   representative evaluation shows lexical search is insufficient.

When adding embeddings, record:

- extension name, version, platform support, and loading policy
- embedding provider/model and vector dimension
- distance metric and normalization
- chunking and metadata-filter strategy
- source-document ownership and deletion propagation
- index rebuild procedure when model or dimension changes
- evaluation dataset, latency target, and maximum local storage size

Keep canonical content outside the vector index or in ordinary source tables.
Treat embeddings and vector indexes as derived data that can be rebuilt. Never
load an arbitrary SQLite extension from a user-controlled path.

## Local Security

- Do not add accounts or sessions to a strictly single-user local tool unless
  they protect a real boundary.
- Do not store API keys in the database. Prefer the operating-system credential
  store; use environment variables only when packaging constraints require it.
- Redact secrets and sensitive content from logs and crash reports.
- Validate imported files before attaching or querying them.
- Document whether uninstall preserves or deletes user data.

## Migration Triggers

Reconsider PostgreSQL or another client/server database when:

- multiple machines need direct shared access
- write contention becomes a measured problem
- the application needs multiple server instances
- centralized authorization, audit, or remote administration becomes necessary
- backups, replication, or availability need independent operators
- the database must live on a different machine from the code issuing SQL

Do not migrate merely because the row count grows. Migrate when access,
concurrency, operations, or ownership changes.

## Mandatory Architecture Decisions

Record:

- database and backup locations
- journal mode and busy timeout
- migration ownership and pre-migration backup behavior
- restore and export workflow
- secret-storage mechanism
- FTS tokenizer/ranking, if search is used
- vector extension and embedding lifecycle, if semantic retrieval is used
- triggers that require migration to a client/server database

## Primary References

- SQLite appropriate uses: https://www.sqlite.org/whentouse.html
- SQLite write-ahead logging: https://www.sqlite.org/wal.html
- SQLite backup API: https://www.sqlite.org/backup.html
- SQLite FTS5: https://www.sqlite.org/fts5.html
