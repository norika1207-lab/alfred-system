// Copy this file to web/local-tts-config.js for local demo narration.
// local-tts-config.js is ignored by git. Never commit your API key.
window.ALFRED_TTS_CONFIG = {
  provider: "elevenlabs",
  apiKey: "YOUR_ELEVENLABS_API_KEY",
  // If voiceId is empty, the demo will try to find this cloned voice by name.
  voiceId: "",
  voiceName: "Alfred 阿福",
  modelId: "eleven_multilingual_v2",
  stability: 0.72,
  similarityBoost: 0.78,
  style: 0.0,
  speakerBoost: true
};
