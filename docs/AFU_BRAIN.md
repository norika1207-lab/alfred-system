# Afu Brain

Afu Brain is the cognition layer.

Its job is not to sound smart. Its job is to make route, memory, safety, and
learning decisions inspectable.

## Responsibilities

- classify intent
- identify mode
- choose route
- decide risk
- choose capability
- enforce final-action boundaries
- decide what should be remembered
- update behavior from feedback

## Decision Contract

Every request should produce a structured `BrainDecision` before high-risk work
executes.

```text
allow    safe work can run
prepare  prepare output but do not commit final action
ask      human approval required
block    do not execute
```

## Why It Matters

Without Afu Brain, Alfred is a collection of tools. With Afu Brain, Alfred can
learn which prepared memories matter, which routes are cheap, which actions are
risky, and which user corrections should change future behavior.

