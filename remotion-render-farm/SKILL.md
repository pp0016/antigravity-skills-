---
name: remotion-render-farm
description: >
  Sets up a Remotion video render farm using GitHub Actions.
  Use this skill whenever the user wants to render a Remotion (React) video
  on GitHub Actions to save their laptop. Supports single video rendering,
  batch rendering for faceless channels (multiple compositions in parallel),
  and auto-merging of pre-recorded voiceover audio. Works with the
  faceless-craft-defaults and remotion-craft-skill for design values.
  Triggers on: "render remotion on github", "remotion render farm",
  "remotion github actions", "render video on cloud", "faceless video
  render", "batch render remotion".
---

# Remotion GitHub Actions Render Farm

This skill generates the infrastructure for rendering Remotion videos on GitHub Actions for free, keeping the user's laptop safe.

## Prerequisites
- A public GitHub repository (unlimited free Actions minutes)
- Remotion project initialized (`npx create-video@latest`)
- Audio file (voiceover) in the repo at `public/audio/voiceover.mp3` (optional)

When the user requests this setup in a Remotion project, create the following file:

## 1. `.github/workflows/render.yml`

Create this file exactly as follows:

```yaml
name: Remotion Render Farm

on:
  push:
    branches: [ "main" ]
    paths:
      - 'src/**'
      - 'public/**'
  workflow_dispatch:
    inputs:
      composition:
        description: "Composition name to render"
        required: true
        default: "MainVideo"
      output_name:
        description: "Output filename"
        required: true
        default: "out.mp4"
      quality:
        description: "CRF quality (lower = better, 0-51)"
        required: false
        default: "18"

jobs:
  render:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: "npm"

      - name: Install dependencies
        run: npm ci || npm install

      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Render Video
        run: |
          npx remotion render src/index.ts \
            ${{ github.event.inputs.composition || 'MainVideo' }} \
            ${{ github.event.inputs.output_name || 'out.mp4' }} \
            --codec h264 \
            --crf ${{ github.event.inputs.quality || '18' }}

      - name: Upload Video
        uses: actions/upload-artifact@v4
        with:
          name: remotion-video
          path: ${{ github.event.inputs.output_name || 'out.mp4' }}
          retention-days: 7
```

## 2. `.github/workflows/batch-render.yml` (Faceless Channel Batch Mode)

For faceless channels that need to render multiple videos at once, create this additional workflow:

```yaml
name: Faceless Batch Render

on:
  workflow_dispatch:
    inputs:
      compositions:
        description: "Comma-separated composition names (e.g. Ep01,Ep02,Ep03)"
        required: true
        default: "Ep01"

jobs:
  parse:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: |
          IFS=',' read -ra ITEMS <<< "${{ github.event.inputs.compositions }}"
          JSON="["
          for i in "${!ITEMS[@]}"; do
            [ $i -gt 0 ] && JSON+=","
            JSON+="\"${ITEMS[$i]}\""
          done
          JSON+="]"
          echo "matrix=${JSON}" >> $GITHUB_OUTPUT

  render:
    needs: parse
    runs-on: ubuntu-latest
    timeout-minutes: 30
    strategy:
      fail-fast: false
      matrix:
        composition: ${{ fromJson(needs.parse.outputs.matrix) }}
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: "npm"

      - name: Install dependencies
        run: npm ci || npm install

      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Render ${{ matrix.composition }}
        run: |
          npx remotion render src/index.ts \
            ${{ matrix.composition }} \
            ${{ matrix.composition }}.mp4 \
            --codec h264 --crf 18

      - name: Upload ${{ matrix.composition }}
        uses: actions/upload-artifact@v4
        with:
          name: ${{ matrix.composition }}
          path: ${{ matrix.composition }}.mp4
          retention-days: 7
```

## Guidance to provide the user

After generating the files, remind the user of the following:

1. Ensure the GitHub repository is set to **Public** to get unlimited free rendering minutes.
2. **Single render:** Actions tab → "Remotion Render Farm" → "Run workflow" → type composition name.
3. **Batch render:** Actions tab → "Faceless Batch Render" → type `Ep01,Ep02,Ep03` → each renders on its own machine in parallel.
4. **Audio:** Place your ElevenLabs voiceover at `public/audio/voiceover.mp3`. Reference it in your Remotion composition with `<Audio src={staticFile('audio/voiceover.mp3')} />`.
5. **Design defaults:** Use the `faceless-craft-defaults` skill for consistent color palettes, typography, and timing across all compositions.
6. **Quality:** CRF 18 is visually lossless. Lower = better quality but larger files. Range: 0 (lossless) to 51 (worst).
7. The final `.mp4` files will be available to download from workflow artifacts (kept for 7 days).
8. **CRITICAL:** GitHub Actions has a 6-hour timeout per job. For videos longer than ~10 minutes at 1080p, split into chunks using a matrix strategy (see the Manim render farm skill for the chunk-and-stitch pattern).
