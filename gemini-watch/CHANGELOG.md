# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-05-17
### Added
- **Native Multimodal Audio**: Migrated transcription fallback from Whisper API to Gemini-native audio processing. The extension now extracts audio and provides it directly to the model when captions are missing.
- **Sandbox Compatibility**: Updated working directory logic to respect `GEMINI_PROJECT_TMP`, ensuring frames and audio are accessible within the agent's sandbox.

### Changed
- **Simplified Setup**: Removed mandatory Whisper API key requirements. `setup.py` now passes as long as system binaries are present.
- **Improved Instructions**: Rewrote `GEMINI.md` to guide the agent on parallel multimodal reading (visuals + audio).

## [2.0.0] - 2026-05-17
### Added
- **Multimodal Video Capabilities**: Automatically extracts auto-scaled JPEG frames using `ffmpeg` to give the Gemini CLI native "eyes" to watch video files.
- **Multi-Platform Support**: Replaced the YouTube-only parser with `yt-dlp`, allowing you to analyze video links from YouTube, Vimeo, TikTok, Twitch, Twitter/X, and more, as well as local video files (`.mp4`, `.mov`, etc.).
- **Smart Transcription Fallbacks**: Pulls native captions first. If captions are unavailable, it converts the audio track and transcribes it via the Whisper API (supporting Groq for ultra-fast, cheap transcriptions, and OpenAI as a fallback).
- **Interactive Setup Wizard**: Added `scripts/setup.py` to seamlessly scaffold configuration files and preflight check missing dependencies in a single command.
- **Windows Integration Fallbacks**: Automatically maps local Python Scripts directory paths at runtime on Windows, preventing path-not-found issues with `yt-dlp` or `ffmpeg`.

### Changed
- Replaced the `youtube-transcript-api` python package with standard-library Python scripts and system binaries, resulting in **zero** external pip dependencies.
- Completely rewrote `GEMINI.md` to instruct the Gemini agent on how to use `read_file` to load the JPEGs in parallel into its multimodal context.

## [1.1.0] - 2026-05-02
### Added
- **Titanium Parser**: Robust Regex engine to flawlessly extract video IDs from any URL format (Shorts, mobile links, query parameters).
- **Smart Caching**: Automatically saves large transcripts to local `.txt` files to bypass CLI console truncation limits.
- **Auto-Cleanup**: Automatically deletes cached transcripts older than 7 days to keep your system clean.

### Fixed
- Fixed an issue where YouTube Shorts URLs would crash the script due to illegal filename characters.
- Fixed a bug where a failed fetch would generate a useless error file.
- Removed artificial console truncation and alarming warnings, opting for a clean data dump.

## [1.0.0] - 2026-04-29
### Added
- Initial release of **Gemini Watch**.
- Native transcription engine using `youtube-transcript-api`.
- Real-time **Timestamp** formatting (`[MM:SS]`) for precise navigation.
- **Metadata Extraction** (Title and Channel) for instant context.
- Auto-dependency installation logic for zero-friction setup.
- Multi-language support with automatic translation fallback.
- Comprehensive `README.md` and `LICENSE`.
- Gemini-native `GEMINI.md` instruction set.
