---
name: documentary-style
description: >
  Programmatic documentary/commentary-style video editing using Remotion, FFmpeg,
  and ElevenLabs. Covers keyframe animation (Ken Burns), word-synced text popups,
  era-coded color grading, film grain, transitions, and pacing logic — all
  controlled from terminal with zero manual editing. Based on forensic visual
  analysis of Indian documentary/commentary channels. MUST activate when the user
  mentions: documentary style, documentary editing, documentary video, commentary
  style, Ken Burns effect, keyframe animation, word-synced text, film grain overlay,
  era-coded color grading, faceless documentary, make a video, edit my video,
  render my video, video editing style, Remotion documentary, programmatic video
  editing, documentary template, or any task involving assembling images + voiceover
  into a cinematic documentary-format video.
---

# Documentary Style — Complete Editing Skill

> **Origin**: Forensic visual breakdown of [https://youtu.be/FSpmUNG2JCY](https://youtu.be/FSpmUNG2JCY) (Shivanshu Agrawal — "The Sad Downfall of Mumbai Dabbawala"). Every technique below is extracted from frame-by-frame analysis of this video and mapped to programmatic tools.

---

## WHAT THIS SKILL IS

This skill turns a **script + AI images + voiceover** into a **cinematic documentary-style video** using only terminal commands. No manual editing. No GUI. The agent (Antigravity/Gemini/any AI) controls the entire editing pipeline.

**This skill is ONLY about editing style.** Not about scripts, SEO, niche research, thumbnails, or workflow. Priyanshu has separate workflows for all of those. This skill handles the visual editing and rendering.

---

## THE 5 SIGNATURE TECHNIQUES

These 5 techniques define the documentary visual identity. If you replicate only these 5, any video instantly looks cinematic and not like a slideshow.

### 1. Narration-Locked Keyword Typography
- Bold geometric sans-serif (Montserrat), popping on screen **exactly when the narrator says the word**
- **Yellow** (`#FFE600`) for emphasis keywords, **white** (`#FFFFFF`) for neutral, **red** (`#EF4444`) for failure/negative, **cyan** on black for end cards
- Text entry: scale-pop with `spring()` animation (damping: 10-12, stiffness: 120-220)
- Text background: either bare with drop shadow + stroke, OR solid banana-yellow pill (`background + borderRadius`)
- Word timestamps come from **ElevenLabs `with-timestamps` API** — returns character-level timing, aggregate to words

### 2. Era-Coded Color Grading + Global Grain & Vignette
- **Two-grade system**, not one look:
  - **Period/warm grade**: warm desaturated sepia, golden-hour feel — for historical/past sections
  - **Crisis/cold grade**: cool desaturated blue-grey, heavy vignette, high contrast — for downfall/negative sections
  - **Modern/neutral grade**: crisp, high-contrast, cool-toned — for present-day sections
- **Film grain**: applied over EVERYTHING (AI stills + any archival-style images). Procedural, per-frame flicker using `@remotion/effects` `noise()` with `seed: useCurrentFrame()`
- **Vignette**: soft vignette throughout, heavy vignette in crisis sections
- The grade carries narrative weight — the shift from warm to cold IS the story turn

### 3. Relentless Ken Burns Motion on 100% of Stills
- **Every single image moves** — slow zoom-in, zoom-out, or horizontal/vertical pan
- Duration: stills hold **3-6 seconds** standard, **1.5-3 seconds** in dense argument sections
- Scale change: ~5-8% per shot, runs continuously for the ENTIRE hold (never stops mid-shot)
- Speed is **coupled to shot length** — same scale delta whether shot is 2s or 6s
- Implementation: Remotion `interpolate()` + `Easing.bezier(0.33, 1, 0.68, 1)` on CSS `transform: scale() translate3d()`
- **Never use FFmpeg `zoompan`** — has the infamous jitter bug (#4298). Always use Remotion CSS transforms.

### 4. Full-Frame Images as First-Class Shots
- Images fill the entire 1920×1080 frame — no borders, no pillarboxing, no letterboxing
- Single canvas: 16:9, full-frame, one composition root
- Graphics and diagrams (when used) are designed as **full-frame art**, cut like any other shot — not overlaid as chart furniture
- Newspaper clippings: paper texture background, drop shadow, slight rotation
- Screenshots/UI: clean white background, rounded corners, subtle drop shadow

### 5. Cut-to-the-Sentence Pacing + Transitions
- **Hard cuts** are the backbone (default — no transition = hard cut)
- **Crossfade/dissolve** (0.25-0.4s, ~8-12 frames): reserved for era/tone changes only
- **Slide/wipe**: between graphics or infographic panels only
- **Glitch flash**: dramatic keyword reveals (RGB channel split + burst noise)
- **Fade to/from black**: only at the very end (outro)
- Pacing rule: **"Cut to the sentence, not to the clock"**
  - Hook: 1-2s per shot
  - Exposition: 3-6s per shot
  - Dense argument: 1.5-3s per shot
  - Dramatic hold: 2-3s static hold (used once or twice at emotional low point)
  - Outro: 3-4s per card, then static black end card

---

## APPROVED TOOLS (Priyanshu's Decisions)

### ✅ USE THESE

| Tool | Role |
|---|---|
| **ElevenLabs v3** (via MCP) | Voiceover + word-level timestamps. User gives voice name + ID, agent generates audio |
| **Remotion 4.x** | Main video compositor — Ken Burns, text sync, color grading, transitions, grain |
| **`@remotion/effects`** | Color grading (LUTs, sepia, desaturation), film grain, vignette, paper shader |
| **`@remotion/transitions`** | Hard cuts, crossfade, slide/wipe, glitch |
| **`@remotion/captions`** | Word-level text sync from ElevenLabs timestamps |
| **FFmpeg** (WinGet path) | Final encode only. MUST use: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe` with `-pix_fmt yuv420p -crf 17` |
| **Nano Banana 2** | Primary image generation (AI cinematic stills, diagrams, graphics) |
| **Google Flow** | Batch image generation |
| **WhisperX** | Backup word-level timestamp alignment (if ElevenLabs timestamps aren't precise enough) |
| **Groq Whisper** | Fast transcription for reference/research |
| **GitHub Actions** | Cloud rendering when local is too slow |
| **Freesound / BBC SFX** | Transition sound effects (whoosh, hit, reveal) |
| **YouTube Audio Library / Mixkit** | Background music |
| **Montserrat font** | All on-screen text (variable font, all weights) |

### ❌ DO NOT USE (Explicitly Rejected)

| Tool | Why |
|---|---|
| ImageFX | Not using |
| Google Veo 3.1 | No video clips — images only |
| NotebookLM | Nano Banana 2 handles diagrams |
| Manim | No complex animated diagrams needed |
| MapLibre / Turf.js | Maps irrelevant for user's niche |
| CapCut | No manual editing — terminal only |
| Humanizer skill | This skill is editing only, not scripts |
| Voiceover Enhancer skill | This skill is editing only, not scripts |
| MoviePy | Toy — too slow, terrible transitions |
| Editly | Stagnant, dependency hell, avoid |
| google-genai SDK | Adds complexity, Antigravity already does orchestration |
| Pillow / OpenCV / Librosa | Not needed for video editing pipeline |

---

## PROJECT LOCATION

| Item | Path |
|---|---|
| Remotion Project | `C:\Users\renu5\.gemini\antigravity\scratch\documentary-style\documentary-template` |
| Source Files | `C:\Users\renu5\.gemini\antigravity\scratch\documentary-style\documentary-template\src\` |
| Public Assets | `C:\Users\renu5\.gemini\antigravity\scratch\documentary-style\documentary-template\public\` |
| Montserrat Font | `C:\Users\renu5\.gemini\antigravity\scratch\documentary-style\documentary-template\public\Montserrat-Variable.ttf` |
| Toolkit Reference | `C:\Users\renu5\Downloads\priyanshu readme\youtube\Stickman_toolkit\toolkit.md` (has "Documentary Style Tools Required" section) |

### Installed Packages (package.json)
```json
{
  "@remotion/captions": "^4.0.535",
  "@remotion/cli": "4.0.535",
  "@remotion/effects": "^4.0.535",
  "@remotion/transitions": "^4.0.535",
  "react": "19.2.3",
  "react-dom": "19.2.3",
  "remotion": "4.0.535"
}
```

---

## THE PIPELINE (How a Video Gets Made)

```
INPUT (from Priyanshu):
  1. Script (text)
  2. Voice ID (ElevenLabs voice name + ID)
  3. Images (generated via Nano Banana 2 / Google Flow)
  4. Music choice (YouTube Audio Library / Mixkit track)

AGENT DOES:
  1. Generate voiceover → ElevenLabs MCP → audio.mp3 + word_timestamps.json
  2. Mark keywords in script → which words get yellow text popups
  3. Assign each image to a script segment with:
     - Duration (based on narration timing)
     - Ken Burns direction (zoom-in, zoom-out, pan-left, pan-right)
     - Color grade mode (period / modern / crisis)
     - Transition to next shot (hard cut / dissolve / wipe / glitch)
  4. Generate Remotion composition code (TypeScript/React)
  5. Preview render (local, low-res)
  6. Final render (local or GitHub Actions, 1080p)
  7. FFmpeg final encode with zero-degradation flags

OUTPUT:
  FINAL_VIDEO.mp4 (ready to upload to YouTube)
```

---

## QUICK BUILD REFERENCE (From the Forensic Breakdown)

| Parameter | Value |
|---|---|
| Canvas | 1920×1080, 16:9, single composition root, no letterboxing |
| Still hold | 3-6s standard, 1.5-3s in dense sections |
| Ken Burns | Continuous push-in or pan for full hold, ~5-8% scale delta |
| Cut rate | ~2-4s average; 1-2s in hook and sponsor bursts |
| Text stack | Montserrat Bold/Black · yellow / white / red / cyan-on-black |
| Text background | None (shadow + stroke) or solid banana-yellow pill |
| Text entry | Fade + scale-pop via `spring()`, triggered on the spoken keyword |
| Grade | Warm sepia (period) · cool blue-grey desaturated (crisis) · neutral high-key (modern) |
| Global overlay | Film grain + soft vignette; heavy vignette in crisis sections |
| Transitions | Hard cut (default) · 0.25-0.4s dissolve at era changes · slide/wipe between graphics · glitch flash on dramatic reveals |
| Branding | No logo, no watermark, no intro animation, no subscribe card |
| End card | Static black + glowing cyan "WATCH NEXT" text, ambient fade-out |
| FPS | 30fps |
| Render flags | `--gl=angle`, `--scale=2` for crisp text |

---

## WORD-LEVEL SYNC ARCHITECTURE

### ElevenLabs (Primary — Zero Extra Tools)
```
POST /v1/text-to-speech/{voice_id}/with-timestamps
→ Returns: audio_base64 + alignment (character-level start/end times)
→ Aggregate characters into words using whitespace boundaries
→ Output: words_and_keywords.json
→ Feed into Remotion useCurrentFrame() + spring()
```

### WhisperX (Backup — Local GPU)
```
whisperx audio.wav --language hi --align_model wav2vec2
→ Sub-50ms word-level accuracy
→ Use when ElevenLabs timestamps drift on fast Hindi speech
```

---

## REMOTION COMPONENT PATTERNS

### Ken Burns Image Component
```tsx
// CSS transform with bezier easing — zero jitter, sub-pixel precision
const scale = interpolate(frame, [0, durationInFrames], [1.0, 1.08], {
  easing: Easing.bezier(0.33, 1, 0.68, 1),
  extrapolateRight: "clamp",
});
// Apply: transform: `scale(${scale}) translate3d(${translateX}px, 0, 0)`
```

### Keyword Text Popup
```tsx
// Spring animation fires at exact word timestamp
const startFrame = Math.round((word.startMs / 1000) * fps);
const pop = spring({
  frame: frame - startFrame,
  fps,
  config: { damping: 12, stiffness: 200, mass: 0.8 },
});
// Yellow text, Montserrat Black, scale-pop entrance
```

### Color Grade Config
```tsx
type GradeMode = 'period' | 'modern' | 'crisis';
// period: filter: 'sepia(0.6) contrast(1.1) brightness(0.9) saturate(0.7)'
// crisis: filter: 'saturate(0.4) contrast(1.3) brightness(0.85)' + hue-rotate towards blue
// modern: filter: 'contrast(1.05) brightness(1.0) saturate(1.1)'
// ALL get: film grain via noise() + vignette via vignette()
```

---

## OPTIONAL REMOTION LIBRARIES (Install When Needed)

| Library | Install | Purpose |
|---|---|---|
| Remocn | `npx shadcn add ...` from [Remocn/remocn](https://github.com/Remocn/remocn) | Typewriter text, RGB Glitch, Kinetic Type, VHS filter |
| remotion-bits | `npx remotion-bits fetch ...` from [av/remotion-bits](https://github.com/av/remotion-bits) | Ken Burns presets, text effects |
| @remotion/rough-notation | `npm install @remotion/rough-notation` | Hand-drawn highlight markers on documents |

---

## RENDER OPTIONS

| Method | Speed | When to Use |
|---|---|---|
| Local preview | ~1-2 fps | Quick visual check during development |
| Local full render | ~2.5-5 hours for 10-min video | Overnight render when GitHub Actions isn't needed |
| GitHub Actions (parallel) | ~15-30 minutes | Production renders — user's recommended approach |

---

## CRITICAL RULES

1. **Never use FFmpeg `zoompan`** for Ken Burns — has jitter bug. Always use Remotion CSS transforms.
2. **Never create a static frame** — every image must have continuous Ken Burns motion + grain.
3. **Never use generic `ffmpeg` alias** — always use the full WinGet path with `-pix_fmt yuv420p -crf 17`.
4. **Text syncs to narration words**, not to the clock or music beats.
5. **This skill is editing ONLY** — don't touch scripts, SEO, niche strategy, or other workflow concerns.
6. **No video clips** — this pipeline uses images only (Nano Banana 2 / Google Flow).
7. **No maps or animated diagrams** unless user explicitly asks for a geography-heavy video.
8. **The grade carries the story** — warm past → neutral present → cold crisis is a narrative device, not decoration.
