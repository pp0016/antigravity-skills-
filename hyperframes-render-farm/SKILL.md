---
name: hyperframes-render-farm
description: >
  Sets up a HyperFrames video render farm using GitHub Actions.
  Use this skill whenever the user wants to render HyperFrames (HTML/CSS/JS)
  videos on GitHub Actions instead of their laptop. Perfect for faceless
  YouTube Shorts and quick explainer clips. Triggers on: "render hyperframes
  on github", "hyperframes render farm", "hyperframes github actions",
  "render shorts on cloud", "hyperframes cloud render".
---

# HyperFrames GitHub Actions Render Farm

This skill generates the infrastructure to render HyperFrames video compositions on GitHub Actions for free, keeping the user's laptop safe from heavy processing.

## Prerequisites
- A public GitHub repository (for unlimited free Actions minutes)
- HyperFrames project initialized (`npx hyperframes init my-video`)
- Audio file (voiceover) already in the repo as `audio/voiceover.mp3`

When the user requests this setup, create the following file:

## 1. `.github/workflows/hyperframes-render.yml`

Create this file exactly as follows:

```yaml
name: HyperFrames Render Farm

on:
  push:
    branches: [ "main" ]
    paths:
      - 'compositions/**'
      - 'src/**'
      - '*.html'
  workflow_dispatch:
    inputs:
      project_dir:
        description: "Project directory to render (relative path)"
        required: true
        default: "."
      output_name:
        description: "Output filename"
        required: true
        default: "output.mp4"
      resolution:
        description: "Resolution (e.g. 1920x1080 or 1080x1920 for Shorts)"
        required: true
        default: "1080x1920"

jobs:
  render:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "22"
          cache: "npm"

      - name: Install dependencies
        working-directory: ${{ github.event.inputs.project_dir || '.' }}
        run: npm ci || npm install

      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Install HyperFrames CLI
        run: npm install -g hyperframes

      - name: Render Video
        working-directory: ${{ github.event.inputs.project_dir || '.' }}
        run: |
          npx hyperframes render \
            --output ${{ github.event.inputs.output_name || 'output.mp4' }} \
            --resolution ${{ github.event.inputs.resolution || '1080x1920' }}

      - name: Merge Audio (if exists)
        working-directory: ${{ github.event.inputs.project_dir || '.' }}
        run: |
          if [ -f "audio/voiceover.mp3" ]; then
            ffmpeg -i ${{ github.event.inputs.output_name || 'output.mp4' }} \
                   -i audio/voiceover.mp3 \
                   -c:v copy -c:a aac -shortest \
                   final_${{ github.event.inputs.output_name || 'output.mp4' }}
            mv final_${{ github.event.inputs.output_name || 'output.mp4' }} \
               ${{ github.event.inputs.output_name || 'output.mp4' }}
          fi

      - name: Upload Video
        uses: actions/upload-artifact@v4
        with:
          name: hyperframes-video
          path: ${{ github.event.inputs.project_dir || '.' }}/${{ github.event.inputs.output_name || 'output.mp4' }}
          retention-days: 7

  render-batch:
    if: github.event_name == 'push'
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        composition: [short-01, short-02, short-03, short-04, short-05]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "22"

      - name: Install dependencies
        run: npm ci || npm install

      - name: Install FFmpeg & HyperFrames
        run: |
          sudo apt-get update && sudo apt-get install -y ffmpeg
          npm install -g hyperframes

      - name: Render ${{ matrix.composition }}
        run: |
          if [ -d "compositions/${{ matrix.composition }}" ]; then
            cd compositions/${{ matrix.composition }}
            npx hyperframes render --output ${{ matrix.composition }}.mp4 --resolution 1080x1920
          fi
        continue-on-error: true

      - name: Upload Short
        if: success()
        uses: actions/upload-artifact@v4
        with:
          name: ${{ matrix.composition }}
          path: compositions/${{ matrix.composition }}/${{ matrix.composition }}.mp4
          retention-days: 7
```

## 2. Recommended Project Structure

Tell the user to organize their repo like this:

```
my-faceless-shorts/
├── .github/workflows/hyperframes-render.yml
├── compositions/
│   ├── short-01/
│   │   ├── index.html
│   │   ├── style.css
│   │   └── audio/voiceover.mp3
│   ├── short-02/
│   │   ├── index.html
│   │   └── audio/voiceover.mp3
│   └── ...
├── package.json
└── README.md
```

## Guidance to provide the user

After generating the files, remind the user of the following:

1. Ensure the GitHub repository is set to **Public** for unlimited free Actions minutes.
2. **Manual trigger:** Go to Actions tab → "HyperFrames Render Farm" → "Run workflow" → set resolution to `1080x1920` for Shorts or `1920x1080` for landscape.
3. **Batch mode:** On push to main, it auto-renders ALL compositions in the `compositions/` folder across parallel machines (up to 5 by default — edit the matrix to add more).
4. **Audio:** Drop your ElevenLabs voiceover as `audio/voiceover.mp3` inside each composition folder. The workflow auto-merges it.
5. Download the rendered `.mp4` from the workflow artifacts (kept for 7 days).
6. **CRITICAL:** This is CPU-only rendering. HyperFrames works great on CPU. Do NOT try to run GPU-dependent tools (SadTalker, LivePortrait) with this workflow — they will fail.
