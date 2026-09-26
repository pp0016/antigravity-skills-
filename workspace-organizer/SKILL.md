---
name: workspace-organizer
description: >
  Organizes a YouTube creator's markdown workspace from chaos into a clean,
  AI-readable structure. Scans existing files, diagnoses problems (messy names,
  duplicates, orphan files, broken references), proposes a folder structure,
  executes the reorganization, merges overlapping files, creates an AI entry
  point context file with prompt-forge optimizations, and fixes all cross-references.
  
  Use this skill whenever the user mentions organizing files, cleaning up their
  workspace, restructuring their folder layout, merging duplicate docs, creating
  an agent context file, making their workspace AI-readable, or preparing their
  workflow docs for a new AI conversation. Also triggers on "organize my files",
  "clean up my workspace", "restructure my folders", "merge these docs",
  "make this AI-friendly", "create an agent file", "set up my workspace".
  
  Tailored for YouTube creators using AI production pipelines (Remotion, FFmpeg,
  ElevenLabs, vidIQ, NotebookLM) but the principles apply to any content creator
  with a markdown-heavy workflow.
---

# Workspace Organizer — YouTube Creator Edition

Reorganize a YouTube creator's markdown workspace so any AI (Gemini, Opus, GPT, etc.) can read one file and understand everything. The human navigates fewer folders. Nothing gets lost.

---

## Phase 1: SCAN — Read Everything Before Touching Anything

### Step 1.1: Map the full directory tree

```
List every file and folder recursively. Record:
- Full path
- File size
- File type (markdown, script, media, config)
- Last modified date if available
```

Output: A complete tree listing. Save to scratch if large.

### Step 1.2: Read every markdown file

Read ALL `.md` files in the workspace. For each file, extract:

| Field | What to capture |
|---|---|
| **Purpose** | What this file is about in one sentence |
| **Status** | Active (still referenced), Historical (snapshot from past), Stale (outdated) |
| **Overlaps with** | Other files covering the same content |
| **References** | Other files this file links to or mentions by name |
| **Owner** | Which conversation/session created this file |

### Step 1.3: Diagnose problems

Check for these specific issues:

**Naming issues:**
- Spaces in filenames (break CLI tools, cause URL encoding issues)
- Special characters: apostrophes, parentheses, emojis in folder/file names
- Model names in filenames (e.g., `opus4.6`, `gemini`) — content matters, not which AI wrote it
- Spaces before file extensions (e.g., `dump .md`)
- Unnecessarily long names that can be shortened without losing meaning
- Mixed naming conventions (some-kebab-case, some_snake_case, some With Spaces)

**Content issues:**
- Two or more files covering >50% of the same content → candidates for merging
- Files that reference paths/names that no longer exist → broken cross-references
- Empty files or placeholder-only files → candidates for deletion or filling
- Intermediate AI conversation artifacts (handoffs, undone checklists, status updates) cluttering the main folder → candidates for archiving

**Structure issues:**
- More than 10 files loose in a single folder → group by type
- Multiple files of the same type scattered across the root → create a subfolder
- Nested folder depth > 3 levels → flatten
- System/config files mixed with content files → prefix system folders with `_`

Output: A diagnostic report listing every issue found, grouped by category.

---

## Phase 2: PROPOSE — Design the New Structure

### Step 2.1: Classification rules

Classify every file into exactly one category:

| Category | Prefix/Location | What goes here |
|---|---|---|
| **AI Entry Point** | Root: `[name]-agent.md` | The ONE file AI reads first. Identity, tools, schedule, rules, workspace map. |
| **Active Plans** | Root | Implementation plans, checklists, calendars still in use |
| **Reference Docs** | Root | Tool references, video watch lists, style guides |
| **System Folders** | `_[name]/` (underscore prefix) | Toolkit, templates, prompts — things the AI reads for capability info |
| **Business Units** | `[name]/` | Separate business streams (clipping, sponsorships, merch) |
| **Research** | `[topic]_research/` | Niche research, competitor analysis, keyword data |
| **Research Snapshots** | `[topic]_research/live_data/` | Point-in-time data scrapes |
| **Research Archives** | `[topic]_research/_conversation_archive/` | Old AI conversation artifacts kept for reference |
| **Archive** | `archive/` | Superseded or deprecated files |

### Step 2.2: The workspace map principle

Every organized workspace has exactly ONE file at the root that serves as the AI entry point. This file:

1. **Starts with a workspace map** — a directory tree with one-line descriptions of every file/folder. This is what the AI reads FIRST.
2. **Contains all context the AI needs** to work without reading other files (identity, tools, channels, schedule, rules).
3. **Ends with a file reference table** mapping topics to exact filenames for deeper reading.
4. **Uses XML tags** to separate sections — LLMs parse XML as hard structure boundaries.
5. **Uses positive directives** — "give the next 1-2 actions" instead of "don't give 20-step plans."
6. **Includes a grounding anchor** — honest status check (e.g., "0 videos published") to prevent aspirational drift.

### Step 2.3: Merge rules

When two or more files have >50% content overlap:

1. Identify which file has the MORE DETAILED version of each overlapping section
2. Create the merged file using the more detailed version of each section
3. Deduplicate — remove any repeated information (tool lists, schedules, channel descriptions that appear in both)
4. Delete the source files AFTER the merge is verified
5. Update all cross-references in other files that pointed to the old filenames

**Merge checklist:**
- [ ] Every section from File A appears in merged file
- [ ] Every section from File B appears in merged file
- [ ] No section is duplicated
- [ ] Old files deleted
- [ ] All cross-references updated

### Step 2.4: Naming conventions

Apply these rules to every file and folder:

| Rule | Example |
|---|---|
| Use snake_case or kebab-case, never spaces | `channel_matrix.md` not `channels org opus4.6.md` |
| No special characters except `-` and `_` | `_toolkit/` not `Priyanshu's YouTube Creator Toolkit/` |
| No model/tool names in filenames | `channel_matrix.md` not `channels org opus4.6.md` |
| System folders get `_` prefix | `_toolkit/`, `_templates/`, `_prompts/` |
| Archive folders get `_` prefix | `_conversation_archive/` |
| Shorten without losing meaning | `strategy_audit.md` not `strategy_audit_and_course_correction.md` |
| Date-stamped snapshots use `YYYYMMDD_` prefix | `20260813_overview.md` |

### Step 2.5: Present the before/after tree

Show the user:
1. Current folder tree (BEFORE)
2. Proposed folder tree (AFTER)
3. A migration table: `old path → new path → action (rename/move/merge/archive/keep)`
4. Count of files changed vs unchanged

Get approval before executing.

---

## Phase 3: EXECUTE — Do the Reorganization

### Step 3.1: Create new directories first

Create all new folders before moving anything. This prevents orphan errors.

### Step 3.2: Move and rename files

Execute in this order:
1. Group files into new subfolders (move operations)
2. Rename files (within same folder)
3. Rename folders
4. Remove empty old folders

### Step 3.3: Create the AI entry point file

Build `[name]-agent.md` with these sections, using XML tags:

```markdown
# [Name] — Agent Context
# Last updated: [DATE]

<workspace_map>
## Workspace Map — Read This First
[Full directory tree with one-line descriptions]
</workspace_map>

<identity>
## Who [Name] Is
[Background, status, honest assessment]
</identity>

<channels>  (or <projects> for non-YouTube creators)
## Channels / Projects
[Each channel/project with: niche, language, tools, status, strategy, key data]
</channels>

<role>
## Your Role
[How the AI should behave: mentor, assistant, manager, etc.]
[Work sequence / priority order]
</role>

<tools>
## Tool Stack
[Table of tools with what each does]
[Tool rules and cost constraints]
</tools>

<schedule>
## Schedule
[Daily/weekly schedule blocks]
</schedule>

<[custom_section]>
## [Custom sections as needed]
[ADHD management, content philosophy, production pipeline, etc.]
</[custom_section]>

<communication_rules>
## Communication Rules
[Response format, honesty rules, anti-sycophancy signals]
</communication_rules>

<file_references>
## Key File References
[Table mapping topics → exact filenames for deeper reading]
</file_references>
```

**Prompt-forge optimizations to apply:**
- Front-load stable instructions (workspace map FIRST — enables prompt caching)
- Dynamic/changing content at the END
- Positive directives for desired behavior
- Explicit negative constraints ONLY for safety/scope boundaries (pair each with the desired alternative)
- Grounding anchors to prevent hallucination about status
- Scope locks for tool usage (e.g., "do not call vidIQ without permission")
- File reference table so AI knows WHERE to look without guessing

### Step 3.4: Merge overlapping files

For each identified merge:
1. Create the new merged file
2. Verify all sections present
3. Delete source files
4. Log what was merged

### Step 3.5: Fix cross-references

After ALL renames and moves are complete:

1. Search every `.md` file for references to old filenames/paths
2. Update to new filenames/paths
3. Skip files in `archive/` and `_conversation_archive/` — those are historical snapshots
4. Log every reference updated

```
Search patterns to check:
- Old filenames (exact match)
- Old folder names
- Old full paths
- File links: [text](file:///old/path)
- Inline mentions: `old_filename.md`
- See references: "See old_filename.md"
```

---

## Phase 4: VERIFY — Confirm Nothing Is Broken

### Step 4.1: Structure verification

Run a recursive directory listing and confirm it matches the proposed structure.

### Step 4.2: Content verification

- Count files before and after — explain any difference (merges reduce count, new files increase it)
- Confirm zero content was lost (every section from merged files exists in the new file)
- Confirm all cross-references resolve to existing files

### Step 4.3: AI readability test

Read the AI entry point file and verify:
- [ ] Workspace map accurately reflects the current folder structure
- [ ] Every file in the workspace appears in the map
- [ ] File reference table points to files that exist
- [ ] No sections reference old/deleted filenames
- [ ] XML tags are properly opened and closed

### Step 4.4: Create a walkthrough

Document what was changed in a walkthrough artifact:
- Files merged (old → new)
- Files renamed (old → new)
- Files moved (old location → new location)
- Files kept unchanged
- Cross-references fixed
- How to use the new workspace (the one-line paste for new conversations)

---

## Anti-Patterns — What NOT to Do

| Anti-Pattern | Why It's Wrong | Do This Instead |
|---|---|---|
| Creating empty project folders "for later" | Empty folders are noise. Create when you have content. | Only create folders that will immediately contain files. |
| Mixing media assets with markdown files | Different systems. Markdown = brain/planning. Media = production. | Keep markdown workspace separate from video/audio/image storage. |
| More than 3 levels of nesting | Humans and AIs both lose navigation context past 3 levels. | Flatten. Use prefixes instead of subfolders. |
| Putting model/AI names in filenames | "opus4.6" in a filename is noise — the content matters, not who wrote it. | Name files by content: `channel_matrix.md` not `channels_org_opus4.6.md`. |
| Creating "system" folders that duplicate installed skills | A `_prompts/` folder with prompts that overlap your installed Antigravity skills causes conflicts. | Add a rule in the agent file: "installed skills take priority over `_prompts/` files." |
| Over-engineering YAML frontmatter | 10+ metadata fields nobody maintains. | Max 4 fields: `status`, `created`, `target_date`, `tags`. |
| Archiving by deleting | "I'll remember what was in there" — no you won't. | Move to `archive/` folder. Delete nothing. |

---

## Quick Reference — File Types and Where They Go

| File Type | Location | Naming Pattern |
|---|---|---|
| AI context/identity | Root: `[name]-agent.md` | One file only |
| Active plans/checklists | Root | `implementation_plan.md`, `7-day_checklist.md` |
| Tool references | Root or `_toolkit/` | `vidiq_reference.md`, `toolkit.md` |
| Niche/competitor research | `[topic]_research/` | `channel_matrix.md`, `key_channels_analysis.md` |
| Raw data dumps | `[topic]_research/` | `raw_dump.md` (prefix with `raw_`) |
| Point-in-time data | `[topic]_research/live_data/` | `YYYYMMDD_[source].md` |
| Old AI conversation artifacts | `[topic]_research/_conversation_archive/` | Group by conversation |
| Side businesses | `[business_name]/` | `clipping/`, `sponsorships/` |
| Superseded files | `archive/` | Keep original names |
| Scratch scripts | `[topic]_research/scratch/` or root `scratch/` | `fetch_metadata.py` |

---

## Usage Example

When a user says "organize my workspace" or "clean up my files", follow this exact sequence:

1. Ask for the folder path
2. Run Phase 1 (SCAN) — read everything
3. Run Phase 2 (PROPOSE) — show before/after tree
4. Get user approval
5. Run Phase 3 (EXECUTE) — do the work
6. Run Phase 4 (VERIFY) — confirm nothing broke
7. Create walkthrough showing what changed

Total expected time: 10-20 minutes depending on workspace size.
