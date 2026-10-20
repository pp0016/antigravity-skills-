---
name: srt-whiteboard-animation
description: Transforms SRT subtitles into warm-beige paper whiteboard hand-drawn animations. Reads subtitles -> outputs visual storyboard strategy -> generates consistent minimalist line-art illustrations -> creates semantic narrative region annotations -> interactive visual preview/adjust -> renders full MP4 animations with continuous hand-drawn stream strokes (ink line-art -> color wash). Triggers when the user provides SRT subtitles and asks for whiteboard hand-drawn video, SRT to whiteboard animation, or subtitle-synced doodle animations.
---

# SRT Whiteboard Animation (Mask Scheduling + Continuous Stream Drawing)

Converts SRT subtitles into whiteboard hand-drawn animation videos:
- **Scheduling (Mask Orchestration):** Sequential region-by-region reveals based on subtitle events (`annotation.json` / `sequence` / `startMs` / `protectedRegions`). Unstarted elements remain strictly hidden. Overlapping subjects are protected using `protectedRegions`.
- **Drawing Technique (Stream Rendering):** Real continuous hand-drawn stroke movement. Inside each element's allowed mask, the pen tip glides along skeleton/grid contours depositing ink (initial `ink` line-art -> subsequent `color` wash). All elements share a persistent canvas, preserving finished artwork across the scene.

Unlike frame-by-frame jump cuts or simple rectangular wipe transitions, strokes here are **smooth, continuous, and drawn by a visible hand**. Unlike whole-image stream renderers, this workflow is **partitioned by subtitle narrative**, giving you precise control over element order and timing.

## Default Specification Parameters

| Parameter | Specification |
|---|---|
| Canvas Background | Warm vintage beige paper (recommended: `#F5EBD7`). The renderer samples paper background from the four corners of the source image to eliminate stark white borders. |
| Drawing Style | Stream continuous strokes per region: Initial `ink` (line-art sketch) -> `color` (restore artwork color). Ratio `ink:color = 2:1`. |
| Stroke Path | `--ink-path grid` (grid cell clustering, robust, default) or `skeleton` (Zhang-Suen morphological line tracing, best for clean line art). |
| Coloring Style | `--color-fill contour-wipe` (top-down resistance scan across line art, default) or `brush` (wash along stroke paths). |
| Mask Invariant | Writable mask = element `region` minus `subsequent elements` minus `protectedRegions`. Unstarted elements never appear prematurely. |
| Scene Duration | `sceneDurationMs` derived directly from subtitle timestamps (recommended 25–35 seconds per scene). |
| Proxy Editor | `assets/preview.html` displays editable bounding boxes, sequence order, and subtitle syncing. |

## Visual Artwork Guidelines (Mandatory)

All generated source illustrations must adhere strictly to a unified visual language:

- **Style & Composition:** Minimalist hand-drawn doodle/sketch aesthetic (similar to Notion or Dan Koe minimalist line drawings). Conceptual expression over photorealism. Clean, uncluttered backgrounds with generous negative space. Consistent character design, line weight, and color palette across all scenes.
- **Color Palette:** Warm beige paper background (`#F5EBD7`), dark gray charcoal sketch lines (`#2A2A2A`), with minimal accent touches restricted to Red, Orange, or Blue. Avoid high saturation, busy textures, or multi-color gradients.
- **Subjects & Figures:** Minimal outlines, expressive gestures, and clear spatial relationships over anatomical detail or complex shading.
- **Strictly Prohibited:** No embedded scene text, typography, labels, watermarks, 3D renders, photo textures, or cluttered backgrounds.
- **Drawing Hand Asset:** Uses bundled `drawing-hand.png`. The pen tip anchor aligns with stroke progress.

## Step-by-Step Workflow & Confirmation Gates

To ensure zero wasted render cycles, adhere to the staged confirmation workflow:

1. **Parse Subtitles & Formulate Storyboard Strategy (No Image Generation Yet):**
   Run `scripts/parse_srt.py <subtitles.srt> --target-sec 30 --min-sec 25 --max-sec 35`.
   Group cues into 25–35 second scenes. Output a structured storyboard plan:
   - Scene ID (`scene-01`, `scene-02`, etc.)
   - Core concept/message (single focus per scene)
   - Visual subject & composition description
   - Subtitle time range & `sceneDurationMs`
   *Stop and wait for user confirmation of the storyboard strategy.*

2. **Generate Line-Art Illustrations:**
   Once the storyboard plan is approved, generate 16:9 warm-beige line-art illustrations (`scene-01.png`, etc.) following the Visual Artwork Guidelines.
   *Stop, display generated artwork, and wait for user confirmation.*

3. **Read Subtitles, Inspect Image, Create Annotations & Open Visual Editor:**
   Match visible subjects in the illustration to narrative events in the subtitles:
   - Order: `Scene Setting -> Key Subject -> Action / Conflict -> Reaction / Resolution`.
   - Measure actual pixel dimensions of the image.
   - Generate `scene-xx.annotation.json` with integer pixel coordinates (`x`, `y`, `width`, `height`).
   - Immediately open `assets/preview.html` in Chrome/Edge, load the directory, and inspect the sequence.
   *Stop and wait for user confirmation of annotations.*

4. **Generate Region Check Preview:**
   Run `python scripts/render_annotation_preview.py <image.png> <annotation.json> <preview.png>` to generate numbered bounding boxes and motion arrows. Verify no elements overlap incorrectly.
   *Stop and wait for user confirmation of preview.*

5. **Adjust in Visual Editor & Save:**
   In `assets/preview.html`, drag boxes to adjust boundaries, refine `startMs` and `endMs`, reorder sequence, and verify subtitles. Save updates directly back to `scene-xx.annotation.json`.
   *Stop and wait for user confirmation of finalized timings.*

6. **Render Full MP4 Scene Video:**
   Render the full animation using:
   ```bash
   python scripts/render_stream_whiteboard.py <image.png> <annotation.json> <output.mp4> assets/drawing-hand.png \
       --ink-path grid --color-fill contour-wipe
   ```
   Inspect opening frame, midpoint overlapping segments, and closing gaze frame.
   *Stop and wait for user confirmation of rendered scene.*

7. **Merge Multi-Scene Project:**
   Once all individual scenes are approved, concatenate with:
   ```bash
   python scripts/merge_scenes.py --inputs scene1.mp4 scene2.mp4 scene3.mp4 --output final.mp4
   ```

## Directory Structure Convention

Organize project files as follows:

```text
assets/whiteboard/<project-name>/
├── scene-01-<name>.png
├── scene-01-<name>.annotation.json     # Must match PNG stem
├── scene-01-<name>-whiteboard.mp4      # Rendered scene video
└── scene-02-<name>.png
```

Image and annotation files **must share the same base name** (e.g., `scene-01-intro.png` and `scene-01-intro.annotation.json`).

## Annotation JSON Schema

```json
{
  "sceneId": "scene-01",
  "canvas": { "width": 1672, "height": 941 },
  "storyBasis": "Summary of the scene event and narrative purpose",
  "sceneDurationMs": 9000,
  "elements": [
    {
      "id": "intro_setting",
      "label": "Landscape Setup",
      "sequence": 1,
      "narrativeRole": "Scene Setting",
      "subtitle": "At the summit of the mountain, a little monkey sat peacefully.",
      "type": "structure",
      "region": { "x": 20, "y": 120, "width": 540, "height": 780 },
      "reveal": {
        "direction": "top_to_bottom",
        "startMs": 300,
        "durationMs": 2600,
        "maskPaddingPx": 22,
        "protectedRegions": []
      },
      "handPath": { "start": [290, 130], "end": [290, 890], "easing": "easeInOut" }
    }
  ]
}
```

## CLI Reference

1. **Environment Setup & Verification:**
   ```bash
   python scripts/prepare_env.py --check
   python scripts/prepare_env.py
   ```

2. **Parse Subtitles & Suggest Scenes:**
   ```bash
   python scripts/parse_srt.py <subtitles.srt> --target-sec 30 --min-sec 25 --max-sec 35
   ```

3. **Generate Static Annotation Preview:**
   ```bash
   python scripts/render_annotation_preview.py <image.png> <annotation.json> <preview.png>
   ```

4. **Visual Editor (Browser):**
   Open `assets/preview.html` in Chrome or Edge, click "Open Folder…", select your scene directory, and visually adjust regions, timings, and subtitles.

5. **Render Scene Animation:**
   ```bash
   python scripts/render_stream_whiteboard.py <image.png> <annotation.json> <output.mp4> assets/drawing-hand.png \
       --ink-path grid --color-fill contour-wipe --fps 60 --cap-long-edge 1080
   ```

6. **Merge Scenes into Final Video:**
   ```bash
   python scripts/merge_scenes.py --inputs scene1.mp4 scene2.mp4 scene3.mp4 --output final.mp4
   ```

## Quality Checklist

- [ ] Initial frame starts on a clean warm beige paper texture (`#F5EBD7`) without premature lines.
- [ ] Bounding boxes in `annotation.json` use integer pixel values strictly within canvas boundaries.
- [ ] Drawing sequence matches subtitle narrative order.
- [ ] Overlapping objects are protected with `protectedRegions` so later objects never appear early.
- [ ] Pen tip tracks active strokes smoothly.
- [ ] Scene ends with at least a 0.5s static gaze hold displaying the complete artwork.
- [ ] Final video is encoded in clean H.264 (yuv420p) at high quality.
