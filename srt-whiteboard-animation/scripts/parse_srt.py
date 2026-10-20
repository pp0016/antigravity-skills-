#!/usr/bin/env python3
"""
SRT Parser + Scene Storyboard Suggester

Parses .srt subtitle files into structured cues, and groups them into logical scenes
aiming for 25–35 seconds of voiceover narration per scene. Outputs start/end timestamps,
total scene duration (which feeds into sceneDurationMs), and aggregated subtitle text.

Usage:
  python parse_srt.py <subtitles.srt> [--target-sec 30] [--min-sec 25] [--max-sec 35]

Output: JSON (stdout), fields:
  cues    List of subtitle cues: {index, startMs, endMs, durMs, text}
  scenes  Suggested scene cuts: {sceneIndex, startMs, endMs, sceneDurationMs, cueRange, text}
Standard stderr prints a human-readable summary.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
if sys.stderr.encoding and sys.stderr.encoding.lower() != "utf-8":
    try:
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

_TIME = re.compile(r"(\d+):(\d{2}):(\d{2})[,.](\d{1,3})")


def _to_ms(h: str, m: str, s: str, ms: str) -> int:
    return ((int(h) * 60 + int(m)) * 60 + int(s)) * 1000 + int(ms.ljust(3, "0"))


def parse_srt(text: str) -> list[dict]:
    """Parse raw SRT text into a structured list of cue dicts. Tolerates BOM and comma/dot milliseconds."""
    text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    blocks = re.split(r"\n\s*\n", text.strip())
    cues: list[dict] = []
    for block in blocks:
        lines = [ln for ln in block.split("\n") if ln.strip() != ""]
        if not lines:
            continue
        time_line_idx = next((i for i, ln in enumerate(lines) if "-->" in ln), None)
        if time_line_idx is None:
            continue
        times = _TIME.findall(lines[time_line_idx])
        if len(times) < 2:
            continue
        start = _to_ms(*times[0])
        end = _to_ms(*times[1])
        body = " ".join(lines[time_line_idx + 1:]).strip()
        cues.append({
            "index": len(cues) + 1,
            "startMs": start,
            "endMs": end,
            "durMs": max(0, end - start),
            "text": body,
        })
    return cues


def group_scenes(cues: list[dict], target_sec: float, min_sec: float, max_sec: float) -> list[dict]:
    """
    Cluster consecutive cues into scenes based on target duration:
    Splits when accumulated time approaches target_sec, bounded between min_sec and max_sec.
    """
    scenes: list[dict] = []
    bucket: list[dict] = []
    target_ms, min_ms, max_ms = target_sec * 1000, min_sec * 1000, max_sec * 1000

    def flush() -> None:
        if not bucket:
            return
        start = bucket[0]["startMs"]
        end = bucket[-1]["endMs"]
        scenes.append({
            "sceneIndex": len(scenes) + 1,
            "startMs": start,
            "endMs": end,
            "sceneDurationMs": max(0, end - start),
            "cueRange": [bucket[0]["index"], bucket[-1]["index"]],
            "text": " ".join(c["text"] for c in bucket).strip(),
        })
        bucket.clear()

    for cue in cues:
        if bucket:
            span_with = cue["endMs"] - bucket[0]["startMs"]
            if span_with > max_ms:
                flush()
        bucket.append(cue)
        span = bucket[-1]["endMs"] - bucket[0]["startMs"]
        if span >= target_ms and span >= min_ms:
            flush()
    flush()
    return scenes


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="SRT Subtitle Parser + Scene Storyboard Suggester")
    p.add_argument("srt", help="Path to SRT subtitle file (.srt)")
    p.add_argument("--target-sec", type=float, default=30.0, help="Target voiceover seconds per scene (default: 30)")
    p.add_argument("--min-sec", type=float, default=25.0, help="Minimum seconds per scene (default: 25)")
    p.add_argument("--max-sec", type=float, default=35.0, help="Maximum seconds per scene (default: 35)")
    args = p.parse_args(argv)

    try:
        raw = Path(args.srt).read_text(encoding="utf-8-sig")
    except OSError as e:
        print(f"[err] Failed to read subtitle file: {e}", file=sys.stderr)
        return 1

    cues = parse_srt(raw)
    if not cues:
        print("[err] No subtitle cues found; please verify SRT format", file=sys.stderr)
        return 1
    scenes = group_scenes(cues, args.target_sec, args.min_sec, args.max_sec)

    total_ms = cues[-1]["endMs"] - cues[0]["startMs"]
    print(f"Subtitle cues: {len(cues)}  Total Duration: {total_ms/1000:.1f}s  Suggested Scenes: {len(scenes)}", file=sys.stderr)
    for s in scenes:
        print(f"  Scene {s['sceneIndex']:>2}  {s['startMs']/1000:6.1f}-{s['endMs']/1000:6.1f}s "
              f"({s['sceneDurationMs']/1000:4.1f}s, Cues {s['cueRange'][0]}-{s['cueRange'][1]}): "
              f"{s['text'][:50]}...", file=sys.stderr)

    json.dump({"cues": cues, "scenes": scenes}, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
