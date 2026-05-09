# Release Checklist

Use this before publishing the repository.

## Source Boundary

- [ ] Confirm all release files live under `alfred-system-release/`.
- [ ] Confirm no production Alfred, Afu, LINE, Telegram, Google, ElevenLabs, or
  VPS source file was modified.
- [ ] Confirm no private database is copied into the repository.
- [ ] Confirm no private user file is copied into the repository.

## Local Verification

Run from inside the release folder:

```bash
python3 -m compileall src examples
PYTHONPATH=src python3 examples/demo.py
bash scripts/scan_secrets.sh .
```

Expected result:

- Python compiles without syntax errors.
- Demo returns JSON with worker results, brain decision, and file hits.
- Secret scan prints no credential values.

## GitHub Readiness

- [ ] `README.md` explains the product in plain public language.
- [ ] `docs/ARCHITECTURE.md` explains runtime roles.
- [ ] `docs/OPEN_SOURCE_BOUNDARY.md` explains what is public and private.
- [ ] `docs/SECURITY_AND_PRIVACY.md` explains approval gates and private data
  rules.
- [ ] `.env.example` contains placeholders only.
- [ ] `.gitignore` excludes local DBs, caches, virtualenvs, and secrets.
- [ ] No generated `__pycache__` or `.pyc` files are present.

## Suggested First Release Message

```text
Alfred System is a reference architecture for background cognition:
local file memory, Afu Brain routing, Afu-style work memory, and Parallel
Claw concurrent workers.

The goal is simple: prepare context before the user asks, then finish complex
tasks faster, safer, and with less foreground token burn.
```

## Next Public Milestones

- Add a browser demo.
- Add a mock LINE adapter.
- Add a mock calendar adapter.
- Add a local OCR example.
- Add a small local reranker example.
- Add benchmark scripts for file-search latency and worker throughput.

