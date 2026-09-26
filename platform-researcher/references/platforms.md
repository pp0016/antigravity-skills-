# Platform Access Reference

Tested on 2026-09-23. These results are based on live access tests, not
assumptions.

## Reddit

**Access level:** Full  
**Method:** `search_web` with `site:reddit.com` + `read_url_content` for direct
thread fetching (including `.json` endpoint for structured data)  
**What works:**
- Searching any public subreddit
- Reading full threads with all comments
- Pulling top/hot/new posts by timeframe
- Fetching via `.json` endpoint for structured post data

**India-specific subreddits tested:**
- r/IndianYoutubers — YouTube creator discussions in Indian context
- r/developersIndia — Indian developer career/tool discussions
- r/IndiaInvestments — financial decisions, side hustles
- r/india — general Indian life discussions
- r/Entrepreneur — business/freelancing (global but India-relevant)

**Best search patterns:**
```
site:reddit.com r/[subreddit] "[exact phrase]"
site:reddit.com "I switched from" [tool]
site:reddit.com "honest review" [product] 2025
site:reddit.com "in my experience" [topic] India
```

**Limitations:** Reddit occasionally serves login walls on direct URL fetch.
The `.json` endpoint is more reliable. Old.reddit.com format also works well.

---

## Hacker News

**Access level:** Full  
**Method:** `read_url_content` for `news.ycombinator.com/item?id=` threads  
**What works:**
- Reading full discussion threads with nested comments
- All comment text and metadata visible
- Search via web search with `site:news.ycombinator.com`

**Best search patterns:**
```
site:news.ycombinator.com "Ask HN" [topic]
site:news.ycombinator.com "Show HN" [product]
site:news.ycombinator.com [topic] experience
```

**Best for:** Tech decisions, developer tools, startup ideas, career strategy,
SaaS evaluations.

**Limitations:** Skews heavily toward Silicon Valley tech perspective. Not
representative of Indian or non-English-speaking audiences.

---

## Product Hunt

**Access level:** Full  
**Method:** `search_web` with `site:producthunt.com`  
**What works:**
- Reading product launch pages with maker and user comments
- Finding real user reviews with usage duration mentioned
- Comparing competing products via launch discussions

**Best search patterns:**
```
site:producthunt.com "I've been using" [product]
site:producthunt.com [product] review
site:producthunt.com [category] 2025
```

**Best for:** New tool/SaaS evaluations, early adopter feedback, alternatives
discovery.

**Limitations:** Comments are often from the product's own community (launch
day supporters), so astroturfing risk is higher. Weight long-term user comments
over launch-day praise.

---

## Quora

**Access level:** Partial (~60-70% success rate)  
**Method:** `search_web` with `site:quora.com`, direct fetch sometimes blocked  
**What works:**
- Web search surfaces Quora answers reliably
- Some direct page fetches work, some hit login walls

**Best search patterns:**
```
site:quora.com "in my experience" [topic]
site:quora.com [topic] India
site:quora.com "I would recommend" [topic]
```

**Best for:** Career advice (especially India-specific), "is X worth it"
questions, educational path decisions.

**Limitations:** Quora has significant content quality variance. Many answers
are thin, generic, or from unqualified respondents. Weight answers with
specific details and named experiences over generic advice. Login walls block
direct page fetching intermittently.

---

## YouTube (without vidIQ)

**Access level:** Partial  
**Method:** `search_web` only (no vidIQ MCP in this skill)  
**What works:**
- Finding video titles and descriptions about a topic
- Getting search-snippet-level content about what creators say
- Finding which channels cover a topic

**Best search patterns:**
```
site:youtube.com "[topic] honest review"
site:youtube.com "[topic] after 1 year"
site:youtube.com "[topic]" India hindi
```

**Best for:** Finding WHICH videos/creators covered the topic. Not good for
extracting the actual crowd opinion (comments are not accessible without vidIQ).

**Limitations:** Cannot read YouTube comment sections. Cannot pull transcripts.
Video content is behind a playback wall. Use YouTube results as pointers, not as
evidence of crowd opinion.

---

## X / Twitter

**Access level:** Surface only  
**Method:** `search_web` returns content ABOUT X discussions  
**What works:**
- Finding that a topic is being discussed on X
- Getting general sentiment direction from search summaries

**Cannot do:**
- Read actual tweet threads with replies
- Pull specific user tweets
- Access reply chains or quote tweets

**Best for:** Confirming something is trending. Not reliable for extracting
specific opinions.

---

## Platforms with ZERO access

| Platform | Why | User action |
|---|---|---|
| Discord servers | Message content behind auth | Join relevant servers manually |
| Facebook Groups | Login required for all content | Search groups manually |
| Instagram comments | Walled off | Check manually |
| WhatsApp groups | Private/encrypted | No alternative |
| Telegram channels | Some public, most private | Check manually if link known |
| Private Slack communities | Invitation only | Join manually |

---

## Hindi/Hinglish Search Strategies

When the topic is India-relevant, add these search patterns:

```
[topic] "mere experience mein"
[topic] "mera experience"
[topic] review hindi 2025
[topic] India "worth it"
site:reddit.com r/india [topic]
site:reddit.com r/developersIndia [topic]
```

Hindi discussions are harder to find on Reddit (most Indian subreddits use
English or Hinglish). The best Hindi-language discussions often live on YouTube
comments and WhatsApp groups — both of which have limited access. Be honest
about this gap when it matters.
