"""
Minimalist Animation Style Engine (Comprehensive Production Edition)
=====================================================================
A self-contained Python animation engine for rendering "Minimalist Editorial Motion Graphics"
(Dan Koe / Money Stick style explainers) with multi-directional track matte reveals.

Capabilities:
1. Procedural Paper Backdrop (tactile paper grain, no external background file required).
2. Procedural Stick Figure & Prop Vector Generator (poses: neutral, thinking, pointing,
   celebrating, working; props: coin, dollar, chart, desk, lightbulb).
3. Multi-directional Track Matte Portals:
   - 'up': rises through floor line (bottom-to-top)
   - 'down': descends through ceiling line (top-to-bottom)
   - 'right': slides from left boundary (left-to-right)
   - 'left': slides from right boundary (right-to-left)
   - Supports 'enter' and 'exit' transitions.
4. Auto-wrapping Typography (multi-line bounding boxes, centered tracking, Segoe UI Black).
5. Scene Transitions: Directional paper seam wipes ('wipe_left', 'wipe_up') with edge shadow.
6. Audio Alignment: Built-in word timestamp extraction via faster-whisper.
7. Declarative Cue Sheet Orchestrator: Takes a structured JSON timeline and renders end-to-end.
8. Streaming FFmpeg Pipeline: Pipes rawvideo directly to FFmpeg stdin (zero temporary PNGs).
"""

import os
import sys
import math
import textwrap
import subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont

FFMPEG_PATH = r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"

def ease_out_cubic(t: float) -> float:
    """Asymmetric cubic deceleration curve for snappy launch and silky settle."""
    t = max(0.0, min(1.0, t))
    return 1.0 - math.pow(1.0 - t, 3)

def ease_in_cubic(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return math.pow(t, 3)

def spring_pop(t: float) -> float:
    """Snappy spring bounce overshoot for badges, stamps, and icon pop-ins."""
    t = max(0.0, min(1.0, t))
    if t <= 0.0:
        return 0.0
    return 1.0 - math.exp(-6.0 * t) * math.cos(8.0 * t)

def get_audio_word_timestamps(audio_path: str):
    """Extracts millisecond-accurate word timestamps using faster-whisper."""
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel("tiny.en", device="cpu", compute_type="int8")
        segments, _ = model.transcribe(audio_path, word_timestamps=True)
        words = []
        for seg in segments:
            for w in seg.words:
                words.append({
                    "word": w.word.strip(),
                    "start": round(w.start, 2),
                    "end": round(w.end, 2)
                })
        return words
    except ImportError:
        print("[Warning] faster-whisper not installed. Falling back to empty alignment list.")
        return []

def isolate_cream_bg_asset(
    input_image_path: str,
    output_png_path: str = None,
    bg_target: tuple = (242, 235, 219),
    threshold_low: float = 12.0,
    threshold_high: float = 28.0,
    watermark_margin_ratio: float = 0.85
) -> Image.Image:
    """
    Keys out solid warm cream backgrounds (#F2EBDB) from Nano Banana AI generations.
    Automatically detects and crops the subject bounding box while ignoring corner watermarks,
    applying smooth alpha feathering for 100% seamless compositing.
    """
    img = Image.open(input_image_path).convert("RGBA")
    arr = np.array(img, dtype=np.uint8)
    h, w, _ = arr.shape
    
    # Auto-sample corner if very close to cream, else use bg_target
    corner_sample = np.mean(arr[:15, :15, :3], axis=(0, 1))
    if np.linalg.norm(corner_sample - np.array(bg_target)) < 35.0:
        target_color = corner_sample
    else:
        target_color = np.array(bg_target, dtype=np.float32)
        
    diff = np.linalg.norm(arr[:, :, :3].astype(np.float32) - target_color, axis=2)
    
    # Exclude bottom-right corner from bounding box search to avoid Gemini sparkle watermark
    search_mask = (diff > 22.0).astype(np.uint8)
    search_mask[int(h * watermark_margin_ratio):, int(w * watermark_margin_ratio):] = 0
    
    y_idx, x_idx = np.where(search_mask > 0)
    if len(y_idx) == 0:
        return img
        
    ymin, ymax = max(0, np.min(y_idx) - 8), min(h, np.max(y_idx) + 8)
    xmin, xmax = max(0, np.min(x_idx) - 8), min(w, np.max(x_idx) + 8)
    
    crop_arr = arr[ymin:ymax, xmin:xmax].copy()
    crop_diff = diff[ymin:ymax, xmin:xmax]
    
    # Smooth anti-aliased alpha
    alpha = np.clip((crop_diff - threshold_low) / max(0.1, threshold_high - threshold_low), 0.0, 1.0) * 255.0
    crop_arr[:, :, 3] = alpha.astype(np.uint8)
    
    result = Image.fromarray(crop_arr, "RGBA")
    if output_png_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_png_path)), exist_ok=True)
        result.save(output_png_path, "PNG")
    return result

def isolate_white_bg_asset(input_image_path: str, output_png_path: str = None, threshold: int = 240) -> Image.Image:
    """Legacy compatibility alias: routes to isolate_cream_bg_asset if image has cream backdrop."""
    return isolate_cream_bg_asset(input_image_path, output_png_path)

class ProceduralAssetGenerator:
    """Generates clean 32-bit RGBA stick figures and props with crisp black linework."""
    
    @staticmethod
    def create_canvas(width=400, height=500):
        return Image.new("RGBA", (width, height), (0, 0, 0, 0))

    @classmethod
    def generate_stickman(cls, pose: str = "neutral", ink_color=(10, 10, 10), stroke_width=8):
        img = cls.create_canvas(400, 500)
        draw = ImageDraw.Draw(img)
        
        # Head (Circle at cx=200, cy=100, radius=40)
        head_box = [160, 60, 240, 140]
        draw.ellipse(head_box, outline=ink_color, width=stroke_width)
        
        # Torso (cy=140 to cy=280)
        draw.line([(200, 140), (200, 280)], fill=ink_color, width=stroke_width)
        
        # Limbs based on pose
        if pose == "thinking":
            # Hand to chin, other arm on hip
            draw.line([(200, 180), (250, 190), (225, 125)], fill=ink_color, width=stroke_width)
            draw.line([(200, 180), (145, 220), (160, 260)], fill=ink_color, width=stroke_width)
            # Legs standing straight
            draw.line([(200, 280), (160, 420)], fill=ink_color, width=stroke_width)
            draw.line([(200, 280), (240, 420)], fill=ink_color, width=stroke_width)
        elif pose == "pointing":
            # Right arm pointing forward/up
            draw.line([(200, 180), (280, 150), (340, 130)], fill=ink_color, width=stroke_width)
            draw.line([(200, 180), (150, 230)], fill=ink_color, width=stroke_width)
            # Legs
            draw.line([(200, 280), (160, 420)], fill=ink_color, width=stroke_width)
            draw.line([(200, 280), (240, 420)], fill=ink_color, width=stroke_width)
        elif pose == "celebrating":
            # Both arms raised high in V-shape
            draw.line([(200, 180), (130, 90)], fill=ink_color, width=stroke_width)
            draw.line([(200, 180), (270, 90)], fill=ink_color, width=stroke_width)
            # Wide stance legs
            draw.line([(200, 280), (140, 420)], fill=ink_color, width=stroke_width)
            draw.line([(200, 280), (260, 420)], fill=ink_color, width=stroke_width)
        elif pose == "working":
            # Seated posture
            draw.line([(200, 140), (190, 260)], fill=ink_color, width=stroke_width)
            # Arms on desk
            draw.line([(195, 190), (250, 220), (290, 215)], fill=ink_color, width=stroke_width)
            # Seated legs
            draw.line([(190, 260), (250, 270), (255, 360)], fill=ink_color, width=stroke_width)
        elif pose == "walking":
            # Arms swinging
            draw.line([(200, 180), (160, 230)], fill=ink_color, width=stroke_width)
            draw.line([(200, 180), (240, 225)], fill=ink_color, width=stroke_width)
            # Stride legs
            draw.line([(200, 280), (145, 410)], fill=ink_color, width=stroke_width)
            draw.line([(200, 280), (255, 410)], fill=ink_color, width=stroke_width)
        else: # Neutral
            draw.line([(200, 180), (140, 240)], fill=ink_color, width=stroke_width)
            draw.line([(200, 180), (260, 240)], fill=ink_color, width=stroke_width)
            draw.line([(200, 280), (160, 420)], fill=ink_color, width=stroke_width)
            draw.line([(200, 280), (240, 420)], fill=ink_color, width=stroke_width)
            
        return img

    @classmethod
    def generate_prop(cls, prop_type: str = "coin", color=(10, 10, 10), stroke_width=6):
        img = cls.create_canvas(300, 300)
        draw = ImageDraw.Draw(img)
        
        if prop_type == "coin":
            # Outer coin ring + dollar sign
            draw.ellipse([50, 50, 250, 250], outline=color, width=stroke_width)
            draw.text((120, 95), "$", fill=color, font=ImageFont.truetype(r"C:\Windows\Fonts\seguibl.ttf", 90) if os.path.exists(r"C:\Windows\Fonts\seguibl.ttf") else None)
        elif prop_type == "chart":
            # Axes
            draw.line([(40, 40), (40, 260), (260, 260)], fill=color, width=stroke_width)
            # Upward exponential curve
            pts = [(50, 240), (100, 220), (150, 180), (200, 110), (250, 50)]
            draw.line(pts, fill=(165, 12, 12), width=stroke_width + 2) # Crimson line
            # Arrowhead
            draw.polygon([(250, 50), (230, 60), (245, 75)], fill=(165, 12, 12))
        elif prop_type == "desk":
            # Desktop line
            draw.line([(20, 180), (280, 180)], fill=color, width=stroke_width + 2)
            # Legs
            draw.line([(50, 180), (50, 280)], fill=color, width=stroke_width)
            draw.line([(250, 180), (250, 280)], fill=color, width=stroke_width)
            # Laptop on desk
            draw.line([(100, 180), (160, 180)], fill=color, width=stroke_width)
            draw.line([(160, 180), (145, 130)], fill=color, width=stroke_width)
        elif prop_type == "lightbulb":
            draw.ellipse([100, 60, 200, 160], outline=color, width=stroke_width)
            draw.line([(120, 160), (120, 190), (180, 190), (180, 160)], fill=color, width=stroke_width)
            draw.line([(130, 205), (170, 205)], fill=color, width=stroke_width)
            # Glow rays
            draw.line([(150, 25), (150, 45)], fill=(165, 12, 12), width=stroke_width)
            draw.line([(70, 70), (85, 85)], fill=(165, 12, 12), width=stroke_width)
            draw.line([(230, 70), (215, 85)], fill=(165, 12, 12), width=stroke_width)
        elif prop_type in ("cross", "red_x"):
            # Red circle with white X badge for negation items
            draw.ellipse([40, 40, 260, 260], fill=(210, 30, 30))
            draw.line([(90, 90), (210, 210)], fill=(255, 255, 255), width=stroke_width + 10)
            draw.line([(210, 90), (90, 210)], fill=(255, 255, 255), width=stroke_width + 10)
        else:
            draw.rectangle([60, 60, 240, 240], outline=color, width=stroke_width)
            
        return img

class LayoutGuide:
    """Calculates balanced layout coordinates, typography sizes, and asset proportions."""
    
    @staticmethod
    def get_slots(aspect_ratio: str = "16:9", width: int = 1920, height: int = 1080):
        if aspect_ratio == "16:9":
            return {
                "aspect": "16:9",
                "width": width,
                "height": height,
                "font_title": 64,
                "font_subtitle": 44,
                "font_label": 32,
                "max_text_width": 850,
                "hero_height": int(height * 0.45), # ~480px
                "prop_height": int(height * 0.28), # ~300px
                # 2-Column Split (Editorial Dan Koe layout)
                "left_hero": (int(width * 0.30), int(height * 0.52)),
                "right_hero": (int(width * 0.70), int(height * 0.52)),
                # Centered Layout
                "center_top_title": (int(width * 0.50), int(height * 0.18)),
                "center_hero": (int(width * 0.50), int(height * 0.52)),
                "center_bottom_sub": (int(width * 0.50), int(height * 0.84)),
                # 3-Column Comparative Layout
                "col_1": (int(width * 0.22), int(height * 0.52)),
                "col_2": (int(width * 0.50), int(height * 0.52)),
                "col_3": (int(width * 0.78), int(height * 0.52)),
            }
        else: # 9:16 Vertical Reel
            return {
                "aspect": "9:16",
                "width": width,
                "height": height,
                "font_title": 56,
                "font_subtitle": 44,
                "font_label": 36,
                "max_text_width": 920,
                "hero_height": int(height * 0.28), # ~540px
                "prop_height": int(height * 0.18), # ~350px
                # Vertical Stack
                "top_title": (int(width * 0.50), int(height * 0.18)),
                "center_hero": (int(width * 0.50), int(height * 0.50)),
                "bottom_sub": (int(width * 0.50), int(height * 0.80)),
                # Flanking
                "flank_left": (int(width * 0.28), int(height * 0.50)),
                "flank_right": (int(width * 0.72), int(height * 0.50)),
            }

class MinimalistCompositor:
    def __init__(self, width: int = None, height: int = None, aspect_ratio: str = "9:16", fps: int = 30, bg_path: str = None, bg_color: tuple = (242, 235, 219)):
        self.aspect_ratio = aspect_ratio
        if width is None and height is None:
            if aspect_ratio == "16:9":
                self.width, self.height = 1920, 1080
            else:
                self.width, self.height = 1080, 1920
        else:
            self.width = width or 1080
            self.height = height or 1920
            
        self.fps = fps
        self.bg_color = bg_color
        self.layout_slots = LayoutGuide.get_slots(self.aspect_ratio, self.width, self.height)
        
        if bg_path and os.path.exists(bg_path):
            self.base_bg = Image.open(bg_path).convert("RGB")
            if self.base_bg.size != (self.width, self.height):
                self.base_bg = self.base_bg.resize((self.width, self.height), Image.Resampling.LANCZOS)
        else:
            # Procedural organic paper texture (base color + subtle paper grain noise)
            np.random.seed(42)
            bg_arr = np.full((self.height, self.width, 3), bg_color, dtype=np.float32)
            noise = np.random.normal(0.0, 3.5, (self.height, self.width, 1)) # ±3.5% texture grain
            bg_arr = np.clip(bg_arr + noise, 0, 255).astype(np.uint8)
            self.base_bg = Image.fromarray(bg_arr, "RGB")
            
        self.font_cache = {}
        self.asset_cache = {}

    def get_font(self, font_name: str = "seguibl.ttf", size: int = 56):
        cache_key = (font_name, size)
        if cache_key in self.font_cache:
            return self.font_cache[cache_key]
        
        paths = [
            os.path.join(r"C:\Windows\Fonts", font_name),
            os.path.join(r"C:\Windows\Fonts", "seguibl.ttf"),
            os.path.join(r"C:\Windows\Fonts", "ariblk.ttf"),
            os.path.join(r"C:\Windows\Fonts", "arialbd.ttf"),
        ]
        font = None
        for p in paths:
            if os.path.exists(p):
                try:
                    font = ImageFont.truetype(p, size)
                    break
                except Exception:
                    continue
        if font is None:
            font = ImageFont.load_default()
        self.font_cache[cache_key] = font
        return font

    def render_portal_asset(
        self,
        canvas: Image.Image,
        asset_img: Image.Image,
        target_center: tuple,
        progress: float,
        direction: str = "up",
        portal_coord: int = None,
        feather: int = 3,
        mode: str = "enter",
        target_height: int = None
    ):
        """
        Renders an RGBA asset through a 1D track matte (portal).
        mode: 'enter' (progress 0->1 arrives at target_center), 
              'exit'  (progress 0->1 retreats back behind portal).
        target_height: Rescales asset to ideal proportional height (int or slot name e.g. 'hero_height').
        """
        if progress <= 0.0 and mode == "enter":
            return
        if progress >= 1.0 and mode == "exit":
            return
            
        if target_height:
            if isinstance(target_height, str) and target_height in self.layout_slots:
                target_height = self.layout_slots[target_height]
            if isinstance(target_height, (int, float)) and asset_img.size[1] != int(target_height):
                th = int(target_height)
                aspect = asset_img.size[0] / max(1, asset_img.size[1])
                new_w = max(1, int(th * aspect))
                asset_img = asset_img.resize((new_w, th), Image.Resampling.LANCZOS)

        eased = ease_out_cubic(progress) if mode == "enter" else ease_in_cubic(progress)
        effective_progress = eased if mode == "enter" else (1.0 - eased)
        
        asset_w, asset_h = asset_img.size
        final_cx, final_cy = target_center
        final_left = int(final_cx - asset_w // 2)
        final_top = int(final_cy - asset_h // 2)
        final_right = final_left + asset_w
        final_bottom = final_top + asset_h
        
        # When element has settled completely in 'enter' mode, render unclipped
        if progress >= 1.0 and mode == "enter":
            canvas.paste(asset_img, (final_left, final_top), asset_img)
            return
        
        if direction == "up":
            floor_y = portal_coord if portal_coord is not None else final_bottom
            current_top = int(floor_y - effective_progress * (floor_y - final_top))
            current_bottom = current_top + asset_h
            current_left = final_left
            clip_box = (0, 0, asset_w, max(0, min(asset_h, floor_y - current_top)))
        elif direction == "down":
            ceiling_y = portal_coord if portal_coord is not None else final_top
            current_top = int(ceiling_y - (1.0 - effective_progress) * (final_bottom - ceiling_y))
            current_bottom = current_top + asset_h
            current_left = final_left
            cut_offset = max(0, min(asset_h, ceiling_y - current_top))
            clip_box = (0, cut_offset, asset_w, asset_h)
        elif direction == "right":
            seam_x = portal_coord if portal_coord is not None else final_left
            current_left = int(seam_x - (1.0 - effective_progress) * (final_right - seam_x))
            current_top = final_top
            cut_offset = max(0, min(asset_w, seam_x - current_left))
            clip_box = (cut_offset, 0, asset_w, asset_h)
        elif direction == "left":
            seam_x = portal_coord if portal_coord is not None else final_right
            current_left = int(seam_x - effective_progress * (seam_x - final_left))
            current_top = final_top
            clip_box = (0, 0, max(0, min(asset_w, seam_x - current_left)), asset_h)
        else:
            raise ValueError(f"Unknown direction: {direction}")

        if clip_box[2] <= clip_box[0] or clip_box[3] <= clip_box[1]:
            return
            
        cropped_asset = asset_img.crop(clip_box)
        
        if feather > 0:
            np_asset = np.array(cropped_asset, dtype=np.uint8)
            alpha = np_asset[:, :, 3].astype(np.float32)
            
            if direction == "up" and clip_box[3] < asset_h:
                f_len = min(feather, alpha.shape[0])
                for f in range(f_len):
                    alpha[-(f + 1), :] *= ((f + 1) / (f_len + 1))
            elif direction == "down" and clip_box[1] > 0:
                f_len = min(feather, alpha.shape[0])
                for f in range(f_len):
                    alpha[f, :] *= ((f + 1) / (f_len + 1))
            elif direction == "left" and clip_box[2] < asset_w:
                f_len = min(feather, alpha.shape[1])
                for f in range(f_len):
                    alpha[:, -(f + 1)] *= ((f + 1) / (f_len + 1))
            elif direction == "right" and clip_box[0] > 0:
                f_len = min(feather, alpha.shape[1])
                for f in range(f_len):
                    alpha[:, f] *= ((f + 1) / (f_len + 1))
                    
            np_asset[:, :, 3] = np.clip(alpha, 0, 255).astype(np.uint8)
            cropped_asset = Image.fromarray(np_asset, "RGBA")

        paste_x = current_left + clip_box[0]
        paste_y = current_top + clip_box[1]
        canvas.paste(cropped_asset, (paste_x, paste_y), cropped_asset)

    def render_pop_asset(
        self,
        canvas: Image.Image,
        asset_img: Image.Image,
        target_center: tuple,
        progress: float,
        target_height: int = 120
    ):
        """Pops an asset into view with spring overshoot bounce."""
        if progress <= 0.0:
            return
        scale = spring_pop(progress)
        if scale <= 0.01:
            return
            
        aspect = asset_img.size[0] / max(1, asset_img.size[1])
        th = max(2, int(target_height * scale))
        tw = max(2, int(th * aspect))
        scaled = asset_img.resize((tw, th), Image.Resampling.LANCZOS)
        cx, cy = target_center
        paste_x = int(cx - tw // 2)
        paste_y = int(cy - th // 2)
        canvas.paste(scaled, (paste_x, paste_y), scaled)

    def render_portal_text(
        self,
        canvas: Image.Image,
        text: str,
        target_center: tuple,
        progress: float,
        direction: str = "up",
        portal_coord: int = None,
        font_size: int = 56,
        color: tuple = (10, 10, 10),
        font_name: str = "seguibl.ttf",
        max_width: int = 920,
        mode: str = "enter"
    ):
        """Renders multi-line auto-wrapped text sliding in through a track matte portal."""
        if (progress <= 0.0 and mode == "enter") or not text:
            return
            
        font = self.get_font(font_name, font_size)
        
        # Word wrap text if line exceeds max_width
        approx_chars = max(10, int(max_width / (font_size * 0.58)))
        lines = []
        for raw_line in text.split("\n"):
            lines.extend(textwrap.wrap(raw_line, width=approx_chars))
        if not lines:
            return
            
        line_height = int(font_size * 1.25)
        total_text_h = line_height * len(lines)
        
        dummy_img = Image.new("RGBA", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)
        max_w = 0
        line_bboxes = []
        for l in lines:
            bbox = draw_dummy.textbbox((0, 0), l, font=font)
            lw = bbox[2] - bbox[0]
            max_w = max(max_w, lw)
            line_bboxes.append(bbox)
            
        pad = 24
        surf_w = max_w + 2 * pad
        surf_h = total_text_h + 2 * pad
        
        text_surf = Image.new("RGBA", (surf_w, surf_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(text_surf)
        
        for idx, (l, bbox) in enumerate(zip(lines, line_bboxes)):
            lw = bbox[2] - bbox[0]
            lx = (surf_w - lw) // 2
            ly = pad + idx * line_height - bbox[1]
            draw.text((lx, ly), l, font=font, fill=color)
            
        self.render_portal_asset(
            canvas=canvas,
            asset_img=text_surf,
            target_center=target_center,
            progress=progress,
            direction=direction,
            portal_coord=portal_coord,
            feather=2,
            mode=mode
        )

    def render_portal_text_spans(
        self,
        canvas: Image.Image,
        spans: list, # [(text_str, font_size, rgb_color)]
        target_center: tuple,
        progress: float,
        direction: str = "up",
        portal_coord: int = None,
        font_name: str = "seguibl.ttf",
        mode: str = "enter"
    ):
        """Renders multi-color text spans on a line sliding through a track matte (e.g. black + crimson)."""
        if (progress <= 0.0 and mode == "enter") or not spans:
            return
            
        dummy = Image.new("RGBA", (1, 1))
        draw_d = ImageDraw.Draw(dummy)
        
        total_w = 0
        max_h = 0
        span_layouts = []
        
        for txt, sz, col in spans:
            f = self.get_font(font_name, sz)
            bb = draw_d.textbbox((0, 0), txt, font=f)
            tw = bb[2] - bb[0]
            th = bb[3] - bb[1]
            span_layouts.append((txt, f, col, tw, th, bb))
            total_w += tw
            max_h = max(max_h, th)
            
        pad = 24
        surf_w = total_w + 2 * pad
        surf_h = max_h + 2 * pad
        surf = Image.new("RGBA", (surf_w, surf_h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(surf)
        
        cur_x = pad
        for txt, f, col, tw, th, bb in span_layouts:
            draw.text((cur_x - bb[0], pad - bb[1]), txt, font=f, fill=tuple(col))
            cur_x += tw
            
        self.render_portal_asset(
            canvas=canvas,
            asset_img=surf,
            target_center=target_center,
            progress=progress,
            direction=direction,
            portal_coord=portal_coord,
            feather=2,
            mode=mode
        )

    def draw_dashed_arrow(
        self,
        canvas: Image.Image,
        start_pt: tuple,
        end_pt: tuple,
        progress: float,
        color: tuple = (10, 10, 10),
        width: int = 4,
        dash_len: int = 14,
        gap_len: int = 10,
        arrow_size: int = 16
    ):
        """Draws an animated progressive dashed line with arrowhead."""
        if progress <= 0.0:
            return
            
        eased = ease_out_cubic(progress)
        x1, y1 = start_pt
        x2, y2 = end_pt
        dx = x2 - x1
        dy = y2 - y1
        total_len = math.hypot(dx, dy)
        if total_len < 1:
            return
            
        ux = dx / total_len
        uy = dy / total_len
        current_len = total_len * eased
        
        draw = ImageDraw.Draw(canvas)
        curr_dist = 0.0
        
        while curr_dist < current_len:
            segment_end = min(curr_dist + dash_len, current_len)
            sx = x1 + ux * curr_dist
            sy = y1 + uy * curr_dist
            ex = x1 + ux * segment_end
            ey = y1 + uy * segment_end
            draw.line([(sx, sy), (ex, ey)], fill=color, width=width)
            curr_dist += dash_len + gap_len
            
        if progress > 0.8:
            cur_tip_x = x1 + ux * current_len
            cur_tip_y = y1 + uy * current_len
            angle = math.atan2(dy, dx)
            left_angle = angle + math.radians(145)
            right_angle = angle - math.radians(145)
            
            p1 = (cur_tip_x, cur_tip_y)
            p2 = (cur_tip_x + arrow_size * math.cos(left_angle), cur_tip_y + arrow_size * math.sin(left_angle))
            p3 = (cur_tip_x + arrow_size * math.cos(right_angle), cur_tip_y + arrow_size * math.sin(right_angle))
            draw.polygon([p1, p2, p3], fill=color)

    def render_scene_wipe(self, canvas_old: Image.Image, canvas_new: Image.Image, progress: float, direction: str = "left"):
        """Performs a directional paper wipe between two scene canvases with a subtle drop shadow."""
        eased = ease_out_cubic(progress)
        out_canvas = canvas_old.copy()
        
        if direction == "left":
            wipe_x = int(self.width * (1.0 - eased))
            if wipe_x < self.width:
                crop_new = canvas_new.crop((wipe_x, 0, self.width, self.height))
                out_canvas.paste(crop_new, (wipe_x, 0))
                # Soft paper shadow seam
                draw = ImageDraw.Draw(out_canvas)
                draw.line([(wipe_x, 0), (wipe_x, self.height)], fill=(200, 195, 185), width=3)
        elif direction == "up":
            wipe_y = int(self.height * (1.0 - eased))
            if wipe_y < self.height:
                crop_new = canvas_new.crop((0, wipe_y, self.width, self.height))
                out_canvas.paste(crop_new, (0, wipe_y))
                draw = ImageDraw.Draw(out_canvas)
                draw.line([(0, wipe_y), (self.width, wipe_y)], fill=(200, 195, 185), width=3)
        return out_canvas

    def render_cue_sheet(self, cue_sheet: dict, output_mp4: str, audio_path: str = None):
        """
        Orchestrates an entire multi-scene animation timeline from a structured cue sheet dict
        and streams frames directly to FFmpeg stdin (no temporary PNGs on disk).
        """
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(line_buffering=True)
        fps = cue_sheet.get("fps", self.fps)
        total_duration = cue_sheet.get("duration", 10.0)
        total_frames = int(total_duration * fps)
        scenes = cue_sheet.get("scenes", [])
        
        # Build FFmpeg streaming command
        cmd = [
            FFMPEG_PATH,
            "-y",
            "-f", "rawvideo",
            "-vcodec", "rawvideo",
            "-s", f"{self.width}x{self.height}",
            "-pix_fmt", "rgb24",
            "-r", str(fps),
            "-i", "-", # Pipe stdin
        ]
        if audio_path and os.path.exists(audio_path):
            cmd.extend(["-i", audio_path])
            cmd.extend(["-c:a", "aac", "-b:a", "192k"])
            
        cmd.extend([
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-crf", "17",
            "-t", str(total_duration),
            output_mp4
        ])
        
        print(f"[MinimalistEngine] Launching streaming render ({total_frames} frames @ {fps}fps)...")
        ffmpeg_log_path = output_mp4 + ".ffmpeg.log"
        log_f = open(ffmpeg_log_path, "w", encoding="utf-8")
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=log_f)
        
        try:
            for f in range(total_frames):
                t = f / fps
                
                # Determine current active scene
                active_scene = None
                for s in scenes:
                    if s["start"] <= t < (s["start"] + s["duration"]):
                        active_scene = s
                        break
                if not active_scene and scenes:
                    active_scene = scenes[-1]
                    
                canvas = self.base_bg.copy()
                
                if active_scene:
                    scene_t = t - active_scene["start"]
                    elements = active_scene.get("elements", [])
                    
                    for el in elements:
                        el_enter = el.get("enter_time", 0.0)
                        el_dur = el.get("duration", 0.5)
                        el_exit = el.get("exit_time")
                        el_exit_dur = el.get("exit_duration", 0.4)
                        
                        if scene_t < el_enter:
                            continue # Not yet entered
                            
                        mode = "enter"
                        if el_exit is not None and scene_t >= el_exit:
                            mode = "exit"
                            progress = min(1.0, (scene_t - el_exit) / max(0.01, el_exit_dur))
                            if progress >= 1.0:
                                continue # Element has completely exited, do not draw
                        else:
                            progress = min(1.0, (scene_t - el_enter) / max(0.01, el_dur))
                            
                        el_type = el.get("type", "text")
                        direction = el.get("direction", "up")
                        raw_center = el.get("target_center", [self.width // 2, self.height // 2])
                        if isinstance(raw_center, str) and raw_center in self.layout_slots:
                            target_center = self.layout_slots[raw_center]
                        else:
                            target_center = tuple(raw_center)
                            
                        portal_coord = el.get("portal_coord")
                        target_height = el.get("target_height")
                        default_fs = self.layout_slots.get("font_title", 56)
                        default_mw = self.layout_slots.get("max_text_width", int(self.width * 0.8))
                        font_size = el.get("font_size", default_fs)
                        max_width = el.get("max_width", default_mw)
                        
                        if el_type == "text":
                            self.render_portal_text(
                                canvas=canvas,
                                text=el["text"],
                                target_center=target_center,
                                progress=progress,
                                direction=direction,
                                portal_coord=portal_coord,
                                font_size=font_size,
                                color=tuple(el.get("color", [10, 10, 10])),
                                max_width=max_width,
                                mode=mode
                            )
                        elif el_type == "text_spans":
                            self.render_portal_text_spans(
                                canvas=canvas,
                                spans=el.get("spans", []),
                                target_center=target_center,
                                progress=progress,
                                direction=direction,
                                portal_coord=portal_coord,
                                font_name=el.get("font_name", "seguibl.ttf"),
                                mode=mode
                            )
                        elif el_type == "stickman":
                            pose = el.get("pose", "neutral")
                            asset = ProceduralAssetGenerator.generate_stickman(pose=pose)
                            self.render_portal_asset(
                                canvas=canvas,
                                asset_img=asset,
                                target_center=target_center,
                                progress=progress,
                                direction=direction,
                                portal_coord=portal_coord,
                                mode=mode,
                                target_height=target_height or "hero_height"
                            )
                        elif el_type == "prop":
                            prop_name = el.get("prop", "coin")
                            asset = ProceduralAssetGenerator.generate_prop(prop_type=prop_name)
                            if el.get("animation") == "pop":
                                self.render_pop_asset(
                                    canvas=canvas,
                                    asset_img=asset,
                                    target_center=target_center,
                                    progress=progress,
                                    target_height=target_height or 120
                                )
                            else:
                                self.render_portal_asset(
                                    canvas=canvas,
                                    asset_img=asset,
                                    target_center=target_center,
                                    progress=progress,
                                    direction=direction,
                                    portal_coord=portal_coord,
                                    mode=mode,
                                    target_height=target_height or "prop_height"
                                )
                        elif el_type in ("image", "pop"):
                            asset_path = el.get("path")
                            if asset_path and os.path.exists(asset_path):
                                if asset_path not in self.asset_cache:
                                    self.asset_cache[asset_path] = Image.open(asset_path).convert("RGBA")
                                asset = self.asset_cache[asset_path]
                                if el_type == "pop" or el.get("animation") == "pop":
                                    self.render_pop_asset(
                                        canvas=canvas,
                                        asset_img=asset,
                                        target_center=target_center,
                                        progress=progress,
                                        target_height=target_height or 120
                                    )
                                else:
                                    self.render_portal_asset(
                                        canvas=canvas,
                                        asset_img=asset,
                                        target_center=target_center,
                                        progress=progress,
                                        direction=direction,
                                        portal_coord=portal_coord,
                                        mode=mode,
                                        target_height=target_height
                                    )
                        elif el_type == "arrow":
                            if mode == "enter":
                                sp = el.get("start_pt", [self.width // 2, int(self.height * 0.4)])
                                ep = el.get("end_pt", [self.width // 2, int(self.height * 0.7)])
                                start_pt = self.layout_slots[sp] if isinstance(sp, str) and sp in self.layout_slots else tuple(sp)
                                end_pt = self.layout_slots[ep] if isinstance(ep, str) and ep in self.layout_slots else tuple(ep)
                                self.draw_dashed_arrow(
                                    canvas=canvas,
                                    start_pt=start_pt,
                                    end_pt=end_pt,
                                    progress=progress,
                                    color=tuple(el.get("color", [10, 10, 10])),
                                    width=el.get("width", 4)
                                )
                
                # Stream raw frame bytes to FFmpeg stdin
                proc.stdin.write(canvas.tobytes())
                
            proc.stdin.close()
            proc.wait()
            log_f.close()
            
            if proc.returncode != 0:
                with open(ffmpeg_log_path, "r", encoding="utf-8", errors="ignore") as lf:
                    stderr_out = lf.read()
                raise RuntimeError(f"FFmpeg render failed: {stderr_out}")
            
            if os.path.exists(ffmpeg_log_path):
                try:
                    os.remove(ffmpeg_log_path)
                except Exception:
                    pass
            print(f"[MinimalistEngine] Successfully streamed and encoded video: {output_mp4}")
            
        except Exception as e:
            try:
                proc.kill()
            except Exception:
                pass
            try:
                log_f.close()
            except Exception:
                pass
            raise e

if __name__ == "__main__":
    print("Minimalist Animation Style Engine (Comprehensive Production Edition) Initialized.")
