---
name: minimalist-animation-style
description: Creates minimalist editorial motion graphics and viral 2D explainer videos (Dan Koe, Money Stick, and Ali Abdaal visual style) with multi-directional track matte "portal" reveals, high-contrast typography, and paper-textured backdrops. Use whenever the user asks to create, animate, or replicate minimalist explainers, stickman finance videos, doodle animations, Dan Koe style visuals, track matte masked reveals, portal keyframing, or programmatic 2D vector motion graphics.
---

# Minimalist Animation Style (Editorial Motion Graphics)

> [!IMPORTANT]
> **The Master Aesthetic "Salt" (Core Contract for New Conversations):**
> 1. **Backdrop is Immutable:** Always `#F2EBDB` (RGB `242, 235, 219`) warm organic cream paper tone. Never pure white `#FFFFFF`. Never cold grey.
> 2. **Two Visual Archetypes Only:**
>    - **Archetype A (Stickman Mascot):** Circular head, 2 small oval eyes, crescent smile, 2-strand hair tuft, 5px black ink stroke linework.
>    - **Archetype B (Human Characters):** **Storyset "Rafiki" Modern Flat Vector Editorial Character Illustration**. Realistic 1:6.5 human proportions, natural joints and posture, authentic skin tones. Strictly NO Corporate Memphis (no noodle limbs, no swollen legs, no micro pinheads, no neon skin). Thin 2px uniform contour line, 100% solid flat color blocking, zero gradients, zero 3D shading.
> 3. **Motion Standard:** Masked track matte portal reveals (`direction="up"|"down"|"left"|"right"`) using `ease_out_cubic`. Elements slide out of an invisible edge seam and remain at 100% constant scale once settled.
> 4. **Asset Generation Rule:** Every image prompt MUST pin `#F2EBDB` background so the engine's built-in keyer (`isolate_cream_bg_asset`) automatically extracts flawless 32-bit RGBA PNGs with zero edge haloing.

## 1. Style DNA & Visual Standard

This framework produces the high-retention aesthetic popularized by **Dan Koe**, **Money Stick**, and leading financial/educational creators:

| Attribute | Specification |
| :--- | :--- |
| **Canvas Formats** | **16:9 Widescreen (1920×1080)** for YouTube long-form OR **9:16 Vertical (1080×1920)** for Shorts/Reels/TikTok, 30 fps |
| **Permanent Backdrop** | **Warm Organic Cream Paper Tone: `#F2EBDB` (RGB `242, 235, 219`)** with subtle per-pixel paper grain (never pure white `#FFFFFF` or cold grey) |
| **Primary Palette** | Pitch Ink Black (`#0A0A0A`), Crimson Accent (`#A50C0C`), Alert/Rejection Red (`#D32F2F`) |
| **Typography** | `Segoe UI Black` (`seguibl.ttf`) or `Arial Black` (`ariblk.ttf`), uppercase, auto-wrapped with ascender baseline alignment |
| **Motion Archetypes** | **1. Multi-Directional Track Matte Portals** (`up`, `down`, `left`, `right`) with asymmetric cubic deceleration (`ease_out_cubic`).<br>**2. Spring Overshoot Pops** for rejection badges, stamps, and alert icons (`spring_pop`).<br>**3. Progressive Dashed Vector Arrows** for conceptual convergence. |
| **Scale Rule** | Content stays at **100% constant scale** once arrived. Never apply rubbery balloon pops to characters or text. |

---

## 2. Anti-Hallucination Visual Architecture (Two Character Archetypes)

To prevent AI agents in new conversations from hallucinating generic cartoons, 3D renders, or inconsistent characters, all visual assets MUST strictly follow one of two defined character archetypes:

### Archetype A: The Money Stick Mascot (Stickman)
* **Usage**: Lead narrator, solopreneur, beginner actions (Scene 1 & Scene 2).
* **Head**: Clean, perfectly circular vector head (thin black contour).
* **Facial Features**: Two small solid black oval eyes placed close together in the upper third, a gentle friendly upward crescent smile, and two subtle curved eyebrow lines.
* **Signature Detail**: A small 2-to-3 strand hair tuft sprouting playfully from the top of the head.
* **Body & Limbs**: Clean single-stroke black ink limbs (4–5px stroke weight), dynamic poses (climbing stairs, vacuuming, pointing, holding broom), small flat horizontal feet.
* **Props**: Realistically proportioned vector tools (canister vacuum with ribbed hose, clipboard, mop).

### Archetype B: Modern Flat Vector Editorial Character Illustration (Storyset "Rafiki" Style)
* **Official Industry Name**: **Modern Flat Vector Editorial Character Illustration** (standardized in vector marketplaces like Freepik/Storyset as **Storyset "Rafiki" Style**; in graphic design taxonomies as **Flat Design 2.0 Line-and-Fill** or **Editorial Vector Line Art**).
* **Usage**: Teams, customers waiting in retail lines, commercial corporate clients, workforce/cleaners (Scenes 3, 5, 6, 7).
* **Core Purpose**: Visual editorial storytelling for business and educational explainers (popularized by publications like *Bloomberg Businessweek*, *Vox*, and modern financial creators).
* **Anatomical Rules (Crucial Distinction from Corporate Memphis / Alegria)**:
  - **Natural, Realistic Human Proportions**: 1:6.5 to 1:7 head-to-body ratio. Proper joints (distinct elbows, knees, wrists) and natural posture.
  - **NO Noodle Limbs**: Unlike "Corporate Memphis" (which relies on absurdly tiny pinheads, massive swollen legs, and rubbery jointless noodle arms), Rafiki/Editorial characters maintain grounded, believable human anatomy.
  - **Authentic Diverse Human Skin Tones**: Warm, realistic human skin tones (peach, warm beige, caramel, deep bronze) rather than unnatural neon colors (no purple, blue, or yellow alien skin).
* **Linework & Contours**:
  - Thin, crisp, uniform continuous black vector ink contour lines (2px–3px weight).
  - Clean separation between limbs, collars, sleeves, and handheld props.
* **Color & Shading Rules**:
  - **100% Flat Solid Color Blocking**: High contrast, crisp vector boundaries.
  - **Zero Gradients & Zero 3D Shading**: Absolutely no airbrushing, no specular highlights, no 3D lighting, no soft drop shadows.
* **Facial Detailing**:
  - Minimalist and approachable: small solid black dot/oval eyes, clean curved eyebrow arcs, subtle line smile, or stylized featureless silhouettes for background crowds.
* **Wardrobe & Props**:
  - Realistic contemporary everyday attire: dark navy denim overalls/aprons, light cyan/turquoise t-shirts, bright yellow rubber cleaning gloves, modern casual office wear, clipboards, laptops, industrial brooms.

---

## 3. Nano Banana Prompt Engineering Contract (Mandatory Paired Negative Prompts)

When generating assets with Nano Banana, ChatGPT, Stable Diffusion, or Midjourney, **always pin the permanent `#F2EBDB` background** and **ALWAYS provide the Negative Prompt paired directly with every single prompt**. Omitting the negative prompt causes image models to default to 3D clay renders, gradients, ground planes, or rubber hose limbs.

### Formula 1: The Money Stick Mascot (Stickman)
* **Positive Prompt:**
  ```text
  A minimalist 2D stick figure character [EXACT ACTION, e.g. vacuuming the floor / climbing upward on a 4-step geometric staircase / seated at a desk], Money Stick video aesthetic. The character has a perfectly round circular head, two small solid black oval eyes, a wide friendly upward curved smile, subtle eyebrow lines, and a playful 2-strand tuft of hair sticking up from the top of the head. Thin uniform black ink stroke linework (5px), clean 2D doodle art, completely isolated on a flat solid cream paper background #F2EBDB (RGB 242, 235, 219), zero shadows, zero gradients, zero floor textures.
  ```
* **Negative Prompt:**
  ```text
  3D render, CGI, photorealism, Pixar 3D, Disney cartoon, color gradients, soft airbrush shading, drop shadows, floor shadows, floor ground plane, realistic human face, realistic eyes, realistic clothing, complex background, texture overlay, blur, watermark.
  ```

### Formula 2: Modern Flat Vector Editorial Character Illustration (Storyset "Rafiki" Style)
* **Positive Prompt:**
  ```text
  A 2D flat vector editorial character illustration of [EXACT SUBJECT, e.g. two friendly professional cleaners standing side-by-side / a queue of 5 diverse everyday customers waiting in line / 4 corporate business people at a white conference table]. Storyset Rafiki style, modern editorial vector line art, clean uniform thin black vector outlines (2px), realistic anatomical human proportions, natural posture, no noodle limbs, flat solid color fills, zero gradients, zero 3D shading, completely isolated on a flat solid cream paper background #F2EBDB (RGB 242, 235, 219), zero drop shadows, zero floor plane.
  ```
* **Negative Prompt:**
  ```text
  3D render, CGI, photorealism, Pixar 3D, Disney style, airbrush shading, smooth color gradients, drop shadows, floor shadows, ground textures, Corporate Memphis noodle arms, rubber hose limbs, distorted giant legs, microscopic pinhead, alien blue skin, neon purple skin, hyper-detailed wrinkles, messy line art, complex background.
  ```

### Formula 3: Props & Commercial Buildings
* **Positive Prompt:**
  ```text
  A 2D flat vector illustration of [OBJECT/STOREFRONT, e.g. a charming retail boutique storefront / an open contractor toolbox / a modern coffee shop storefront]. Clean vector outlines (3px), flat spot colors, completely isolated on a flat solid cream paper background #F2EBDB (RGB 242, 235, 219), zero drop shadows, zero floor plane.
  ```
* **Negative Prompt:**
  ```text
  3D render, CGI, photorealism, glossy textures, bevels, gradients, specular highlights, drop shadows, floor reflections, ground planes, realistic perspective distortion, complex background.
  ```

### Formula 4: Circular Rejection / Alert Badge
* **Positive Prompt:**
  ```text
  A bold circular crimson red badge (#D32F2F) with a crisp solid white cross mark 'X' centered inside, 2D flat vector icon, high contrast, clean vector edges, completely isolated on a flat solid cream paper background #F2EBDB (RGB 242, 235, 219), zero drop shadow.
  ```
* **Negative Prompt:**
  ```text
  3D sphere, bevel, emboss, plastic shine, drop shadow, gradient shading, glow, grunge texture, background elements.
  ```

---

## 4. Automated Asset Ingestion (`isolate_cream_bg_asset`)

Nano Banana outputs 1376×768 JPGs with a faint Gemini sparkle watermark (`✨`) in the bottom-right corner. The engine's built-in keyer automatically removes the background and crops out the watermark:

```python
from engine import isolate_cream_bg_asset

# 1. Samples corner color (#F2EBDB)
# 2. Masks out watermark region (bottom-right 15%) from bounding box calculation
# 3. Auto-crops subject with smooth anti-aliased alpha feathering
# 4. Exports 32-bit transparent RGBA PNG
clean_png = isolate_cream_bg_asset(
    input_image_path="nano_banana_output.jpg",
    output_png_path="assets/clean_hero.png",
    bg_target=(242, 235, 219)
)
```

---

## 5. Proportional Ratio Standards: 16:9 vs 9:16

To prevent assets from appearing microscopic or overflowing the screen:

```
┌────────────────────────────────────────────────────────┐
│ 16:9 Widescreen (1920×1080)                            │
│  ┌───────────────────────┐   ┌──────────────────────┐  │
│  │ 'left_hero' (576, 560) │   │'right_hero'(1344,560)│  │
│  │ Text / Key Insight    │   │ Character / Diagram  │  │
│  └───────────────────────┘   └──────────────────────┘  │
│  Headline: 64px | Hero Asset Height: 480px (~45% H)    │
└────────────────────────────────────────────────────────┘

┌────────────────────────┐
│ 9:16 Vertical Reel     │
│ (1080×1920)            │
│                        │
│ 'top_title' (540, 350) │
│                        │
│ 'center_hero'(540, 960)│
│                        │
│ 'bottom_sub'(540, 1540)│
│                        │
│ Headline: 76px–96px    │
│ Hero Height: 520px     │
└────────────────────────┘
```

| Parameter | 16:9 Widescreen (`1920×1080`) | 9:16 Vertical (`1080×1920`) |
| :--- | :--- | :--- |
| **Hero Character Height** | `480px` (~45% of screen height) | `520px–560px` (~28% of screen height) |
| **Prop / Icon Height** | `280px–320px` | `320px–420px` |
| **Rejection Badges (Red X)**| `100px` | `110px–120px` |
| **Primary Title Font** | `64px` | `76px–96px` (Segoe UI Black) |
| **Accent Text Color** | `#A50C0C` (Crimson) | `#A50C0C` (Crimson) |
| **Body / Label Font** | `36px–44px` | `54px–64px` |

---

## 6. Core Motion Mechanics

1. **Multi-Directional Track Matte Portals (`direction="up"|"down"|"left"|"right"`)**:
   - Elements slide smoothly through an invisible boundary line using `ease_out_cubic(t) = 1.0 - (1.0 - t)^3`.
   - **Settled Bypass**: Once `progress >= 1.0`, the element renders fully unclipped to prevent edge trimming.
2. **Spring Overshoot Pops (`animation="pop"`)**:
   - Rejection stamps, badges, and icons scale up with a snappy damped spring bounce (`1.0 - exp(-6t)*cos(8t)`), reaching ~1.15 overshoot before settling.
3. **Multi-Word In-Line Color Spans (`type="text_spans"`)**:
   - High-retention hooks require accent words on the same line (e.g. `BUILD` in black and `BUSINESS` in crimson).
   - Formatted as `spans: [("BUILD ", 76, [10, 10, 10]), ("BUSINESS", 76, [165, 12, 12])]`.
   - Engine applies explicit font ascender offset `(cur_x - bb[0], pad - bb[1])` so letter descenders are never clipped.
4. **Progressive Dashed Vector Arrows (`type="arrow"`)**:
   - Procedural black dashed lines animate from source coordinates to destination with an arrowhead appearing at the tip.

---

## 7. Complete 15-Second Reference Cue Sheet (Battle-Tested)

Below is the verified production cue sheet matching the 15-second Money Stick explainer:

```python
cue_sheet = {
    "fps": 30,
    "duration": 15.0,
    "scenes": [
        # Scene 1: Hook (0.0s - 2.5s)
        {
            "id": "scene_01",
            "start": 0.0,
            "duration": 2.5,
            "elements": [
                {"type": "text", "text": "BUSINESSES", "font_size": 84, "color": [10, 10, 10], "target_center": [540, 360], "enter_time": 0.0, "duration": 0.35, "direction": "up"},
                {"type": "image", "path": "assets/stairs_climber.png", "target_height": 420, "target_center": [540, 680], "enter_time": 0.25, "duration": 0.45, "direction": "right"},
                {"type": "text", "text": "PART 1", "font_size": 96, "color": [165, 12, 12], "target_center": [540, 1120], "enter_time": 1.95, "duration": 0.35, "direction": "up"}
            ]
        },
        # Scene 2: Niche Reveal (2.5s - 3.5s)
        {
            "id": "scene_02",
            "start": 2.5,
            "duration": 1.0,
            "elements": [
                {"type": "text", "text": "CLEANING", "font_size": 84, "color": [10, 10, 10], "target_center": [540, 320], "enter_time": 0.0, "duration": 0.25, "direction": "up"},
                {"type": "text", "text": "BUSINESS", "font_size": 96, "color": [165, 12, 12], "target_center": [540, 430], "enter_time": 0.2, "duration": 0.25, "direction": "up"},
                {"type": "image", "path": "assets/vacuum_stickman.png", "target_height": 560, "target_center": [540, 1020], "enter_time": 0.1, "duration": 0.40, "direction": "up"}
            ]
        },
        # Scene 3: Negation Triangle (3.5s - 7.5s)
        {
            "id": "scene_03",
            "start": 3.5,
            "duration": 4.0,
            "elements": [
                {"type": "image", "path": "assets/fancy_office.png", "target_height": 320, "target_center": [320, 560], "enter_time": 0.2, "duration": 0.40, "direction": "up"},
                {"type": "image", "path": "assets/red_x_badge.png", "target_height": 110, "target_center": [320, 740], "enter_time": 0.7, "duration": 0.30, "animation": "pop"},
                {"type": "image", "path": "assets/toolbox.png", "target_height": 280, "target_center": [760, 560], "enter_time": 1.3, "duration": 0.40, "direction": "up"},
                {"type": "image", "path": "assets/red_x_badge.png", "target_height": 110, "target_center": [760, 740], "enter_time": 1.8, "duration": 0.30, "animation": "pop"},
                {"type": "image", "path": "assets/huge_team.png", "target_height": 340, "target_center": [540, 1150], "enter_time": 2.4, "duration": 0.40, "direction": "up"},
                {"type": "image", "path": "assets/red_x_badge.png", "target_height": 110, "target_center": [540, 1360], "enter_time": 2.9, "duration": 0.30, "animation": "pop"}
            ]
        },
        # Scene 4: Demand Convergence (7.5s - 9.8s)
        {
            "id": "scene_04",
            "start": 7.5,
            "duration": 2.3,
            "elements": [
                {"type": "image", "path": "assets/people_group_icon.png", "target_height": 220, "target_center": [320, 360], "enter_time": 0.1, "duration": 0.35, "direction": "up"},
                {"type": "text", "text": "PEOPLE", "font_size": 64, "color": [10, 10, 10], "target_center": [320, 500], "enter_time": 0.2, "duration": 0.30, "direction": "up"},
                {"type": "image", "path": "assets/businesses_storefront.png", "target_height": 260, "target_center": [760, 360], "enter_time": 0.3, "duration": 0.35, "direction": "up"},
                {"type": "text", "text": "BUSINESSES", "font_size": 64, "color": [10, 10, 10], "target_center": [760, 500], "enter_time": 0.4, "duration": 0.30, "direction": "up"},
                {"type": "arrow", "start_pt": [350, 560], "end_pt": [470, 840], "enter_time": 0.6, "duration": 0.40, "color": [10, 10, 10], "width": 5},
                {"type": "arrow", "start_pt": [730, 560], "end_pt": [610, 840], "enter_time": 0.6, "duration": 0.40, "color": [10, 10, 10], "width": 5},
                {"type": "image", "path": "assets/cleaning_supplies.png", "target_height": 460, "target_center": [540, 1140], "enter_time": 0.8, "duration": 0.45, "direction": "up"}
            ]
        },
        # Scene 5: Retail Shop & Customer Queue (9.8s - 12.0s)
        {
            "id": "scene_05",
            "start": 9.8,
            "duration": 2.2,
            "elements": [
                {"type": "text_spans", "spans": [("BUILD ", 76, [10, 10, 10]), ("BUSINESS", 76, [165, 12, 12])], "target_center": [540, 320], "enter_time": 0.0, "duration": 0.35, "direction": "up"},
                {"type": "text", "text": "AROUND", "font_size": 76, "color": [10, 10, 10], "target_center": [540, 420], "enter_time": 0.3, "duration": 0.30, "direction": "up"},
                {"type": "image", "path": "assets/retail_shop.png", "target_height": 460, "target_center": [340, 960], "enter_time": 0.25, "duration": 0.45, "direction": "right"},
                {"type": "image", "path": "assets/customer_queue_line.png", "target_height": 440, "target_center": [750, 980], "enter_time": 0.65, "duration": 0.45, "direction": "left"}
            ]
        },
        # Scene 6: Client Acquisition (12.0s - 14.0s)
        {
            "id": "scene_06",
            "start": 12.0,
            "duration": 2.0,
            "elements": [
                {"type": "text", "text": "START", "font_size": 96, "color": [10, 10, 10], "target_center": [540, 350], "enter_time": 0.05, "duration": 0.35, "direction": "up"},
                {"type": "image", "path": "assets/client_conference_table.png", "target_height": 520, "target_center": [540, 980], "enter_time": 0.20, "duration": 0.45, "direction": "up"}
            ]
        },
        # Scene 7: Scale with Cleaners (14.0s - 15.0s)
        {
            "id": "scene_07",
            "start": 14.0,
            "duration": 1.0,
            "elements": [
                {"type": "image", "path": "assets/cleaners_duo.png", "target_height": 560, "target_center": [540, 840], "enter_time": 0.0, "duration": 0.40, "direction": "up"},
                {"type": "text", "text": "CLEANERS", "font_size": 88, "color": [10, 10, 10], "target_center": [540, 1260], "enter_time": 0.20, "duration": 0.35, "direction": "up"}
            ]
        }
    ]
}
```

## 8. Production Execution Protocol & Turnkey Workflow

### Standard 4-Step Operating Workflow for Any New Conversation:
1. **Step 1: Script & Cue Sheet Planning:** Draft high-retention script (15s–30s) and construct the JSON cue sheet using Section 5 coordinate standards (`9:16` or `16:9`).
2. **Step 2: Paired Image Prompt Generation:** Output prompts paired with mandatory negative prompts using Section 3 formulas, pinning `#F2EBDB`.
3. **Step 3: Automated Asset Ingestion:** Run `isolate_cream_bg_asset()` on the raw JPGs to crop the watermark and export clean 32-bit transparent RGBA PNGs.
4. **Step 4: Streaming Render Execution:** Run the Python script below to stream frames to FFmpeg with zero disk overhead.

### Complete Python Execution Script:
To render a complete video from scratch in any new agent conversation without guessing or recreating the pipeline:

```python
import sys
import os

# 1. Add skill scripts directory to sys.path
SKILL_SCRIPTS_DIR = r"C:\Users\renu5\.gemini\config\skills\minimalist-animation-style\scripts"
if SKILL_SCRIPTS_DIR not in sys.path:
    sys.path.append(SKILL_SCRIPTS_DIR)

from engine import MinimalistCompositor, isolate_cream_bg_asset

# 2. Ingest & key out raw Nano Banana assets (crops watermark, feathers alpha, outputs RGBA PNG)
isolate_cream_bg_asset(
    input_image_path="raw_nano_banana.jpg",
    output_png_path="assets/clean_hero.png"
)

# 3. Initialize the compositor ('9:16' for Shorts/Reels/TikTok, '16:9' for Widescreen)
compositor = MinimalistCompositor(
    aspect_ratio="9:16", # or "16:9"
    fps=30
)

# 4. Stream render the structured cue sheet directly to final MP4 with audio
compositor.render_cue_sheet(
    cue_sheet=cue_sheet,
    output_mp4="final_output.mp4",
    audio_path="voiceover.aac" # Optional: paths to AAC/MP3/WAV, or None for silent
)
```

---

## 9. Strict FFmpeg Execution Policy

All renders strictly adhere to the global agent policy:
* **Path**: `C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe`
* **Preservation Flags**: `-pix_fmt yuv420p -crf 17` (Zero color banding, lossless visual fidelity)
* **Audio**: `-c:a aac -b:a 192k`
* **Subprocess Deadlock Prevention**: FFmpeg `stderr` must always be directed to a log file on disk (`output.mp4.ffmpeg.log`), never left on `subprocess.PIPE` (which causes Windows deadlocks after 64KB buffer).
