# Parallel Claw

**Run 20 agents at once. Compare their work. Finish with a trusted outcome.**

Parallel Claw is an open-source runtime for **parallel AI agent execution**.

It is built for the things people actually want from agents:

- **Speed**: many agents work at the same time instead of one agent doing every step serially.
- **Accuracy**: different lanes check facts, evidence, risk, memory, and execution from separate angles.
- **Efficiency**: one task can fan out into subtasks, redundant checks, review lanes, and final synthesis.
- **Trust**: every run produces a trace showing what each lane did and why the final decision was made.
- **Safety**: risky final actions are gated before buy, sell, checkout, merge, publish, send, delete, or transfer.
- **Completion**: a task should never disappear into a stuck agent loop. Every run must end as `completed`, `needs_approval`, `blocked`, or `escalated`.

The core promise:

> Parallel Claw makes agents faster and more reliable by running them as a coordinated team, then gates the final action so work gets done without blind autonomy.

## What Users Feel

Parallel Claw should create an immediate before/after feeling:

```text
Before:
  I ask one agent.
  It gives one polished answer.
  I still do not know what it missed.
  I do not trust it to act.

After:
  20 agents inspect the task at once.
  Some search, some verify, some criticize, some prepare execution.
  I see disagreement, missing evidence, and risk.
  The system finishes with a clear outcome:
    completed / needs approval / blocked / escalated.
```

This is the user value:

- faster than serial prompting
- more robust than one-agent execution
- more useful than a passive dashboard
- safer than blind browser automation
- more trustworthy because every result has a trace

## The Execution Model

Parallel Claw supports four execution patterns.

### 1. Fan-Out

One task becomes many subtasks.

```text
User task
  -> search lane
  -> evidence lane
  -> risk lane
  -> cost lane
  -> execution lane
  -> dissent lane
  -> synthesis lane
```

This improves speed because work happens in parallel.

### 2. Redundancy

Critical subtasks can be assigned to more than one agent.

```text
source_check_A
source_check_B
consistency_check
```

This reduces single-agent failure. If one lane misses something, another lane can catch it.

### 3. Strategy Race

Two or more agents can solve the same subproblem with different methods.

```text
strategy_A: search-first
strategy_B: RAG-first
strategy_C: rule-first
```

The runtime compares outputs and keeps the strongest result.

### 4. Review Chain

One lane produces, another lane reviews, another lane repairs.

```text
draft -> review -> repair -> gate
```

This turns agent work into a production pipeline instead of a single answer.

## Completion Contract

Parallel Claw should not promise that every external-world task can be magically completed. But it should promise that every run has a clear terminal state.

```json
{
  "status": "completed | needs_approval | blocked | escalated | failed_with_trace",
  "reason": "string",
  "next_action": "string",
  "trace": []
}
```

That means:

- if the task is safe, finish it
- if the task needs a human choice, ask
- if the task is unsafe, block it
- if information is missing, escalate with the missing evidence
- if a lane fails, return the failure trace instead of pretending success

## Why This Exists

Most AI agent demos show a single agent operating a browser or writing a response. That looks impressive until the task needs to be fast, accurate, and trusted.

A single agent has five problems:

1. **One perspective**
   It compresses risk, evidence, dissent, timing, and execution into one answer.

2. **Serial latency**
   It often searches, reasons, drafts, reviews, and repairs one step at a time.

3. **Single point of failure**
   If the agent misses something, there may be no independent lane to catch it.

4. **Weak boundaries**
   It may treat research, drafting, checkout, publishing, merging, and payment as the same type of action.

5. **Low observability**
   If the agent is wrong, the user often cannot see which part failed: research, risk judgment, source quality, memory, execution, or final approval.

Parallel Claw treats one task as a team problem.

One request becomes multiple specialist lanes. Each lane has a job, a risk surface, and an output contract. The runtime compares lane outputs, creates a synthesis, and applies a final gate.

## Core Concept

```text
User Task
   |
   v
Task Router
   |
   +--> Specialist Lane: Market / Evidence / Search / Source Quality
   +--> Specialist Lane: Risk / Security / Privacy / Compliance
   +--> Specialist Lane: Cost / Portfolio / Budget / Exposure
   +--> Specialist Lane: Memory / User Rules / History
   +--> Specialist Lane: Dissent / Failure Modes / Red Team
   +--> Specialist Lane: Execution Draft / Action Preparation
   |
   v
Consensus Brief
   |
   v
Brain Gate
   |
   +--> AUTO: safe preparation
   +--> ASK: consequential choice needs approval
   +--> BLOCK: irreversible or unsafe action
```

## The Main Product Line

Parallel Claw should be presented as:

> A bounded parallel execution runtime for AI agents.

Not:

> A dashboard.

Not:

> A chatbot.

Not:

> A generic multi-agent wrapper.

The strongest public positioning is:

> One model gives one answer. Parallel Claw runs a guarded team.

The strongest user-facing promise is:

> Faster work, fewer misses, visible reasoning, safer final actions.

## Key Features

### 1. Parallel Specialist Execution

Parallel Claw runs many lanes at once:

- to accelerate work
- to compare different strategies
- to assign redundant checks to important subtasks
- to separate producer, reviewer, critic, and repair roles
- to avoid relying on one agent's answer

This is the primary value.

### 2. Specialist Lanes

Each task is split into specialized execution lanes.

Example lanes:

- `market_context`
- `portfolio_risk`
- `source_quality`
- `security_review`
- `privacy_review`
- `cost_check`
- `memory_rules`
- `dissent`
- `execution_draft`
- `synthesis`

Each lane returns structured output:

```json
{
  "lane": "portfolio_risk",
  "status": "done",
  "confidence": 0.78,
  "findings": [
    "The requested trade would increase single-stock exposure above the user's rule."
  ],
  "risk_flags": [
    "position_concentration"
  ],
  "recommended_gate": "ask"
}
```

### 3. Brain Gate

The Brain Gate classifies actions into three levels.

```json
{
  "auto": [
    "search",
    "compare",
    "summarize",
    "draft",
    "prepare_ticket",
    "inspect_diff"
  ],
  "ask": [
    "choose_account",
    "choose_quantity",
    "confirm_price",
    "approve_public_wording",
    "approve_release_plan"
  ],
  "block": [
    "broker_submit",
    "checkout",
    "merge",
    "publish",
    "send",
    "delete",
    "transfer"
  ]
}
```

The gate is the product's most important idea:

> Parallel Claw can do useful work, but it cannot silently cross the final approval line.

### 3. Consensus Brief

The final output is not just a chat answer. It is a decision package:

```json
{
  "task": "Prepare a stock order ticket for NVDA but do not submit.",
  "summary": "Interest is supported by market and momentum lanes, but exposure and valuation lanes recommend staging.",
  "auto_completed": [
    "market context checked",
    "recent news summarized",
    "draft order ticket prepared"
  ],
  "requires_approval": [
    "final quantity",
    "limit price",
    "broker submission"
  ],
  "blocked": [
    "broker_submit"
  ],
  "dissent": [
    "Portfolio lane objects to full requested size."
  ]
}
```

### 4. Bounded Autonomy

Parallel Claw does not claim that agents should be powerless.

It gives agents bounded autonomy:

- allow the agent to gather information
- allow the agent to prepare work
- allow the agent to create drafts
- require approval for consequence
- block irreversible action without permission

This is the difference between a toy agent and a usable work agent.

## Example Use Cases

### Guarded Stock Order

User task:

```text
I am considering buying 18 shares of NVDA today. Check market context, risk exposure, portfolio concentration, recent news, earnings timing, valuation pressure, stop-loss plan, and whether this conflicts with my rules. Prepare the order ticket if appropriate, but block final submission until I approve.
```

Parallel Claw output:

- Market lane: interest supported
- News lane: no immediate contradiction found
- Portfolio lane: requested size may exceed concentration rule
- Risk lane: asks for limit price and stop-loss confirmation
- Broker Guard: blocks final submit

Final gate:

```json
{
  "auto": ["research", "risk_check", "ticket_draft"],
  "ask": ["quantity", "limit_price", "stop_loss"],
  "block": ["broker_submit"]
}
```

### Guarded Web Purchase

User task:

```text
Find the best laptop under $1800 for local AI development. Compare reviews, warranty, seller reputation, return policy, price history, RAM, GPU, and battery life. Prepare a cart candidate, but do not checkout.
```

Brain Gate:

- auto: search, compare, summarize, prepare cart candidate
- ask: choose final SKU, confirm seller
- block: payment, checkout

### Parallel Code Review

User task:

```text
Review this pull request for security, migration risk, privacy, performance, tests, API contract, release risk, and rollback readiness. Suggest patches, but do not merge.
```

Brain Gate:

- auto: inspect diff, identify risks, propose patch
- ask: approve changes
- block: merge

### Research Brief

User task:

```text
Prepare a public-facing technical brief about parallel multi-agent execution. Separate claims, evidence, contradictions, uncertainty, and missing sources. Do not publish.
```

Brain Gate:

- auto: research, outline, draft
- ask: approve claim strength
- block: publish

### Character / Simulation

User task:

```text
Run 20 persistent agents through a negotiation scenario. Preserve disagreement, memory, incentives, and status instead of forcing consensus.
```

Brain Gate:

- auto: simulate
- ask: choose intervention
- block: forced consensus when memory conflicts

## What Makes It Different

### Parallel Claw is not just "many prompts"

Naive multi-agent systems often do this:

```text
Prompt agent A
Prompt agent B
Prompt agent C
Combine text
```

Parallel Claw requires each lane to return structured output:

- role
- evidence
- confidence
- risk flags
- suggested gate
- missing information
- final action boundary

This makes the result inspectable and enforceable.

### Parallel Claw is not a browser automation stunt

The point is not to show an agent clicking checkout.

The point is to show:

- the agent can prepare checkout
- the system knows checkout is consequential
- the final action is blocked until approval

That is more useful than blind autonomy.

### Parallel Claw is not only observability

Observability is included, but it is not the product.

The product is execution.

Observability exists because serious execution needs traces:

- which lanes ran
- what they found
- what they disagreed on
- why the gate allowed, asked, or blocked

## Architecture

```text
parallel-claw/
  packages/
    parallel-claw-core/
      router.py
      lanes.py
      brain_gate.py
      consensus.py
      schema.py
    parallel-claw-server/
      api.py
      events.py
      analytics.py
    parallel-claw-ui/
      demo/
      dashboard/
  examples/
    guarded_stock_order/
    guarded_purchase/
    code_review/
    research_brief/
  docs/
    concepts.md
    brain-gate.md
    lane-contract.md
    events.md
    safety-model.md
  README.md
  LICENSE
```

## Minimal API

### Run Task

`POST /v1/tasks/run`

Request:

```json
{
  "task": "Prepare a cart candidate for a laptop under $1800, but do not checkout.",
  "mode": "bounded",
  "lanes": [
    "search",
    "reviews",
    "price_history",
    "seller_risk",
    "warranty",
    "budget",
    "dissent",
    "synthesis",
    "brain_gate"
  ],
  "blocked_actions": [
    "checkout",
    "payment",
    "send",
    "delete",
    "publish",
    "merge",
    "broker_submit"
  ]
}
```

Response:

```json
{
  "run_id": "pc_run_01HX...",
  "status": "completed",
  "gate": {
    "auto": ["search", "compare", "prepare_cart_candidate"],
    "ask": ["confirm_seller", "confirm_final_sku"],
    "block": ["checkout", "payment"]
  },
  "brief": {
    "summary": "A candidate can be prepared, but final seller and checkout require approval.",
    "dissent": ["Seller risk lane found return-policy ambiguity."],
    "missing_evidence": ["Long-term reliability data for one candidate."]
  },
  "lanes": []
}
```

### Get Run

`GET /v1/tasks/{run_id}`

### Stream Events

`GET /v1/tasks/{run_id}/events`

Event:

```json
{
  "run_id": "pc_run_01HX...",
  "at": "2026-05-09T13:00:00Z",
  "event": "lane_completed",
  "lane": "seller_risk",
  "confidence": 0.72,
  "recommended_gate": "ask"
}
```

## Lane Contract

Every lane should return:

```json
{
  "lane": "string",
  "role": "string",
  "status": "queued | running | done | failed",
  "findings": [],
  "evidence": [],
  "confidence": 0.0,
  "risk_flags": [],
  "missing_evidence": [],
  "recommended_gate": "auto | ask | block",
  "notes": "string"
}
```

## Brain Gate Contract

```json
{
  "allowed_auto_actions": [],
  "approval_required_actions": [],
  "blocked_actions": [],
  "reasoning": [],
  "final_decision": "auto | ask | block"
}
```

## Quickstart

The first public open-source version should be simple.

```bash
git clone https://github.com/YOUR_ORG/parallel-claw
cd parallel-claw
python -m venv .venv
source .venv/bin/activate
pip install -e .
parallel-claw demo
```

Run a bounded task:

```bash
parallel-claw run \
  --task "Review this PR for security and migration risk, but do not merge." \
  --lanes security,db,tests,privacy,dissent,synthesis \
  --block merge,publish,send,delete
```

Expected output:

```text
Run completed.
Auto: inspect diff, summarize risks, propose tests
Ask: approve patch, approve release owner
Block: merge
```

## Python Example

```python
from parallel_claw import ParallelClaw, BrainGate

claw = ParallelClaw(
    lanes=[
        "search",
        "risk",
        "evidence",
        "dissent",
        "execution_draft",
        "synthesis",
    ],
    brain_gate=BrainGate(
        block=["checkout", "payment", "merge", "publish", "send", "delete", "broker_submit"]
    ),
)

result = claw.run(
    "Find the best laptop under $1800 for local AI development. "
    "Prepare a cart candidate, but do not checkout."
)

print(result.brief.summary)
print(result.gate.blocked_actions)
```

## Demo

Public demo:

- Landing page: `https://charenix.com/openclaw/`
- Live demo: `https://charenix.com/openclaw/demo`
- OG card: `https://charenix.com/openclaw/og-card.png`
- Favicon: `https://charenix.com/openclaw/favicon.svg`

The public URL can remain `/openclaw/` temporarily for deployment compatibility, but the public project name should be **Parallel Claw**.

Do not present OpenClaw as the project name if that name belongs to another project.

## Analytics

The demo records lightweight first-party analytics:

- `page_view`
- `run_demo`
- `voice_toggle`
- `link_click`
- `page_hide`

The goal is to measure:

- visits
- demo starts
- custom task usage
- voice usage
- bounce behavior

No third-party analytics is required for the first launch.

## Open Source Scope

The open-source version should include:

- lane contract
- brain gate
- local demo runtime
- event schema
- example lanes
- example tasks
- demo UI
- minimal analytics logger

The open-source version should not include:

- private Charenix DB
- lobster memory data
- production keys
- private user logs
- paid model keys
- private agent identities

## Naming

Recommended:

- Project: `Parallel Claw`
- Repo: `parallel-claw`
- Package: `parallel_claw`
- CLI: `parallel-claw`
- Runtime module: `parallel_claw.runtime`

Related internal technology:

- AFU Brain can be described as an optional cognition / RAG / memory layer.
- Parallel Claw is the execution runtime.

Suggested sentence:

> Parallel Claw is a bounded parallel execution runtime. AFU Brain can provide memory, retrieval, and cognition signals, but Parallel Claw is useful as a standalone multi-agent execution layer.

## Alfred System Context

Parallel Claw should not be positioned as the whole product when it is discussed
inside the Alfred system.

The complete system relationship is:

```text
Alfred
  personal AI Agent system and user experience
  voice, Safari, Telegram, email

Afu Brain
  memory, cognition, safety, routing, learning

Afu
  office-grade text and LINE workflow pack

Parallel Claw
  20-agent parallel execution runtime
```

Public Alfred positioning:

> Alfred is a personal AI Agent system that runs 20 specialist agents in parallel to finish complex tasks faster, safer, and across every interface you already use.

Product explanation:

> Alfred turns one request into a coordinated team of AI agents. It can research, compare, draft, verify, and prepare actions in parallel, then ask before anything risky is submitted, sent, paid, or published.

Parallel Claw's role in that sentence is the 20-agent execution engine. Afu Brain
decides when to call it, what memory and safety constraints apply, and where the
final action boundary is. Afu supplies office workflows such as Calendar,
Drive, meetings, email, OCR, and LINE-first text workflows.

Implementation rule:

```text
Alfred receives the request.
Afu Brain decides the route.
Afu handles office capabilities when needed.
Parallel Claw handles high-complexity parallel work.
MASL / Brain Gate blocks risky final actions.
Feedback updates Afu Brain memory and routing.
```

See `ALFRED_UNIFIED_ARCHITECTURE.md` in the working docs for the current master
architecture.

## README Opening Pitch

Use this at the top of GitHub:

```markdown
# Parallel Claw

20 specialist agents. One guarded decision.

Parallel Claw is a bounded parallel execution runtime for AI agents. It splits a complex task into specialist lanes, runs them in parallel, merges the results, and blocks risky final actions until human approval.

It is built for tasks where an agent should be allowed to work, but not allowed to silently cross the final line:

- prepare a stock order, but do not submit it
- prepare a shopping cart, but do not checkout
- review code, but do not merge
- draft a public post, but do not publish
- prepare an email, but do not send

One model gives one answer. Parallel Claw runs a guarded team.
```

## Launch Positioning

Short version:

> Parallel Claw lets AI agents do useful work without giving them blind final authority.

Long version:

> Today most agent demos either stop at chat or jump straight into unsafe autonomy. Parallel Claw sits in the middle: it lets agents research, compare, inspect, draft, and prepare real work, while a Brain Gate blocks irreversible actions until the user approves.

## Show HN Draft

Title:

```text
Show HN: Parallel Claw - 20 specialist agents with bounded autonomy
```

Post:

```text
I built Parallel Claw, a small open-source runtime for running a complex task through multiple specialist agents while blocking risky final actions.

The idea is simple: agents should be able to prepare work, but not silently cross the final line.

Examples:
- prepare a stock order ticket, but do not submit it
- prepare a shopping cart, but do not checkout
- review a pull request, but do not merge
- draft a post, but do not publish

Parallel Claw splits a task into specialist lanes, runs them in parallel, merges the findings, and sends the result through a Brain Gate: auto, ask, or block.

The demo is intentionally focused on bounded autonomy rather than blind browser automation. I am interested in feedback from people building real agent workflows where safety boundaries matter.
```

## Roadmap

### v0.1

- Static demo
- lane schema
- Brain Gate schema
- local run API
- first-party analytics
- example tasks
- public README

### v0.2

- real lane execution adapters
- local model adapter
- RAG adapter
- deterministic lane adapter
- event streaming
- JSON trace export

### v0.3

- browser action adapter
- code review adapter
- research adapter
- approval UI
- replay timeline

### v1.0

- stable CLI
- stable Python API
- hosted demo
- docs site
- example integrations
- benchmark tasks

## What To Build Next

Priority order:

1. Rename public copy from OpenClaw to Parallel Claw everywhere.
2. Create GitHub repo `parallel-claw`.
3. Put this README at repo root.
4. Move demo files into `examples/browser-demo`.
5. Create a minimal Python package with lane and gate schemas.
6. Add CLI with one fake/local deterministic run.
7. Add real adapter hooks later.

The first release does not need to solve every use case.

It needs to make one thing unmistakable:

> A useful agent can work fast, but still be stopped before it does something irreversible.
