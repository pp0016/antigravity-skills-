---
name: ffmpeg-render-farm
description: >
  Sets up an FFmpeg processing pipeline using GitHub Actions.
  Use this skill whenever the user wants to use FFmpeg to process videos (compress, stitch, convert) on GitHub instead of their laptop.
---

# FFmpeg GitHub Actions Cloud Processor

This skill instructs the agent on how to instantly generate a GitHub Actions workflow that acts as a free cloud FFmpeg processor.

When the user requests this setup, create the following file:

## 1. `.github/workflows/ffmpeg.yml`

Create this file exactly as follows:

```yaml
name: FFmpeg Cloud Processor

on:
  workflow_dispatch:
    inputs:
      ffmpeg_command:
        description: "The FFmpeg command to run (use in.mp4 and out.mp4)"
        required: true
        default: "-i in.mp4 -vf scale=1280:720 out.mp4"

jobs:
  process:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install FFmpeg
        run: sudo apt-get update && sudo apt-get install -y ffmpeg

      - name: Run FFmpeg
        run: ffmpeg ${{ github.event.inputs.ffmpeg_command }}
        
      - name: Upload Output
        uses: actions/upload-artifact@v4
        with:
          name: ffmpeg-output
          path: out.mp4
          retention-days: 7
```

## Guidance to provide the user
After generating the files, remind the user of the following:
1. They need to upload their source files (like `in.mp4` or a bunch of chunks) to the repository first.
2. They can trigger the processing manually from the GitHub Actions tab by clicking "Run workflow" and typing their custom FFmpeg command.
3. Make sure their FFmpeg command outputs to a file named `out.mp4` (or whatever path they specify in the artifact upload step).

