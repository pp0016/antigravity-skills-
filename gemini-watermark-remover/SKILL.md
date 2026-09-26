---
name: gemini-watermark-remover
description: >
  Expert instructions for removing Google Flow, Gemini, and Veo "sparkle" watermarks from images and videos using the `gwr` CLI tool.
---

# Gemini Watermark Remover Skill

This skill teaches how to use the `@pilio/gemini-watermark-remover` CLI tool (`gwr`) correctly, specifically addressing its hidden flags and quality issues on Windows.

## Setup / Installation on a New PC

If you are running this on a brand new PC, you must install the tool and its dependencies first:

1. **Install Node.js**: Download and install it from [nodejs.org](https://nodejs.org/).
2. **Install the Tool**: Open a terminal (Command Prompt or PowerShell) and run:
   `npm install -g @pilio/gemini-watermark-remover`
3. **Install Video Dependencies**: To allow video processing, you MUST install Playwright's browser engine by running:
   `npx playwright install chromium`

Once those three steps are done, the `gwr` command will be permanently available on that PC.

## Core Rules

1. **Always Force Low Confidence:** The `gwr` tool often fails video processing around 12% with a Chinese error about low confidence. You MUST append the hidden flag `--allow-low-confidence` to bypass this error on all video requests.
2. **Always Force High Quality:** By default, `gwr` compresses re-encoded video output heavily, causing noticeable quality loss. You MUST append `--video-bitrate-mbps 30` to preserve the original 1080p fidelity.
3. **Overwrite:** Use `--overwrite` to automatically replace existing files and prevent the tool from pausing to prompt the user.

## Command Template

To remove a watermark from a single video/image:
```powershell
gwr remove "C:\path\to\input.mp4" --output "C:\path\to\output_clean.mp4" --allow-low-confidence --video-bitrate-mbps 30 --overwrite
```

To remove watermarks from a whole directory:
```powershell
gwr remove "C:\path\to\input_dir" --out-dir "C:\path\to\output_dir" --allow-low-confidence --video-bitrate-mbps 30 --overwrite
```

## Troubleshooting
- If `gwr` throws a `playwright` browser executable error, run `npx playwright install chromium` first.
