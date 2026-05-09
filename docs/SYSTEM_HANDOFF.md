# Alfred System README

Version: 2026-05-09

This document is the canonical handoff for the integrated Alfred system. Read
this before discussing Alfred, Afu, Afu Brain, Parallel Claw, or any related
agent architecture.

## 1. The Core Insight

Alfred is not just a voice assistant, chatbot, dashboard, or multi-agent demo.

Alfred is a personal AI Agent system that prepares the user's work memory in the
background, then uses that prepared memory to answer, act, and coordinate agents
quickly and safely across voice, Safari, Telegram, email, and future channels.

The key product insight:

```text
Do not burn expensive foreground tokens every time the user asks.
Use cheap background cognition to prepare the world before the user asks.
```

Alfred's value is not only that it can run agents. The value is that it can run
background workers, local models, file-map indexing, extraction, summaries,
calendar linkage, and memory updates ahead of time, so the user experiences
LLM-like outcomes without LLM-like cost.

Core phrase:

```text
Background cognition instead of foreground token burn.
```

## 2. Public Product Story

Use public language people already understand:

- AI Agent
- local model
- private file search
- 20 concurrent agents / workers
- LINE / App / Safari / Telegram
- faster, safer, cheaper
- asks before risky actions

Do not lead with only "proactive butler." It is true internally, but too abstract
for people who do not already understand the system.

### One-Sentence Pitch

```text
Alfred is a personal AI Agent system that prepares your work memory in the
background, then uses local models and concurrent agents to find files, read
images, summarize documents, prepare meetings, and finish complex tasks faster
and safer across every interface you already use.
```

### Short External Pitch

```text
Install Alfred, connect your files and calendar, and let it work in the
background. When you wake up, Alfred already knows your files, meetings,
summaries, risks, and next actions. Ask in Telegram, Safari, Telegram, or the app;
Alfred can answer from prepared local memory instead of burning expensive
cloud tokens every time.
```

### Demo-First Story

Lead with measurable moments:

```text
1 second:
LINE message -> search 30,000 files -> return the correct file.

14.3 seconds:
LINE image upload -> read a dense exam sheet -> extract questions and answers.

20 concurrent workers:
background indexers, extractors, summarizers, meeting-prep agents, risk scanners,
relationship mappers, and synthesis workers prepare context before the user asks.
```

The public should feel:

```text
This is not a chatbot. This is an AI work memory that is already prepared.
```

## 3. The Four Main Parts

The integrated system has four major parts.

| Part | Role | What It Means |
|---|---|---|
| Alfred | Personal AI Agent product and user experience | The thing people use through voice, App, Safari, LINE, Telegram |
| Afu | High-performance office/local runtime | File-map, local model, Drive, Calendar, meetings, LINE workflow, tracing, enterprise tier |
| Afu Brain | Memory, cognition, routing, safety, learning | The layer that decides what matters, what route to use, what is safe, and what to learn |
| Parallel Claw | Parallel execution engine | The runtime for foreground complex tasks and coordinated specialist lanes |

Correct hierarchy:

```text
Alfred is the product.
Afu is Alfred's optimized work/runtime skill system.
Afu Brain is Alfred's cognition and decision layer.
Parallel Claw is Alfred's parallel execution engine.
```

Do not present these as competing products.

## 4. The Real Architecture

```text
User
  -> Alfred Interface
       iOS voice
       Safari web
       LINE
       Telegram
       future desktop/API channels

  -> Unified Event Router
       owner identity
       channel normalization
       mode detection
       attachment classification

  -> Afu Brain
       memory lookup
       intent/risk classification
       route decision
       safety boundary
       learning update plan

  -> Capability Runtime
       Alfred native skills
       Afu office/local runtime skills
       Parallel Claw complex-task execution
       RAG / file vault / search

  -> MASL / Brain Gate
       allow
       prepare
       ask
       block

  -> Result
       voice reply
       LINE message
       Telegram message
       Safari/App card
       file attachment
       report

  -> Feedback + Learning
       accepted
       rejected
       corrected
       ignored
       completed
       blocked
       remembered
```

## 5. Alfred

Alfred is the user-facing system.

Original Alfred direction:

- zero-interface
- voice-first
- proactive
- private butler feeling
- knows one owner
- follows through
- does not ask the same question forever

Current Alfred capabilities include:

- iOS voice app
- Safari/web-capable backend
- LINE and Telegram channels
- ElevenLabs cloned Alfred voice
- STT
- TTS
- passive ambient recording
- image/photo analysis
- document analysis
- Google Calendar
- Google Drive
- Mac file index
- location context
- family and HealthKit features
- long response distribution through LINE, Telegram, and Gmail
- per-user DB boundary

Alfred should remain the product that users experience. The internal modules
should serve Alfred, not replace it.

## 6. Afu

Afu must not be reduced to "office LINE bot."

Afu is a high-performance office agent runtime and local-model execution
substrate. It is one of the most valuable parts of the integrated system.

Afu provides:

- LINE-first office workflow
- Calendar
- Google Drive
- meeting audio transcription and diarization
- OCR
- web search
- memory
- scheduler
- request queue
- tracing with `requestGroupId`
- quota and user gate
- provider routing
- home and enterprise deployment tiers
- local vLLM / Qwen runtime
- GX10 file-map and summary runtime

### Afu Local Runtime

Afu has two tiers:

```text
home:
  Mac mini
  cloud provider chain
  small deployment

enterprise:
  NVIDIA/GX10-class host
  vLLM first
  local Qwen model
  privacy and throughput focused
```

Afu enterprise tier:

```text
LLM_PROVIDER=vllm
VLLM_BASE_URL=http://host.docker.internal:8000
provider chain: vLLM -> copilot -> anthropic
```

This matters because Alfred should not call cloud LLMs for every familiar work
task. Afu gives Alfred a local, optimized, cheaper path.

### Afu File Map + Summary Runtime

This is a major product asset.

Afu can turn scattered files into AI-readable work memory:

```text
Drive materialization
file extraction
summary backfill
local smart-search
file-map sqlite
local Qwen/vLLM rerank
LINE return path
```

The value:

```text
30,000 files can become an indexed private work memory.
The user can ask in LINE and receive the correct file in about one second.
```

This is not ordinary search and not ordinary RAG. It is a prepared local memory
surface that makes the system feel instant.

## 7. Afu Brain

Afu Brain is Alfred's cognition and decision layer.

It should decide:

- what the user means
- what memory matters
- whether the user is in home, office, travel, family, or silent mode
- whether Afu should handle the task
- whether Parallel Claw should run
- whether a local model is enough
- whether a cloud/frontier model is needed
- whether the final action can run, should prepare only, must ask, or must block
- what should be learned afterward

Afu Brain is not only a safety library.

It is the layer that turns repeated work into cheaper future cognition.

Important rule:

```text
The more Alfred is used, the less it should need to ask or spend expensive
cloud tokens for familiar situations.
```

Structured decision shape:

```json
{
  "owner_id": "string",
  "request_id": "string",
  "intent": "file_search | calendar | meeting | document | image_ocr | research | message | purchase | code_review | other",
  "mode": "home | office | travel | family | silent | unknown",
  "risk": "low | medium | high | irreversible",
  "route": "alfred_native | afu_local_runtime | afu_office | parallel_claw | rag_only | ask_owner | block",
  "decision": "allow | prepare | ask | block",
  "approval_required": true,
  "memory_refs": [],
  "capabilities": [],
  "blocked_final_action": "send | pay | publish | submit | merge | delete | trade | none",
  "reason": "inspectable reason",
  "learning_update": {}
}
```

## 8. Parallel Claw

Parallel Claw is the parallel execution runtime.

Earlier framing focused too much on foreground "20 agents after the user asks."
That is useful, but not the whole point.

The stronger framing:

```text
20 concurrent workers can operate in the background under Afu's architecture.
They do not have to be 20 expensive LLM calls.
```

Parallel Claw should support two modes:

### 8.1 Background Worker Mode

Runs before the user asks.

Examples:

- Drive indexer
- Mac file indexer
- OCR extractor
- text extractor
- summary backfill worker
- duplicate/stale file detector
- calendar planner
- meeting prep worker
- email/message context mapper
- promise tracker
- relationship graph updater
- topic clusterer
- risk scanner
- search optimizer
- daily brief writer
- local model distiller
- safety boundary marker

Many of these workers can use cheap tools:

- SQLite
- FTS
- metadata
- file hashes
- local indexes
- deterministic rules
- local embeddings
- local Qwen/vLLM
- cached summaries

They should not default to cloud LLM calls.

### 8.2 Foreground Specialist Mode

Runs when the user asks a complex task that benefits from parallel reasoning.

Examples:

- contract comparison
- code review
- purchase research
- market research
- launch plan
- strategy decision
- high-risk action preparation

Foreground Parallel Claw produces:

- lane results
- disagreement
- synthesis
- prepared actions
- blocked final action
- approval prompt
- trace

## 9. The Cost Curve

This is one of the most important parts of the system.

Bad cost curve:

```text
user asks
  -> send huge context to cloud LLM
  -> pay tokens
  -> wait
  -> repeat every time
```

Alfred cost curve:

```text
background workers prepare context
  -> file map
  -> summaries
  -> memory
  -> routing
  -> local model distillation
  -> user asks
  -> retrieve prepared answer/context
  -> small local or cloud call only if needed
```

The product claim:

```text
Alfred gives LLM-like outcomes without LLM-like cost.
```

More precise:

```text
Alfred uses cheap background cognition and local runtime to reduce expensive
foreground reasoning.
```

This is why Afu is strategic. Afu already contains the local runtime and
file-map machinery that makes this cost curve real.

## 10. User Experience

The ideal first-use experience:

```text
Install Alfred.
Connect files, calendar, LINE/Telegram, and optional local runtime.
Alfred says: "Let me prepare your work memory in the background."
The user goes to sleep.
Background workers index, extract, summarize, cluster, link, and prepare.
The next morning Alfred has a useful brief ready.
```

Morning experience:

```text
Good morning.
I prepared today's work memory.

You have three meetings.
The 10:30 meeting has four related files.
One quote sheet differs from last week's version.
The V121 land file you mentioned is ready.
Two follow-ups are still open.
I can send you the brief, open the files, or prepare the meeting notes.
```

This is the "Alfred feeling."

The user should feel:

```text
It worked while I slept.
It already knows where my work is.
It gives me results before I ask.
It is fast because the work was already prepared.
```

## 11. Concrete Demo Ladder

Use this sequence for demos, investor pitches, README visuals, and product
videos.

### Demo 1: One-Second File Retrieval

```text
Input:
LINE message: "Find the V121 land file."

System:
Afu file-map searches 30,000 prepared files.

Output:
Alfred returns the correct file in about one second.
```

Why it matters:

```text
This proves the system has private work memory, not just chat.
```

### Demo 2: 14.3-Second Dense Image Reading

```text
Input:
LINE image upload: dense exam questions and answers.

System:
OCR / vision extraction / structure parsing / response.

Output:
Alfred replies with extracted content in 14.3 seconds.
```

Why it matters:

```text
This proves Alfred can read new real-world input, not only search old files.
```

### Demo 3: Overnight Work Memory Preparation

```text
Input:
Connect Drive and Calendar.

System:
Background workers index, summarize, cluster, and link files to meetings.

Output:
Morning brief with meetings, relevant files, open promises, risks, and next actions.
```

Why it matters:

```text
This proves proactive background cognition.
```

### Demo 4: Complex Task With Approval Gate

```text
Input:
"Compare these documents, prepare a response, but do not send it."

System:
Parallel Claw runs specialist lanes.
Afu Brain checks final action risk.

Output:
Report and draft are prepared.
Send action is blocked until approval.
```

Why it matters:

```text
This proves useful autonomy without blind authority.
```

## 12. Integration Rules

Future coding work should follow these rules.

1. Alfred is the product entry.
2. Afu should be integrated as Alfred's local/office runtime skill system.
3. Afu Brain must sit before high-risk action and routing decisions.
4. Parallel Claw should support background worker mode and foreground complex-task mode.
5. The system should prefer prepared local memory before expensive cloud calls.
6. Private user data must not be shipped into public RAG packs.
7. Every result should create a feedback/learning event.
8. Dashboards are evidence, not the main product experience.
9. The public story should start with concrete speed and utility, not internal philosophy.
10. Do not mutate production Alfred directly. Work in a sandbox, review diff, then deploy.

## 13. Suggested Technical Integration Path

### Phase 1: Sandbox Copy

Pull Alfred and Afu code into a local sandbox. Do not patch production VPS
directly.

### Phase 2: Unified Event Schema

Normalize inputs from:

- iOS voice
- Safari
- LINE
- Telegram
- Afu LINE
- file/image upload
- calendar events
- background worker events

into one `AlfredEvent`.

### Phase 3: Identity Mapping

Create unified owner identity across:

- Alfred device id
- Alfred user id
- LINE user id
- Telegram chat id
- Google account
- Afu office user id
- Afu Brain memory namespace

### Phase 4: Afu Brain Decision API

Add an internal decision path:

```text
POST /internal/afu/decide
```

It should return `BrainDecision`.

### Phase 5: Afu Skill Bridge

Expose Afu as Alfred capabilities:

```text
afu.file.find
afu.file.summarize
afu.file.materialize
afu.calendar.brief
afu.meeting.prepare
afu.ocr.extract
afu.local_model.rerank
afu.daily_brief
```

### Phase 6: Background Worker Scheduler

Create a background worker registry:

```text
file_indexer
text_extractor
summary_backfill
calendar_linker
meeting_prep
risk_scanner
daily_brief
relationship_mapper
search_optimizer
```

### Phase 7: Parallel Claw Runtime

Add two modes:

```text
parallel_claw.background_workers
parallel_claw.foreground_task
```

### Phase 8: Feedback Loop

Write every result into learning events:

```text
accepted
rejected
corrected
ignored
completed
blocked
```

Afu Brain uses these to improve routing and memory.

## 14. The Final Product Claim

The integrated Alfred system is:

```text
A personal AI Agent system that prepares your work memory in the background,
uses local models and concurrent workers to reduce cloud-token burn, retrieves
your files and context at human speed, reads real-world inputs, coordinates
specialist agents for complex work, and asks before risky final actions.
```

Shorter:

```text
Alfred works before you ask.
```

Commercial version:

```text
Alfred turns your files, calendar, meetings, and messages into instant private
work memory, then uses local models and concurrent agents to finish real tasks
faster, cheaper, and safer.
```

## 15. What Future Windows Must Remember

If you only remember one thing, remember this:

```text
The breakthrough is not 20 expensive LLM calls.
The breakthrough is 20 cheap background cognition workers, local file memory,
and Afu Brain routing, so Alfred can feel as capable as an LLM while costing far
less and responding much faster.
```

Afu is not a small side skill.

Afu is the proof that this works:

```text
30,000 files.
LINE query.
Correct file returned in about one second.
```

That is the foundation for Alfred's next stage.
