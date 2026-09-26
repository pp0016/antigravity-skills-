---
name: manim-setup
description: >
  Sets up a complete Manim environment for the user, combining both local workspace
  setup and the 50-machine cloud render farm (GitHub Actions). Use this whenever 
  the user wants to start a new Manim project.
---

# Manim End-to-End Setup Skill

This skill instructs the agent on how to instantly create a ready-to-use Manim workspace on the user's computer. It handles installing the core engines (ManimCE and ManimGL) locally, AND it automatically provisions the GitHub Actions 50-machine render farm so the user can easily offload heavy rendering to the cloud.

When the user asks you to set up Manim, perform the following steps:

## 1. Create the Project Directory and GitHub Actions Folders
Run these terminal commands to create a clean folder structure that includes the `.github` workflows folder:

```powershell
mkdir -p C:\Users\renu5\.gemini\antigravity\scratch\manim_workspace\.github\workflows
cd C:\Users\renu5\.gemini\antigravity\scratch\manim_workspace
```

## 2. Set Up a Local Python Virtual Environment
Always isolate the local installation using a `venv`:

```powershell
python -m venv venv
```

## 3. Install the Engines & Plugins Locally
Install both core engines (`manim` for CE, `manimgl` for 3b1b's version) and the top content creator plugins using the virtual environment's pip:

```powershell
& "venv\Scripts\pip.exe" install manim manimgl manim-voiceover manim-slides
```

## 4. Create the `requirements.txt`
Create a `requirements.txt` file in the root of the workspace. This is needed for the GitHub Actions render farm:

```text
manim==0.21.0
manim-voiceover
manim-slides
```

## 5. Create a Starter Template (`main.py`)
Write a basic test file to the workspace so the user can immediately test if it works:

```python
from manim import *

class TestScene(Scene):
    def construct(self):
        text = Text("Manim Environment Ready!")
        self.play(Write(text))
        self.wait(1)
```

## 6. Generate the 50-Machine Render Farm (`render.yml`)
Create a file at `.github/workflows/render.yml` inside the workspace containing the distributed render farm code. This ensures the user can instantly render their videos fast using GitHub's cloud.

```yaml
name: Distributed Manim Render Farm

on:
  push:
    branches: [ "main" ]
  workflow_dispatch:

jobs:
  render_chunk:
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        chunk: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'
          cache: 'pip'

      - name: Install System Dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y ffmpeg libcairo2-dev libpango1.0-dev texlive texlive-latex-extra texlive-fonts-extra texlive-latex-recommended texlive-science tipa

      - name: Install Python Dependencies
        run: pip install -r requirements.txt

      - name: Set Chunk ID
        run: echo "CHUNK_ID=$(printf '%02d' ${{ matrix.chunk }})" >> $GITHUB_ENV

      - name: Render Chunk ${{ matrix.chunk }}
        run: |
          START_ANIM=${{ matrix.chunk }}
          END_ANIM=$(( ${{ matrix.chunk }} + 1 ))
          manim -qm -n $START_ANIM,$END_ANIM main.py TestScene --format mp4 -o chunk_${{ env.CHUNK_ID }}.mp4

      - name: Upload Chunk Artifact
        uses: actions/upload-artifact@v4
        with:
          name: chunk_${{ env.CHUNK_ID }}
          path: media/videos/**/chunk_${{ env.CHUNK_ID }}.mp4
          retention-days: 1

  stitch:
    needs: render_chunk
    runs-on: ubuntu-latest
    steps:
      - name: Download all chunks
        uses: actions/download-artifact@v4
        with:
          path: chunks_dir

      - name: Generate concat inputs.txt
        run: |
          > inputs.txt
          for i in {0..49}; do
            CHUNK_ID=$(printf "%02d" $i)
            FILE=$(find chunks_dir/chunk_$CHUNK_ID -name "chunk_$CHUNK_ID.mp4" | head -n 1)
            if [ -z "$FILE" ]; then echo "Error: Could not find chunk_$CHUNK_ID.mp4!"; exit 1; fi
            echo "file '$FILE'" >> inputs.txt
          done

      - name: Stitch video chunks
        run: ffmpeg -f concat -safe 0 -i inputs.txt -c copy final_video.mp4

      - name: Upload Final Video
        uses: actions/upload-artifact@v4
        with:
          name: final_video
          path: final_video.mp4
          retention-days: 7
```

## 7. Automatically Push to GitHub
If the user asks you to push it for them, run the following commands to initialize the repository and push to their pre-configured remote. (The repository URL is `https://github.com/vempatipawan/manim-video-.git`):

```powershell
git init
git config user.name "AI Agent"
git config user.email "agent@example.com"
git add .
git commit -m "Auto-generated Manim setup and render farm"
git branch -M main
git remote add origin https://github.com/vempatipawan/manim-video-.git
git push -u origin main
```

## 8. Guide the User
Once the setup is complete, tell the user exactly how to run their first animation locally:
> "To preview your scene locally on your laptop, run: `& 'venv\Scripts\manim.exe' -ql main.py TestScene`"

And remind them how to trigger the cloud render farm (or tell them you just pushed it for them):
> "I just pushed your code to GitHub! The 50 cloud machines are spinning up now. You can check the progress in the 'Actions' tab of your GitHub repository."
