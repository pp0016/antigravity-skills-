# vidIQ MCP Tools — Complete Reference

This document contains detailed documentation for every tool exposed by the vidIQ MCP server.
Use this as a reference when you need to understand tool parameters, outputs, and best use cases.

---

## 🟢 Free Tools (0 Credits)

### `credits_balance`
- **Cost**: 0 credits
- **Purpose**: Check how many AI credits remain in the current vidIQ account
- **When to use**: ALWAYS call this before starting any paid workflow
- **Parameters**: None
- **Returns**: Current credit balance, monthly limit, reset date
- **Example**: "Check my vidIQ credit balance before we start"

### `your_connected_channels`
- **Cost**: 0 credits
- **Purpose**: List all YouTube and Instagram channels linked to the vidIQ account
- **When to use**: At the start of any session to identify which channels are available
- **Parameters**: None
- **Returns**: Channel names, IDs, platform (YouTube/Instagram), subscriber counts
- **Example**: "Show me which channels are connected to my vidIQ"

### `async_job_tracking`
- **Cost**: 0 credits
- **Purpose**: Monitor status and retrieve results for long-running asynchronous jobs
- **When to use**: After launching heavy operations (clips generation, deep audits)
- **Parameters**: Job ID (returned from the original tool call)
- **Returns**: Job status (pending/processing/completed/failed), results when complete
- **Example**: "Check if my clip generation job is done"

### `voice_library`
- **Cost**: 0 credits
- **Purpose**: List available AI voice options for script/audio synthesis
- **When to use**: When the user wants to generate voiceover scripts or audio content
- **Parameters**: None
- **Returns**: List of voice names, descriptions, language support, tone characteristics

### `trend_categories`
- **Cost**: 0 credits
- **Purpose**: Browse available content categories and niches for trending topic research
- **When to use**: When exploring what niches or categories are available to research
- **Parameters**: None (may support optional filters)
- **Returns**: List of category names, subcategories, current trending status
- **Example**: "What content categories can I explore for trends?"

### `feedback`
- **Cost**: 0 credits
- **Purpose**: Submit user feedback or bug reports to the vidIQ team
- **When to use**: When something isn't working or the user has suggestions
- **Parameters**: Feedback text, optional category
- **Returns**: Confirmation of submission

---

## 🟡 Standard Tools (5 Credits Each)

### `keyword_research`
- **Cost**: 5 credits
- **Purpose**: Get search volume, competition scores, keyword overall score, and low-competition opportunity keywords
- **When to use**: When planning video topics, optimizing titles/descriptions, or finding content gaps
- **Key Parameters**:
  - `keyword` (required): The seed keyword or phrase to research
  - `language` (optional): Target language for results
  - `country` (optional): Target country for regional data
- **Returns**: Search volume (monthly), competition score (0-100), overall score, related keywords with scores, trending direction
- **Best Practice**: Start broad ("cooking tips") then narrow based on results ("air fryer recipes for beginners")
- **Example**: "Research the keyword 'AI tools for students' in India"

### `outliers`
- **Cost**: 5 credits
- **Purpose**: Find videos that significantly overperformed their channel's baseline view velocity (3x-10x+ normal views)
- **When to use**: When looking for viral content blueprints, content gap opportunities, or understanding what breaks through
- **Key Parameters**:
  - `topic` or `niche` (required): What topic area to scan
  - `timeframe` (optional): Recent vs historical outliers
- **Returns**: Video URLs, view counts, view velocity multiplier, channel size, video metadata
- **Best Practice**: Look at outliers from small channels (< 10K subs) — these reveal content gaps that big channels haven't exploited
- **Example**: "Find outlier videos in the personal finance niche from small channels"

### `trending_videos`
- **Cost**: 5 credits
- **Purpose**: Fetch real-time trending YouTube content by category, topic, or views-per-hour velocity
- **When to use**: For daily content inspiration, trend-jacking opportunities, or understanding what's hot right now
- **Key Parameters**:
  - `category` (optional): Content category filter
  - `topic` (optional): Specific topic to find trends for
  - `sort_by` (optional): Sort by views-per-hour, recency, or total views
- **Returns**: Video URLs, titles, view counts, views-per-hour, channel info, upload time
- **Example**: "What's trending in tech right now?"

### `video_transcript`
- **Cost**: 5 credits
- **Purpose**: Extract the full text transcript of any public YouTube video
- **When to use**: When analyzing competitor video structure, extracting talking points, or creating similar content
- **Key Parameters**:
  - `video_url` or `video_id` (required): The YouTube video to transcribe
- **Returns**: Full text transcript with timestamps, language detected
- **Best Practice**: Use this to reverse-engineer successful video structures — look at intro hooks, segment transitions, and CTAs
- **Example**: "Get the transcript of https://youtube.com/watch?v=ABC123"

### `channel_analytics`
- **Cost**: 5 credits
- **Purpose**: Generate channel health reports including subscriber velocity, total views, watch time trends, top traffic sources
- **When to use**: When auditing a competitor channel or analyzing your own channel performance
- **Key Parameters**:
  - `channel_url` or `channel_id` (required): The channel to analyze
- **Returns**: Subscriber count and growth rate, total views, average views per video, upload frequency, top performing videos, traffic source breakdown
- **Example**: "Analyze the channel MrBeast"

### `subscriber_insights`
- **Cost**: 5 credits
- **Purpose**: Audience demographics, overlapping subscribed channels, and optimal posting times
- **When to use**: When understanding audience composition or finding the best time to upload
- **Key Parameters**:
  - `channel_url` or `channel_id` (required): The channel to analyze
- **Returns**: Age/gender demographics, geographic distribution, overlapping channel subscriptions, best days/times to post
- **Example**: "What's the best time to post for my channel's audience?"

### `generate_titles`
- **Cost**: 5 credits
- **Purpose**: Generate high-CTR, SEO-optimized title ideas tailored to search trends
- **When to use**: When the user has a video topic and needs compelling title options
- **Key Parameters**:
  - `topic` (required): The video topic or concept
  - `style` (optional): Listicle, how-to, story, etc.
  - `channel_context` (optional): Channel name/URL for personalized suggestions
- **Returns**: 5-10 title options with estimated CTR potential, keyword integration notes
- **Example**: "Generate titles for a video about 'how to start dropshipping in 2026'"

### `generate_thumbnail`
- **Cost**: 5 credits
- **Purpose**: Generate detailed thumbnail concepts, visual briefs, or image prompts
- **When to use**: When the user needs thumbnail ideas that pair with their title
- **Key Parameters**:
  - `title` (required): The video title to design a thumbnail for
  - `style` (optional): Preference for text-heavy, face-focused, comparison, etc.
- **Returns**: 3-5 thumbnail concepts with color palettes, text overlay suggestions, composition notes, image generation prompts
- **Example**: "Create thumbnail concepts for 'I Tried AI for 30 Days — Here's What Happened'"

### `generate_clips`
- **Cost**: 5 credits
- **Purpose**: Analyze long-form YouTube videos and identify candidate timestamps for Shorts/Reels
- **When to use**: When the user wants to repurpose long-form content into short-form
- **Key Parameters**:
  - `video_url` or `video_id` (required): The source long-form video
- **Returns**: Clip timestamps (start/end), suggested hooks, engagement prediction, clip themes
- **Note**: This tool may run **asynchronously** — use `async_job_tracking` to poll for results
- **Example**: "Find the best clips from my latest 20-minute video for Shorts"

---

## 🔴 Heavy Tools (10 Credits Each)

### `video_watch`
- **Cost**: 10 credits
- **Purpose**: Deep multimodal understanding (visual + audio + text) of a YouTube video
- **When to use**: When you need comprehensive analysis of WHY a video performed well — editing style, pacing, hooks, visual techniques, audio design
- **Key Parameters**:
  - `video_url` or `video_id` (required): The YouTube video to analyze
- **Returns**: Content breakdown (intro/body/outro structure), hook analysis, editing technique identification, pacing assessment, engagement prediction, replication suggestions
- **Best Practice**: Use this sparingly (10 credits = expensive). Reserve for top-performing outlier videos you want to deeply understand and replicate.
- **Example**: "Do a deep analysis of this viral video: https://youtube.com/watch?v=XYZ"

### `reel_watch`
- **Cost**: 10 credits
- **Purpose**: Deep multimodal analysis of a public Instagram Reel
- **When to use**: When analyzing successful short-form content on Instagram for cross-platform strategy
- **Key Parameters**:
  - `reel_url` (required): The Instagram Reel URL
- **Returns**: Content analysis, hook timing, visual techniques, audio/music choices, engagement drivers
- **Example**: "Analyze this Instagram Reel to understand what makes it engaging"

---

## Tool Chaining Best Practices

### Effective Combinations

1. **Topic Discovery Chain** (10 credits):
   `trend_categories` (free) → `trending_videos` (5) → `keyword_research` on trending topic (5)

2. **Competitor Reverse-Engineering** (15-25 credits):
   `channel_analytics` (5) → `outliers` (5) → `video_transcript` of top outlier (5) → optional `video_watch` (10)

3. **Full Video Planning** (15 credits):
   `keyword_research` (5) → `generate_titles` (5) → `generate_thumbnail` (5)

4. **Content Repurposing** (10-15 credits):
   `generate_clips` (5) → `async_job_tracking` (free) → `keyword_research` for short-form tags (5)

### Anti-Patterns to Avoid

- ❌ Calling `keyword_research` 5 times with similar keywords (25 credits wasted — batch variations in one call)
- ❌ Using `video_watch` on mediocre videos (10 credits — only use on confirmed outliers)
- ❌ Running `channel_analytics` on your own channel repeatedly (5 credits each — data doesn't change that fast, cache it)
- ❌ Chaining 5+ paid tools without user confirmation (potential 25+ credit burn)
