---
name: manim-animator
description: >
  Create mathematical and cinematic animations using Manim (Community Edition).
  Triggers on: "manim", "animate", "3blue1brown style", "math animation",
  "create animation", "make a video with code", "programmatic video", "animated explainer",
  "visualize this concept", "animate this diagram", "scene animation".
  Covers scene creation, 2D/3D objects, camera control, LaTeX rendering,
  color/glow effects, SVG import, and rendering commands.
---

# Manim Animator Skill

## Environment Setup (Windows)

The user has Manim installed in a virtual environment:

```
Project folder: C:\Users\renu5\.gemini\antigravity\scratch\manim-projects
Venv: C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv
Python: C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\python.exe
Manim CLI: C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe
FFmpeg: C:\Users\renu5\Downloads\nishe found\ffmpeg\ffmpeg.exe (also in PATH)
LaTeX: NOT installed (skip LaTeX features unless user installs MiKTeX later)
```

## How to Run Manim

Always use the venv's manim executable:

```powershell
# Low quality (fast preview)
& "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -ql scene_file.py ClassName

# Medium quality
& "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -qm scene_file.py ClassName

# High quality (1080p)
& "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -qh scene_file.py ClassName

# 4K quality
& "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -qk scene_file.py ClassName

# GIF output
& "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -ql --format gif scene_file.py ClassName

# PNG image (last frame)
& "C:\Users\renu5\.gemini\antigravity\scratch\manim-projects\venv\Scripts\manim.exe" render -ql -s scene_file.py ClassName
```

Output goes to: `./media/videos/<filename>/<quality>/`

## Core Concepts

### Scene Structure
Every animation is a class inheriting from `Scene` (2D) or `ThreeDScene` (3D):

```python
from manim import *

class MyScene(Scene):
    def construct(self):
        # All animation code goes here
        circle = Circle(color=BLUE)
        self.play(Create(circle))
        self.wait(1)
```

### Key Mobjects (Mathematical Objects)
- **Shapes**: `Circle`, `Square`, `Rectangle`, `Triangle`, `Polygon`, `Ellipse`, `Arc`, `Annulus`, `Star`
- **Lines**: `Line`, `Arrow`, `DoubleArrow`, `DashedLine`, `CurvedArrow`, `ArcBetweenPoints`
- **Text**: `Text("hello")`, `MathTex(r"\int_0^1 x^2 dx")` (needs LaTeX), `Tex(r"Hello \textbf{World}")`
- **Groups**: `VGroup(*mobjects)`, `Group(*mobjects)`
- **3D**: `Sphere`, `Cube`, `Cylinder`, `Cone`, `Torus`, `Surface`
- **Graphs**: `Graph(vertices, edges)`, `DiGraph(vertices, edges)`
- **SVG**: `SVGMobject("file.svg")`
- **Code**: `Code("file.py", language="python")`

### Key Animations
```python
# Creation
self.play(Create(mob))           # Draw outline then fill
self.play(Write(text))           # Write text stroke by stroke
self.play(FadeIn(mob))           # Fade in
self.play(GrowFromCenter(mob))   # Grow from center point
self.play(DrawBorderThenFill(mob))

# Transformation
self.play(Transform(mob1, mob2))        # Morph one into another
self.play(ReplacementTransform(a, b))   # Replace a with b
self.play(mob.animate.shift(RIGHT * 2)) # Move right
self.play(mob.animate.scale(2))         # Scale up
self.play(mob.animate.set_color(RED))   # Change color
self.play(mob.animate.rotate(PI / 2))   # Rotate

# Removal
self.play(FadeOut(mob))
self.play(Uncreate(mob))

# Multiple simultaneous
self.play(Create(a), FadeIn(b), c.animate.shift(UP))

# Sequential with run_time
self.play(Create(mob), run_time=2)
```

### Colors & Styling
```python
# Built-in colors: RED, BLUE, GREEN, YELLOW, PURPLE, ORANGE, WHITE, GREY, PINK, TEAL, GOLD
# Hex: "#FF5733"
# Opacity: mob.set_opacity(0.5)
# Fill: mob.set_fill(BLUE, opacity=0.7)
# Stroke: mob.set_stroke(WHITE, width=3)
# Gradient: mob.set_color_by_gradient(RED, BLUE)
# Glow: mob.set_stroke(YELLOW, width=8, opacity=0.3)  # fake glow with thick transparent stroke
```

### Positioning
```python
mob.move_to(ORIGIN)              # Center
mob.shift(RIGHT * 2 + UP * 1)   # Relative move
mob.next_to(other, DOWN, buff=0.5)  # Next to another object
mob.align_to(other, LEFT)        # Align edges
mob.to_edge(UP)                  # Move to screen edge
mob.to_corner(UR)                # Upper right corner
```

### Camera (3D)
```python
class My3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60*DEGREES, theta=-45*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        # ... add 3D objects
```

### ValueTracker (for animating parameters)
```python
t = ValueTracker(0)
dot = always_redraw(lambda: Dot(point=[t.get_value(), np.sin(t.get_value()), 0]))
self.add(dot)
self.play(t.animate.set_value(2 * PI), run_time=3)
```

## Common Patterns

### Neural Network / Brain Nodes
```python
# Create nodes
nodes = VGroup(*[Circle(radius=0.2, color=BLUE, fill_opacity=0.8) for _ in range(5)])
nodes.arrange(RIGHT, buff=0.5)

# Create edges
edges = VGroup()
for i in range(len(nodes) - 1):
    edges.add(Line(nodes[i].get_right(), nodes[i+1].get_left(), color=GREY))
```

### Glowing Effect
```python
# Layer multiple strokes with decreasing opacity
def glow(mob, color=YELLOW, layers=5, max_width=20):
    glows = VGroup()
    for i in range(layers):
        g = mob.copy()
        g.set_stroke(color, width=max_width * (1 - i/layers), opacity=0.3 * (1 - i/layers))
        glows.add(g)
    return glows
```

### Animated Signal Along Edge
```python
dot = Dot(color=YELLOW).move_to(edge.get_start())
self.play(MoveAlongPath(dot, edge), run_time=0.5)
```

## Rendering Tips
- Use `-ql` (480p) for quick previews during development
- Use `-qm` (720p) for draft reviews
- Use `-qh` (1080p) for final output
- Use `-qk` (4K) only for final production
- Add `--disable_caching` if animations look stale
- Output files are in `media/videos/` relative to the script

## Without LaTeX
Since LaTeX is NOT installed, avoid `MathTex()` and `Tex()`. Use `Text()` instead:
```python
# DO THIS:
text = Text("f(x) = x²", font_size=36)

# DON'T DO THIS (will fail without LaTeX):
# tex = MathTex(r"f(x) = x^2")
```

If the user installs MiKTeX later (`choco install miktex` or from https://miktex.org), then MathTex and Tex become available.

## Gotchas
1. **Scene class name must match CLI argument** — `manim render file.py ClassName`
2. **Always call `self.play()` or `self.add()`** — creating an object doesn't show it
3. **`Transform` keeps the original object** — use `ReplacementTransform` to swap
4. **3D needs `ThreeDScene`** — regular `Scene` won't show 3D objects properly
5. **Large scenes are slow** — reduce `run_time` and use `-ql` during development
6. **Windows paths**: Use raw strings `r"C:\path\to\file"` or forward slashes
