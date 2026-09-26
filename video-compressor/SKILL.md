---
name: video-compressor
description: How to compress videos, reduce video file sizes, and fix missing codec errors for Windows. Make sure to use this skill whenever the user mentions compressing a video, reducing video size, or making a video smaller.
---

# Video Compressor Skill

This skill expertly compresses videos using FFmpeg, achieving massive file size reductions (up to 90%) while ensuring the video plays perfectly on Windows out of the box.

## Core Rules
1. **Universal Windows Compatibility**: ALWAYS use the **H.264 (libx264)** codec. Do NOT use H.265 (HEVC) because it requires a paid Microsoft Store extension and causes the `0xc00d5212` missing codec error for the user. H.264 guarantees it plays instantly everywhere.
2. **Standard Compression (15% Quality Drop)**: Use `-crf 28` as the absolute default for all compression requests. This drops quality by roughly 15%, which is visually almost identical to the original, but slashes the file size drastically. 
3. **Audio**: Use AAC audio (`-c:a aac`) at `128k` bitrate.
4. **Preset**: Always use `-preset fast` for speed and efficiency.
5. **Always Report Sizes**: Before and after compressing, you MUST check and report the exact file sizes (in MB) and the percentage of space saved. Do not explain how the quality was impacted; just report the numbers.

## FFmpeg Command Template
```powershell
ffmpeg -y -i "C:\path\to\original.mp4" -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k "C:\path\to\compressed_output.mp4"
```

## Workflow
1. Check the original file size using `dir` or `ffprobe`.
2. Run the FFmpeg command asynchronously.
3. Once completed, check the new file size.
4. Report the original size, the new size, and the percentage reduction to the user.
