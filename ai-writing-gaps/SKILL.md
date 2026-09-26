---
name: ai-writing-gaps
description: "Fixes structural problems in AI-generated YouTube scripts that /humanizer cannot catch. Handles deeper architecture: pacing, source integration, emotional contrast, narrative bridges, and the specific choices that make human-written scripts retain viewers. This is Pass 2 — run AFTER /humanizer (Pass 1). MUST activate when the user mentions: fix my script, check for AI patterns, structural pass, script DNA, writing gaps, deep script check, why does this sound like AI, make this sound human, retention check, anti-slop audit, script QA, pass 2, audit my script, script review, does this sound natural, check my writing, structural edit, deep edit, pacing check, source density check. Also activate when the user uploads a competitor transcript and wants to learn from it, or when they want to feed a new script into the learning loop. Do NOT activate for surface-level humanizer tasks like removing em dashes or fixing AI vocabulary — those go to /humanizer."
---

## Overview

> [!CAUTION]
> **Do NOT try to "fix" a raw AI draft.** Starting from an AI-generated script creates "Structural Rottenness" — monotone pacing, generic abstractions, throat-clearing transitions, academic summaries, and fatal outro cliffs. Fixing an AI script takes 2.5x longer than writing clean with Script DNA. If the script was AI-drafted, advocate for a full rewrite using the production templates, not a patch job.

This skill is the structural layer of a two-pass YouTube script QA system.
- Pass 1: /humanizer catches 33 surface AI tells (vocabulary, em dashes, rule-of-three, etc.)
- Pass 2: ai-writing-gaps catches 17 structural failures that survive humanizer (pacing, sourcing, emotional contrast, narrator voice, open loops, readability, etc.)

The skill operates in THREE MODES:
1. **Audit Mode** — User submits their own script → skill flags structural failures with specific rewrite suggestions
2. **Learn Mode** — User uploads a competitor transcript → skill extracts new patterns and appends to learned_patterns.md
3. **Blueprint Mode** — User selects a channel style → skill applies that blueprint's specific patterns during script generation

## Mode 1: Self-Audit (For User's Own Scripts)

When the user runs the skill on their OWN script:

1. Read the pattern library: `./pattern_library.md` (base patterns)
2. Read learned patterns: `./learned_patterns.md` (accumulated patterns from transcripts)
3. Read benchmarks: `./benchmarks.md` (quantitative reference)
4. Run the QA checklist: `./qa_checklist.md`
5. For EACH of the 17 patterns in the library:
   - Check if the pattern is present in the script
   - If absent, flag the specific lines that need fixing
   - Provide a SPECIFIC rewrite (not "make it more vivid" — show the actual rewritten line)
6. Score the script on each dimension (1-10)
7. Calculate an overall "Human Score" percentage
8. List the top 3 most impactful fixes

Output format:
```
# Script Audit: [SCRIPT_TITLE]

## Human Score: [X]%

## Top 3 Priority Fixes
1. [PATTERN_NAME]: [specific fix with rewritten line]
2. [PATTERN_NAME]: [specific fix with rewritten line]
3. [PATTERN_NAME]: [specific fix with rewritten line]

## Dimension Scores
| Dimension | Score (1-10) | Status | Key Issue |
|-----------|-------------|--------|----------|
| Wrong Detail Density | X/10 | ✅/⚠️/❌ | [issue] |
| Emotional Whiplash | X/10 | ✅/⚠️/❌ | [issue] |
| Source Integration | X/10 | ✅/⚠️/❌ | [issue] |
... (all 15 patterns)

## Detailed Flags
### [PATTERN_NAME]
- **Line [X]:** "[exact quote from script]"
- **Problem:** [why this fails the pattern]
- **Fix:** "[specific rewritten version]"
```

## Mode 2: Learning Loop (For Competitor Transcripts)

When the user uploads a competitor transcript:

1. Read the existing `./pattern_library.md` and `./learned_patterns.md`
2. SCAN the transcript for human writing patterns that AI + humanizer still can't produce
3. CATCH those patterns — identify exactly what the pattern is, why it works, and why AI wouldn't generate it
4. FILTER — only keep truly exceptional, novel patterns. Ask: "Is this pattern already in the library? Is it genuinely different? Would adding it make future scripts measurably better?" If the answer to any is no, SKIP it.
5. ADD filtered patterns to `./learned_patterns.md` using this exact format:

```
## New Pattern Detected: [PATTERN_NAME]
- **Source:** [transcript filename]
- **Topic relevance:** [how this pattern relates to the specific topic being researched]
- **Example:** [exact quote from transcript]
- **What makes it human:** [why AI wouldn't generate this]
- **Detection:** [how to check if a script is missing this]
- **Fix:** [how to add this pattern to a script]
- **Quality gate:** [why this pattern passed the filter — what makes it exceptional]
- **Added to:** learned_patterns.md on [date]
```

6. TELL the user exactly what got added and what got filtered out (and why)

IMPORTANT: The transcripts the user uploads will be competitor videos on the SAME TOPIC they're currently making a video about. So also extract topic-specific patterns (how competitors handle THIS specific subject), not just general writing patterns.

## Mode 3: Blueprint Selection (Channel Styles)

The user can say "write in [STYLE] style" to apply a specific channel blueprint:

| Command | Blueprint | Best For |
|---------|-----------|----------|
| "Brofessor Stein style" | Esoteric Catalog | Relic/artifact/symbol listicles, dense archival sourcing |
| "EverythingProfessor style" | Diagnostic Armor | Psychological/scientific explainers, second-person immersion |
| "Serious History style" | Retribution Anthology | 3-story deep narratives, dark comedic juxtaposition |
| "The Analyst style" | Pop-Culture Autopsy | System/concept explainers, sardonic comparisons |

When a blueprint is selected, read the channel-specific section in `./pattern_library.md` and apply those patterns on top of the universal patterns.

## Reference Files

Read these files as needed:
- `./pattern_library.md` — 17 universal patterns + 4 channel-specific blueprints (READ FIRST for any mode)
- `./learned_patterns.md` — Accumulated patterns from user-uploaded transcripts (READ for audit mode, WRITE for learn mode)
- `./qa_checklist.md` — Step-by-step two-pass QA procedure (READ for audit mode)
- `./benchmarks.md` — Quantitative competitor benchmarks for scoring (READ for audit mode)
- `./production_templates.md` — 4 fill-in-the-blank script drafting templates, one per blueprint (READ when user wants to write from scratch)

## Integration with /humanizer

This skill is Pass 2. Always recommend running /humanizer first:
1. /humanizer strips 33 surface AI tells (vocabulary, punctuation patterns, structural tics)
2. ai-writing-gaps then checks 17 structural patterns that humanizer cannot detect
3. The two passes together produce scripts that are structurally indistinguishable from top human competitors

If the user hasn't run /humanizer yet, remind them: "Run /humanizer first for the surface pass, then come back here for the structural pass."

## The Skill Gets Smarter

Every transcript uploaded through the learning loop adds to learned_patterns.md. Over time, the pattern library grows from the base 17 patterns to dozens of patterns, each with real competitor evidence. The more transcripts fed in, the sharper the audit becomes.
