<p align="center">
  <img src="public/assets/banner.png" width="100%" alt="Gemini Watch Banner" />
</p>

# Gemini Watch 👁️

**Gemini Watch** is a native, multimodal extension for the [Gemini CLI](https://github.com/google-gemini/gemini-cli) that gives the agent "eyes" to watch videos from YouTube, Vimeo, TikTok, or local files.

Instead of relying on heavy MCP servers or complex setups, `gemini-watch` provides a highly optimized pipeline that downloads videos with `yt-dlp`, extracts frames with `ffmpeg`, and transcribes audio natively using Gemini's multimodal capabilities. The Gemini CLI then natively loads these visual and audio cues directly into its multimodal context window to answer any question about the video.

## ✨ Features
* **Multimodal Visual & Audio Inputs:** Automatically extracts auto-scaled video frames and native audio tracks. It uses the CLI's `read_file` tool to feed both visuals and audio into Gemini's massive multimodal context window.
* **Multi-Platform Support:** Works flawlessly with YouTube, Vimeo, TikTok, Twitter/X, Twitch, and most `yt-dlp` compatible websites, as well as local video files (`.mp4`, `.mov`, `.mkv`, etc.).
* **Smart Native Fallback:** Automatically pulls native or auto-generated captions first. If unavailable, it extracts the audio track for Gemini to "hear" and transcribe natively—**no external API keys (Whisper/Groq) required.**
* **Denser Focused Zoom:** Supports focusing on specific timestamps (e.g. `--start 01:00 --end 01:30`) to extract frames at a higher density for detailed analysis of brief moments.
* **Pure Python Standard Library:** Requires **zero** external Python packages (no pip installs needed outside standard tools).
* **Setup Wizard:** Includes a built-in preflight checker (`setup.py`) to detect missing binaries in one command.

## 🛠️ Prerequisites

To use this extension, you must have **Python 3**, **FFmpeg**, and **yt-dlp** installed on your system.

### Install Dependencies:
* **macOS:**
  ```bash
  brew install ffmpeg yt-dlp
  ```
* **Windows (via Winget):**
  ```bash
  winget install Gyan.FFmpeg
  winget install yt-dlp.yt-dlp
  ```
* **Linux:**
  ```bash
  sudo apt install ffmpeg
  ```
  (And install `yt-dlp` via your package manager or pipx)

## 📦 Installation

You can install this extension directly into Gemini CLI using the following command (replace `<your-username>` with your actual GitHub username once published):

```bash
gemini extensions install https://github.com/sudoax0n/gemini-watch
```

*Note: If you have cloned this repository locally, you can link it instead:*
```bash
gemini extensions link ./gemini-watch
```

## 🚀 Setup & Config

Once installed, run the setup wizard to scaffold your environment and configuration files:

```bash
py scripts/setup.py
```

This creates a configuration directory at `~/.config/gemini-watch/` with a `.env` file. While you can still provide a Groq or OpenAI API key for legacy Whisper support, it is no longer required as Gemini now handles audio transcription natively.

## 💻 Usage

Drop a video link or local file path into your Gemini CLI session and ask it a question!

**Example Prompts:**
* *"What is happening in this video? [URL]"*
* *"Explain what the speaker is demonstrating at timestamp 02:40: [URL]"*
* *"Analyze the slide shown at the beginning of my local presentation: C:\Users\me\presentation.mp4"*

### CLI Commands (for development or direct execution):
```bash
# Check if binaries and config are ready
py scripts/setup.py --check

# Watch a video (URL or local file)
py scripts/watch.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Watch a focused section of a local file
py scripts/watch.py "C:\Users\me\clip.mp4" --start 00:30 --end 01:00
```

## 🧠 How it Works
1. When you ask Gemini CLI about a video, the agent reads `GEMINI.md`.
2. It executes `scripts/watch.py` with your URL/file path (and optional start/end timestamps).
3. The script downloads the video (if a URL) via `yt-dlp` and uses `ffmpeg` to extract auto-scaled JPEG frames and an audio track.
4. It fetches captions or falls back to providing the raw audio file for native transcription.
5. The script outputs a markdown report listing JPEGs and the audio path.
6. The Gemini agent uses the `read_file` tool to load all frames and the audio file in parallel into its multimodal context, allowing it to "watch" and "listen" to the video to synthesize a precise answer.

## 🤝 Socials
Follow me for more Gemini CLI tools and hacks:
* **X (Twitter):** [@beyondwudan](https://x.com/beyondwudan)
* **GitHub:** [@sudoax0n](https://github.com/sudoax0n)

## License
[MIT License](LICENSE)
