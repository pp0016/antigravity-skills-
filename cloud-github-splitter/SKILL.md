---
name: cloud-github-splitter
description: Safely copies a heavy media project into a backup folder and divides it into a GitHub folder and a Cloud leftover folder, and automatically scrubs API keys.
---

# Cloud & GitHub Splitter

Use this skill whenever the user wants to split a project into a "GitHub" (code) folder and a "leftover for cloud" (media) folder inside their backup directory.

The user prefers not to do everything in one giant step. Treat this as a two-phase workflow. Only proceed to Phase 2 if the user explicitly triggers it with the specific prompt.

## Phase 1: Copy and Divide the Project

When the user asks to split a project:
1. Run the provided Python script on the source directory.
2. The script will first **COPY** the entire source folder into `C:\Users\renu5\Downloads\backup` (leaving the original untouched).
3. Then, inside the backup folder, it will split the files into:
   - `C:\Users\renu5\Downloads\backup\github\[Project] copy for git`
   - `C:\Users\renu5\Downloads\backup\leftover for cloud\[Project] copy for git leftover`
4. **100MB Limit:** Any file >= 100MB (along with all media files) automatically goes to the leftover folder.
5. The script automatically scrubs API keys (OpenRouter/Groq) from the GitHub folder, so you do not need to do this manually.
6. The script auto-generates a `MERGE_INSTRUCTIONS_AI.md` file in the GitHub folder. This file instructs future AI agents on how to run `npm install` and merge the cloud leftover files back into the project.

**Command to run:**
```powershell
python "C:\Users\renu5\.gemini\config\skills\cloud-github-splitter\scripts\split_project.py" "<SOURCE_DIRECTORY_PATH>"
```

Once Phase 1 is complete, inform the user that the project has been copied and divided. **Stop here**. Do not push to GitHub yet.

## Phase 2: Push to GitHub

Only proceed to this phase when the user types this exact prompt:
**"Init git, commit all files, and push to [GITHUB LINK]"**

When you see that trigger:
1. Navigate to the `copy for git` backup folder created in Phase 1.
2. Initialize Git, add files, commit, and push to the GitHub link provided by the user in their prompt.

**Commands:**
```powershell
# Inside the "copy for git" backup folder:
git init
git add .
git commit -m "Initial commit (Code only, media copied to cloud)"
git branch -M main
git remote add origin <GITHUB_URL>
git push -u origin main
```
