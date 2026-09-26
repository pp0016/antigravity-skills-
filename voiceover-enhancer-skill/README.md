# Voiceover Enhancer Skill

Enhances any script for ElevenLabs text-to-speech voiceover. Adds audio tags, pacing, emphasis, text normalization, and settings recommendations. Works with English, Hindi, and Hinglish scripts across any content style.

## Installation

### Antigravity IDE / Gemini

The skill is already installed if you're reading this. It lives at:
```
~/.gemini/config/skills/voiceover-enhancer-skill/
```

### Other Platforms

Clone to the platform's native skill path:

**Claude Code:**
```bash
cp -R ./voiceover-enhancer-skill ~/.claude/skills/voiceover-enhancer-skill
```

**GitHub Copilot (project-level):**
```bash
cp -R ./voiceover-enhancer-skill .github/skills/voiceover-enhancer-skill
```

**Cursor (project-level only):**
```bash
cp -R ./voiceover-enhancer-skill .cursor/skills/voiceover-enhancer-skill
```

**Gemini CLI:**
```bash
cp -R ./voiceover-enhancer-skill ~/.gemini/skills/voiceover-enhancer-skill
```

Or run the installer:
```bash
./voiceover-enhancer-skill/install.sh
```

## Usage

Open a new chat session and type:

```
/voiceover-enhancer [paste your script here]
```

### Options

| Flag | Purpose | Example |
|------|---------|---------|
| `--style` | Force a specific style | `--style horror` |
| `--model` | Force v2 or v3 model | `--model v2` |
| `--lang` | Force language detection | `--lang hindi` |

### Supported Styles

- Horror/Thriller
- Motivational
- Educational/Explainer
- News
- Meditation/ASMR
- Custom (tell the AI to add a new style)

### Output

1. **Settings Recommendation** — Model, stability, speed with explanation
2. **Enhanced Script** — Copy-paste-ready text with audio tags, pacing, emphasis

## File Structure

```
voiceover-enhancer-skill/
├── SKILL.md                          # Main instructions (the AI reads this)
├── AGENTS.md                         # Platform discovery companion
├── references/
│   ├── elevenlabs-v3-guide.md        # v3 audio tags, settings, examples
│   ├── elevenlabs-v2-guide.md        # v2 SSML, phoneme tags, settings
│   ├── text-normalization.md         # TTS normalization rules
│   └── style-profiles.md            # Per-style input/output examples
├── install.sh                        # Cross-platform installer
└── README.md                         # This file
```

## License

MIT
