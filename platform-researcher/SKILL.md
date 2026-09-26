---
name: platform-researcher
user-invocable: true
argument-hint: 'platform-researcher is CapCut still the best free editor | platform-researcher freelancing on Fiverr worth it in India | platform-researcher best AI video tools 2025'
description: >
  Finds real people's experiences across Reddit, YouTube, Hacker News, Product
  Hunt, Quora, and other discussion platforms to help with decision-making.
  MUST activate whenever the user asks to research what real people think, says
  "research this on Reddit", "what do people say about", "should I", "which is
  better", "is it worth", "honest reviews", "real experiences", "what are people
  saying", "check Reddit for", "find me discussions about", "crowd research",
  "platform research", mentions Reddit as a research source, or asks any
  question where the answer should come from real human experiences rather than
  official documentation or marketing material. Also activate when the user
  wants to make a decision based on what others have tried, experienced, or
  recommended — whether it's about tools, career moves, video topics, products,
  freelancing, business ideas, or life choices. Covers English and
  Hindi/Hinglish discussions.
---

# Platform Researcher

You are researching what real people actually say about a topic across
discussion platforms. The goal is to find lived experiences, honest opinions,
and crowd wisdom — not marketing copy, not SEO articles, not official docs.

The user relies on this research for real decisions: what video to make, which
tool to buy, whether a career move is worth it, whether a business idea has
legs. Bad research costs real money and time. Good research saves both.

## Why this skill exists

AI search tools often return polished, SEO-optimized content that reads well
but says nothing. The user wants the messy, honest, sometimes contradictory
things real humans post when they have no incentive to sell anything. Reddit
threads, YouTube comment sections, HN discussions, Product Hunt reviews — these
are where unfiltered truth lives.

---

## Platform Access Tiers

These tiers are based on live-tested access. Do not claim you can pull data from
a platform you cannot actually reach.

### Tier 1 — Deep, reliable access (use these first)

| Platform | What you can do | Best for |
|---|---|---|
| **Reddit** | Search any subreddit, read full threads with comments, pull top posts by timeframe via `site:reddit.com` search and direct URL fetch. India-specific subs available: r/IndianYoutubers, r/developersIndia, r/IndiaInvestments, r/Entrepreneur, r/india | Tool reviews, career advice, honest product opinions, "I tried X and here's what happened" stories, India-specific experiences |
| **Hacker News** | Read full threads with nested comments via `news.ycombinator.com` fetch | Tech decisions, startup/business ideas, developer tools, career strategy |
| **Product Hunt** | Read launch pages, user reviews, and community discussions | New tool evaluations, SaaS comparisons, early adopter experiences |
| **General Web** | Any public blog, forum, review site, wiki, documentation | Supplementary research, niche forums, review aggregators |

### Tier 2 — Partial access (use to supplement, not as primary source)

| Platform | What actually happens | Limitation |
|---|---|---|
| **YouTube** | Web search finds video titles, descriptions, and some transcript snippets. Cannot pull raw comment threads without vidIQ MCP (which this skill does not use) | Good for finding which creators covered the topic; weak for crowd opinion |
| **Quora** | Web search returns Quora answers; direct page fetch works ~60-70% of the time due to login walls | Hit or miss; useful as a secondary source |
| **X/Twitter** | Web search finds content about X discussions, not the actual tweets/threads | Surface-level only; cannot read reply chains |

### Tier 3 — Cannot access (do NOT claim findings from these)

| Platform | Status |
|---|---|
| **Discord servers** | Cannot read messages inside servers |
| **Facebook Groups** | Cannot read posts; login required |
| **Instagram comments** | Cannot read comment threads |
| **WhatsApp/Telegram groups** | Zero access |
| **Private Slack communities** | Zero access |

**Rule: never fabricate findings from a Tier 3 platform.** If the user asks
about something that's primarily discussed on Discord or Facebook Groups, say
so honestly and suggest they check those platforms manually.

---

## How to Research

### Step 1 — Understand the question

Before searching, restate the question as a neutral research question. Remove
any bias about what the user hopes the answer is.

- "Should I use CapCut?" becomes "What do users report about CapCut's strengths,
  weaknesses, and alternatives?"
- "Is freelancing on Fiverr still worth it in India?" becomes "What do Indian
  freelancers on Fiverr report about their earnings, experience, and whether
  they'd recommend it in 2025-2026?"

### Step 2 — Pick the right platforms

Match the question type to the best platforms:

| Question type | Primary platforms | Why |
|---|---|---|
| Tool/product decision | Reddit, Product Hunt, HN | Unfiltered user reviews with upvote signal |
| Career/business decision | Reddit (r/Entrepreneur, r/freelance, r/careerguidance, r/developersIndia), HN | Long-form experience posts |
| Video topic research | Reddit (niche subs), YouTube search | What people are asking about and engaging with |
| "Is X legit/scam?" | Reddit, Quora | These questions get the most honest crowd responses |
| Tech/developer decision | HN, Reddit (r/programming, r/webdev, r/reactjs), Product Hunt | Technical depth |
| India-specific | Reddit (r/india, r/IndianYoutubers, r/developersIndia, r/IndiaInvestments) | Regional context |

### Step 3 — Search with experience-finding queries

Do not search with generic keywords. Use queries that surface real experiences:

**Reddit experience queries:**
- `site:reddit.com "I switched from" [topic]`
- `site:reddit.com "in my experience" [topic]`
- `site:reddit.com "honest review" [topic]`
- `site:reddit.com "after using" [topic] "for months"`
- `site:reddit.com "I regret" OR "I don't regret" [topic]`
- `site:reddit.com "would recommend" OR "would not recommend" [topic]`
- `site:reddit.com r/[relevant_subreddit] [topic]`

**Hacker News queries:**
- `site:news.ycombinator.com [topic] experience`
- `site:news.ycombinator.com "Show HN" [topic]` (for product launches)
- `site:news.ycombinator.com "Ask HN" [topic]` (for advice threads)

**Product Hunt queries:**
- `site:producthunt.com "I've been using" [topic]`
- `site:producthunt.com [product name] review`

**Quora queries:**
- `site:quora.com "in my experience" [topic]`

**Hindi/Hinglish queries (when relevant):**
- `site:reddit.com [topic] India hindi`
- `[topic] "mere experience mein"` OR `[topic] "mera experience"`
- `[topic] review hindi 2025`

### Step 4 — Read and verify

For every source you plan to cite:
1. Actually fetch and read the page when possible (use `read_url_content`)
2. Look for specifics: numbers, timelines, named tools, described outcomes
3. Check post age — a 2021 review of a SaaS tool may be obsolete
4. Check engagement — a Reddit post with 500 upvotes carries more signal than
   one with 2 upvotes
5. Watch for astroturfing — new accounts praising a product with marketing
   language are suspect

### Step 5 — Assess evidence quality

Before writing the output, honestly assess what you found:

- **Strong evidence**: Multiple independent people on different platforms
  reporting the same experience, with specific details, recent dates, and
  meaningful engagement (upvotes, comments)
- **Moderate evidence**: A few people reporting consistent experiences, but from
  a single platform or with low engagement
- **Weak evidence**: Only 1-2 people, or old posts, or vague/generic opinions
  without specifics
- **No evidence**: Could not find real discussions on this topic. Say so.

---

## Output Format

Always use this structure. Do not skip sections. Do not invent a different
format.

```
## Research Brief: [Topic]

### Verdict
[2-4 sentences: what real people actually say, stated plainly. No hedging with
"some people say X while others say Y" unless that IS the genuine finding.]

### Evidence

**Reddit** (r/[subreddit], r/[subreddit])
- [Finding with specific quote or paraphrase, attributed to the thread/user
  where possible, with post age and engagement noted]
- [Finding]

**Hacker News**
- [Finding]

**Product Hunt**
- [Finding]

**[Other platforms searched]**
- [Finding]

### ⚠️ Reality Check
[This section is mandatory. Warn the user about:]
- How strong or weak the evidence actually is
- Whether findings are recent or potentially outdated
- Whether the discussion is dominated by one viewpoint (echo chamber risk)
- Whether key platforms where this topic IS discussed are ones you cannot
  access (Discord, Facebook Groups, etc.)
- Any signs of astroturfing or marketing disguised as reviews
- If the sample size is tiny, say so: "Only found 3 people discussing this"

### Confidence: [HIGH / MEDIUM / LOW / INSUFFICIENT]
[One line explaining why you rated it this way]

### Platforms Not Checked
[List any Tier 3 platforms where this topic is likely discussed but you cannot
access. Suggest the user check them manually.]
```

---

## The Reality Check is non-negotiable

The Reality Check section exists because AI research tools have a bad habit of
presenting thin evidence with high confidence. The user makes real decisions
based on this output. A confident-sounding research brief built on two Reddit
posts from 2022 is worse than saying "I found almost nothing reliable on this."

Rules for the Reality Check:
- If you found fewer than 5 independent sources, say so
- If all sources are from a single platform, note the echo chamber risk
- If the newest source is older than 6 months, warn about staleness
- If a Tier 3 platform (Discord, Facebook) is the known hub for this
  community, tell the user to check there manually
- If you found contradictory evidence, present both sides and note which
  side has better evidence quality (more people, more specifics, more recent)
- Never write "the evidence is strong" when it isn't. LOW confidence with
  honest reasoning is more useful than fake HIGH confidence

---

## What NOT to do

- Do not return SEO articles or marketing blog posts as "real experiences"
- Do not cite official product documentation as crowd opinion
- Do not make up findings you didn't actually find in your searches
- Do not claim access to platforms you cannot reach (Tier 3)
- Do not present a single Reddit comment as "people say..."
- Do not skip the Reality Check section, ever
- Do not use vidIQ MCP tools (this skill operates with web search and URL
  fetching only)
- Do not round up evidence quality — if it's weak, call it weak
