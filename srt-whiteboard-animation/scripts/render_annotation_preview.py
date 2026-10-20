#!/usr/bin/env python3
"""
Annotation Region Preview Generator

Generates a static preview image overlaying numbered bounding boxes, sequence order,
reveal directions, and motion paths on top of the scene image. Used for visual verification
before video rendering.

Usage:
  python render_annotation_preview.py <image_path> <annotation_path> <output_preview_path>
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def _load_font(size: int) -> ImageFont.ImageFont:
    """Attempt to load a clean sans-serif system font, with cross-platform fallbacks."""
    candidate_fonts = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/tahoma.ttf",
        "C:/Windows/Fonts/msyh.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for font_path in candidate_fonts:
        if Path(font_path).exists():
            try:
                return ImageFont.truetype(font_path, size)
            except Exception:
                continue
    try:
        return ImageFont.load_default()
    except Exception:
        return None


def main(image_path: str, annotation_path: str, output_path: str) -> None:
    image = Image.open(image_path).convert("RGBA")
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font = _load_font(24) or ImageFont.load_default()
    small_font = _load_font(16) or ImageFont.load_default()
    colors = [(38, 103, 255, 225), (255, 105, 92, 225), (41, 167, 102, 225), (181, 100, 255, 225)]

    data = json.loads(Path(annotation_path).read_text(encoding="utf-8"))
    for index, element in enumerate(data.get("elements", []), start=1):
        region = element["region"]
        x, y = int(region["x"]), int(region["y"])
        right, bottom = int(x + region["width"]), int(y + region["height"])
        color = colors[(index - 1) % len(colors)]
        fill = (*color[:3], 24)

        # Draw bounding rectangle
        draw.rounded_rectangle((x, y, right, bottom), radius=12, outline=color, width=4, fill=fill)
        # Draw number badge
        draw.ellipse((x + 8, y + 8, x + 44, y + 44), fill=color)
        draw.text((x + 20, y + 10), str(index), anchor="ma", font=small_font, fill="white")

        # Label tag
        direction = element.get("reveal", {}).get("direction", "")
        label_text = f"{index}. {element.get('label', '')} [{direction}]"
        tag_width = len(label_text) * 10 + 20
        draw.rounded_rectangle((x + 52, y + 8, min(right - 8, x + 52 + tag_width), y + 44), radius=6, fill=(255, 255, 255, 225))
        draw.text((x + 60, y + 12), label_text, font=small_font, fill=color)

        # Hand motion path vector
        hand_path = element.get("handPath", {})
        if "start" in hand_path and "end" in hand_path:
            start = tuple(int(v) for v in hand_path["start"])
            end = tuple(int(v) for v in hand_path["end"])
            draw.line((start, end), fill=color, width=4)
            draw.polygon((end, (end[0] - 12, end[1] - 6), (end[0] - 12, end[1] + 6)), fill=color)

    result = Image.alpha_composite(image, overlay).convert("RGB")
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    result.save(output_path, quality=95)
    print(f"Annotation preview generated: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python render_annotation_preview.py <image_path> <annotation_path> <output_preview_path>")
        sys.exit(1)
    main(*sys.argv[1:4])
