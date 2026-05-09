# Security And Privacy

This release is a public reference architecture. It must not include private
production data.

## Never Commit

- `.env`
- LINE tokens
- Telegram tokens
- Google OAuth tokens
- private keys
- user DBs
- file-map DBs from real users
- private Drive metadata
- private logs
- raw files

## Private vs Shared Data

Private memory:

- owner files
- calendars
- location
- family data
- messages
- user corrections
- private summaries

Shared cognition:

- public schemas
- safety policies
- worker contracts
- synthetic examples
- redacted patterns

## Final Action Boundaries

The reference system gates actions such as:

- send
- pay
- publish
- submit
- merge
- delete
- trade
- transfer

Preparation is useful. Silent irreversible action is not allowed.

