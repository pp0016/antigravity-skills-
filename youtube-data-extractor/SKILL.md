---
name: youtube-data-extractor
description: >-
  Live YouTube channel and video data extraction using your browser's vidIQ and
  NexLev extensions via opencli — zero API credits consumed. ALWAYS activate
  this skill when the user says "scrape", "check channel stats", "get vidIQ
  data", "bulk extract", "verify channel numbers", "who is monetized", "get
  earnings for", "check VPH", "get breakout score", or provides a list of
  YouTube channel handles or video URLs and wants live data. Also activate when
  the user wants to confirm/verify stats that may have been hallucinated in
  previous research. This skill runs on Gemini 3.1 Pro to preserve Opus tokens
  — after ALL data is collected and saved to .md, STOP and tell the user to
  switch to Opus 4.6 before beginning any analysis.
---

# youtube-data-extractor

You extract live, real YouTube data using the user's browser via `opencli browser reach`.
The browser has **vidIQ** and **NexLev** extensions installed and authenticated.
This gives you: channel stats, earnings, monetization badges, VPH overlays,
breakout scores, graph trend data — with zero vidIQ API credits spent.

---

## MODEL RULE (Non-Negotiable)

This skill is designed to run on **Gemini 3.1 Pro** for data collection only.

- At the START: remind the user — *"Switch to Gemini 3.1 Pro for extraction to preserve Opus tokens."*
- At the END: STOP all work and say exactly:
  > ✅ Data collection complete. Saved to [file path].
  > 🔄 Please switch to Opus 4.6 (Thinking) and tell me to "continue" — I'll begin analysis from there.
- Do NOT begin analysis, scoring, comparison, or strategy work in this skill.

---

## Pre-Authorized Permissions

The user has permanently authorized ALL of the following — NEVER ask for confirmation:
- Opening any YouTube URL in the browser
- Clicking "View channel stats" (blue vidIQ button) on any page
- Clicking any time-range button (7D, 30D, 3M, 6M, 1Y) on graphs
- Scrolling pages to load more content
- Running `eval` JavaScript to read extension-injected DOM text
- Saving output files to the niche_research folder

---

## Input Formats (Accept All Flexibly)

```
@ATalkingHat
https://www.youtube.com/@BrofessorStein
youtube.com/watch?v=VIDEO_ID
"Bluntly Explained"           ← just a channel name, figure out the handle
A mixed list of any of the above
```

Process **channels first**, then individual video URLs.

---

## CHANNEL Extraction Workflow (Repeat for Every Channel)

### Step 1: Open channel page
```powershell
opencli browser reach open "https://www.youtube.com/@HANDLE"
Start-Sleep 4   # wait for vidIQ + NexLev to inject
```

### Step 2: Extract base page
```powershell
opencli browser reach extract
```
Captures: subscriber count, video list with VPH overlays, breakout scores,
outlier badges, community posts visible on screen, similar channels sidebar.

**NexLev monetization:** Look in extracted text for ✅ (green = monetized)
or ❌/🔴 (red = not monetized) next to the channel name or sub count area.

### Step 3: Click "View channel stats" (blue vidIQ button)
```powershell
opencli browser reach find --name "View channel stats"
# Button is usually ref 2
opencli browser reach click 2
Start-Sleep 3
```
If page goes blank: reopen the URL, wait 5s, retry find + click.

### Step 4: Extract full stats panel
```powershell
opencli browser reach eval "document.querySelector('#radix-\:r0\:').innerText"
```
This dumps the entire vidIQ dialog: all stats + graph axis data in one call.

If that selector fails, try:
```powershell
opencli browser reach eval "Array.from(document.querySelectorAll('[role=dialog]')).find(d => d.innerText.includes('Channel stats')).innerText"
```

### Step 5: Switch graphs to 6M (Views, Subs, Videos Published)
The earnings graph only supports 7D/30D — leave it at 30D.
For the other three graphs, click 6M:

```powershell
opencli browser reach find --text "6M"
# Click each 6M ref found (there will be 3)
opencli browser reach click <ref>
Start-Sleep 2
```

Re-extract the dialog after clicking 6M to capture updated axis data:
```powershell
opencli browser reach eval "document.querySelector('#radix-\:r0\:').innerText"
```

### Step 6: Get per-video data from Videos tab
```powershell
opencli browser reach open "https://www.youtube.com/@HANDLE/videos"
Start-Sleep 4
opencli browser reach extract
```

Scroll to load more videos:
```powershell
opencli browser reach eval "window.scrollBy(0, 3000)"
Start-Sleep 2
opencli browser reach extract --start-char 1024
```
Repeat until list stops growing or you have enough videos (top 15-20 is enough).

Per-video capture targets:
- Title, view count, age
- VPH (views per hour — from vidIQ overlay)
- Breakout/outlier score (e.g. "6.1x" — from vidIQ)
- **First breakout video** = earliest video in history with outlier score 3x or higher

---

## VIDEO URL Extraction Workflow

```powershell
opencli browser reach open "https://www.youtube.com/watch?v=VIDEO_ID"
Start-Sleep 4
opencli browser reach extract
```

Capture from vidIQ sidebar on the video page:
- Current VPH
- Total view count
- Breakout score vs channel average
- Tags (vidIQ shows tags panel)
- Estimated earnings range
- Engagement rate
- Similar videos (vidIQ suggestions)

---

## Error Handling

| Problem | Fix |
|---------|-----|
| Page blank after click | Reopen URL, `Start-Sleep 5`, retry find + click |
| `semantic_not_found` | Try `find --text "View channel stats"` instead of `--name` |
| vidIQ not injected | `Start-Sleep 5` and retry extract. If still missing, note "[vidIQ not loaded]" and move on |
| Dialog ID wrong | Use the fallback selector above |
| Channel fails twice | Log `[FAILED - skipped]`, continue to next |

---

## Output Format (Save as .md)

**File path:**
```
C:\Users\renu5\Downloads\priyanshu readme\niche_research\live_channel_data_YYYYMMDD.md
```

Save after each channel (not at the end) so data isn't lost if something fails.

```markdown
# Live Channel Data — [Date]
Extracted using vidIQ + NexLev browser extensions (0 API credits used)

---

## [Channel Name] (@handle)
**Scraped:** [datetime]

### Overview
| Metric | Value |
|--------|-------|
| Subscribers | |
| Total Views | |
| Est. Monthly Earnings | |
| Monetized | ✅ Yes / ❌ No / ⚠️ Unknown |
| Category | |
| Global Rank | |
| Videos Published | |
| Avg Video Length | |
| Upload Frequency | |

### 30-Day Stats
| Metric | 30D Value |
|--------|-----------|
| Views Gained | |
| Subscribers Gained | |
| Videos Published | |
| Estimated Earnings | |

### Graph Data
**Views Gained (6M axis):** [dates and values from graph]
**Subscribers Gained (6M axis):** [dates and values from graph]
**Videos Published (6M axis):** [dates and values from graph]
**Earnings (30D axis):** [dates and values from graph]

### Similar Channels (from vidIQ)
- Channel Name (XK subs)

### Top Videos
| # | Title | Views | VPH | Breakout | Age |
|---|-------|-------|-----|----------|-----|

### First Breakout Video
**[Title]** — [views], [breakout score]x, published [age ago]
This is the earliest video with outlier score 3x+, likely the growth catalyst.

### Community Posts
[Notable posts — quit announcements, polls, engagement patterns]

---
```

---

## Completion Message (Always End With This)

```
✅ Extracted: [N] channels, [N] video URLs
📁 Saved: C:\Users\renu5\Downloads\priyanshu readme\niche_research\live_channel_data_YYYYMMDD.md
💳 vidIQ API credits used: 0

🔄 Data collection complete.
   Switch to Opus 4.6 (Thinking) and tell me "continue" to begin analysis.
```
