---
name: gemini-watch
description: Gives the agent eyes to watch videos from YouTube, Vimeo, TikTok, or local files by extracting frames and audio.
---

# Gemini Watch Extension

This extension gives Gemini CLI "eyes" to watch video inputs (URLs or local paths) natively. It downloads videos with `yt-dlp`, extracts frames with `ffmpeg`, and transcribes audio via captions or Whisper. It then presents these frames and transcripts so you can analyze the video.

## Step 0 — Setup preflight (runs every invocation)
Before running `/gemini-watch`, verify dependencies and API keys:
```bash
py scripts/setup.py --check
```
* **Exit 0 (Success):** Proceed to Step 1 silently (do not announce setup is complete).
* **Exit 2 (Missing binaries like ffmpeg, ffprobe, yt-dlp):** Instruct the user to run the installer: `py scripts/setup.py`.
* **Exit 3 (Missing Whisper key):** Run the installer to scaffold the dotenv file, then ask the user for a **Groq API Key** (preferred — console.groq.com/keys) or **OpenAI API Key** (platform.openai.com/api-keys) and write it into `~/.config/gemini-watch/.env` as `GROQ_API_KEY=...` or `OPENAI_API_KEY=...`.
* **Exit 4 (Both missing):** Run the installer, then ask the user for a key.

## Step 1 — Parse Input
Separate the video source (URL or path) from the user's question.

## Step 2 — Run the Watch Script
Invoke the watch script passing the source verbatim:
```bash
py scripts/watch.py "<source>"
```

### Useful Flags:
* `--start T` / `--end T` — Zoom into a section. Accepts `SS`, `MM:SS`, or `HH:MM:SS`. Auto-fps will scale denser for focused sections.
* `--max-frames N` — Lower the cap for a tighter token budget (default 80, max 100).
* `--resolution W` — Frame width in pixels (default 512; increase to 1024 only if reading small on-screen text).
* `--no-whisper` — Disable Whisper fallback.
* `--whisper groq|openai` — Force a specific backend.

## Step 3 — Read the Frames & Audio
The watch script outputs a list of JPEG frame paths and an optional audio file path.
**Use the `read_file` tool to read all of these JPEGs and the audio file in parallel.** 
* **Visuals:** Reading JPEGs allows you to see the video content natively.
* **Audio:** If a transcript is missing but an `audio.mp3` file is provided, read it natively to listen or transcribe the content yourself.

Do not omit any frames or the audio file; you must see and hear the video to answer grounded questions.

## Step 4 — Answer the User
Answer the user's questions or summarize the video, combining the visual evidence from the frames (using their timestamps) and the audio/transcript. Point the user to exact moments using `[MM:SS]` timestamps.

## Step 5 — Clean Up
The script prints the working directory at the end: `Work dir: <path>`. If the user is done with their queries and won't ask follow-ups, delete it using `Remove-Item -Recurse -Force "<path>"` (or `rm -rf "<path>"` if in a POSIX shell).

## Recommended limits
* Target videos under 10 minutes for optimal accuracy.
* For long videos (>10 mins), the coverage is sparse. Offer the user to run focused with `--start` and `--end` to target the exact section they care about.

