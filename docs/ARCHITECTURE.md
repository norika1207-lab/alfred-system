# Architecture

Alfred is organized around prepared work memory.

```text
Channel input
  -> AlfredEvent
  -> Afu Brain decision
  -> Afu Skill Runtime or Parallel Claw
  -> MASL / Brain Gate
  -> response
  -> learning event
```

## Runtime Roles

### Alfred

Owns user identity and user experience across voice, Safari, Telegram, email, and
future channels.

### Afu Skill Runtime

Owns office and local-runtime capabilities:

- file-map
- local model reranking
- Drive and Mac file search
- Calendar and meeting context
- OCR/document extraction
- tracing and request queue

The important Afu lesson is that useful answers can be prepared before the
user asks.

### Afu Brain

Owns route and safety decisions:

- route to file memory
- route to office runtime
- route to foreground Parallel Claw
- ask before risky final actions
- update memory from feedback

### Parallel Claw

Runs two classes of work:

- background workers that prepare memory cheaply
- foreground specialist lanes for complex tasks

## Cost Curve

The system should prefer:

```text
prepared local memory -> local model -> cloud/frontier model
```

not:

```text
cloud/frontier model for every request
```

This is the architectural reason Alfred can feel fast and capable without
turning every request into an expensive token burn.

