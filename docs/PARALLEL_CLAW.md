# Parallel Claw

Parallel Claw is the concurrent execution layer.

In the Alfred system, its strongest role is not merely "20 chat prompts." Its
strongest role is concurrent work:

- background workers prepare context before the user asks
- foreground specialist lanes handle complex tasks after the user asks

## Background Mode

Examples:

- file indexer
- text extractor
- summary backfill
- calendar linker
- meeting prep worker
- risk scanner
- relationship mapper
- daily brief writer

These workers should use cheap tools before expensive LLMs.

## Foreground Mode

Examples:

- research lane
- evidence lane
- risk lane
- dissent lane
- memory lane
- synthesis lane

Foreground mode is used when a user task needs multiple viewpoints, not for
every simple request.

