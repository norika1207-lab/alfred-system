# Afu Skill Runtime

Afu is the office/local runtime layer behind Alfred.

It should not be described as only a LINE bot or text assistant. In the Alfred
system, Afu contributes the prepared work-memory substrate:

- file materialization
- text extraction
- summary backfill
- file-map SQLite
- local smart search
- local model reranking
- calendar and meeting linkage
- request tracing
- quota and user gates

## File Map Pattern

```text
source files
  -> materialize
  -> extract text
  -> summarize
  -> index
  -> rerank
  -> return exact file / summary / related context
```

This enables experiences like:

```text
LINE query -> 30,000 prepared files -> correct file in about one second.
```

## Open Source Boundary

The public repo should expose contracts and reference code, not private data:

- include schemas
- include local SQLite demo
- include worker contracts
- do not include production OAuth tokens
- do not include private file indexes
- do not include private user DBs

