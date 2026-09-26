# ElevenLabs v3 — Complete Reference

## Audio Tags — Full Working List

These tags are confirmed functional with Eleven v3. Effectiveness depends on the voice's training data — a calm voice won't execute `[shouting]` well.

### Emotion/Delivery Tags

| Tag | Best For | Notes |
|-----|----------|-------|
| `[happy]` | Upbeat narration | Works broadly across most voices |
| `[sad]` | Emotional moments | Subtle — don't pair with excited text |
| `[excited]` | Reveals, celebrations | Strong effect on expressive voices |
| `[angry]` | Conflict, frustration | Can overwhelm — use sparingly |
| `[scared]` | Horror, tension | Pairs well with `[whispers]` |
| `[curious]` | Questions, discovery | Raises pitch slightly |
| `[sarcastic]` | Comedy, commentary | Voice-dependent — test first |
| `[annoyed]` | Mild frustration | Subtler than `[angry]` |
| `[appalled]` | Shock, disbelief | Strong emotional spike |
| `[thoughtful]` | Reflection, analysis | Slows delivery naturally |
| `[surprised]` | Reveals, twists | Brief energy spike |
| `[mischievously]` | Playful, scheming | Works on lighter voices |
| `[sympathetic]` | Comforting moments | Soft, warm delivery |
| `[reassuring]` | Calming, supportive | Even, steady tone |
| `[professionally]` | Business, formal | Neutral, measured |
| `[dramatically]` | Climactic moments | Big delivery — use at peaks only |
| `[deadpan]` | Dry humor, contrast | Flat delivery — effective for comedy |
| `[dismissive]` | Rejection, indifference | Quick, throwaway delivery |
| `[warmly]` | Connection, kindness | Gentle, approachable |
| `[nervously]` | Anxiety, uncertainty | Slight hesitation in delivery |
| `[frustrated]` | Struggle, annoyance | Between annoyed and angry |
| `[passionately]` | Conviction, inspiration | Strong, energetic |
| `[firmly]` | Authority, certainty | Controlled power |
| `[gently]` | Soft guidance | Meditation, bedtime stories |
| `[calmly]` | Even, peaceful | No emotional spikes |
| `[urgently]` | Breaking news, danger | Fast, pressured delivery |

### Non-Verbal Tags

| Tag | Effect | Use Case |
|-----|--------|----------|
| `[whispers]` | Drops to whisper | Secrets, tension, intimacy |
| `[sighs]` | Audible sigh | Resignation, relief, tiredness |
| `[exhales]` | Breath out | Tension release, pauses |
| `[laughs]` | Laughter | Joy, amusement |
| `[laughs harder]` | Bigger laugh | Building comedy |
| `[starts laughing]` | Laugh building up | Mid-sentence break |
| `[wheezing]` | Extreme laughter | Comedy peaks |
| `[chuckles]` | Soft laugh | Mild amusement |
| `[crying]` | Tears in voice | Emotional scenes |
| `[snorts]` | Dismissive laugh | Comedy, disbelief |
| `[clears throat]` | Throat clear | Transitions, nervousness |
| `[inhales deeply]` | Deep breath | Before important statements |
| `[exhales sharply]` | Quick breath out | Shock, surprise reaction |
| `[gulps]` | Audible swallow | Fear, nervousness |
| `[short pause]` | Brief pause | Beat between thoughts |
| `[long pause]` | Extended pause | Dramatic weight |
| `[trembling voice]` | Shaky delivery | Fear, extreme emotion |

### Special Tags

| Tag | Effect | Notes |
|-----|--------|-------|
| `[strong X accent]` | Switches accent | Replace X: French, Russian, Indian, etc. Less consistent — test thoroughly |
| `[sings]` | Singing delivery | Unreliable. Only use with voices trained on singing |
| `[singing quickly]` | Fast singing | Same caveat as above |

## Voice Selection (v3)

The voice you choose is the MOST important parameter. Tags modify the voice's natural delivery — they cannot force it into something completely different.

**Rules:**
- If the voice is calm/neutral in its training data, tags like `[angry]` or `[shouting]` will underperform
- If the voice already has emotional range in its training data, tags are highly effective
- Neutral voices are more stable across languages and styles
- Emotionally diverse voices are better for storytelling and expressive content

**Voice types for common use cases:**
- **Storytelling**: Emotionally diverse voice (trained on varied tones)
- **Educational**: Neutral, clear voice (consistent, reliable)
- **News**: Neutral, authoritative voice
- **Meditation**: Soft, calm voice (trained on gentle speech)
- **Motivational**: Energetic, passionate voice

**IVC vs PVC:**
- Instant Voice Clones (IVC) work better with v3 currently
- Professional Voice Clones (PVC) are not fully optimized for v3 yet — quality may be lower

## Stability Settings

The stability slider is the most important setting in v3.

| Setting | Behavior | When to Use |
|---------|----------|-------------|
| **Creative** | Most emotional, most expressive. Responds strongly to audio tags. Risk: occasional hallucinations or unstable output. | Horror, motivational, storytelling — anything needing strong emotional delivery |
| **Natural** | Closest to the original voice recording. Balanced expression and consistency. | Educational, general narration, Hinglish content — reliable baseline |
| **Robust** | Highly stable and consistent. Barely responds to audio tags. Similar to v2 behavior. | News, formal content, or when v3 creative/natural produces inconsistent results |

**Rule of thumb:** Start with Natural. Move to Creative if you need more expression. Move to Robust only if Natural is too variable.

## Speed Setting

Range: 0.7 (minimum, slowest) to 1.2 (maximum, fastest). Default: 1.0.

| Speed | Use Case |
|-------|----------|
| 0.7-0.85 | Meditation, ASMR, calm narration |
| 0.85-0.95 | Horror (slow tension), bedtime stories |
| 1.0 | Default — educational, general narration |
| 1.0-1.1 | Motivational (energy), conversational |
| 1.1-1.2 | News (brisk), energetic commentary |

**Warning:** Extreme values (0.7 or 1.2) may affect audio quality. Stay within 0.8-1.15 for best results.

## Punctuation Effects on v3

v3 does NOT support SSML `<break>` tags. Use punctuation and text structure instead:

| Punctuation | Effect on v3 |
|-------------|-------------|
| Comma `,` | Micro-pause (0.2-0.3s feel) |
| Period `.` | Standard sentence-end pause |
| Ellipsis `...` | Weighted pause — adds hesitation or dramatic weight |
| Em dash `—` | Sharp interruption/cut |
| Exclamation `!` | Energy spike in delivery |
| Question mark `?` | Rising intonation |
| ALL CAPS word | Vocal emphasis on that word |
| Line break | Natural breath point |

**Ellipses are your primary pause tool in v3.** They are more reliable than audio tags like `[pause]` for controlling timing.

## Single-Speaker Example: Expressive Monologue

This is the ElevenLabs reference example showing effective v3 tag usage for a single speaker:

```
"Okay, you are NOT going to believe this.

You know how I've been totally stuck on that short story?

Like, staring at the screen for HOURS, just... nothing?

[frustrated sigh] I was seriously about to just trash the whole thing. Start over.

Give up, probably. But then!

Last night, I was just doodling, not even thinking about it, right?

And this one little phrase popped into my head. Just... completely out of the blue.

And it wasn't even for the story, initially.

But then I typed it out, just to see. And it was like... the FLOODGATES opened!

Suddenly, I knew exactly where the character needed to go, what the ending had to be...

It all just CLICKED. [happy gasp] I stayed up till, like, 3 AM, just typing like a maniac.

Didn't even stop for coffee! [laughs] And it's... it's GOOD! Like, really good.

It feels so... complete now, you know? Like it finally has a soul.

I am so incredibly PUMPED to finish editing it now.

It went from feeling like a chore to feeling like... MAGIC. Seriously, I'm still buzzing!"
```

**What makes this effective:**
- CAPS on key emotional words (NOT, HOURS, FLOODGATES, CLICKED, GOOD, PUMPED, MAGIC)
- Ellipses for pauses and hesitation
- Audio tags placed at emotional peaks, not every sentence
- Natural speech patterns (incomplete sentences, "like", "you know?")
- Mix of tag types (sigh, gasp, laughs) for variety

## The ElevenLabs "Enhance" Prompt

ElevenLabs built this into their UI. This is their own LLM prompt for adding audio tags — use it as a quality benchmark for your enhancements:

**Core rules from ElevenLabs' own system:**
1. Add audio tags to make text more expressive for speech — tags MUST describe something auditory
2. NEVER alter, add, or remove words from the original text
3. Audio tags are NEW additions, not reformatting of existing narrative descriptions
4. Do NOT use visual tags: `[standing]`, `[grinning]`, `[pacing]`, `[music]`
5. Do NOT use tags for anything other than voice (no music, no sound effects in narration)
6. Can add emphasis via CAPS, question marks, exclamation marks, and ellipses
7. Output ONLY the enhanced text — no explanations

**Tag placement from ElevenLabs:**
- Before the dialogue: `[appalled] Are you serious?`
- After the dialogue: `I guess you're right. [sighs]`
- At natural pauses: `I can't believe you did that! [sighs]`
- Mid-text for emphasis shift: `[muttering] difficult.`
