# Target notes

Last checked: 2026-09-20. Read only the section for the target he named. These
are differences the vendors themselves document. Vendor guidance changes with
every model version and sometimes reverses inside one family, so if a note
here is more than about six months old, check the vendor's current prompting
guide before relying on it, and tell him the note may be stale.

Shared by all current chat models: they follow wording literally. "Can you
suggest changes" gets suggestions, not edits. An instruction given for one
item is not generalised to the others unless the prompt says so ("apply this
to every section, not only the first").

## Claude (Anthropic)

- Explain why a constraint exists; Claude generalises from the reason.
- Emphasis words ("CRITICAL", "MUST", capitals) make recent Claude models
  over-apply the rule. Use normal sentences.
- Long documents go at the top, the question at the end. For document-heavy
  work, ask it to pull the relevant quotes first and then answer from them.
- Verbosity differs by model: Opus 5 runs long, so ask for concision if he
  wants it; Fable 5.1 runs terse during agentic work. Do not add blanket "be
  thorough" or "double-check your work" lines; on recent models they cause
  over-work.
- For format or voice, one complete example plus a sentence on why it is
  right works better than a description.

## GPT (OpenAI)

- Contradictory or vague instructions hurt GPT-5-class models more than
  others, because they spend reasoning effort trying to reconcile them.
  Resolve every contradiction before sending; this makes the contradiction
  section of the gap report the top priority for this target.
- Do not add step-by-step reasoning instructions for reasoning models.
- Try without examples first; add examples only if the output shape is wrong.
- Length is better controlled by the verbosity setting than by wording, where
  he has access to it.

## Gemini (Google)

- Gemini 3 wants short, direct prompts and tends to over-analyse elaborate
  prompt structures written for older models. Trim scaffolding harder here.
- It answers tersely by default. If he wants depth or a conversational
  answer, the prompt has to ask for it explicitly.
- Supply all context first, put the specific question at the very end, and
  bridge with a phrase such as "Based on the information above, ...".
- If he controls settings, leave temperature at the default 1.0; lower values
  can cause looping on Gemini 3.

## Coding and desktop agents (Claude Code, Antigravity, Cursor, Codex)

The prompt should state: where things stand now, what done looks like (tests
passing, files that should exist, behaviour to observe), which folders are in
scope, and what needs his confirmation first (deleting files, adding
dependencies, schema changes, pushing, deploying, sending anything outward).
Ask for a short list of changed files at the end. Include these only from
what he said; whatever is absent goes in the gap report, because a missing
scope line is how an agent ends up editing the wrong thing.

## Image and video generators

If a dedicated skill for the tool is installed (Higgsfield, ad prompts,
thumbnails), hand over to it. Otherwise:

- Generation: subject, action, setting, style, lighting, composition, aspect
  ratio, and what must not appear. Tag-style tools (Midjourney, Stable
  Diffusion) take comma-separated descriptors; prose-style tools take
  sentences. Video adds camera movement, duration and pacing.
- Editing an existing image: describe only the change and list what must stay
  identical. Re-describing the whole scene causes the model to regenerate it.
- Parameters and syntax change between tool versions. Do not write version
  flags or weights from memory; ask which version he is on, or leave them out
  and raise it in the gap report.
