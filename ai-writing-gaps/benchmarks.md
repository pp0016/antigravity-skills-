# Competitor Benchmarks — ai-writing-gaps

> Quantitative reference card from forensic analysis of 9 competitor videos across 4 channels.
> **Corpus:** 24,035 words | ~2.5 hours of content | 4 channels | 9 videos

---

## Cross-Corpus Averages

| Metric | Competitor Average | Notes |
|--------|-------------------|-------|
| Time to topic | 0.10 seconds | Zero throat-clearing. Topic in first word. |
| Speech rate | 149.8 WPM | Range: 127.9 (Kratom calm) to 178.2 (Nice People Snapped) |
| Source density | 10.23 named sources / 1K words | Range: 4.38 to 16.25 |
| Flesch-Kincaid grade | 9.6 | Range: 7.1 (EverythingProfessor) to 12.2 (The Analyst) |
| Flesch reading ease | 60.7 / 100 | Range: 48.5 to 74.8 |
| Segment count | 10.0 per video | Range: 3 (Serious History) to 15 (Brofessor Stein) |
| Segment duration | 164.3 seconds | Range: 58.4s to 574.6s |
| Outro duration | < 4 seconds | Range: 0.29s to 9.0s |
| Outro word count | < 5 words | Most are 0 words |
| Tier-3 detail density | 2+ per 1,000 words | The "Wrong Detail" minimum |
| Register collisions | 3-4 per script | Modern slang in formal context |
| Narrator reactions | 1+ per segment | Fourth-wall breaks, sarcasm, "you" |
| Hedged positions | 0 per script | BANNED across all competitors |
| Pop culture anchors | 1 per complex concept | Audience-world comparisons |

---

## Per-Channel Metrics

### Brofessor Stein ($62 RPM)
| Video | Duration | Words | WPM | Grade | Sources/1K | Segments | Avg Segment |
|-------|----------|-------|-----|-------|-----------|----------|-------------|
| Mystical Artifacts | 17:10 | 2,367 | 137.8 | 10.8 | 13.52 | 12 | 85.4s |
| Censored Symbols | 16:07 | 2,342 | 145.3 | 11.4 | 11.96 | 15 | 64.5s |
| Disturbing Books | 19:10 | 2,756 | 143.7 | 10.6 | 9.43 | 13 | 88.5s |

### EverythingProfessor (Fastest Growth)
| Video | Duration | Words | WPM | Grade | Sources/1K | Segments | Avg Segment |
|-------|----------|-------|-----|-------|-----------|----------|-------------|
| Manipulation Techniques | 12:25 | 1,826 | 147.1 | 7.1 | 4.38 | 8 | 93.1s |
| Rare Drugs & Effects | 20:58 | 2,987 | 142.5 | 8.2 | 6.03 | 12 | 104.8s |

### Serious History (6.35M Breakout)
| Video | Duration | Words | WPM | Grade | Sources/1K | Segments | Avg Segment |
|-------|----------|-------|-----|-------|-----------|----------|-------------|
| Extreme Vigilante Justice | 29:02 | 4,700 | 161.9 | 8.2 | 8.94 | 3 stories | 574.6s |
| When Nice People Snapped | 16:32 | 2,946 | 178.2 | 7.4 | 11.54 | 3 stories | 327.6s |

### The Analyst (4.36M Views)
| Video | Duration | Words | WPM | Grade | Sources/1K | Segments | Avg Segment |
|-------|----------|-------|-----|-------|-----------|----------|-------------|
| Every Banned Book | 15:04 | 2,325 | 155.6 | 10.4 | 11.61 | 11 | 81.5s |
| Every Government Form | 12:40 | 1,723 | 136.1 | 12.2 | 16.25 | 13 | 58.4s |

---

## Hook Architecture Benchmark

All 9 videos follow this hook structure:

```
[0-8 seconds]   Category Anchor / Topic Name / Character Introduction
[8-18 seconds]  Paradox, Discord, or Cognitive Contradiction
[18-30 seconds] Macro Promise (what the viewer will learn/feel)
```

| Channel | Hook Timing | Hook Type |
|---------|------------|----------|
| Brofessor Stein | 0.00-0.22s | Tactile Artifact Anchor |
| EverythingProfessor | 0.10-0.20s | 1-Word Category Drop |
| Serious History | 0.00s (topic), 7.8s (character) | In-Medias-Res Cold Open |
| The Analyst | 0.10-0.18s | Taxonomic Prime / Cross-Domain Metaphor |

---

## Outro Architecture Benchmark

| Channel & Video | Final Sentence Theme | Outro Words | Tail Duration |
|----------------|---------------------|-------------|---------------|
| Brofessor Stein (Artifacts) | Imperial Seal lost 10th century | 0 | 5.8s |
| Brofessor Stein (Symbols) | Falun Gong in Indonesia | 2 ("Thank you") | 0.6s |
| Brofessor Stein (Books) | Blindness cure spreads | 0 | 5.6s |
| EverythingProfessor (Manipulation) | DARVO truth & cruelty | 0 | 3.6s |
| EverythingProfessor (Drugs) | Toad venom deletion | 0 | 3.0s |
| Serious History (Vigilante) | Host update | 38 | 9.0s |
| Serious History (Nice People) | Queen's funeral mystery | 0 | 4.2s |
| The Analyst (Banned Books) | Invisible Man invisible | 0 | 6.5s |
| The Analyst (Gov Forms) | Totalitarian abuse | 2 | 0.29s |

---

## Pacing & Intensity Benchmarks

### WPM by Emotional Context
| Context | WPM Range | Purpose |
|---------|-----------|--------|
| Calm setup / seduction | 127-138 WPM | Build false comfort |
| Standard narration | 140-150 WPM | Baseline delivery |
| Action / escalation | 155-165 WPM | Urgency and momentum |
| Frantic climax | 165-185 WPM | Peak tension |
| Clinical deceleration | 125-138 WPM | Horror, paralysis, dread |

### Inter-Segment Gaps
| Transition Type | Gap Duration |
|----------------|-------------|
| Staccato topic snap | 0.20-0.80s |
| Story-to-story | 1.5-2.0s |
| Breather reset | 2.0-4.0s |

---

## Scoring Thresholds

Use these to calibrate the 1-10 scores in the QA checklist:

| Score | Meaning | Benchmark Comparison |
|-------|---------|---------------------|
| 10 | Elite | Matches or exceeds best competitor video |
| 8-9 | Strong | Within range of competitor averages |
| 6-7 | Acceptable | Below competitor average but not AI-detectable |
| 4-5 | Weak | Noticeably below competitor standard |
| 1-3 | Failed | AI-level performance, needs complete rewrite |

---

## Algorithmic Drop-Off Profile

Where viewers abandon AI-generated scripts:

| Drop-Off Point | What Causes It | Viewer Loss |
|---------------|----------------|-------------|
| 0:30 Hook Cliff | Rhetorical questions, throat-clearing intros, "Hey guys" | ~45% at 0:30 |
| 2:30 Monotony Trough | Unbroken rhythm of 20-word sentences without tonal shifts | Steady bleed |
| Outro Announce Cliff | "In conclusion" / "To summarize" / any recap signal | ~70% of remaining |

## Verbatim Competitor Hook Quotes

| Channel | Video | Exact Opening Words |
|---------|-------|--------------------|
| Brofessor Stein | Mystical Artifacts | "The Voynich Manuscript, this 15th century book made of calfskin parchment, is dubbed the world's most mysterious book." |
| EverythingProfessor | Manipulation | "Gaslighting. Everyone's heard of gaslighting, but not everyone knows what it is..." |
| Serious History | Vigilante Justice | "John Brown. It's 1856 and a radical abolitionist has just watched pro-slavery forces burn Lawrence, Kansas to the ground." |
| The Analyst | Banned Books | "Lady Chatterley's Lover. It's the early 1900s and a book so scandalous it could give a nun a heart attack..." |

## Channel Performance Context

| Channel | Total Views | VPH | RPM | Niche |
|---------|------------|-----|-----|-------|
| Brofessor Stein | 1.5M | — | $62 | Esoteric history |
| EverythingProfessor | 5.1M | — | — | Psychopharmacology |
| Serious History | 6.35M | 362 | — | Historical drama |
| The Analyst | 4.36M | — | — | Systems analysis |
