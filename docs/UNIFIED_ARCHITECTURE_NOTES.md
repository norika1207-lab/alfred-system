# Alfred Unified Architecture

Version: 2026-05-09

Canonical companion README:

```text
ALFRED_SYSTEM_README.md
```

Read `ALFRED_SYSTEM_README.md` first when opening a new window. It contains the
updated product logic: Alfred uses Afu's local runtime and file-map machinery
plus Afu Brain routing and background workers to create LLM-like outcomes
without LLM-like foreground token cost.

Core line:

> Alfred is a personal AI Agent system that runs 20 specialist agents in parallel to finish complex tasks faster, safer, and across every interface you already use.

Product explanation:

> Alfred turns one request into a coordinated team of AI agents. It can research, compare, draft, verify, and prepare actions in parallel, then ask before anything risky is submitted, sent, paid, or published.

## 1. What This System Is

Alfred is the product.

It is not only a voice app, not only a chatbot, not only a dashboard, not only a safety library, and not only a multi-agent demo. Alfred is the user-facing personal AI Agent system that can work through voice, Safari, Telegram, email, and future channels.

The system has four major parts:

| Layer | Role | Product meaning |
|---|---|---|
| Alfred | Personal AI Agent system and user experience | The product people use |
| Afu Brain | Memory, cognition, safety, routing, learning | The brain that makes Alfred know the owner and decide safely |
| Afu | Office-grade agent runtime, local-model tier, and LINE/text workflow pack | The optimized work/execution substrate that fills Alfred's office and local-inference gap |
| Parallel Claw | 20-agent parallel execution runtime | The engine that splits one complex task into specialist lanes |

The correct relationship:

```text
User
  -> Alfred interface
       voice app
       Safari web
       LINE
       Telegram
  -> Afu Brain
       owner memory
       relationship graph
       mode/context
       intent/risk
       tool policy
       learning updates
  -> Capability router
       Alfred native skills
       Afu office skills
       Parallel Claw specialist lanes
       RAG/search/file vault
  -> MASL / Brain Gate
       allow
       prepare
       ask
       block
  -> Execution
  -> Result
  -> Feedback and memory update
```

## 2. External Positioning

Do not lead with "proactive butler" in public technical positioning. That sentence is true internally, but too abstract for people who do not already know the system.

Lead with language people understand:

- AI Agent
- 20 specialist agents
- parallel execution
- faster completion
- safer final actions
- App, Safari, LINE, Telegram

Primary public copy:

```text
Alfred is a personal AI Agent system that runs 20 specialist agents in parallel to finish complex tasks faster, safer, and across every interface you already use.
```

Secondary public copy:

```text
Alfred turns one request into a coordinated team of AI agents. It can research, compare, draft, verify, and prepare actions in parallel, then ask before anything risky is submitted, sent, paid, or published.
```

Internal product truth:

```text
Alfred is still a zero-interface, voice-first, proactive personal butler.
The outside pitch starts from AI Agent and parallel work because that is easier to understand.
```

## 3. Alfred Responsibilities

Alfred owns the user experience and identity.

Current Alfred source of truth:

- iOS app: `/Users/norikaoda/Dropbox/Alfred/Alfred/`
- backend: `/opt/alfred/backend/main.py`
- service: `systemctl restart alfred`
- server: `https://alfred.31.97.221.240.nip.io`
- shared DB: `/opt/alfred/data/alfred.db`
- per-user DB: `/opt/alfred/data/users/<user_id>.db`

Alfred already has:

- voice-first iOS interface
- Safari/web-capable backend surface
- LINE integration
- Telegram integration
- Gemini chat/tool reasoning
- ElevenLabs cloned Alfred voice
- Whisper STT
- passive ambient recording
- location context
- family/location features
- HealthKit sync
- Google Calendar
- Google Drive
- Mac file index
- document/photo analysis
- long response distribution to LINE, Telegram, and Gmail
- per-user DB memory boundary

Alfred must remain the top-level product, not be reduced to a UI shell.

## 4. Afu Brain Responsibilities

Afu Brain is Alfred's cognition, memory, routing, and safety layer.

It decides:

- what the user is asking for
- which owner memory matters
- whether the request is personal, office, family, travel, file, research, or execution-oriented
- whether Afu office tools are needed
- whether Parallel Claw should run
- whether a local/RAG/frontier path is enough
- whether the task can execute, should prepare only, must ask, or must block
- what should be learned after the outcome

Afu Brain must produce structured decisions, not just text:

```json
{
  "owner_id": "string",
  "request_id": "string",
  "intent": "calendar | file_search | research | message | purchase | code_review | personal_followup | other",
  "mode": "home | office | travel | family | silent | unknown",
  "risk": "low | medium | high | irreversible",
  "route": "alfred_native | afu_office | parallel_claw | rag_only | ask_owner | block",
  "decision": "allow | prepare | ask | block",
  "approval_required": true,
  "memory_refs": [],
  "capabilities": [],
  "blocked_final_action": "send | pay | publish | submit | merge | delete | trade | none",
  "reason": "short inspectable reason",
  "learning_update": {}
}
```

Afu Brain is also responsible for the long-term value claim:

```text
The more Alfred works with one person, the more repeated judgment becomes local memory, routing, and decision parameters.
```

## 5. Afu Responsibilities

Afu is not a rival product to Alfred.

Afu is Alfred's office-grade agent runtime and local-inference substrate. It
fills the cases where Alfred's original voice-first design is not enough, but it
also brings a highly optimized execution stack that Alfred should reuse instead
of rebuilding.

- the user cannot speak
- the task is text-heavy
- the task is office/work related
- the task requires LINE-first workflows
- the task uses Google Calendar, Drive, meeting, email, OCR, web search, or workplace memory
- the task should run through an optimized local model path instead of a cloud model
- the task benefits from Afu's request queue, tracing, provider chain, and file-map workers

Afu capabilities should be exposed to Alfred as registered tools:

```text
afu.calendar.list
afu.calendar.create
afu.calendar.update
afu.drive.search
afu.drive.summarize
afu.drive.create
afu.meeting.transcribe
afu.meeting.summarize
afu.email.draft
afu.web.search
afu.office.daily_brief
afu.office.followup
afu.memory.lookup
afu.memory.write
```

Afu has strong engineering primitives that Alfred should reuse:

- channel-agnostic adapter thinking
- request queue
- per-user/session flow
- Google OAuth
- Drive/Calendar/Meeting/Voice modules
- tracing with `requestGroupId`
- quota and user gate
- admin/security design
- home/enterprise deployment tiers
- local vLLM provider chain
- provider failover and circuit-breaker behavior
- GX10 file-map runtime and summary backfill
- Drive materialization and file extraction workers
- pyannote/Whisper voice processing pipeline
- synthetic eval endpoint with auth-token gating

Afu should become `Alfred Office / Local Runtime Mode`, not a disconnected
product.

### Afu Local Model And Enterprise Runtime

Afu is already designed with two deployment tiers:

| Tier | Purpose | Default model path |
|---|---|---|
| home | Mac mini, low-cost household or small deployment | cloud provider chain |
| enterprise | NVIDIA/GX10-class host, privacy and throughput | local vLLM first |

The enterprise tier uses:

```text
LLM_PROVIDER=vllm
VLLM_BASE_URL=http://host.docker.internal:8000
provider chain: vLLM -> copilot -> anthropic
current production local model: qwen3.6-35b-a3b
```

Afu's vLLM scripts document Qwen 3.6 35B-A3B FP8 as the current production
path, with roughly 3B active parameters and much higher decode throughput than
the older dense route. This matters to Alfred because it gives Alfred a path to:

- answer familiar office tasks locally
- reduce repeated cloud calls
- keep sensitive office/file context on local hardware
- serve multiple users with better throughput
- use cloud/frontier models only when the local route is not enough

Afu also has a GX10 file-map and summary runtime:

```text
Drive file materialization
text extraction
algorithmic digest
summary backfill
local smart-search through vLLM
file-map.sqlite
```

This means Afu is not merely a LINE command surface. In the unified Alfred
system, Afu contributes the serious local execution and retrieval backbone.

The corrected integration sentence:

```text
Alfred owns the user experience.
Afu Brain decides memory, risk, route, and learning.
Afu supplies optimized office workflows and local-model runtime.
Parallel Claw supplies 20-agent parallel execution for complex tasks.
```

## 6. Parallel Claw Responsibilities

Parallel Claw is Alfred's high-complexity execution accelerator.

It should run when one request benefits from multiple specialist perspectives:

- research
- market comparison
- contract/document review
- code review
- shopping comparison
- strategy decision
- launch planning
- trade/order preparation
- high-stakes writing or publishing

Parallel Claw does not replace Alfred. Alfred calls it.

Parallel Claw input:

```json
{
  "request_id": "string",
  "owner_id": "string",
  "task": "string",
  "context": {},
  "risk_boundary": {
    "blocked_final_actions": ["send", "pay", "publish", "submit", "merge", "delete", "trade"]
  },
  "lanes": [
    "research",
    "risk",
    "cost",
    "legal",
    "security",
    "evidence",
    "dissent"
  ]
}
```

Parallel Claw output:

```json
{
  "request_id": "string",
  "status": "completed | needs_approval | blocked | failed_with_trace",
  "lane_results": [],
  "dissent": [],
  "synthesis": "string",
  "prepared_actions": [],
  "blocked_final_action": "string",
  "approval_prompt": "string",
  "audit": {}
}
```

The system promise is not "agents can magically do everything." The promise is:

```text
Every run ends in a clear state: completed, needs approval, blocked, or failed with trace.
```

## 7. Shared Event Schema

Every channel should be normalized before it reaches Afu Brain.

```json
{
  "event_version": 1,
  "request_id": "uuid",
  "owner_id": "string",
  "channel": "ios_voice | safari | line | telegram | afu_line | api",
  "input_type": "speech | text | image | file | location | ambient",
  "text": "string",
  "attachments": [],
  "timestamp": "ISO_TIME",
  "context": {
    "mode": "home | office | travel | family | silent | unknown",
    "location_label": "home | office | transit | overseas | unknown",
    "device_id": "string",
    "conversation_id": "string"
  },
  "auth": {
    "authenticated": true,
    "source": "device | line | telegram | web | admin"
  }
}
```

Channel-specific code should end at this schema boundary.

## 8. Unified Identity

The first real integration task is identity mapping.

Alfred needs one owner identity across:

- iOS `device_id`
- Alfred `user_id`
- LINE user id
- Telegram chat id
- Google OAuth account
- Afu office user id
- per-user DB path
- Afu Brain memory namespace

Suggested table:

```sql
CREATE TABLE IF NOT EXISTS alfred_identity_links (
  owner_id TEXT NOT NULL,
  provider TEXT NOT NULL,
  provider_user_id TEXT NOT NULL,
  display_label TEXT,
  verified_at TEXT,
  last_seen_at TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  PRIMARY KEY (provider, provider_user_id)
);
```

Suggested owner profile table:

```sql
CREATE TABLE IF NOT EXISTS alfred_owner_profiles (
  owner_id TEXT PRIMARY KEY,
  primary_name TEXT,
  timezone TEXT,
  default_language TEXT,
  active_mode TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP,
  updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
  memory_json TEXT NOT NULL DEFAULT '{}',
  preferences_json TEXT NOT NULL DEFAULT '{}',
  safety_json TEXT NOT NULL DEFAULT '{}'
);
```

## 9. Memory And Learning Contract

Memory must be separated into private memory and shared cognition.

Private memory:

- owner relationship graph
- family data
- files
- location
- personal preferences
- health and schedule
- private corrections

Shared cognition:

- public RAG packs
- safe execution policies
- task routing lessons
- anti-template patterns
- decision benchmarks
- tool boundary lessons

Afu Brain can subscribe to shared cognition while keeping private memory local.

Every completed task should write an inspectable learning event:

```json
{
  "request_id": "string",
  "owner_id": "string",
  "source": "alfred | afu | parallel_claw | owner_feedback",
  "event_type": "accepted | rejected | corrected | completed | abandoned | blocked",
  "summary": "string",
  "memory_delta": {},
  "routing_delta": {},
  "safety_delta": {},
  "created_at": "ISO_TIME"
}
```

## 10. Integration Roadmap

### Phase 1: Unify Architecture And Naming

- Treat Alfred as the main product.
- Treat Afu Brain as Alfred's cognition layer.
- Treat Afu as Alfred Office Mode.
- Treat Parallel Claw as Alfred's 20-agent execution runtime.
- Avoid public dependence on the OpenClaw name where it can be confused with another project.

### Phase 2: Identity And Channel Router

- Create `alfred_identity_links`.
- Normalize iOS voice, Safari, Telegram, email, and Afu LINE into `AlfredEvent`.
- Map every incoming request to one `owner_id`.

### Phase 3: Afu Brain Decision API

- Add a local/internal endpoint or module:

```text
POST /internal/afu/decide
```

Input: `AlfredEvent`.

Output: `BrainDecision`.

The existing Alfred backend should call this before tool execution.

### Phase 4: Afu As Capability Pack

- Wrap Afu tools behind an internal capability bridge.
- Route office tasks from Alfred to Afu capability names.
- Return all Afu results through Alfred's response system.

### Phase 5: Parallel Claw Complex Task Runtime

- Add `parallel_claw.run_task`.
- Only invoke for complex tasks or when Afu Brain routes there.
- Keep final actions approval-gated.

### Phase 6: Feedback And Learning Loop

- After every result, write an `alfred_learning_events` record.
- Let Afu Brain update local memory/routing/safety parameters.
- Keep private memory out of public RAG packs.

### Phase 7: Product Surface

- Update public pages to sell Alfred first:

```text
Alfred: 20 AI Agents working for you at once.
```

- Use Parallel Claw as the technical proof.
- Use Afu Brain as the trust and memory proof.
- Use Afu as the office workflow proof.

## 11. Implementation Guardrails

- Do not split Alfred, Afu, Afu Brain, and Parallel Claw into competing product stories.
- Do not make users understand internal module names before they see value.
- Do not let any channel bypass Afu Brain for high-risk tool actions.
- Do not let Parallel Claw submit/pay/publish/send/merge/delete/trade without explicit approval.
- Do not store private owner memory in public shared RAG packs.
- Do not make dashboards the primary product. Dashboards are evidence, not the main user experience.
- Do not describe Alfred as only a butler in the public headline. Use AI Agent, parallel execution, and multi-interface first.

## 12. Final System View

The integrated product:

```text
Alfred
  A personal AI Agent system
  available by voice, Safari, LINE, and Telegram
  powered by Afu Brain memory and decision routing
  extended by Afu office workflows
  accelerated by Parallel Claw's 20 specialist agents
  protected by MASL approval gates
  improved by owner feedback over time
```

This combined system is much more valuable than any isolated part:

- Alfred gives the product a human-facing reason to exist.
- Afu Brain gives it memory, judgment, and compounding learning.
- Afu gives it real office workflow depth.
- Parallel Claw gives it a concrete speed and capability claim.
- MASL gives it trust.

Together, the claim becomes:

```text
One request. Twenty coordinated agents. Same Alfred everywhere. Safer final actions. Better memory every time.
```
