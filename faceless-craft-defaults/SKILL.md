---
name: faceless-craft-defaults
description: >-
  Curated design defaults for faceless YouTube channel video generation.
  Pins color palettes, typography, transition timings, and layout rules
  for educational explainers, data visualizations, and horror/story
  narration videos. Works with both Remotion and HyperFrames.
  Activates when generating faceless video code, creating explainers,
  building data-viz videos, or writing horror narration visuals.
  Triggers on: faceless video, explainer, data visualization, horror
  narration, story video, design defaults, video branding, channel style.
  Extensible — user can add new content types later.
---

# /faceless-craft — Design Defaults for Faceless Channels

When generating video code (Remotion or HyperFrames) for faceless channels, apply these curated defaults instead of guessing values. These are organized by content type.

## Global Defaults (Apply to ALL content types)

### Resolution Presets
| Format | Resolution | FPS | Use |
|---|---|---|---|
| YouTube Long | 1920×1080 | 30 | Main videos |
| YouTube Shorts | 1080×1920 | 30 | Shorts, TikTok, Reels |
| Square | 1080×1080 | 30 | Instagram posts |

### Typography (1920×1080 base)
| Role | Size | Weight | Font Stack |
|---|---|---|---|
| Hero Title | 96px | 800 | `Inter, system-ui, sans-serif` |
| Section Header | 64px | 700 | `Inter, system-ui, sans-serif` |
| Body | 42px | 400 | `Inter, system-ui, sans-serif` |
| Caption/Label | 28px | 500 | `JetBrains Mono, monospace` |
| Data Number | 72px | 700 | `JetBrains Mono, monospace` |

For Shorts (1080×1920), multiply all sizes by 0.75.

### Transition Timing
| Transition | Duration | Easing | When |
|---|---|---|---|
| Scene fade | 0.6s | ease-in-out | Between major sections |
| Slide-in | 0.4s | cubic-bezier(0.16, 1, 0.3, 1) | New elements entering |
| Scale pop | 0.3s | cubic-bezier(0.34, 1.56, 0.64, 1) | Emphasis/highlight |
| Ken Burns | 8-12s | linear | Static image zoom |
| Data counter | 1.5s | ease-out | Number animations |

### Audio Integration
- **Voiceover:** Always placed manually by user (ElevenLabs website → download → `audio/voiceover.mp3`)
- **Music:** Royalty-free, 20-30% volume relative to voice
- **SFX:** Swoosh on transitions, subtle pop on data reveals

---

## Content Type: Educational Explainers

### Color Palette
| Role | Color | Hex |
|---|---|---|
| Background | Deep Navy | `#0a1628` |
| Surface/Card | Dark Slate | `#1a2744` |
| Primary Text | Warm White | `#f0f4f8` |
| Accent 1 | Electric Blue | `#3b82f6` |
| Accent 2 | Emerald | `#10b981` |
| Highlight | Amber | `#f59e0b` |
| Warning/Negative | Rose | `#f43f5e` |

### Layout Rules
- **Scene structure:** Hook (3s) → Problem (10s) → Explanation (30-60s) → Summary (5s) → CTA (3s)
- **Visual density:** Max 3 elements on screen at once
- **Icons:** Use Lucide or Phosphor icon sets, 48px, stroke-only (not filled)
- **Diagrams:** White lines on dark background, animated draw-on effect
- **Charts:** Animate bars/lines growing from zero, stagger 0.1s per data point

### Remotion-Specific
```typescript
// Scene beat timing (30fps)
const SCENE_BEATS = {
  hook: 90,        // 3 seconds
  problem: 300,    // 10 seconds
  explain: 1800,   // 60 seconds (adjust per script)
  summary: 150,    // 5 seconds
  cta: 90,         // 3 seconds
};
```

### HyperFrames-Specific
```css
/* Base composition style */
.scene {
  background: linear-gradient(135deg, #0a1628 0%, #1a2744 100%);
  font-family: 'Inter', system-ui, sans-serif;
  color: #f0f4f8;
  padding: 80px;
}
.accent { color: #3b82f6; }
.highlight { color: #f59e0b; }
```

---

## Content Type: Data Visualization

### Color Palette
| Role | Color | Hex |
|---|---|---|
| Background | Charcoal | `#111827` |
| Grid/Axes | Muted Gray | `#374151` |
| Primary Text | Pure White | `#ffffff` |
| Data Series 1 | Cyan | `#06b6d4` |
| Data Series 2 | Violet | `#8b5cf6` |
| Data Series 3 | Lime | `#84cc16` |
| Data Series 4 | Orange | `#f97316` |
| Positive/Up | Green | `#22c55e` |
| Negative/Down | Red | `#ef4444` |

### Layout Rules
- **Chart area:** 70% of frame width, centered, with 15% padding on each side
- **Legend:** Bottom-left, horizontal, 28px labels
- **Animation:** Always animate data from zero. Stagger bars by 0.15s each
- **Labels:** Data point values appear AFTER animation completes, not during
- **Comparison:** Side-by-side layout, never overlapping charts
- **Source citation:** Bottom-right, 20px, 40% opacity, always visible

### Number Animation Pattern
```typescript
// Count up from 0 to target value
const animateNumber = (target: number, duration: number = 45) => {
  const frame = useCurrentFrame();
  const progress = Math.min(frame / duration, 1);
  const eased = 1 - Math.pow(1 - progress, 3); // ease-out cubic
  return Math.round(target * eased);
};
```

---

## Content Type: Horror / Story Narration

### Color Palette
| Role | Color | Hex |
|---|---|---|
| Background | Void Black | `#050505` |
| Surface | Blood Mist | `#1a0a0a` |
| Primary Text | Bone White | `#e8e0d8` |
| Accent | Crimson | `#dc2626` |
| Secondary | Sickly Amber | `#b45309` |
| Glow | Pale Blue | `#93c5fd` (20% opacity) |

### Layout Rules
- **Pacing:** Slow. Scene transitions 1.2s minimum. Let emptiness breathe.
- **Text reveal:** Character-by-character typewriter effect, 0.04s per character
- **Background:** Subtle grain overlay (CSS noise or SVG filter), 5% opacity
- **Vignette:** Radial gradient darkening edges, always present
- **Glitch effect:** Random 2-frame displacement every 15-20 seconds
- **Sound design:** Bass rumble on scene changes, whisper SFX on text reveals

### Remotion-Specific
```typescript
// Vignette overlay
const Vignette = () => (
  <AbsoluteFill style={{
    background: 'radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.8) 100%)',
    pointerEvents: 'none',
  }} />
);

// Film grain
const Grain = () => (
  <AbsoluteFill style={{
    backgroundImage: `url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.05'/%3E%3C/svg%3E")`,
    pointerEvents: 'none',
  }} />
);
```

### HyperFrames-Specific
```css
.scene-horror {
  background: #050505;
  color: #e8e0d8;
  font-family: 'Crimson Text', Georgia, serif;
}
.scene-horror::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at center, transparent 50%, rgba(0,0,0,0.8) 100%);
  pointer-events: none;
}
.typewriter { animation: typing 3s steps(40, end); }
.blood-accent { color: #dc2626; }
```

---

## Adding New Content Types

This skill is extensible. To add a new content type later:

1. Define a **Color Palette** table (background, surface, text, 2-3 accents)
2. Define **Layout Rules** (scene structure, visual density, animation patterns)
3. Add **Remotion-Specific** code snippets (components, timing constants)
4. Add **HyperFrames-Specific** code snippets (CSS classes, HTML structure)
5. Append the new section to this file

The agent should always ask which content type to use before generating video code.
