# SRT Whiteboard Animation Skill (English Version)

Transform SRT subtitles into narrative-driven whiteboard hand-drawn animation videos. This pipeline combines **region-based mask orchestration** with **continuous stream stroke rendering**: each element is drawn in sync with the spoken voiceover, with the pen tip gliding along contours depositing ink first, then washing with color, and finally exporting clean H.264 MP4 videos.

Perfect for educational explainers, YouTube video essays, storytelling narrations, online courses, and book summaries on warm vintage paper textures.

## Example Output

**Scene: Monkey Mountain Banana Snatch** — Following the subtitle narrative, the mountain setup and baby monkey are drawn first, followed by the big monkey rushing in to snatch the banana, and finally the reacting children.

![Demo](examples/scene-01-monkey-mountain-stream.gif)

Original Line Art: [View PNG](examples/scene-01-monkey-mountain.png).

## Core Capabilities

- **SRT Subtitle Parsing:** Automatically clusters voiceover subtitles into optimal 25–35 second scenes.
- **Narrative Storyboard Planning:** Plans visual composition before generating images, ensuring every scene conveys one core concept.
- **Semantic Drawing Order:** Draws elements according to the flow of the spoken story rather than arbitrary screen coordinates.
- **Precision Annotation Management:** Manages element boundaries, start times, durations, subtitle bindings, and overlap occlusion protection via clean JSON (`annotation.json`).
- **Continuous Stream Stroke Rendering:** The pen tip moves continuously: first laying down line art (`ink`), then applying color (`color`).
- **Zero-Install Local Visual Editor:** Interactive browser tool (`assets/preview.html`) to drag bounding boxes, adjust timings, and preview proxy reveals without running a server.
- **High-Quality Video Export:** Renders individual scenes to MP4 and stitches multi-scene videos losslessly with zero quality degradation.

## Workflow

1. Parse SRT subtitles into suggested scene cuts.
2. Confirm storyboard strategy and generate minimalist line-art illustrations.
3. Create semantic element annotations and review in the visual editor.
4. Generate static preview images to verify bounding boxes and drawing directions.
5. Fine-tune regions, timings, and subtitles in the visual editor.
6. Render individual scene MP4 videos via CLI.
7. Merge all scenes into a final complete MP4 video.

## Visual Design Standards

- **Paper Background:** Warm vintage beige (`#F5EBD7`). The renderer samples corners from the source image to eliminate pure white edges.
- **Linework:** Deep charcoal sketch lines with subtle conceptual accent touches in Red, Orange, or Blue.
- **Aesthetic:** Minimalist hand-drawn doodle style with generous negative space.
- **No Embedded Text:** The source illustration must not contain text or typography; subtitles and narration carry the spoken message.

## Quick Start

### 1. Check or Setup Dependencies
```bash
python scripts/prepare_env.py --check
python scripts/prepare_env.py
```
Required Python packages: `opencv-python`, `numpy`, `av`, `Pillow`.

### 2. Parse Subtitles & Plan Scenes
```bash
python scripts/parse_srt.py voiceover.srt --target-sec 30 --min-sec 25 --max-sec 35
```

### 3. Generate Static Bounding Box Preview
```bash
python scripts/render_annotation_preview.py scene-01.png scene-01.annotation.json preview.png
```

### 4. Interactive Visual Editor
Open `assets/preview.html` in Chrome or Edge. Click **Open Folder…** to select your scene folder. Drag bounding boxes, adjust start/end times, edit subtitles, and click **Save Scene**.

### 5. Render Scene Animation
```bash
python scripts/render_stream_whiteboard.py scene-01.png scene-01.annotation.json scene-01.mp4 assets/drawing-hand.png \
  --ink-path grid --color-fill contour-wipe --fps 60 --cap-long-edge 1080
```

### 6. Concatenate Scenes
```bash
python scripts/merge_scenes.py --inputs scene-01.mp4 scene-02.mp4 scene-03.mp4 --output final.mp4
```

## Repository Structure

```text
srt-whiteboard-animation/
├── SKILL.md                         # Complete agent workflow and specifications
├── README.md                        # Documentation and usage guide
├── LICENSE                          # MIT License
├── assets/
│   ├── drawing-hand.png             # Hand drawing asset
│   └── preview.html                 # Interactive visual annotation editor
├── examples/                        # Demonstration assets and sample scene
├── scripts/
│   ├── parse_srt.py                 # Subtitle parsing and scene clustering
│   ├── prepare_env.py               # Dependency checking and venv setup
│   ├── render_annotation_preview.py # Static region preview generator
│   ├── render_stream_whiteboard.py  # Integrated scene whiteboard renderer
│   ├── stream_render.py             # Core stream-drawing engine
│   └── merge_scenes.py              # Lossless multi-scene video merger
└── agents/
    └── openai.yaml                  # Agent metadata configuration
```

## License

MIT License. See [LICENSE](LICENSE) for details.
