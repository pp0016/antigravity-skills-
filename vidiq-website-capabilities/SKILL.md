---
name: vidiq-website-capabilities
description: >
  Complete reference for vidIQ's website interface (app.vidiq.com) — the AI Coach
  chat, Scriptwriter with tone matching, thumbnail generator, and all other tools
  accessible through the browser. Use this skill whenever you need to know what
  vidIQ's website can do, what to recommend the user paste into vidIQ's web
  interface, what features require a connected channel, or when crafting prompts
  for the vidIQ AI Coach. This is the WEBSITE — not the MCP API. For MCP API
  tools, use vidiq-youtube-creator. For routing between vidIQ and NexLev, use
  vidiq-nexlev-router. Triggers on: "vidIQ website", "vidIQ AI Coach", "paste
  into vidIQ", "vidIQ scriptwriter", "vidIQ tone", "match reference video",
  "vidIQ thumbnail", "what can vidIQ do", "vidIQ features", "vidIQ web app",
  "app.vidiq.com", "vidIQ credits", "connect channel vidIQ", "vidIQ daily ideas",
  "vidIQ compose video", "clone my voice vidIQ", "vidIQ B-roll", "vidIQ AI Shorts".
---

# vidIQ Website Capabilities

This skill documents what the vidIQ website (app.vidiq.com) can do when accessed
through a browser. It exists because the agent often underestimates or
misrepresents what vidIQ's web interface is capable of — particularly around
scriptwriting, tone matching, thumbnail analysis, and video generation. This
reference prevents the agent from telling the user "vidIQ can't do that" when
it actually can.

This skill covers the **website only**. For the MCP API (programmatic access
from agents), see `vidiq-youtube-creator`. For routing decisions between vidIQ
and NexLev, see `vidiq-nexlev-router`.

## How the Website Is Structured

The main interface at app.vidiq.com has:

### Left Sidebar Navigation
- **New Chat** — starts a fresh AI Coach conversation
- **Feed** — content feed / trending
- **Optimize** — optimization recommendations
- **Research** — research tools
- **More** — expands the full feature menu (see below)
- **Upgrade** — plan upgrade

### The "More" Menu (Full Feature List)

When you click "More" in the sidebar, these features are listed:

| Feature | What It Does | Requires Channel? |
|---|---|---|
| **Thumbnails** | Generate, score, and analyze thumbnails | Partially — generation works without, personalized scoring needs channel |
| **Clipping** | AI clip maker — converts long-form to Shorts | Yes — needs your videos |
| **Competitors** | Track and audit competitor channels | Yes — needs your channel for context |
| **Create** | General content creation hub | No |
| **Daily Ideas** | Fresh personalized video ideas each day with view prediction scores | Yes — personalized to your niche |
| **Calendar** | 30-day content calendar planning | Partially |
| **Generate** | General AI generation tools | No |
| **Learn** | Educational resources and tutorials | No |
| **Script Writer** | Full AI scriptwriter with tone matching (see detailed section below) | No — works without channel |
| **Subscribers** | Subscriber analytics and insights | Yes |
| **Title Generator** | AI-powered CTR-optimized title suggestions | No |
| **Video Generator** | End-to-end AI video generation | No |

### Main Chat Interface Quick Actions

The main page ("Where should we start?") shows quick-action buttons:

**Row 1:** Audit my channel · Find niche · New thumbnail · Video ideas · Make clips · AI Shorts
**Row 2:** Find B-roll · AI voiceover · Clone my voice · Compose video

### Chat Input Settings

The chat input box has:
- **Topic field** — "What's your video about?"
- **Format toggle** — Long video (default)
- **Duration** — 15 mins (default, adjustable)
- **Tone** — Optional (see Scriptwriter section below)
- **Credits indicator** — Shows cost (e.g., ✦ 15)
- **Mode selector** — Regular / Deep Thinking
- **Attachment** — Can attach images for analysis
- **Voice input** — Microphone button for voice prompts

## Scriptwriter — Detailed Breakdown

The Scriptwriter is one of vidIQ's most powerful features. When you enter a
video topic and click the Tone button, three options appear:

### 1. Match Reference Video
Opens a modal: "Choose a video to match its tone." Has three tabs:
- **Your Videos** — requires connected channel
- **For You** — personalized recommendations (requires channel)
- **Trending** — currently trending videos (works WITHOUT a channel)
- **Search bar** — search for any video by keyword

This lets you select an existing YouTube video, and vidIQ will analyze its tone,
pacing, and style, then write your script in that same voice. This is the
competitor-analysis-driven scriptwriting capability — it can study a
competitor's video and replicate the tone.

### 2. Quick Preset Tones
Pre-built tone presets you can select with one click. Common presets include
styles like casual, informative, persuasive, storytelling, high-energy, etc.

### 3. Custom Tone
A text field where you describe your desired tone in free text.
Placeholder: "Mr. Beast Style, British humor, etc..."
Examples shown: "Like Mr. Beast", "British humor", "David Attenborough style",
"Energetic and fun"
Has a "Use This Tone" button to apply.

### Scriptwriter Output
The scriptwriter generates structured scripts including:
- Hook / intro
- Talking points with transitions
- Call-to-action sections
- Closing

### Credit Cost
Script writing costs approximately **1 credit per minute** of script length.
A 15-minute script costs ~15 credits.

## Correction: What vidIQ CAN Do (Previously Understated)

The agent has previously claimed vidIQ cannot do some of these. Setting the
record straight:

| Capability | Verdict | Details |
|---|---|---|
| Write full scripts | ✅ CAN DO | Scriptwriter generates complete scripts with hooks, body, CTAs |
| Match competitor video tone | ✅ CAN DO | "Match Reference Video" analyzes a video and replicates its tone |
| Analyze thumbnails precisely | ✅ CAN DO | Thumbnail scoring, competitor thumbnail analysis, design recommendations |
| Generate thumbnails | ✅ CAN DO | AI-powered thumbnail generation |
| Clone your voice | ✅ CAN DO | Voice cloning from audio sample for AI voiceover |
| Generate AI voiceover | ✅ CAN DO | Text-to-speech with multiple voice options |
| Find B-roll | ✅ CAN DO | B-roll discovery and suggestions |
| Generate AI Shorts | ✅ CAN DO | Automated short-form content generation |
| Compose full videos | ✅ CAN DO | End-to-end video composition |
| Make clips from long-form | ✅ CAN DO | AI identifies best moments and auto-clips |
| Deep competitor analysis | ✅ CAN DO | Channel audit, strategy breakdown, content gap analysis |
| Transcript-based script analysis | ✅ CAN DO | Can pull transcripts and analyze structure |

## What Requires a Connected Channel

Some features are locked or limited until you connect a YouTube channel via
Google OAuth:

**Fully locked without channel:**
- Clipping (needs your videos to clip)
- Subscribers analytics
- "Your Videos" tab in Match Reference Video
- "For You" tab in Match Reference Video
- Audit my channel
- Daily Ideas (personalized)
- Competitor tracking (needs your channel as baseline)

**Works WITHOUT a channel:**
- AI Coach chat (general research, niche analysis, competitor lookup)
- Script Writer (full functionality including Custom Tone and Quick Presets)
- Match Reference Video → Trending tab and Search bar
- Title Generator
- Thumbnail Generator
- Find B-roll
- AI voiceover
- Video Generator
- Find niche
- New thumbnail
- Calendar (basic)
- Generate
- Learn

## Features We Do NOT Use

Based on the user's workflow, these vidIQ features are excluded:
- **Video Generator** — user has own stack (Remotion, Hyperframes, FFmpeg)
- **Clipping** — not part of current workflow

Everything else is available and useful once the channel is connected.

## Credit System on the Website

| Action | Credits |
|---|---|
| AI Coach message (Regular) | ~10 |
| AI Coach message (Deep Thinking) | Higher (varies) |
| Script writing | ~1 per minute of script |
| Title generation (up to 3) | 3 |
| Description generation | 1 |
| Thumbnail generation/edit | 22 |
| AI Shorts generation (per sec) | 20 |
| Clipping (per min input) | 9 |

The AI Coach batching trick: one AI Coach message costs 10 credits regardless
of how long or complex the prompt is. A single well-crafted prompt that asks
5 questions costs the same as one that asks 1 question. This is why we craft
detailed prompts to paste in — it maximizes value per credit.

## How This Skill Relates to Other Skills

| Skill | What It Covers | When to Use |
|---|---|---|
| **vidiq-website-capabilities** (this) | Browser interface at app.vidiq.com | When crafting prompts to paste into vidIQ web, or when needing to know what the website can do |
| **vidiq-youtube-creator** | MCP API tools (programmatic) | When calling vidIQ tools directly from the agent via MCP |
| **vidiq-nexlev-router** | Routing between vidIQ and NexLev | When deciding which platform to use for a specific task |

## Workflow Integration

When the user wants to use vidIQ's website for their faceless channel workflow:

1. **Research phase** → Use AI Coach chat with detailed prompts (10 credits
   each, unlimited complexity per prompt)
2. **Scriptwriting phase** → Use Scriptwriter with "Match Reference Video"
   to study competitors, then generate scripts in the same tone
3. **Thumbnail phase** → Use thumbnail generator and scorer to analyze
   competitor thumbnails and create optimized ones
4. **SEO phase** → Use the AI Coach for keyword research, title optimization,
   description templates
5. **Post-upload** → Use channel audit, competitor tracking, daily ideas for
   ongoing optimization
