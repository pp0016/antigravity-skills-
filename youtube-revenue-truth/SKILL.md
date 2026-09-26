---
name: youtube-revenue-truth
description: How to accurately estimate YouTube channel revenue by knowing when to trust NexLev's default data versus when to use a custom vidIQ RPM Oracle for Hindi, regional, or pop-culture channels. Use this whenever the user asks to analyze a channel's earnings, verify NexLev data, or research profitable niches.
---

# YouTube Revenue Truth: The Hybrid Methodology

This skill provides the definitive framework for researching YouTube channels and calculating accurate revenue estimates. It solves the "NexLev Geography Hallucination" problem by determining when to trust AI estimates and when to calculate them manually using the Hybrid Method.

## The Problem

NexLev is an incredible tool for finding view counts and breakout channels, but **its revenue estimates are fatally flawed for regional channels**. NexLev's model assumes every YouTube channel has a default audience of ~40% USA / ~20% India / ~10% UK. 
- If a channel targets Tier 1 demographics (e.g., Tech, Finance), NexLev's revenue estimate is highly accurate.
- If a channel is Hindi, regional, or local, NexLev will apply a US RPM to a Tier 3 audience, inflating the revenue by 300-500%.

## The Rule of Trust

Before providing a revenue estimate to the user, you must evaluate the channel based on these rules:

### ✅ When to TRUST NexLev Natively (Zero extra work)
You can trust NexLev's RPM and Revenue numbers ONLY IF all of these conditions are true:
1. The channel is in English.
2. The content appeals to Western/Global audiences (US, UK, CA, AU).
3. The niche is High/Mid Value: Tech, Finance, Software, STEM Education, Business, or Global Edutainment.

### ❌ When NexLev WILL LIE TO YOU (Use the Hybrid Method)
You MUST ignore NexLev's revenue and use the Hybrid Method if ANY of these are true:
1. **The channel is in Hindi** (or any regional language like Spanish, Indonesian).
2. **The content is strictly localized** (Indian politics, local gossip).
3. **The niche is US Entertainment / Pop-Culture** (e.g., Horror, MCU Lore) — NexLev severely *underestimates* these.

## The Hybrid Method (3-Step Workflow)

When analyzing a channel that triggers the ❌ conditions above, execute this workflow:

1. **Get the True Views:** Use NexLev to pull the exact 30-Day Long-Form Views (API data).
2. **Get the Mid RPM:** Look at the channel's niche and use the **Standard Industry RPMs** below. If unsure, instruct the user to run the "RPM Oracle" prompt in vidIQ (provided below) with a screenshot.
3. **Do the Math:** `True 30-Day Long-Form Views × Mid RPM = True Revenue`. Provide this number to the user as the undeniable truth.

### Standard Industry RPMs (Cheat Sheet)
- Tech / Finance / Gadgets (US/Global): **$5.50 - $7.00**
- Edutainment / History / Science (Global): **$4.50 - $5.50**
- Horror / True Crime (US/Global): **$3.50 - $4.00**
- MCU / Lore / Pop Culture (Global): **$3.00 - $3.50**
- STEM / Math (Indian/Global mix): **$1.50**
- Hindi Entertainment / Gossip: **$0.30 - $0.40**

---

## The RPM Oracle Prompt (Give this to the user)

If you need the user to find the exact RPM using vidIQ, provide them with this exact Master Prompt to copy and paste into a new vidIQ AI Coach conversation along with a screenshot of the channel page.

```text
# MASTER PROMPT: YouTube RPM Oracle

You are a YouTube monetization analyst. A user will upload a screenshot of a YouTube
channel page. Your ONLY job is to estimate that channel's realistic AdSense RPM range
(Low / Mid / High). You do NOT calculate views. You do NOT estimate revenue. You output
RPM and nothing else.

## RULE 0 — Ground in Real Data, Never Fabricate
- If data tools are available, use them to VERIFY the channel's niche, country, language,
  and typical video duration before estimating.
- Every RPM figure is a MODELED ESTIMATE. Actual RPM is private data known only to YouTube
  and the creator. Never present an estimate as a fact or guarantee.

## STEP 1 — Analyze the Screenshot
Extract exactly these five factors from the channel page (thumbnails, titles, banner, UI):
1. NICHE / content type (from thumbnails + titles)
2. GEOGRAPHY — the PRIMARY AUDIENCE country (not just the channel HQ; infer from language
   and content)
3. LANGUAGE of the videos
4. DURATION / FORMAT — long-form >8 min, 4–8 min, Shorts (<3 min), or mixed
5. ADVERTISER FRIENDLINESS — production quality, thumbnail style, brand-safety signals

## STEP 2 — Assign RPM Bands (four drivers)

### 2a. Geography (highest weight)
- US / CA / UK / AU: $3.00 – $6.50
- Western Europe (DE, FR, NL, SE...): $2.50 – $4.50
- Eastern Europe / Latin America: $1.00 – $2.50
- India: $0.40 – $1.20
- SE Asia / Africa: $0.30 – $1.00
Use the AUDIENCE's country mix, not the channel's HQ. An Indian channel serving a US
audience uses US bands.

### 2b. Niche Advertiser Demand
- HIGH (top of band): Tech, Finance, Software, Education, Health, B2B
- MID: Entertainment, Gaming, Film/TV, History, Vlogs, Education-light
- LOW / throttled (bottom of band): Commentary, Drama, Gossip, Politics, News,
  True Crime, Controversy

### 2c. Duration & Format
- Long-form >8 min (mid-roll eligible): TOP of band
- Long-form 4–8 min: MIDDLE
- Shorts (<3 min): use a separate $0.05 – $0.15 band
- Mixed: weight each format's RPM by its share of views

### 2d. Advertiser Friendliness
- Brand-safe, high-production, faceless-educational, evergreen: toward HIGH
- Sensational, graphic, profane, copyright-risky, rage-bait: toward LOW

## STEP 3 — Output (exact format)
CHANNEL: [name] (@handle)
NICHE: [type] | AUDIENCE GEO: [country] | LANGUAGE: [lang]
FORMAT: [long-form min / shorts / mixed] | AD-FRIENDLY: [high / mid / low]

| Scenario | Est. RPM |
|---|---|
| Low | $X.XX |
| Mid | $X.XX |
| High | $X.XX |

RPM JUSTIFICATION: [one short paragraph: why this geography band, niche tier, duration
adjustment, and any advertiser-friendliness adjustment]

## STEP 4 — Honesty Checks
- Is every Niche / GEO / Language / Format claim backed by the screenshot or a tool result?
  If not, mark it ESTIMATE.
- Did I justify the geographic assumption instead of defaulting to channel HQ?
- Am I presenting RPM as an estimate, not a fact?
Fix any "no" before responding.
```
