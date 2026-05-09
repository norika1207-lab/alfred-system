# Voice / TTS Handoff

## Absolute Rule

The demo must never play two narration lines at the same time.

This matters because overlapping voices make the product feel broken even when
the visual demo is correct.

## Root Cause To Remember

Stopping the current `Audio` element is not enough.

ElevenLabs requests are asynchronous. A previous request can finish after the
user has already switched scenario, clicked another step, replayed narration, or
started the demo again. If that late response is still allowed to create and
play an `Audio` object, two voices will overlap.

## Current Fix

The HTML demo uses `ttsState.runId`.

Every call to `stopVoice()` increments `runId`.

Every `speakNarration()` call stores the active `runId`, then checks it after:

- voice lookup
- TTS fetch
- audio blob creation
- before playback
- after playback starts
- error handling
- final busy-state cleanup

If the stored `runId` is stale, the old request exits and must not play.

## Playback Pacing Rule

The demo must not advance to the next stage before narration finishes.

Do not use fixed short timers such as:

```js
setTimeout(() => renderStep(step), index * 2200)
```

That makes the visual stage jump while Alfred is still speaking, which causes
the viewer to miss both the screen and the narration.

The current `play()` flow is intentionally controlled by the visual stage
runner, not by the TTS promise:

```text
render step
start narration without awaiting it
advance after voice completion plus reading time, or after the stage watchdog
```

If voice is disabled or TTS fails, the demo falls back to a slower visual delay
so the viewer still has enough time to read the stage.

Do not rely on `audio.onended` alone. Browser audio events can fail to fire for
some remote/generated audio blobs. The demo must use
`monitorNarrationCompletion(audio, text, runId)` to poll:

- `audio.ended`
- `audio.currentTime`
- `audio.duration`
- whether playback is near the end
- whether playback has stalled
- a max estimated duration failsafe

When the watchdog decides narration has finished, Play Demo must advance to the
next stage.

The stage controller must never be fully owned by the TTS promise, and `play()`
must never `await` `speakNarration()` directly. A stuck TTS promise must not
freeze the screen. The visual flow has its own deterministic deadline:

```js
speakNarration(text).then(...)
setTimeout(() => advanceOnce("stage watchdog"), hardDeadlineMs)
```

This prevents the demo from freezing if any of these hang:

- ElevenLabs voice lookup
- ElevenLabs TTS fetch
- `audio.play()`
- browser audio events
- watchdog callback

When the stage advances, call `stopVoice()` to invalidate any old narration
before starting the next stage. The transition is guarded by `advanceOnce()` so
voice completion, voice fallback, and the watchdog cannot double-advance. This
keeps the demo moving while still avoiding overlapping voices.

Single-stage TTS failure must not turn voice off permanently and must not stop
the demo. A failed narration segment should return `false`, show an error in the
voice status, and let `play()` use the visual fallback delay before advancing.

## Voice Consistency Rule

Narration volume and delivery must feel stable.

Use conservative ElevenLabs settings:

```js
stability: 0.72
similarityBoost: 0.78
style: 0.0
speakerBoost: true
playbackVolume: 1.0
```

Playback volume is clamped between `0.85` and `1.0` so a quiet generated line
does not become inaudible in the browser.

Avoid high `style` values for this demo. They can make the cloned voice more
expressive, but they also make loudness and pacing less predictable.

## Narration Content Rule

The voiceover is part of the product experience, not decoration.

Do not reduce narration to short labels such as "workers are running" or
"approval gate." Each narration segment should explain:

- what the user asked for
- what Alfred is doing
- why Afu workers make it faster or more useful
- what safety boundary is being enforced
- why this is better than ordinary chat

The demo also displays the current narration in a visible caption box. Keep that
caption synchronized with the spoken text so viewers can follow even if audio is
muted, delayed, or replayed.

## Browser Autoplay Rule

Voice can be visually default-on, but the page must not attempt audio playback
before the user interacts with the document.

Browsers block autoplay and will throw:

```text
play() failed because the user didn't interact with the document first
```

The initial page render must therefore use:

```js
renderStep(0, { narrate: false })
```

Narration should start only after a click, such as:

- Play Demo
- Replay Voice
- timeline step
- scenario card
- Voice button

## Do Not Regress

Do not remove these checks:

```js
if (runId !== ttsState.runId) return;
```

Do not add another narration path that directly creates `new Audio(...)` without
going through the same cancellation rule.

Do not use browser `speechSynthesis` at the same time as ElevenLabs narration.

## Local Private Config

The demo reads:

```text
web/local-tts-config.js
```

That file is ignored by git and may contain a private ElevenLabs key.

The public template is:

```text
web/local-tts-config.example.js
```

Never commit the private config.
