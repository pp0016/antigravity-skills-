# vidIQ Credit Management Strategy

## Credit Cost Reference Table

| Tool | Credits | Category |
|------|---------|----------|
| `credits_balance` | 0 | Utility |
| `your_connected_channels` | 0 | Utility |
| `async_job_tracking` | 0 | Utility |
| `voice_library` | 0 | Utility |
| `trend_categories` | 0 | Utility |
| `feedback` | 0 | Utility |
| `keyword_research` | 5 | Standard |
| `outliers` | 5 | Standard |
| `trending_videos` | 5 | Standard |
| `video_transcript` | 5 | Standard |
| `channel_analytics` | 5 | Standard |
| `subscriber_insights` | 5 | Standard |
| `generate_titles` | 5 | Standard |
| `generate_thumbnail` | 5 | Standard |
| `generate_clips` | 5 | Standard |
| `video_watch` | 10 | Heavy |
| `reel_watch` | 10 | Heavy |

---

## Monthly Budget Calculator (170 credits)

### Maximum Calls Per Month

| Tool Type | Max Calls | If Used Exclusively |
|-----------|-----------|-------------------|
| Free tools | ∞ | Unlimited daily use |
| Standard (5 credits) | 34 | ~1.1 calls/day |
| Heavy (10 credits) | 17 | ~0.6 calls/day |
| Mixed (3 standard + 1 heavy) | ~7 sessions | ~1.75 sessions/week |

### Recommended Monthly Budget Split

| Allocation | Credits | What You Get |
|------------|---------|-------------|
| Weekly Planning (2x) | 50 | 2 full content planning sessions |
| SEO Optimization (4x) | 40 | 4 videos optimized |
| Competitor Analysis (1x) | 20 | 1 deep competitor dive |
| Trending Research (2x) | 10 | 2 trend scans |
| Deep Video Analysis (1x) | 10 | 1 viral video breakdown |
| **Reserve buffer** | **40** | Emergency/opportunities |
| **Total** | **170** | |

---

## Single-Key Strategy (Current Approach)

The user uses one API key at a time. When credits are exhausted:

### Step 1: Detect Exhaustion
- `credits_balance` returns 0 or <5 credits
- Tool calls return credit-related error messages

### Step 2: Notify the User
Tell them exactly:
> "Your vidIQ credits are exhausted for this account. To continue:
> 1. Open a new browser (or incognito window)
> 2. Log into vidiq.com with a different Gmail account
> 3. Go to **Account Settings → MCP tab**
> 4. Click **Generate API Key**
> 5. Copy the new key
> 6. Give me the new key and I'll tell you how to update it"

### Step 3: Update Instructions
When the user provides a new key, tell them:

**For Antigravity 2.1.4:**
1. Open `C:\Users\renu5\.gemini\config\mcp.json`
2. Find the `"vidiq"` section
3. Replace `PASTE_YOUR_VIDIQ_API_KEY_HERE` (or the old key) with the new key in the `--header` argument:
   ```
   "Authorization: Bearer NEW_KEY_HERE"
   ```
4. Save and restart Antigravity

**For Antigravity IDE 2.1.1:**
1. Open `C:\Users\renu5\.gemini\config\mcp_config.json`
2. Same process — find `"vidiq"` section, replace the key
3. Save and restart

### Step 4: Resume Work
After restart, call `credits_balance` to verify the new account has credits, then continue the workflow.

---

## Credit Warning Thresholds

| Credits Remaining | Action |
|------------------|--------|
| **>50** | ✅ All workflows available, no restrictions |
| **20-50** | ⚠️ Warn user before workflows >20 credits. Suggest smaller workflows. |
| **5-20** | 🟡 Only allow single-tool calls. No multi-step workflows without explicit approval. |
| **<5** | 🔴 Free tools only. Prompt user to swap API key. |
| **0** | 🛑 All paid tools blocked. Free tools only. Immediate key swap notification. |

---

## Maximizing Free Tool Value

Even with 0 paid credits, free tools provide real value:

1. **`trend_categories`** — Browse trending niches daily. Takes 10 seconds. Keeps you aware of what's moving without spending credits.

2. **`your_connected_channels`** — Verify which channels are active. Useful if managing multiple accounts.

3. **`async_job_tracking`** — If you launched any async jobs before credits ran out, you can still retrieve completed results.

4. **`credits_balance`** — Monitor when credits reset (monthly billing anniversary). Plan your heavy workflows for right after reset day.

---

## Credit Efficiency Tips

1. **Batch keyword research**: Instead of 3 separate `keyword_research` calls, research your broadest keyword first and analyze the related keywords returned. Often one call gives you enough data.

2. **Cache everything**: If you analyzed a competitor this week, don't re-analyze them next week. Channel growth doesn't change that fast.

3. **Start free, then go paid**: Always begin with `trend_categories` (free) to identify what's worth spending credits on. Don't blindly research random keywords.

4. **Skip video_watch for most videos**: At 10 credits each, only use `video_watch` on confirmed outliers with 10x+ view velocity. For most videos, `video_transcript` (5 credits) gives you 80% of the useful information.

5. **Use generate_titles before generate_thumbnail**: Titles drive more clicks than thumbnails. If you're low on credits, spend on titles first.

6. **One competitor per month**: Full competitor analysis costs 20 credits. Pick ONE competitor to deep-dive each month rather than shallow-scanning many.
