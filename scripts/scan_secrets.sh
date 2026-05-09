#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"

echo "Scanning $ROOT for likely secrets..."

grep -RInE \
  "(api[_-]?key[[:space:]]*=.+|secret[[:space:]]*=.+|token[[:space:]]*=.+|password[[:space:]]*=.+|private key|BEGIN RSA|BEGIN OPENSSH|LINE_CHANNEL_ACCESS_TOKEN=.+|TELEGRAM_BOT_TOKEN=.+|GOOGLE_CLIENT_SECRET=.+)" \
  "$ROOT" \
  --exclude-dir=.git \
  --exclude-dir=.venv \
  --exclude-dir=docs \
  --exclude="README.md" \
  --exclude=".gitignore" \
  --exclude=".env.example" \
  --exclude="local-tts-config.js" \
  --exclude="scan_secrets.sh" \
  || true

echo "Review matches manually before publishing."
