# Open Source Boundary

This repository is a clean public reference package. It is meant to explain and
demonstrate Alfred's architecture without exposing private production systems.

## Included

- public architecture docs
- public JSON schemas
- installable Python reference package
- deterministic Afu Brain style routing example
- SQLite file-memory reference implementation
- background worker and Parallel Claw execution contracts
- a runnable local demo

## Excluded

- private Alfred iOS project files
- production Alfred backend files
- production Afu deployment secrets
- LINE, Telegram, Google, ElevenLabs, or cloud API tokens
- private databases
- private user files
- VPS configuration
- production logs
- user identity mappings

## Release Rule

The open-source package must be able to run locally with fake sample data.

It must not require access to:

- the production Alfred server
- the production Afu server
- any private Google Drive
- any private user database
- any private LINE or Telegram channel

## Why This Boundary Matters

Alfred's commercial value depends on trust. The public repository should prove
the architecture while keeping private user memory private.

The public release can show the system shape:

```text
channels -> AlfredEvent -> Afu Brain -> Afu file memory -> Parallel Claw -> gate
```

The private production system can keep the real integrations and real user data
behind deployment boundaries.

## Safe Public Claims

Use these claims when presenting the repository:

- Alfred works before you ask.
- Alfred prepares private work memory in the background.
- Alfred uses local file maps and concurrent workers to reduce foreground token
  burn.
- Alfred can coordinate specialist agents, but approval is required before risky
  final actions.
- The public repository is a reference implementation, not a dump of production
  user data.

## Claims To Avoid

Do not claim the open-source package includes:

- production credentials
- all private Alfred features
- all private Afu deployment code
- guaranteed 100 percent success for every task
- automatic execution of payments, trades, sends, publishes, or deletes without
  approval

## Original File Protection

For development and release work, use this folder:

```text
alfred-system-release/
```

Do not patch these sources during public package preparation:

```text
/Users/norikaoda/Dropbox/Alfred/Alfred/
/opt/alfred/
/opt/Afu/
sportverse production services
```

