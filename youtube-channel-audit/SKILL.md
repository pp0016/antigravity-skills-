---
name: youtube-channel-audit
description: >
  Automated YouTube channel audit and analysis using NexLev MCP tools.
  Extracts channel profile, RPM, revenue, demographics, monetization status,
  lifetime earnings, and per-video efficiency metrics. Outputs a structured
  markdown report artifact. MUST activate whenever the user says "analyze this
  channel", "audit this channel", "channel analysis", "check this channel",
  "how much is this channel earning", "do the same analysis", "do it for this
  channel", provides a YouTube channel screenshot, mentions a YouTube handle
  (@username), or wants to know a channel's RPM, revenue, demographics, or
  monetization status. Also activate when the user pastes a YouTube channel URL
  or provides a channel name and wants financial/audience data. Activate even
  when user says "for this channel too", "same thing", "do it again", or
  provides just a screenshot of a YouTube channel page.
---

# YouTube Channel Audit

Run a complete NexLev-powered channel audit for any YouTube channel and output a structured markdown report artifact.

## When to Activate

- User provides a channel handle (@username), screenshot, or URL
- User says "analyze", "audit", "check", "do the same", "for this channel too"
- User asks about RPM, revenue, earnings, demographics, monetization
- User wants to compare channels
- User sends a screenshot of a YouTube channel page

## Prerequisites

- NexLev MCP caller skill must be installed at `C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\`
- NexLev must be authenticated (tokens cached at `C:\Users\renu5\.mcp-auth\`)
- NEVER rewrite the NexLev caller scripts — just call them as-is

## Complete Audit Workflow

Execute these steps in order for every channel analysis.

---

### Step 1: Extract Channel Handle

Get the YouTube handle from the user's input:
- **Screenshot**: Read the @handle visible in the channel page image
- **URL**: Extract from `youtube.com/@handle`
- **Text**: User says the handle or channel name directly

---

### Step 2: Fetch Channel Profile via NexLev

Call `youtube_channel_about` with the handle:

```powershell
Set-Content -Path "$env:TEMP\nexlev_audit.json" -Value '{"username": "HANDLE_HERE"}' -Encoding UTF8
python "C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\scripts\nexlev_call.py" youtube_channel_about "$env:TEMP\nexlev_audit.json"
```

**Fields to extract from response:**

| Field | JSON Key | Use |
|-------|----------|-----|
| Channel ID | `channelId` | Needed for ALL subsequent API calls |
| Name | `title` | Report header |
| Handle | `channelHandle` | Report header |
| Subscribers | `subscriberCount` | Profile table |
| Total Views | `viewCount` | Lifetime earnings calc |
| Video Count | `videosCount` | Per-video efficiency calc |
| Country | `country` | RPM context |
| Join Date | `joinedDate` | Channel age calc |
| Description | `description` | Content style identification |
| Family Safe | `isFamilySafe` | COPPA risk indicator |
| Has Email | `hasEmail` | Brand deal readiness |
| Tabs | `tabs` | Check for "Shorts" tab |
| Keywords | `keywords` | Niche identification |

---

### Step 3: Fetch RPM, Revenue & Demographics via NexLev

Call `get_geography_revenue` with the channel ID from Step 2:

```powershell
Set-Content -Path "$env:TEMP\nexlev_rpm.json" -Value '{"channelId": "CHANNEL_ID_HERE"}' -Encoding UTF8
python "C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\scripts\nexlev_call.py" get_geography_revenue "$env:TEMP\nexlev_rpm.json"
```

**Fields to extract:**

| Field | JSON Key | Use |
|-------|----------|-----|
| Monthly Revenue | `revenue.month_revenue` | Main revenue figure |
| Long-form Revenue | `revenue.month_long_revenue` | Revenue breakdown |
| Shorts Revenue | `revenue.month_short_revenue` | Revenue breakdown |
| Long-form Views | `revenue.long_view_count` | Views breakdown |
| Shorts Views | `revenue.short_view_count` | Views breakdown |
| Category RPM | `revenue.channel_category_rpm` | Industry benchmark |
| Channel Long RPM | `revenue.channel_long_rpm` | Actual earnings rate |
| Channel Short RPM | `revenue.channel_short_rpm` | Shorts earnings rate |
| Avg Duration | `revenue.weighted_avg_duration` | Content format |
| Language | `revenue.channel_language_code` | Audience context |
| Channel Type | `channelType` | LONG_ONLY / SHORT_ONLY / MIXED |
| Category | `category` | Niche classification |
| Gender | `demographics.gender` | Audience profile |
| Age Groups | `demographics.age` | Audience profile |
| Countries | `demographics.viewership_country` | Geographic distribution |

---

### Step 4: Monetization Check (Only if user explicitly requests)

The user said "don't give me monetisation check i will ultimately open their YouTube channel and watch the monetization check" — so SKIP this by default. Only run if user explicitly asks.

```powershell
Set-Content -Path "$env:TEMP\nexlev_mon.json" -Value '{"channelId": "CHANNEL_ID_HERE"}' -Encoding UTF8
python "C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\scripts\nexlev_call.py" check_channel_monetization "$env:TEMP\nexlev_mon.json"
```

---

### Step 5: Calculate Derived Metrics

From the raw data, compute these derived values:

| Metric | Formula |
|--------|---------|
| **Lifetime Earnings** | `total_views × channel_long_rpm / 1000` |
| **Channel Age (months)** | `(today - joinedDate) in months` |
| **Average Monthly Earning** | `lifetime_earnings / channel_age_months` |
| **Revenue per Video** | `lifetime_earnings / total_videos` |
| **Views per Video** | `total_views / total_videos` |
| **Subs per Video** | `subscribers / total_videos` |
| **Tier 1 Traffic %** | `Sum of US + UK + Canada + Australia view percentages` |
| **Growth Signal** | `current_monthly > avg_monthly = GROWING; else DECLINING` |

---

### Step 6: Generate Report Artifact

Save the report as a markdown artifact: `{handle}_analysis.md`

## Report Template (Use This EXACT Structure)

```markdown
# @{handle} ({channel_name}) — Full NexLev Channel Analysis

> **All data sourced from NexLev MCP — zero assumptions.**
> **Date**: {current_date}

---

## 1. Channel Profile (NexLev Data)

| Field | Value |
|-------|-------|
| **Channel Name** | {name} |
| **Handle** | @{handle} |
| **Channel ID** | `{channelId}` |
| **Country** | {country or "Not set"} |
| **Joined** | {joinedDate} (**~{age_months} months ago**) |
| **Subscribers** | {subscriberCount formatted with commas} |
| **Total Views** | **{viewCount formatted}** |
| **Videos** | {videosCount} |
| **Has Shorts** | {Yes/No — check if "Shorts" in tabs array} |
| **Avg Video Duration** | ~{weighted_avg_duration formatted as mm:ss} |
| **Family Safe** | {isFamilySafe} |
| **Has Contact Email** | {hasEmail} |
| **Description** | "{first 100 chars of description}" |
| **NexLev Category** | **{category}** |
| **Content Style** | {1-line description inferred from keywords + description} |

> Add a notable insight about the channel (e.g., uses TTS, no face, daily uploads).

---

## 2. RPM & Revenue (NexLev — Real Data)

| Metric | Value |
|--------|-------|
| **Category RPM** | **${channel_category_rpm}** |
| **Channel Long-form RPM** | **${channel_long_rpm}** |
| **Channel Short RPM** | ${channel_short_rpm or "N/A"} |
| **Estimated Monthly Revenue** | **${month_revenue formatted}** |
| **Monthly Long-form Revenue** | ${month_long_revenue} |
| **Monthly Shorts Revenue** | ${month_short_revenue or "N/A"} |
| **Monthly Long-form Views** | {long_view_count formatted} |
| **Monthly Shorts Views** | {short_view_count or "N/A"} |
| **Channel Type** | {channelType} |
| **Channel Language** | {channel_language_code} |

---

## 3. Total Lifetime Earnings Estimate

| Calculation | Value |
|------------|-------|
| Total views | {viewCount} |
| Channel RPM | ${channel_long_rpm} |
| **Estimated total lifetime earnings** | **~${lifetime_earnings}** |
| Months active | ~{channel_age_months} |
| **Average monthly earning** | **~${avg_monthly}/month** |
| **Current monthly earning** | **${month_revenue}/month** |
| **Revenue per video** | **${rev_per_video}** |
| **Views per video** | **{views_per_video}** |

> Add growth signal: "Channel is GROWING" if current > average, "DECLINING" if lower.

---

## 4. Audience Demographics (NexLev — Real Data)

### Gender Split
| Gender | % |
|--------|---|
| Male | {male_pct}% |
| Female | {female_pct}% |

### Age Distribution
| Age Group | % |
|-----------|---|
| 13-17 | {pct}% |
| 18-24 | {pct}% |
| 25-34 | {pct}% |
| 35-44 | {pct}% |
| 45-54 | {pct}% |
| 55-64 | {pct}% |
| 65+ | {pct}% |

### Top 5 Countries by Views
| Country | % of Views |
|---------|-----------|
| {country_1} | {pct}% |
| {country_2} | {pct}% |
| {country_3} | {pct}% |
| {country_4} | {pct}% |
| {country_5} | {pct}% |

> Add Tier 1 traffic insight and RPM impact.

---

## 5. Key Insight

One paragraph highlighting the most important/surprising finding about this channel.

---

## 6. All Channels Comparison Table (if multiple channels analyzed in session)

Include a comparison table with ALL previously analyzed channels if this isn't the first channel in the conversation.

| Metric | Channel 1 | Channel 2 | ... | **This Channel** |
|--------|-----------|-----------|-----|-------------------|
| Niche | | | | |
| Subs | | | | |
| Views | | | | |
| Videos | | | | |
| Monthly Rev | | | | |
| Lifetime | | | | |
| Rev/Video | | | | |

---

## Data Sources

| Data Point | NexLev Tool Used | Status |
|-----------|-----------------|--------|
| Channel profile | `youtube_channel_about` | ✅ |
| RPM / Revenue / Demographics | `get_geography_revenue` | ✅ |
| Monetization check | `check_channel_monetization` | ⬜ (not requested) |
```

---

## Rate Limit Awareness (NexLev FREE Plan)

| Tool | Daily Limit | Priority |
|------|-------------|----------|
| `youtube_channel_about` | 50/day | Low concern |
| `get_geography_revenue` | **5/day** | ⚠️ MOST LIMITED — plan carefully |
| `check_channel_monetization` | 5/day | Only on request |
| `youtube_channel_videos` | 50/day | Low concern |
| `get_channel_analytics` | 5/day | Optional extras |
| `get_niche_overview` | 5/day | For competitor research |

If rate limited on `get_geography_revenue`, note it in the report and estimate revenue using similar channels from the same niche that were already analyzed.

## Error Handling

| Error | Fix |
|-------|-----|
| Connection timeout / 502 | Retry once — NexLev servers occasionally drop |
| "Proactive token refresh failed" | **IGNORE** — this is normal, not an error |
| Auth/OAuth errors | Run `python nexlev_kill_stale.py` then retry |
| Unicode errors on Windows | Prefix with `$env:PYTHONIOENCODING='utf-8'` |
| Multi-line Python strings fail | Write Python code to a `.py` file first, then run it |

## Key Insights to Always Include

After generating the raw data report, add contextual analysis covering:

1. **Growth trajectory**: Current monthly vs lifetime average — growing or declining?
2. **RPM vs category benchmark**: Above or below category average? Why?
3. **Shorts revenue trap**: If MIXED type, highlight how Shorts drag down effective RPM
4. **Geographic RPM impact**: High India/SEA traffic = lower RPM than category average
5. **Per-video efficiency**: Revenue per video compared to other analyzed channels
6. **Notable patterns**: TTS voice, faceless format, upload frequency, content formula
7. **Audience profile**: Who watches — gender skew, age concentration, parent vs direct viewer

## Batch Mode

If the user wants multiple channels analyzed, use `nexlev_batch.py`:

```powershell
# Create batch config
Set-Content -Path "batch.json" -Value '[
  {"tool": "youtube_channel_about", "args": {"username": "handle1"}},
  {"tool": "youtube_channel_about", "args": {"username": "handle2"}}
]' -Encoding UTF8

python "C:\Users\renu5\.gemini\config\skills\nexlev-mcp-caller\scripts\nexlev_batch.py" "batch.json"
```

## Channel ID Quick Reference

When analyzing channels across a session, maintain a running table of channel IDs to avoid re-fetching:

```
| Channel | Handle | ID |
|---------|--------|----|
| {name}  | @{handle} | {channelId} |
```
