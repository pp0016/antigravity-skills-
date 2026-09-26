---
name: vidiq-nexlev-router
description: >-
  Smart routing between vidIQ and NexLev MCP tools for YouTube research and
  content creation. MUST activate whenever the agent is about to use any
  vidIQ or NexLev MCP tool, or when the user mentions YouTube research,
  channel analysis, monetization check, faceless channel, niche research,
  keyword research, thumbnail generation, video generation, voiceover,
  competitor analysis, sponsorship detection, content creation, SEO scoring,
  or any YouTube-related task. Also activate on "which tool should I use",
  "save credits", "credit optimization", "vidIQ vs nexlev", "platform router",
  "use vidIQ", "use nexlev". This skill ensures the right platform is used
  for each task, tracks NexLev daily usage, and generates batch prompts
  for the vidIQ web AI Coach to save credits.
---

# vidIQ ↔ NexLev Smart Router

Route every YouTube task to the right platform. The user has effectively
unlimited vidIQ credits (5–10 accounts, 150–300 credits each, API keys
swappable). NexLev is OAuth-locked with hard daily caps — every call counts.

---

## CORE RULE: Always Recommend Before Calling

Before using ANY tool from either platform, briefly tell the user:
1. Which platform you recommend and why
2. Which specific tool you'll use
3. For NexLev: the daily limit and how many calls remain in this session

Then proceed. vidIQ calls don't need usage tracking — user manages credits.

---

## ROUTING DECISION TREE

### Step 1: Is This NexLev-Exclusive?

If the task requires ANY of these, you MUST use NexLev — vidIQ cannot do them:

| Category | NexLev Tools | Daily Cap |
|---|---|---|
| **Monetization check** | `check_channel_monetization`, `check_video_monetization` | 5 each |
| **Faceless detection** | `check_faceless_channel`, `latest_discovered_faceless_niches`, `faceless_outliers_videos` | 5, 20, 20 |
| **Niche finder** | `search_niche_finder_channels`, `get_niche_overview`, `get_niche_finder_categories`, `get_niche_finder_formats`, `get_niche_finder_tags` | 10, 5, 10, 10, 5 |
| **Sponsorship/promotions** | `get_channel_promotions`, `get_channel_promotions_realtime` | 5, 2 |
| **Viral small channels** | `search_viral_videos_small_channels` | 20 |
| **RPM & geo revenue** | `get_video_rpm`, `get_geography_revenue` | 5 each |
| **Shorts vs long split** | `get_short_vs_long_views` | 5 |
| **Daily analytics** | `get_daily_analytics` | 5 |
| **Bulk operations** | `get_batch_channel_metrics`, `get_bulk_video_transcripts`, `get_bulk_video_subtitles`, `get_video_subtitle` | 5 each |
| **Find channel types** | `find_long_form_channels`, `find_shorts_channels` | 10 each |
| **Suggested videos** | `search_youtube_suggested_videos` | 20 |
| **Channel resolver** | `channel_resolver` (handle → ID) | 10 |
| **Watch TikTok/IG video** | `watch_tiktok_video_and_ask`, `watch_instagram_video_and_ask` | 1 each |

→ If YES: Use NexLev. Report the tool, its daily cap, and session usage.

### Step 2: Is This vidIQ-Exclusive?

If the task requires ANY of these, you MUST use vidIQ — NexLev cannot do them:

| Category | vidIQ Tools |
|---|---|
| **AI content generation** | `generate_titles`, `generate_script`, `generate_video`, `generate_broll`, `generate_music`, `generate_clips`, `generate_thumbnail`, `refine_thumbnail`, `generate_comment_replies`, `compose`, `motion_graphics`, `edit_media` |
| **Voiceover** | `voiceover_list_voices`, `voiceover_generate`, `voiceover_clone`, `voiceover_clone_start` |
| **SEO & scoring** | `keyword_research`, `score_title`, `score_thumbnail` |
| **Analytics & insights** | `subscriber_insights`, `channel_performance_trends`, `video_change_history`, `trend_categories` |
| **IG/TikTok research** | `ig_profile`, `ig_profile_reels`, `instagram_tiktok_outlier_search`, `ig_accounts_from_outliers`, `watch_shortform_content` |
| **Competitor tracking** | `list_competitors`, `update_competitors` |
| **Earnings estimate** | `video_earnings_estimate`, `earnings_calculate` |

→ If YES: Use vidIQ. No usage tracking needed.

### Step 3: Both Can Do It?

For overlapping capabilities, **ALWAYS use vidIQ** (unlimited credits):

| Task | Use vidIQ | NOT NexLev |
|---|---|---|
| YouTube search | `youtube_search` | ~~youtube_search~~ |
| Channel stats | `channel_stats` | ~~youtube_channel_about~~ |
| Channel videos | `channel_videos` | ~~youtube_channel_videos~~ |
| Video stats | `video_stats` | ~~youtube_video_details~~ |
| Video comments | `video_comments` | ~~youtube_video_comments~~ |
| Video transcript | `video_transcript` | ~~get_video_transcript~~ |
| Similar channels | `similar_channels` | ~~get_similar_channels~~ |
| Similar videos | `similar_videos` | ~~get_similar_videos~~ |
| Similar thumbnails | `similar_thumbnails` | ~~get_similar_thumbnails~~ |
| Outlier videos | `outliers` | ~~youtube_channel_outliers~~ |
| Channel analytics | `channel_analytics` | ~~get_channel_analytics~~ |
| Watch YouTube video | `video_watch` | ~~watch_youtube_video_and_ask~~ |

→ ALWAYS vidIQ for overlapping tools. Never waste NexLev daily calls on something vidIQ can do.

---

## NEXLEV SESSION TRACKER

When using NexLev tools in a session, track usage by reporting after each call:

```
🔔 NexLev: Used `check_channel_monetization` — 5/day limit, 1 used this session (4 remaining)
```

This helps the user understand their remaining daily budget.

---

## VIDIQ AI COACH BATCHING TRICK

The vidIQ web AI Coach charges only **10 credits per message** regardless of
how long or complex the prompt is. For research-heavy tasks, generate a
ready-to-copy batch prompt the user can paste into vidIQ web instead of
burning multiple MCP credits.

### When to Suggest Batching
- User needs keyword research + competitor analysis + content ideas together
- User wants broad SEO/content intelligence across multiple topics
- Any task where 3+ separate vidIQ MCP calls could be replaced by one AI Coach prompt

### How to Generate the Batch Prompt
Create a structured prompt the user can copy-paste into vidIQ web AI Coach:

**Example format:**
```
I need help with the following for my YouTube channel in the [NICHE] niche:

1. KEYWORD RESEARCH: Find top 10 keywords for "[TOPIC]" with search volume and competition
2. TITLE IDEAS: Generate 5 title options for a video about "[TOPIC]"  
3. COMPETITOR ANALYSIS: What are the top 5 channels in [NICHE] doing differently?
4. CONTENT GAPS: What topics in [NICHE] have high search but low competition?
5. TRENDING: What's trending in [NICHE] right now?

Please provide detailed answers for each.
```
→ This costs only **10 credits** on the web AI Coach instead of 50+ credits via MCP.

dont use this example prompt create you own cousmised prompt based on requiement and give add recommended things can do so i can add if i want 


### vidIQ Credit Costs Reference
| Action | Credits |
|---|---|
| AI Coach regular message | **10** | 
| Thumbnail generation/edit | **22** |
| Title generation (up to 3) | **3** |
| Description generation | **1** |
| Shorts generation (per sec) | **20** |
| Clipping (per min input) | **9** |
| Script writing (per min) | **1** |

> Heavy generation tasks (thumbnails, shorts, video) cost significantly more.
> For research and text tasks, always consider the AI Coach batching trick first .

---

## QUICK REFERENCE CHEAT SHEET

| User Wants To... | Platform | Tool |
|---|---|---|
| Check if a channel is monetized | **NexLev** | `check_channel_monetization` |
| Check if a channel is faceless | **NexLev** | `check_faceless_channel` |
| Find faceless niches | **NexLev** | `latest_discovered_faceless_niches` |
| Research a niche | **NexLev** | `get_niche_overview` |
| Find viral videos from small channels | **NexLev** | `search_viral_videos_small_channels` |
| See what brands a channel promotes | **NexLev** | `get_channel_promotions` |
| Get RPM for a video | **NexLev** | `get_video_rpm` |
| Get revenue by country | **NexLev** | `get_geography_revenue` |
| Bulk transcripts | **NexLev** | `get_bulk_video_transcripts` |
| Convert handle to channel ID | **NexLev** | `channel_resolver` |
| Keyword research | **vidIQ** | `keyword_research` |
| Score a title | **vidIQ** | `score_title` |
| Score a thumbnail | **vidIQ** | `score_thumbnail` |
| Generate titles | **vidIQ** | `generate_titles` |
| Generate a script | **vidIQ** | `generate_script` |
| Generate a thumbnail | **vidIQ** | `generate_thumbnail` |
| Generate voiceover | **vidIQ** | `voiceover_generate` |
| Track competitors | **vidIQ** | `list_competitors` |
| Get channel stats | **vidIQ** | `channel_stats` |
| Get video stats | **vidIQ** | `video_stats` |
| Search YouTube | **vidIQ** | `youtube_search` |
| Get video transcript | **vidIQ** | `video_transcript` |
| Find similar channels | **vidIQ** | `similar_channels` |
| Find outlier videos | **vidIQ** | `outliers` |
| Channel analytics | **vidIQ** | `channel_analytics` |
| Subscriber insights | **vidIQ** | `subscriber_insights` |
| Batch research (5+ questions) | **vidIQ Web** | AI Coach batching trick (10 credits) |

vidIQ for estimate, NexLev for precise RPM so we can use nexlev for precise rpm when required Recommend me Based on the work requirement 