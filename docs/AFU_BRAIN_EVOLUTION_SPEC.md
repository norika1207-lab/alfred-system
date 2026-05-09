# Afu Brain Evolution Spec

Version: 0.1 draft  
Date: 2026-05-08  
Core line: Don't rent intelligence every time. Grow a brain that knows you.

## 0. Alfred System Alignment

The current integrated product hierarchy is:

```text
Alfred
  personal AI Agent system and user experience

Afu Brain
  Alfred's memory, cognition, routing, safety, and learning layer

Afu
  Alfred's office-grade text and LINE workflow pack

Parallel Claw
  Alfred's 20-agent parallel execution runtime
```

Publicly, Alfred should lead with the language people already understand:

```text
Alfred is a personal AI Agent system that runs 20 specialist agents in parallel
to finish complex tasks faster, safer, and across every interface you already
use.
```

Afu Brain is what makes that claim durable instead of a one-off demo. It turns
owner memory, context, risk, corrections, and repeated decisions into structured
parameters that affect future routing and execution.

The runtime order is:

```text
Alfred receives the request.
Afu Brain decides route, memory, risk, and approval boundary.
Afu handles office workflows when needed.
Parallel Claw runs specialist lanes for complex work.
MASL / Brain Gate blocks risky final actions.
Owner feedback updates Afu Brain.
```

This means Afu Brain must not be described as only a safety add-on. It is the
reason Alfred gets better with use.

## 1. Positioning

Afu Brain is a local personal cognition layer.

It is not a general assistant interface, and it must not be positioned as another mass-market conversation product. The market is already crowded with frontier systems optimized to answer broadly for everyone. Afu Brain chooses a different axis:

```text
Frontier models: one model for everyone.
Afu Brain: one growing brain for one person.
```

The product is a brain, not a wrapper.

Afu Brain learns how one person works, decides, hesitates, approves, rejects, revises, and uses tools. Its job is to turn repeated judgment into a local asset so the owner does not need to rent expensive cloud reasoning for every familiar situation.

## 2. Market Thesis

Large models face a structural scaling problem:

```text
more users -> more requests -> more tokens -> more compute -> more power -> more cost
```

Afu Brain follows a different cost curve:

```text
more use -> more local understanding -> less repeated cloud reasoning -> lower marginal cost per owner
```

The market opportunity is not general intelligence as a service. It is personal cognition infrastructure:

- local-first personal brains
- domain-specific professional brains
- OpenClaw execution brains
- memory-grounded decision brains
- shared cognition upgrades without private memory leakage

The owner should not need to re-explain the same preferences, risk boundaries, communication patterns, work habits, and safety rules to a remote model every day. High-frequency cognition should be distilled into the local brain.

## 3. Product Promise

Afu Brain solves five concrete problems.

1. Expensive repeated reasoning  
   Repeated decisions, preferences, and safety rules are learned locally instead of re-sent to frontier models every time.

2. Weak continuity  
   Most AI systems remember facts, but do not form stable judgment. Afu Brain turns memory into parameters that affect future decisions.

3. Shallow text understanding  
   Many agents process numbers and labels but do not understand premise, contradiction, responsibility, hidden motive, or the calculation behind an answer. Afu Brain explicitly trains semantic and philosophical interpretation.

4. Unsafe tool execution  
   OpenClaw gives agents hands. Afu Brain decides when those hands may act, when they must prepare only, when they must ask, and when they must stop.

5. Output without soul  
   Generic models can produce polished language without lived continuity. Afu Brain grows from correction, acceptance, rejection, hesitation, and accumulated personal context.

## 4. Canonical Architecture

```text
Human
  -> Afu Interface
  -> Personal Brain
  -> Decision Contract
  -> Local model / RAG / OpenClaw / frontier teacher / silence
  -> Final Gate
  -> Action or reply
  -> Human accept / reject / correction
  -> Distillation Loop
  -> Personal Brain checkpoint
```

### Afu Interface

Afu is the human-facing interface. It listens, asks, drafts, organizes context, and makes the second brain usable through natural interaction.

The interface is not the core product. It is the body language of the brain.

### Personal Brain

The Personal Brain is a local small language/cognition model plus structured parameters. It decides:

- what the owner is trying to do
- whether it already knows how to help
- what memory matters
- what tool can be used
- whether execution is safe
- whether a cloud model is needed
- what should be distilled after acceptance

### Frontier Teacher

Frontier models are not the product. They are teachers and external specialists.

They are called only when:

- the local brain lacks enough knowledge
- the task requires high reasoning capability
- the owner requests a high-quality draft
- the local brain needs teacher labels for distillation

Accepted outputs become training material for the local brain.

### OpenClaw

OpenClaw is the execution layer. Afu Brain controls it through explicit decision contracts.

### MASL

MASL is the safety entry point. It proves the brain can control action. It is not the final value proposition. The deeper value is cognition that compounds.

## 5. Flywheel

The system must improve because it is used.

```text
observe work
  -> infer pattern
  -> update cognitive parameters
  -> retrieve memory/RAG
  -> decide route
  -> act or speak
  -> receive accept/reject/correction
  -> distill repeated judgment
  -> reduce future cloud calls
```

The strongest product claim is compounding local cognition:

```text
Day 1: the brain needs help.
Day 7: the brain remembers corrections.
Day 30: the brain routes familiar work locally.
Day 100: the brain knows the owner deeply enough to prevent repeated mistakes.
```

## 6. Synapse Parameters

Afu Brain should grow parameters like synapses. A parameter is valid only if it:

1. has a clear definition
2. can be observed from behavior or text
3. changes future decisions
4. has an update rule
5. has decay or conflict handling
6. can be inspected

### Cognitive Parameters

- semantic_depth
- premise_tracking
- counterexample_pressure
- uncertainty_calibration
- causal_chain_integrity
- abstraction_level
- self_revision_pressure
- contradiction_tolerance

### Social Parameters

- uptake
- rejection_memory
- correction_absorption
- imitation_risk
- autonomy
- trust_delta
- disagreement_quality
- relationship_pressure

### Language Parameters

- template_similarity
- opening_reuse
- phrase_novelty
- owner_style_alignment
- persona_voice_consistency
- hidden_emotion_reading
- directness_preference

### Execution Parameters

- evidence_sufficiency
- risk_tier
- actionability
- approval_need
- rollback_need
- tool_readiness
- dry_run_required
- external_commitment_risk

### Learning Parameters

- mistake_memory
- transfer_learning
- consolidation_priority
- decay_pressure
- teacher_dependency
- local_confidence
- cloud_call_avoidance

## 7. Why Philosophy Exists

Philosophy training is not decoration.

It teaches the brain to understand text beyond surface tokens:

- What is the premise?
- What is the conclusion?
- What would falsify it?
- What responsibility follows from believing it?
- What contradiction is being hidden?
- What is the answer actually calculating?
- What emotional or social pressure is shaping the answer?

Without this layer, agents remain parameter machines: numbers move, but meaning is not understood.

The goal is not to make the brain sound philosophical. The goal is to make it interpret language, motive, and responsibility with increasing precision.

## 8. Local Small Model Strategy

The first serious model should not be a generic small talk model. It should be a local cognition model.

It should output structured decisions:

```json
{
  "can_handle_locally": true,
  "needs_frontier_teacher": false,
  "route": "local_brain_then_openclaw_prepare",
  "memory_retrieval_plan": ["owner_preference", "recent_correction", "tool_policy"],
  "risk": "medium",
  "decision": "prepare",
  "approval_required": true,
  "cognitive_updates": {
    "correction_absorption": 0.04,
    "tool_restraint": 0.03
  },
  "style_contract": {
    "tone": "direct",
    "avoid": ["repeated reassurance"],
    "must_include": ["specific uncertainty"]
  }
}
```

The local model's role:

- understand the owner
- route the task
- control tool execution
- decide when to call a frontier teacher
- produce prompt contracts
- judge the output
- update the brain

Qwen or another local language model can be used as a language organ, but the Personal Brain owns judgment.

## 9. Distillation Loop

Afu Brain does not blindly distill another model's voice. It distills decision traces.

Teacher models should label:

- intent
- risk
- can_execute
- can_handle_locally
- missing evidence
- memory to retrieve
- tool route
- approval boundary
- parameter update
- reason code

The owner response is the highest-value signal:

```text
accepted -> candidate for local distillation
rejected -> correction memory and negative sample
edited -> style and intent delta
ignored -> low salience or poor timing
blocked -> safety lesson
```

The core loop:

```text
local brain tries
  -> if uncertain, frontier teacher helps
  -> owner accepts/rejects
  -> accepted trace becomes training data
  -> repeated trace becomes local capability
  -> future cloud calls decrease
```

## 10. RAG Boundary

RAG is not raw memory dumping.

Private memory remains local. Shared cognition may be distributed as aggregate lessons:

```text
Private memory stays local.
Shared cognition improves globally.
```

Afu Brain RAG packs should contain:

- policy lessons
- safe/unsafe decision cases
- social cognition patterns
- evidence patterns
- reasoning seeds
- aggregate failure modes

They must not contain:

- raw private conversations
- private owner files
- credentials
- location history
- voice assets
- production database dumps

## 11. Network Effect

The network effect is not harvested private data. It is shared synapse upgrades.

Every local brain can learn privately. Aggregated, anonymized, policy-safe lessons can improve the shared brain:

```text
one brain learns locally
  -> safe aggregate lesson
  -> shared cognition feed
  -> many brains upgrade
  -> each brain remains private
```

If many brains connect to the shared feed, Afu Brain can become the world's largest cognition upgrade network without owning everyone's private memory.

## 12. Business Model

Possible product forms:

- Personal Brain subscription
- Professional Brain for creators, lawyers, traders, researchers, engineers
- OpenClaw execution brain
- Team Brain for departments
- Local appliance or mobile brain
- Managed brain care: backup, migration, upgrades, monitoring
- Shared cognition feed subscription
- Enterprise private deployment

The emotional promise:

```text
Buy a brain. I will care for it for life.
```

The economic promise:

```text
Use expensive frontier models only when needed.
Let the local brain handle what it has already learned.
```

## 13. Investor Narrative

Use this framing:

```text
We are not competing to build the biggest general model.
We are building the local brain layer for personal agents.
```

Key lines:

```text
Don't rent intelligence every time. Grow a brain that knows you.

Big models burn power to think again.
Afu Brain remembers how you think.

It does not need to know everything.
It only needs to know you.

Stop renting intelligence.
Own a brain that compounds.
```

## 14. Demo Requirements

The first investor-facing demo must show growth, not only capability.

Required scenes:

1. Repeated misunderstanding  
   The owner corrects the brain. The correction becomes a parameter.

2. Frontier teacher fallback  
   The local brain admits uncertainty, calls a stronger model, and stores the accepted trace.

3. OpenClaw control  
   The brain prepares safely but blocks external execution until approval.

4. Cost reduction  
   A repeated task no longer calls the frontier model after local distillation.

5. Soul / hidden reading  
   The brain notices hesitation, inconsistency, or hidden motive because prior personal patterns changed the interpretation.

6. Synapse visualization  
   The dashboard shows new parameters, strengthened parameters, decayed parameters, and decision traces.

## 15. Metrics

Track:

- frontier_model_calls_per_task
- local_resolution_rate
- accepted_local_decision_rate
- rejected_local_decision_rate
- correction_absorption_rate
- repeated_error_decay
- template_risk_decay
- approval_gate_precision
- tool_execution_block_success
- memory_retrieval_precision
- owner_edit_distance
- token_cost_per_successful_task
- parameter_growth_per_day
- synapse_stability

The core business metric:

```text
How much expensive repeated reasoning did the local brain eliminate?
```

The core human metric:

```text
Does the brain understand the owner better this week than last week?
```

## 16. Near-Term Build Plan

Phase 1: Spec and trace layer

- define decision contract
- define synapse parameters
- record local/frontier route decisions
- record accept/reject/correction signals
- show traces in dashboard

Phase 2: Local cognition model

- train first local decision model on teacher labels and owner feedback
- output structured JSON, not prose
- route Qwen/frontier/OpenClaw/silence

Phase 3: Distillation flywheel

- periodic accepted-trace distillation
- local benchmark before/after
- cost reduction report
- parameter growth dashboard

Phase 4: Shared cognition feed

- export only aggregate lessons
- publish RAG packs
- pin feed versions
- allow local-only mode

## 17. Non-Negotiables

- Do not position this as a mass-market conversation product.
- Do not leak private owner memory into public packs.
- Do not let a language model directly authorize tool execution.
- Do not train on bad template output as if it were good behavior.
- Do not make the brain dependent on one cloud model.
- Do not optimize only for fluent language.
- Optimize for judgment, continuity, safety, and compounding personal understanding.

## 18. Final Definition

Afu Brain is a local personal cognition asset.

It observes how one person thinks and works, builds synapse-like parameters, controls tools through judgment, learns from accepted answers, distills repeated reasoning into local capability, and becomes more useful every day.

It is not trying to answer the world.

It is trying to know one person deeply enough to become their second brain.
