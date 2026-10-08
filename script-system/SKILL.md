---
name: script-system
description: >-
  Write and audit high-retention faceless YouTube scripts for TTS narration. Pulls reference
  transcripts, comments and stats through the vidIQ MCP, analyses what makes them retain, then
  writes an original script against a locked retention format. Budgets by measured speaking pace
  (never a fixed words-per-minute), writes hooks to pay off the title, tags every line with a
  visual, prepares text for ElevenLabs, bans drop-off structures (numbered sections, announced
  roadmaps, self-disclaiming hooks, verdict-less payoffs, mid-video comment prompts), and screens
  for AI-voice tells and fabricated citations.
  Triggers on: write a script, YouTube script, video script, faceless script, script from a
  reference video, analyse a reference video, pull a transcript, fact-check a script, score a
  script, script retention, hook, re-hooks, book summary script, audiobook script, TTS script.
---

# Script System

Everything needed to run is in this file. Paths are for depth only.

| File (in `C:\Users\renu5\Downloads\script writting idea\`) | Contains |
|---|---|
| `MCP-SCRIPTWRITER.md` | This flow as one paste-in prompt |
| `SCRIPT-SYSTEM.md` | vidIQ-website path + book-summary template §8 |
| `FACT-CHECK.md` | Fact screen, source tiers, per-niche source directories |
| `SCORE-GATE.md` | 100-point rubric → /10, and how to calibrate it |
| `HANDOFF.md` §3 | Measurements behind each rule, with confidence labels |

## Rules that override everything

1. **Never audit a script in the conversation that wrote it.** A session once graded its own
   script 9.5/10; a clean pass measured about 6.5–7 and found four factual errors.
2. **Never accept a self-reported word count or runtime.** Count.
3. **Never assume a speaking pace.** Budget from a measured WPM (Step 0).

## Step 0 — packaging and pace, before any analysis

**Title and thumbnail concept first.** The hook's job is to confirm the promise the viewer clicked
on. If no title exists, draft 3 with `vidiq_generate_titles`, score them with `vidiq_score_title`,
and agree one before writing. The hook is written to that title.

**Measure WPM.** In priority order:
1. **Owner's TTS voice** — ElevenLabs output: words in a ~200-word paragraph ÷ its audio length.
   This is the correct number. Ask for it if unknown.
2. **Reference pace** — measured in Phase 1 (transcript words ÷ runtime). Fast-paced explainer
   channels commonly run 200–250 wpm; the Ice Age reference ran roughly 230–250.
3. **150 wpm** — documentary default. Only if neither above exists, and say so in the report.

Then:
```
WORD BUDGET = RUNTIME (min) × WPM          (±5%)
HOOK CAP    = seconds below × WPM ÷ 60
RE-HOOK     = seconds below × WPM ÷ 60
```

| Runtime | Hook cap | Re-hook every |
|---|---|---|
| under 12 min | 35 s | 45–60 s |
| 12–20 min | 45 s | 45–60 s (under 15) / 75–90 s (15+) |
| 20–35 min | 50 s | 75–90 s |
| 35 min+ | 60 s | ~120 s |

State WPM (and its source), word budget, hook cap in words, and re-hook interval in words before
anything else.

**Hook rotation.** Ask which hook types the last 3 videos on this channel used. Do not repeat the
same type twice in a row: mystery object · live stake · anomaly · scenario · uncomfortable claim ·
reversal. Templated sameness across a channel is a risk under YouTube's inauthentic-content
policy (mass-produced, repetitive videos), not only a creative problem.

## PHASE 1 — pull and analyse. Stop at the end.

**Choose references by outlier score, not raw views.** Use `vidiq_outliers` or compare views ÷
subscribers. An 80K-view video from a 3K-sub channel teaches more than 900K from a 5M-sub channel.

Per reference: `vidiq_video_transcript` (timestamped) · `vidiq_video_comments` (100+, by likes) ·
`vidiq_video_stats`.

The retention heatmap for **other people's** videos is not exposed by any vidIQ MCP tool — never
claim or simulate it. Substitute: comments.

**Comment filtering.** Most-liked comments are often jokes, not signals. First extract every comment
containing a **timestamp** ("3:45 got me") — those point directly at moments that landed. Then
top-liked comments. Report both lists and map them to transcript moments.

Produce per video:
1. **Pace** — transcript words ÷ runtime = WPM. Measured.
2. **Hook** — first 15 s verbatim, word count, beats labelled, technique named, and how it pays
   off the video's title.
3. **Structure** — sections with duration, then the organising *principle*.
4. **Re-hooks** — quote, timestamp, type, average interval in seconds.
5. **Transitions** — quote three; name the mechanism.
6. **Retention devices** — loops planted/paid/held, direct address, analogies, unit translations.
7. **Voice** — six patterns with quotes, average sentence length.
8. **Comment moments** — timestamp comments first, then top-liked.
9. **Ending** — how it hands the viewer to another video, if at all.

With 2–3 references: what they all do **identically** (retention grammar — follow it) · where they
**diverge** (room to be original) · what they all **fail** to do (differentiator).

End with exactly **5 numbered carry-forward rules**. Write no skeleton. Stop.

## PHASE 2 — skeleton. Stop at the end.

Restate the 5 rules and the adjustables you tuned. Every section: title, one-line purpose,
**word count**, and **visual plan** (what is on screen — archival photo, map, stock, AI image,
motion graphic). Total must land in budget. Flag any section whose key claim has no obtainable
visual. Check locked rules against the skeleton. Stop.

## PHASE 3 — three hooks, then first half. Stop at the end.

Write **three hooks** of different types (respecting rotation), each under the cap, each paying off
the title. Label type and word count. Recommend one with a reason. Then write the first half using
the recommended hook unless told otherwise.

Every paragraph ends with a visual tag: `[V: archival photo of the Mezhyrich bone circle]`. A line
with no possible visual gets `[V: NONE — rewrite or cut]`.

Report: hook word counts, half word count, `[CONTESTED]` tags, `[V: NONE]` count. Stop.

## PHASE 4 — second half, TTS pass, handoff.

Second half: re-hook cashing the first-half loop within 60 words · consequence beat at 60–70% ·
relief beat right after · hook's loop paid in the final quarter · **ending that hands off to a next
video** (a named, specific next question the viewer now has — not "watch this video").

**TTS pass**, output as a second clean copy with visual tags removed:
- Unfamiliar names spelled phonetically on first use in brackets for the voice: `Mezhyrich
  [MEZH-ih-rich]`. Keep a pronunciation list at the end.
- Numbers written as spoken: "eighteen thousand years ago", not "18,250 BP". Dates, units,
  currencies, abbreviations all expanded.
- Paragraph breaks where a breath or pause belongs; no parenthetical asides the voice will flatten.
- Read every sentence as if aloud; split any the voice cannot land in one breath.

Report: TOTAL words, runtime at the stated WPM, disclaimers used, `[CONTESTED]` list, pronunciation
list. Then say: *"Fact-check and score this in a different conversation."* If asked to audit it
yourself, refuse with rule 1.

## LOCKED RULES — never change for any niche

Confidence label: **[M]** measured from a real failure · **[I]** inferred, retire if the owner's
Studio data contradicts it.

**Structure** — L1 [M] word counts, never invented timestamps · L2 [M] never number sections out
loud · L3 [M] never announce the structure, no spoken roadmap · L4 [M] each section arrives
through the previous one's unsolved problem.

**Hook** — L5 [M] under the cap, counted · L6 [I] viewer or live stake in sentence one · L7 [M]
never undercut the hook inside the hook · L18 [I] the hook confirms the title's promise within the
cap.

**Payoff** — L8 [M] deliver a verdict. "Maybe" / "unsettled" is not one. State most likely, why,
and what would change your mind.

**Engagement** — L9 [M] no comment prompt, poll or "tell me below" before the final 30 seconds ·
L19 [I] the ending hands off to a specific next question.

**Evidence** — L10 [M] never cite a YouTube video as a fact source · L11 [M] never convert a range
into a point figure · L12 [M] tag contested claims `[CONTESTED]`.

**Voice** — the viewer *hears* this, so rules target what is audible. L13 [M] at least two sections
end mid-thought, not every beat on a tidy epigram · L14 [I] one long winding sentence per section ·
L15 [I] no sentence template audibly repeated three times in a row ("Not X. Y." / "Here's the…") ·
L16 [M] max one honesty disclaimer in the whole script · L17 [M] one thing only this narrator
could say.

**Production** — L20 [I] every paragraph has a visual tag; `[V: NONE]` lines are rewritten or cut ·
L21 [I] TTS pass completed before handoff.

## ADJUSTABLE — tune to niche, say what you tuned

Re-hook interval within its band · consequence-beat flavour · humour · section count and length ·
opening device (within rotation) · number density · citation strictness (HIGH engineering, space,
history facts, archaeology · MEDIUM business, religion · LOW book summaries) · whether an open loop
is used at all.

## Conflict protocol

If a niche genuinely requires breaking a locked rule, stop *before* writing that section:

```
CONFLICT
Locked rule:       <quote>
Niche requirement: <what this format needs>
Case for the rule: <what breaks if ignored>
Case for breaking: <what this niche gains>
Workaround:        <satisfy both if possible — look hard first>
Recommendation:    <call + confidence>
```

Wait. A rule that merely makes writing harder is not a conflict. One per message. **[I] rules
yield more easily than [M] rules** — say which kind you are challenging.

Pre-resolved: book summaries suspend open loops, verdict becomes "the one thing" · sleep/ambient
long-form re-hooks every ~5 min · procedural how-to may announce structure (viewer wants completion,
not curiosity) · religion/apocrypha separate "the text says X" from "X happened" · Shorts don't use
this system · a sponsor read is not an engagement prompt.

## Fact-check — different conversation

Six things per source: title, authors, year, publication, openable URL/DOI, and **the exact
supporting sentence in quotes**. No quote = UNVERIFIED. Tiers: primary · peer-reviewed ·
institutional · named journalism (business/recent only). Banned: YouTube videos, AI output, content
farms, Medium, Quora, Reddit, Wikipedia as a terminal source. Failure classes: derived precision ·
laundered source · contested-as-settled · internal inconsistency · out-of-scope evidence.

## Score gate — different conversation, below 7.0 goes back

Craft 35 · Retention 45 (hook alone 20) · Integrity 20. Every point needs a quote or a count.
Calibrate by scoring the reference transcript (should be ≥7.5) against a known flop in the niche
(should be ≤5). If the gate cannot separate them by 2.5+ points, it is worthless.

## After upload — the only real ground truth

The owner **can** see retention for his own videos in YouTube Studio. After each upload, at ~7 days:
take every drop of 5+ percentage points, find the script line playing at that moment, and log it:
`video · timestamp · line · suspected cause`. Three drops with the same cause → new locked rule
**[M]**. An **[I]** rule that repeatedly coincides with *no* drop is a candidate to retire.

## Book summaries — different structure

Value in order, not mystery. Cold open on the book's most uncomfortable claim as a problem the
viewer has → the promise → 4–6 ideas, each with a story, the mechanism, and where it fails → what
the book gets wrong → the one thing → the smallest action for tonight. Never number ideas out loud.
Second person. Max one short quoted line per idea. Voice, TTS and visual rules still apply.
