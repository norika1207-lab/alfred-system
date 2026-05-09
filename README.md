# Alfred System

**Background cognition instead of foreground token burn.**

Alfred is a personal AI Agent system that prepares your work memory in the
background, then uses local models, file maps, and concurrent workers to find
files, read images, summarize documents, prepare meetings, and finish complex
tasks faster and safer across the interfaces you already use.

This repository is the clean open-source reference architecture for the Alfred
system. It does not include private user data, production secrets, LINE tokens,
Google OAuth tokens, private databases, or proprietary deployment files.

## The Core Idea

Most AI agents wait until the user asks, then send large context to an expensive
model.

Alfred uses a different cost curve:

```text
before the user asks:
  background workers index, extract, summarize, cluster, and link context

when the user asks:
  retrieve prepared local memory
  use a small local model or cloud model only if needed
  return the result quickly
```

The result is an AI system that can feel as useful as a large LLM while using
far cheaper background computation.

## Demo Claims This Architecture Is Built Around

These are the concrete product moments the architecture is designed to support:

```text
1 second:
  Ask in Telegram, search 30,000 prepared files, return the correct file.

14.3 seconds:
  Upload a dense exam sheet image, extract questions and answers, reply.

20 concurrent workers:
  Indexers, extractors, summarizers, meeting-prep workers, risk scanners,
  relationship mappers, and synthesis workers prepare context before the user asks.
```

## System Parts

| Part | Role |
|---|---|
| Alfred | User-facing personal AI Agent system across voice, Safari, Telegram, email, and future channels |
| Afu Skill Runtime | High-performance office/local runtime: file-map, local model, Drive, Calendar, meetings, OCR, tracing |
| Afu Brain | Memory, cognition, routing, safety, and learning layer |
| Parallel Claw | Concurrent background workers and foreground specialist-agent execution |
| MASL / Brain Gate | Final action gate: allow, prepare, ask, or block |

Correct relationship:

```text
Alfred receives the request.
Afu Brain decides memory, route, risk, and approval boundary.
Afu Skill Runtime supplies prepared local work memory.
Parallel Claw runs background workers or foreground specialist lanes.
MASL / Brain Gate stops risky final actions.
Feedback updates Afu Brain.
```

## What Is In This Release

This repository includes:

- architecture docs
- public schemas
- a local SQLite file-memory reference implementation
- Afu Brain style routing and decision contracts
- Parallel Claw style worker contracts
- a small runnable demo
- safety and privacy rules for open-source releases

It intentionally does not include:

- production Alfred backend source
- private Afu deployment files
- private Google/LINE/Telegram credentials
- private user files or DBs
- internal logs
- user identity mappings

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

alfred-system-demo
```

Or run directly:

```bash
python3 examples/demo.py
```

The demo creates a temporary file-memory index, runs background workers, asks a
file-search request, routes it through Afu Brain, and returns a prepared result.

## Browser Demo

Live demo:

```text
https://charenix.com/alfred/demo
```

Local static demo:

```bash
python3 -m http.server 18790
open http://127.0.0.1:18790/web/alfred-morning-brief-demo.html
```

The public demo uses a server-side TTS proxy. Do not put ElevenLabs or other API
keys in the browser. For local narration, copy:

```bash
cp web/local-tts-config.example.js web/local-tts-config.js
```

Then add local credentials to `web/local-tts-config.js`. That file is ignored by
git and must never be committed.

## Why This Is Not Just RAG

RAG usually means "retrieve when asked."

Alfred's file memory is prepared before the question:

```text
materialize -> extract -> summarize -> classify -> link -> cache -> search
```

The search path should be fast because the expensive work happened ahead of
time. A local model can be used for reranking or synthesis, but the system should
not default to sending the entire private file world to a cloud model.

## Why This Is Not 20 Expensive LLM Calls

Parallel Claw has two modes.

### Background Worker Mode

Runs continuously or on schedule:

- file indexer
- text extractor
- summary backfill
- calendar linker
- meeting prep worker
- risk scanner
- duplicate/stale detector
- relationship mapper
- search optimizer
- daily brief writer

Many of these workers use cheap tools:

- SQLite
- metadata
- full-text search
- deterministic rules
- local embeddings
- cached summaries
- local models

### Foreground Specialist Mode

Runs when a complex task needs parallel analysis:

- research lane
- evidence lane
- risk lane
- dissent lane
- memory lane
- execution draft lane
- synthesis lane

Foreground mode is useful, but the bigger breakthrough is background cognition.

## Final Action Safety

Alfred can prepare real work, but must not silently cross dangerous final action
boundaries.

Blocked or approval-gated actions include:

- send
- pay
- publish
- submit
- merge
- delete
- trade
- transfer

Every run should end as:

```text
completed
needs_approval
blocked
failed_with_trace
```

## Repository Layout

```text
src/alfred_system/
  brain.py          Afu Brain style routing and decision logic
  file_memory.py    SQLite file-map and prepared-memory reference
  workers.py        background worker contracts
  parallel_claw.py  foreground/background execution contracts
  schemas.py        dataclasses shared by the reference runtime
  cli.py            demo CLI

schemas/
  alfred_event.schema.json
  brain_decision.schema.json
  worker_result.schema.json
  parallel_run.schema.json

docs/
  ARCHITECTURE.md
  AFU_SKILL_RUNTIME.md
  AFU_BRAIN.md
  PARALLEL_CLAW.md
  PRODUCT_STORY.md
  OPEN_SOURCE_BOUNDARY.md
  SECURITY_AND_PRIVACY.md
  VOICE_TTS_HANDOFF.md
  RELEASE_CHECKLIST.md
  SYSTEM_HANDOFF.md
```

## Recommended Reading Order

1. `docs/PRODUCT_STORY.md`
2. `docs/ARCHITECTURE.md`
3. `docs/AFU_SKILL_RUNTIME.md`
4. `docs/AFU_BRAIN.md`
5. `docs/PARALLEL_CLAW.md`
6. `docs/SECURITY_AND_PRIVACY.md`
7. `docs/OPEN_SOURCE_BOUNDARY.md`
8. `docs/VOICE_TTS_HANDOFF.md`
9. `docs/RELEASE_CHECKLIST.md`

## Product Sentence

```text
Alfred works before you ask.
```

Commercial version:

```text
Alfred turns your files, calendar, meetings, and messages into instant private
work memory, then uses local models and concurrent agents to finish real tasks
faster, cheaper, and safer.
```
