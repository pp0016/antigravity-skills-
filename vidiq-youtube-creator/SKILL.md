---
name: vidiq-youtube-creator
description: |
  Complete YouTube content creation and optimization workflow powered by vidIQ MCP server.
  Use this skill whenever the user mentions YouTube, vidIQ, content creation, video SEO,
  keyword research, thumbnails, titles, trending topics, outlier videos, competitor analysis,
  channel analytics, subscriber insights, shorts strategy, clips, video transcripts, CTR
  optimization, or any YouTube growth-related task. This skill MUST activate even if the user
  doesn't explicitly say "vidIQ" — any YouTube optimization, channel growth, or content
  planning task should trigger it. Also triggers on: "what should I make a video about",
  "find trending topics", "analyze this channel", "video ideas", "YouTube SEO", "go viral",
  "content calendar", "niche research", "YouTube analytics", "watch time", "video performance".
---

# vidIQ YouTube Creator — Full Workflow Skill

## What This Skill Does

This skill connects you to the **vidIQ MCP server** — a live API that gives you access to YouTube's
intelligence infrastructure: keyword data, trending videos, competitor analytics, outlier detection,
AI-powered title/thumbnail generation, video transcripts, and multimodal video analysis.

It works for **ANY niche, ANY language, ANY channel** — you just describe what you want and the
skill handles tool selection, credit budgeting, and workflow orchestration.

## Before You Start — Critical Setup Check

Before using any vidIQ tool, verify the connection:

1. The vidIQ MCP server must be configured in your MCP settings with a valid API key
2. If tools are not available, tell the user:
   > "vidIQ MCP is not connected. To set it up:
   > 1. Go to https://app.vidiq.com/account/settings/mcp
   > 2. Generate an API key
   > 3. Replace `PASTE_YOUR_VIDIQ_API_KEY_HERE` in your mcp.json with the real key
   > 4. Restart Antigravity"

## Credit System — ALWAYS Be Credit-Conscious

vidIQ uses a credit system. The user has **~170 credits/month** on the free tier.

| Tool Type | Cost | Monthly Budget |
|-----------|------|---------------|
| **Utility tools** | 0 credits | Unlimited |
| **Standard tools** | 5 credits | ~34 calls/month |
| **Heavy tools** | 10 credits | ~17 calls/month |

### Credit Protection Rules (MANDATORY)

1. **ALWAYS** call `credits_balance` (free) before starting any workflow
2. **WARN** the user before any workflow costing >15 credits total
3. **Show a running credit tally** during multi-step workflows: `[Credits used: 10/170 remaining]`
4. **NEVER chain more than 3 paid tool calls** without asking the user to confirm
5. When credits < 20, switch to free-only tools and say:
   > "You're running low on credits (X remaining). To continue with paid tools,
   > generate a new API key from a different account at https://app.vidiq.com/account/settings/mcp
   > and update the key in your MCP config. For now, I'll use free tools only."

## Available Tools — Complete Reference

### 🟢 Free Tools (0 Credits) — Use Freely

| Tool | What It Does |
|------|-------------|
| `credits_balance` | Check remaining credit balance |
| `your_connected_channels` | List YouTube/Instagram channels linked to account |
| `async_job_tracking` | Check status of long-running jobs |
| `voice_library` | List available AI voice options |
| `trend_categories` | Browse content categories and niches for trend research |
| `feedback` | Submit feedback to vidIQ team |

### 🟡 Standard Tools (5 Credits Each) — Use Strategically

| Tool | What It Does |
|------|-------------|
| `keyword_research` | Search volume, competition scores, keyword opportunities |
| `outliers` | Find videos that massively overperformed their channel baseline |
| `trending_videos` | Real-time trending content by category, topic, or velocity |
| `video_transcript` | Extract full text transcript of any public YouTube video |
| `channel_analytics` | Channel health: subscribers, views, watch time, traffic sources |
| `subscriber_insights` | Audience demographics, overlapping channels, best post times |
| `generate_titles` | AI-generated high-CTR, SEO-optimized title ideas |
| `generate_thumbnail` | Thumbnail concepts, visual briefs, image prompt ideas |
| `generate_clips` | Identify clip-worthy timestamps in long-form for Shorts/Reels |

### 🔴 Heavy Tools (10 Credits Each) — Use Sparingly

| Tool | What It Does |
|------|-------------|
| `video_watch` | Deep multimodal analysis (visual + audio + text) of a YouTube video |
| `reel_watch` | Deep multimodal analysis of an Instagram Reel |

## Workflow Selection — Match Task to Template

Read `references/workflow-templates.md` for detailed step-by-step templates. Quick selector:

| User Wants | Workflow | Est. Cost |
|------------|----------|-----------|
| "What should I make videos about?" | New Channel Launch Research | ~35 credits |
| "Plan my content for this week" | Weekly Content Planning | ~25 credits |
| "Optimize this video's SEO" | Video SEO Optimizer | ~10 credits |
| "Analyze my competitor" | Competitor Deep Dive | ~20 credits |
| "Help me make Shorts" | Shorts/Clips Strategy | ~15 credits |
| "What's trending right now?" | Free Daily Routine | 0 credits |
| "Break down why this video went viral" | Deep Video Analysis | ~10-20 credits |

## When Credits Are Exhausted

When `credits_balance` returns 0 or near-zero:

1. Tell the user their credits are exhausted for this account
2. Instruct them to:
   - Log into a different Gmail account at https://vidiq.com
   - Go to Account Settings → MCP tab
   - Generate a new API key
   - Update the key in their MCP config file:
     - **Antigravity 2.1.4**: `C:\Users\renu5\.gemini\config\mcp.json` → `vidiq.args` → replace the Bearer token
     - **Antigravity IDE 2.1.1**: `C:\Users\renu5\.gemini\config\mcp_config.json` → same location
   - Restart the application
3. While waiting, use free tools (`trend_categories`, `your_connected_channels`) or work with cached data from previous calls

## Key Behaviors

- **Be niche-agnostic**: Never assume a niche. Always ask or infer from context.
- **Estimate before executing**: Before any workflow, show: "This will cost ~X credits. You have Y remaining. Proceed?"
- **Cache and reuse data**: If you already fetched keyword data or competitor analytics in this conversation, reuse it instead of re-calling.
- **Combine free + paid strategically**: Always start with free tools (trend_categories, connected_channels) to gather context before spending credits.
- **Async job awareness**: Some tools (generate_clips, deep channel audits) run asynchronously. Use `async_job_tracking` to poll for results.

## Detailed References

For complete tool parameters, workflow step-by-step guides, and credit optimization strategies:
- Read `references/tools-reference.md` for full tool documentation
- Read `references/workflow-templates.md` for pre-built workflow templates
- Read `references/credit-strategy.md` for credit management and multi-account strategy
