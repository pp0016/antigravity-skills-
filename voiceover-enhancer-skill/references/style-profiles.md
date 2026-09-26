# Style Profiles — Input/Output Examples

Each style profile shows a raw input and the expected enhanced output. Use these as quality benchmarks.

---

## Horror/Thriller

**Settings:** v3 | Stability: Creative | Speed: 0.85-0.9

**Raw Input:**
```
The house had been empty for years. Nobody talked about what happened there. One night, a group of friends decided to explore. They pushed open the front door. Inside, it was completely dark. Something moved in the corner. They heard breathing. It wasn't one of them.
```

**Enhanced Output:**
```
The house had been empty for years. Nobody talked about what happened there.

One night... a group of friends decided to explore.

They pushed open the front door. [exhales] Inside, it was COMPLETELY dark.

Something moved in the corner.

[whispers] They heard breathing.

...It wasn't one of them.
```

**What changed:**
- Added line breaks for pacing — separates tension beats
- Ellipsis after "One night..." adds dramatic weight
- `[exhales]` before the darkness reveal — breath of tension
- CAPS on "COMPLETELY" for emphasis
- `[whispers]` before the breathing line — drops energy for fear
- Leading ellipsis on final line — pause before the twist

---

## Motivational

**Settings:** v3 | Stability: Creative or Natural | Speed: 1.0-1.1

**Raw Input:**
```
Everyone will tell you it's impossible. They'll say you're not smart enough, not experienced enough, not connected enough. But here's what they don't understand. Every successful person was once where you are right now. Doubting. Struggling. Afraid. The difference is they didn't stop. They kept going. And so will you.
```

**Enhanced Output:**
```
Everyone will tell you it's impossible.

They'll say you're not smart enough, not experienced enough, not connected enough.

[firmly] But here's what they don't understand.

Every successful person was once where YOU are... right now.

Doubting. Struggling. Afraid.

[passionately] The difference is they didn't stop. They KEPT going.

And so will YOU.
```

**What changed:**
- Short sentences on separate lines for punchy delivery
- `[firmly]` before the counter-argument — authority shift
- CAPS on "YOU" for personal address emphasis
- Ellipsis before "right now" — weight on the realization
- Three short words on one line (Doubting. Struggling. Afraid.) — rhythmic punch
- `[passionately]` at the climactic turn
- CAPS on "KEPT" and final "YOU" — driving home the point

---

## Educational/Explainer

**Settings:** v3 | Stability: Natural | Speed: 1.0

**Raw Input:**
```
Photosynthesis is the process by which plants convert sunlight into energy. It happens in the chloroplasts, which contain a green pigment called chlorophyll. The plant takes in carbon dioxide from the air and water from the soil. Using sunlight, it converts these into glucose and oxygen. The glucose is used for energy, and the oxygen is released into the atmosphere. This is why plants are essential for life on Earth.
```

**Enhanced Output:**
```
Photosynthesis is the process by which plants convert sunlight into energy.

It happens in the chloroplasts, which contain a green pigment called chlorophyll.

The plant takes in carbon dioxide from the air... and water from the soil.

[thoughtfully] Using sunlight, it converts these into glucose and oxygen.

The glucose is used for energy, and the oxygen is released into the atmosphere.

This is why plants are ESSENTIAL for life on Earth.
```

**What changed:**
- Minimal tagging — educational content should sound clear, not dramatic
- Line breaks between sentences for natural breathing/pacing
- One ellipsis (before "and water") to let the first concept land
- One `[thoughtfully]` before the key process explanation
- One CAPS on "ESSENTIAL" — the takeaway word
- No exclamation marks — educational tone stays measured

---

## News

**Settings:** v3 | Stability: Robust | Speed: 1.0-1.05

**Raw Input:**
```
The government announced today that inflation has dropped to 4.2 percent, the lowest in 18 months. Finance Minister Nirmala Sitharaman said the new policies are showing results. Markets responded positively, with the Sensex rising 500 points. However, food prices remain high, especially for vegetables and pulses. Economists warn that the situation could change if global oil prices increase.
```

**Enhanced Output:**
```
[professionally] The government announced today that inflation has dropped to four point two percent, the lowest in eighteen months.

Finance Minister Nirmala Sitharaman said the new policies are showing results.

Markets responded positively, with the Sensex rising five hundred points.

However, food prices remain high... especially for vegetables and pulses.

Economists warn that the situation could change if global oil prices increase.
```

**What changed:**
- One `[professionally]` at the start — sets the tone, then let content carry
- Numbers normalized: "4.2" → "four point two", "18" → "eighteen", "500" → "five hundred"
- One ellipsis before "especially" — slight emphasis on the caveat
- No CAPS, no exclamation marks — factual, authoritative delivery
- Line breaks between topics for clear segment transitions

---

## Meditation/ASMR

**Settings:** v3 | Stability: Natural | Speed: 0.8-0.85

**Raw Input:**
```
Close your eyes. Take a deep breath in. And slowly let it out. Feel your body relaxing. Your shoulders dropping. Your jaw unclenching. You are safe here. There is nothing you need to do right now. Just breathe. In and out. Let every thought drift away like clouds passing through the sky. You are at peace.
```

**Enhanced Output:**
```
[gently] Close your eyes.

Take a deep breath in...

And slowly... let it out.

[softly] Feel your body relaxing. Your shoulders dropping. Your jaw unclenching.

You are safe here.

...There is nothing you need to do right now.

[calmly] Just breathe. In... and out.

Let every thought drift away... like clouds passing through the sky.

...You are at peace.
```

**What changed:**
- `[gently]`, `[softly]`, `[calmly]` — all soft tags, no energy spikes
- Heavy ellipsis usage — creates slow, breathing pace
- Leading ellipsis on some lines (...There is, ...You are) — weight before the statement
- No CAPS anywhere — meditation must feel soft
- No exclamation marks — zero energy spikes
- Short lines with generous spacing — slow reading pace
- "In... and out" — ellipsis mimics the breathing rhythm

---

## Adding a Custom Style

To add a new style, provide these 5 elements:

```
Style Name: [e.g., Comedy/Sarcastic]

1. Detection signals: [keywords that identify this style in text]
   e.g., jokes, punchlines, irony, "imagine", absurd comparisons

2. Preferred tags: [which audio tags fit]
   e.g., [sarcastic], [deadpan], [laughs], [dismissive], [dramatically]

3. Pacing rules: [delivery speed and rhythm]
   e.g., Setup lines at normal pace. Pause before punchlines.
   Punchlines short and punchy.

4. Emphasis rules: [how to use CAPS, punctuation]
   e.g., CAPS on absurd words for ironic emphasis.
   Ellipsis before punchlines for timing.

5. Recommended settings:
   Model: v3
   Stability: Creative (for maximum expression)
   Speed: 1.0-1.1 (slightly fast, energetic)
```

Then provide one input/output example pair so the AI calibrates.
