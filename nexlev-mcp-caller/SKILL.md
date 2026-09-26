---
name: nexlev-mcp-caller
description: >-
  Calls NexLev MCP tools directly via Python + mcp SDK when the built-in
  call_mcp_tool fails or NexLev server is not found. ALWAYS activate when
  the user says "use nexlev", "call nexlev", "nexlev mcp", "get channel
  analytics via nexlev", "check monetization via nexlev", "find similar
  channels", "nexlev not working", "nexlev auth", or "fix nexlev". Also
  activate when call_mcp_tool returns "server name nexlev not found".
  Contains ready-to-run Python scripts in the scripts/ subfolder —
  NEVER rewrite these scripts, just import and call them.
---

# nexlev-mcp-caller

Call NexLev MCP tools directly using pre-built Python scripts when the
built-in `call_mcp_tool` tool fails (returns "server not found" or errors).

---

## CRITICAL: DO NOT REWRITE THE SCRIPTS

The `scripts/` folder contains production-ready Python files. You MUST:
1. Use them AS-IS — do not recreate or rewrite them
2. Call them via `python <script_path> <tool_name> <args_file>`
3. Only create small temporary JSON arg files when needed

---

## Quick Start — How To Call Any NexLev Tool

### Step 1: Create a JSON args file (temp)

```powershell
# Write args to a temp file (avoids PowerShell JSON mangling)
Set-Content -Path "$env:TEMP\nexlev_args.json" -Value '{"username": "EverythingProfessor"}'
```

### Step 2: Run the caller script

```powershell
python "C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\scripts\nexlev_call.py" youtube_channel_about "$env:TEMP\nexlev_args.json"
```

### Step 3: Parse the JSON output

The script prints raw JSON text from NexLev. Parse it for your report.

---

## For Multiple Tool Calls (Batch Mode)

Use the batch script to call multiple tools in one run:

```powershell
# Create a batch config file
Set-Content -Path "$env:TEMP\nexlev_batch.json" -Value '[
  {"tool": "youtube_channel_about", "args": {"username": "SomeChannel"}},
  {"tool": "youtube_channel_videos", "args": {"channel_id": "UC...", "sort_by": "popular"}},
  {"tool": "check_channel_monetization", "args": {"channelId": "UC..."}}
]'

python "C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\scripts\nexlev_batch.py" "$env:TEMP\nexlev_batch.json"
```

---

## Available Scripts

| Script | Purpose |
|--------|---------|
| `scripts/nexlev_call.py` | Call a single NexLev tool by name + args file |
| `scripts/nexlev_batch.py` | Call multiple NexLev tools sequentially |
| `scripts/nexlev_kill_stale.py` | Kill stale mcp-remote processes blocking port 28085 |

---

## NexLev Rate Limits (Free Plan) — CHECK BEFORE CALLING

| Limit | Tools |
|-------|-------|
| **50/day** | youtube_search, youtube_channel_videos, youtube_channel_shorts, youtube_channel_playlists, youtube_channel_about |
| **20/day** | latest_discovered_faceless_niches, search_youtube_suggested_videos, search_viral_videos_small_channels, faceless_outliers_videos |
| **10/day** | channel_resolver, search_niche_finder_channels, search_videos, youtube_video_details, youtube_video_comments, youtube_channel_outliers, find_long_form_channels, find_shorts_channels, get_niche_finder_categories, get_niche_finder_formats |
| **5/day** | get_similar_channels, check_faceless_channel, get_similar_videos, get_video_transcript, get_bulk_video_transcripts, get_video_subtitle, get_bulk_video_subtitles, get_similar_thumbnails, get_channel_analytics, get_daily_analytics, get_short_vs_long_views, get_geography_revenue, get_batch_channel_metrics, check_channel_monetization, check_video_monetization, get_video_rpm, get_niche_overview, get_niche_finder_tags, get_channel_promotions |
| **2/day** | get_channel_promotions_realtime |
| **1/day** | watch_youtube_video_and_ask, watch_instagram_video_and_ask, watch_tiktok_video_and_ask |
| **0/day (Paid only)** | get_content_owner, search_cms_networks, swipefile tools, my_channel tools, generate/edit_thumbnail |

### Rate Limit Strategy
1. **ALWAYS start with 50/day tools** (youtube_channel_about → youtube_channel_videos)
2. **Use 5/day tools sparingly** — ask the user before burning get_channel_analytics
3. **If RATE LIMIT EXCEEDED** — tell the user which tool, suggest waiting 24h or enabling NexLev usage credits

### Full rate limit reference file
`C:\Users\renu5\Downloads\Nexlev's official rate-limt mcp.md`

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| `server name nexlev not found` from call_mcp_tool | Use this skill's Python scripts instead |
| `RATE LIMIT EXCEEDED` | Check table above. Wait 24h or enable credits at nexlev.io |
| Auth window doesn't open / "Another instance running" | Run `nexlev_kill_stale.py` then retry |
| `Connection closed` | Stale mcp-remote process. Run `nexlev_kill_stale.py` then retry |
| First time ever / tokens expired | Browser auth window will open automatically — complete it |
| `npx` not found | Scripts already use `npx.cmd` — this is handled |

---

## OAuth Token Cache

After first browser authorization, tokens are cached at:
- `C:\Users\renu5\.mcp-auth\` (or similar npm cache location)
- Tokens survive across conversations — you only auth once

---

## Channel Workflow Template

Standard workflow for analyzing a channel:

1. `youtube_channel_about` (50/day) → Get channel ID, subs, views, join date, links
2. `youtube_channel_videos` with `sort_by: "popular"` (50/day) → Top videos
3. `check_channel_monetization` (5/day) → Monetized?
4. `check_faceless_channel` (5/day) → Faceless?
5. `get_channel_analytics` (5/day) → Growth, revenue estimates — **save this for last, only if needed**
