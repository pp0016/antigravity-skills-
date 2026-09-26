---
name: remotion-craft-skill
description: >-
  Curated motion design values for Remotion video generation. Pins spring
  presets, dark cinematic palettes, typography scale, frame-specific timing
  defaults, camera drift ranges, and Remotion-specific gotchas. Activates
  when generating Remotion code, creating programmatic videos, building
  motion graphics, or editing video compositions. Triggers on remotion,
  video, motion graphics, animation, explainer video, programmatic video,
  create video, make video, render video, cinematic, video editor.
---

# /remotion-craft — Motion Design Defaults

When generating Remotion video code, apply these curated defaults instead of guessing values.

## Spring Presets

Always use named presets. Never use raw spring values without mapping to a mood.

```typescript
const SPRING = {
  default:  { mass: 1, stiffness: 100, damping: 10  }, // Playful UI, interactive feedback
  smooth:   { mass: 1, stiffness: 100, damping: 200 }, // Text reveals, mask fades, slow shifts (no bounce)
  snappy:   { mass: 1, stiffness: 200, damping: 20  }, // UI overlays, secondary menus, small elements
  bouncy:   { mass: 1, stiffness: 100, damping: 8   }, // Brand intros, character pops, sticker drops
  heavy:    { mass: 2, stiffness: 80,  damping: 15  }, // Title cards, major containers, weighty motion
};
```

## Dark Cinematic Palettes

Never use `#000000` backgrounds. Pick from these curated themes based on video mood.

| Theme | Background | Accent | Use When |
|---|---|---|---|
| Midnight Velvet | `hsl(229,60%,5%)` `#050814` | `#f9fafb` | Dramatic, polished, intense |
| Noir City Streets | `hsl(0,0%,2%)` `#050505` | `#f59e0b` | Gritty, urban, vintage |
| Shadowframe Teal | `hsl(224,71%,4%)` `#020617` | `#0f766e` | Cool, tense, technical |
| Charcoal Glass | `hsl(224,71%,4%)` `#020617` | `#e5e7eb` | Sleek, minimal, corporate |
| Obsidian Gold | `hsl(0,0%,1%)` `#020202` | `#fbbf24` | Luxurious, premium |
| Inkstone Editorial | `hsl(220,60%,3%)` `#030712` | `#f3f4f6` | Calm, documentary |
| Night Slate | `hsl(224,71%,4%)` `#020617` | `#cbd5e1` | Refined, corporate |
| Emberlit Studio | `hsl(254,35%,5%)` `#090712` | `#f97316` | Warm, creative, intimate |

Text: lightness 85%, saturation 15%. Surfaces: lightness 10-12%. Keep 40-50% lightness gap between text and background.

## Typography Scale (1920×1080)

| Role | Size | Weight | Line Height |
|---|---|---|---|
| Hero Title | 96px | 700 | 1.1em |
| Scene Header | 80px | 600 | 1.2em |
| CTA | 72px | 500 | 1.2em |
| Body | 48px | 400 | 1.4em |
| Subtitles | 32px | 500 | 1.3em |

Film subtitles: Georgia 42px weight 400, color `#f5d442`, max-width 70%, bottom padding 120px, instant opacity toggle (no fade), no uppercase.

## Frame Timing Defaults (30fps)

| Animation | Frames | Easing |
|---|---|---|
| Standard fade-in | 30 | linear |
| Smooth slide-in | 45 | `Easing.out(Easing.cubic)` |
| Scale pop | 36 | `Easing.bezier(0.16, 1, 0.3, 1)` |
| Kinetic slides | 12-21 | spring snappy |
| Screen beats (scenes) | 90-240 | — |
| Caption entrance | 10-14 | `Easing.bezier(0.16, 1, 0.3, 1)` |
| Lower third fade | 20 in, 20 out | `[0, 20, dur-20, dur] → [0,1,1,0]` |
| Transition overlap | 18 | linearTiming or springTiming |
| Narration breath gap | 12 | `startInFrames={0.4 * fps}` |

## Camera Movement

**Primary moves** (intentional, punchy):
- Scale: 1.0 → 1.5 (never subtle like 1.05 for primary moves)
- Translate: 80-260px (4-13% of 1920px frame)
- Duration: 12-21 frames with aggressive easing

**Ambient drift** (keeps scenes alive, runs full scene length):
- Scale drift: +0.05 to +0.10
- Translate drift: 10-30px (0.5-1.5% of frame)
- Always interpolate FROM negative offset back TO 0 so resting frame is predictable
- Use `objectFit: "cover"` on full-bleed background layers

## cutInMotion Conveyor Pattern

Clips animation curves at scene boundaries so elements are still moving at the cut:

- Scene 1 (intro): enter normal, exit `cutInMotion={0.3}`
- Middle scenes: enter `cutInMotion={0.1}`, exit `cutInMotion={0.2}`
- Last scene: exit `cutInMotion={0.1}`

## Remotion Gotchas (Apply Always)

1. **Audio outside transitions**: Never nest `<Audio>` inside `<TransitionSeries>`. Declare audio globally in the parent `<AbsoluteFill>`. Nesting causes audio pops and clipping at transition boundaries.

2. **Subpixel jitter**: On continuous transforms (scale/translate), add `willChange: 'transform'` and round values to 3 decimals: `Math.round(val * 1000) / 1000`.

3. **Outline over border**: Remotion uses `box-sizing: border-box` by default. Borders shrink containers. Use CSS `outline` instead, or subtract border width from spacing.

4. **No percentages in inline wrappers**: Children of inline animation wrappers must use `px` or `em`, never `width: '100%'` (resolves to 0px because wrapper has no intrinsic size).

5. **Static captions across cuts**: If consecutive scenes share the same caption text, do NOT re-animate it. Keep it static (`staticEntry`) to prevent flicker.

6. **Posterized motion**: For hand-drawn or stop-motion feel, use `posterize: 3` inside interpolate options to quantize updates to every 3rd frame.
