---
name: manim-render-farm
description: >
  Sets up a distributed 50-machine Manim video render farm using GitHub Actions.
  Use this skill whenever the user asks to "setup manim github actions", "build manim render farm",
  "render manim video fast", or "render multiple videos on github".
---

# Manim GitHub Actions Render Farm

This skill instructs the agent on how to instantly generate the infrastructure files for a distributed 50-machine Manim render farm using GitHub Actions. 

When the user requests this setup, you must create two files for them:

## 1. `.github/workflows/render.yml`

Create this file exactly as follows:

```yaml
name: Distributed Manim Render Farm

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  render_chunk:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        chunk: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa

      - name: Install Python Dependencies
        run: pip install -r requirements.txt

      - name: Set Chunk ID
        run: echo "CHUNK_ID=$(printf '%02d' ${{ matrix.chunk }})" >> $GITHUB_ENV

      - name: Render Chunk ${{ matrix.chunk }}
        run: |
          START_ANIM=${{ matrix.chunk }}
          END_ANIM=$(( ${{ matrix.chunk }} + 1 ))
          manim -qm -n $START_ANIM,$END_ANIM main.py MainScene --format mp4 -o chunk_${{ env.CHUNK_ID }}.mp4

      - name: Upload Chunk Artifact
        uses: actions/upload-artifact@v4
        with:
          name: chunk_${{ env.CHUNK_ID }}
          path: media/videos/**/chunk_${{ env.CHUNK_ID }}.mp4
          retention-days: 1

  stitch:
    needs: render_chunk
    runs-on: ubuntu-latest
    steps:
      - name: Download all chunks
        uses: actions/download-artifact@v4
        with:
          path: chunks_dir

      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Generate concat inputs.txt
        run: |
          > inputs.txt
          for i in {0..49}; do
            CHUNK_ID=$(printf "%02d" $i)
            FILE=$(find chunks_dir/chunk_$CHUNK_ID -name "chunk_$CHUNK_ID.mp4" | head -n 1)
            if [ -z "$FILE" ]; then echo "Error: Could not find chunk_$CHUNK_ID.mp4!"; exit 1; fi
            echo "file '$FILE'" >> inputs.txt
          done

      - name: Stitch video chunks
        run: ffmpeg -f concat -safe 0 -i inputs.txt -c copy final_video.mp4

      - name: Upload Final Video
        uses: actions/upload-artifact@v4
        with:
          name: final_video
          path: final_video.mp4
          retention-days: 7
```

## 2. `requirements.txt`

Create this file exactly as follows:

```text
manim==0.21.0
```

## Guidance to provide the user
After generating the files, remind the user of the following:
1. Ensure the GitHub repository is set to **Public** to get unlimited free rendering minutes and bypass the 500MB storage limit.
2. The Manim script must be named `main.py` and contain a class named `MainScene` (or they must edit the YAML to match their actual filenames).
3. Push to the `main` branch to automatically trigger the 50 machines in the cloud.
4. **CRITICAL RULE**: Do NOT use `manim-voiceover` with offline TTS engines like `pyttsx3` or `gTTS`. They sound generic and cause headless Ubuntu crashes. Always instruct the user to handle audio separately using high-quality tools like ElevenLabs.
