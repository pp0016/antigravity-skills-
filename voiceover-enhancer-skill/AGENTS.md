# Voiceover Enhancer Skill

Enhances any script for ElevenLabs text-to-speech voiceover. Strips non-narration
elements, normalizes text for TTS, adds audio tags and pacing markers, and outputs
copy-paste-ready enhanced scripts with model/settings recommendations.

## Purpose

This skill is activated when the user wants to enhance a voiceover script for
ElevenLabs TTS. It handles English, Hindi, and Hinglish scripts across any content
style (horror, motivational, educational, news, meditation, and custom styles).

## Activation

This skill activates on:
- `/voiceover-enhancer` invocation
- "enhance voiceover", "optimize for elevenlabs", "make this TTS-ready"
- "prepare script for voice", "enhance for text to speech"
- "elevenlabs script", "voice over enhancement", "TTS optimization"

## Usage

Provide any raw script and optionally specify style and model:

```
/voiceover-enhancer [paste script]
/voiceover-enhancer --style horror [paste script]
/voiceover-enhancer --model v2 [paste script]
```

## How It Works

The skill runs a 5-stage pipeline:
1. **Language Detection** — Auto-detects English/Hindi/Hinglish
2. **Script Cleaning** — Strips scene descriptions, camera directions, visual cues
3. **Text Normalization** — Converts numbers, dates, currencies to spoken form
4. **Audio Tag Enhancement** — Adds ElevenLabs audio tags, emphasis, pacing per style
5. **Settings Recommendation** — Outputs model, stability, and speed recommendations

## Full Instructions

See `SKILL.md` in this directory for the complete enhancement pipeline, audio tag
reference, style profiles, and all rules.
