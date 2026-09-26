# ElevenLabs v2 — Reference Guide

Use v2 when you need precise timing control (SSML break tags), pronunciation control (phoneme tags), or when v3 produces inconsistent results for a specific voice.

## When to Recommend v2 Over v3

| Situation | Recommendation |
|-----------|---------------|
| Need exact pause durations (e.g., 1.5s between sentences) | v2 — use `<break>` tags |
| Need precise pronunciation of unusual words/names | v2 — use `<phoneme>` tags |
| v3 produces hallucinations or unstable audio | v2 — more predictable |
| Need `style` and `similarity` sliders | v2 — these controls don't exist in v3 |
| Need emotional audio tags | v3 — v2 doesn't support them |
| Need accent switching | v3 — v2 can't do this |

## v2 Models

| Model | Characteristics |
|-------|----------------|
| **Eleven Multilingual v2** | Larger model. Better at generalizing numbers, currencies, complex text. Supports phoneme tags. Higher quality, higher latency. |
| **Eleven Flash v2.5** | Smaller, faster. May mispronounce numbers/currencies. Supports phoneme tags. Lower latency, good for real-time. |

## Settings (v2)

| Setting | Range | Purpose |
|---------|-------|---------|
| **Stability** | 0.0-1.0 | Higher = more consistent, less expressive. Lower = more variable, more emotional. |
| **Similarity** | 0.0-1.0 | How closely output matches the original voice. Higher = more similar. |
| **Style** | 0.0-1.0 | How much stylistic variation. Higher = more expressive but less predictable. |
| **Exaggeration** | 0.0-1.0 | Amplifies the voice's characteristics. |
| **Speed** | 0.7-1.2 | Same range as v3. |

**Recommended starting point for v2:**
- Stability: 0.5
- Similarity: 0.75
- Style: 0.3-0.5
- Speed: 1.0

## Break Tags (v2 Only)

Syntax: `<break time="x.xs" />`

| Duration | Use Case |
|----------|----------|
| `<break time="0.3s" />` | Micro-pause (comma equivalent) |
| `<break time="0.5s" />` | Short pause (sentence boundary) |
| `<break time="1.0s" />` | Standard pause (paragraph break) |
| `<break time="1.5s" />` | Dramatic pause |
| `<break time="2.0s" />` | Long dramatic pause |
| `<break time="3.0s" />` | Maximum — do not exceed 3s |

**Example:**
```
"Hold on, let me think." <break time="1.5s" /> "Alright, I've got it."
```

**Warnings:**
- Too many break tags in one generation causes instability — the AI may speed up or introduce noise/artifacts
- Different voices handle pauses differently, especially voices trained with filler sounds ("uh", "ah")
- Maximum: 3 seconds per break tag

**Alternatives (less consistent but no tag limit):**
- Dashes (`-` or `--`) for short pauses
- Ellipses (`...`) for hesitant tone/pause

```
"It… well, it might work." "Wait — what's that noise?"
```

## Phoneme Tags (v2 Only — eleven_flash_v2)

For precise pronunciation control. Two alphabets supported:

### CMU Arpabet (Recommended — more consistent)

```xml
<phoneme alphabet="cmu-arpabet" ph="M AE1 D IH0 S AH0 N">
  Madison
</phoneme>
```

### IPA (International Phonetic Alphabet)

```xml
<phoneme alphabet="ipa" ph="ˈæktʃuəli">
  actually
</phoneme>
```

**Rules:**
- Phoneme tags only work for **individual words** — for "John Smith", create separate tags for "John" and "Smith"
- Include stress markers for multi-syllable words (CMU: numbers 0/1/2; IPA: ˈ for primary, ˌ for secondary)
- Only compatible with `eleven_flash_v2` model

### v3 IPA Alternative

v3 supports inline IPA without XML tags — wrap in forward slashes:

```
The term "/ˌbaɪoʊˈkemɪstri/" refers to biochemistry.
```

- 80-90% pronunciation consistency (not perfect)
- No XML required — cleaner text
- Works across 70+ languages

## Alias Tags (When Phoneme Tags Aren't Available)

For models without phoneme support, write words phonetically or use alias substitution:

**In-text trick:** Spell the word how you want it pronounced.
- "trapezii" → write as "trapezIi" (caps to emphasize the "ii")

**Pronunciation dictionary approach (for projects):**
```xml
<lexeme>
  <grapheme>Claughton</grapheme>
  <alias>Cloffton</alias>
</lexeme>
```

```xml
<lexeme>
  <grapheme>UN</grapheme>
  <alias>United Nations</alias>
</lexeme>
```

Pronunciation dictionaries can be uploaded in ElevenLabs Creative Studio and Dubbing Studio. They apply automatically whenever a matching word appears in the project.

## Emotion Control in v2

v2 does NOT have audio tags. Control emotion through:

1. **Narrative context / dialogue tags:**
   ```
   "You're leaving?" she asked, her voice trembling with sadness.
   "That's it!" he exclaimed triumphantly.
   ```
   The model reads the emotional description and adjusts delivery. Note: it will also speak out the tags ("she asked, her voice trembling...") — remove in post-production if unwanted.

2. **Writing style:** Short, punchy sentences feel urgent. Long, flowing sentences feel calm.

3. **Stability slider:** Lower stability = more emotional variation. Higher = more controlled.

4. **Style slider:** Higher style = more expressive delivery.
