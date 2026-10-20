#!/usr/bin/env python3
"""
Multi-Scene Merger: Concatenates whiteboard animation scene MP4 files in sequential order.

Prefers lossless ffmpeg stream copy (-c copy, no re-encoding). If input dimensions / codecs
differ or ffmpeg is unavailable, falls back to PyAV frame-by-frame re-encoding scaled to the
first scene's dimensions.

Usage:
  python merge_scenes.py --inputs scene1.mp4 scene2.mp4 scene3.mp4 --output final.mp4
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
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

# Primary WinGet FFmpeg installation path on Windows
WINGET_FFMPEG = Path(
    r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"
)


def _find_ffmpeg() -> str | None:
    if WINGET_FFMPEG.exists():
        return str(WINGET_FFMPEG)
    found = shutil.which("ffmpeg")
    return found if found else None


def _ffmpeg_concat_copy(inputs: list[Path], output: Path) -> bool:
    ffmpeg = _find_ffmpeg()
    if ffmpeg is None:
        return False
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        for p in inputs:
            f.write(f"file '{p.resolve().as_posix()}'\n")
        list_path = Path(f.name)
    try:
        # Step 1: Attempt lossless stream copy (-c copy)
        res = subprocess.run(
            [ffmpeg, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", str(list_path), "-c", "copy", str(output)],
            capture_output=True, text=True,
        )
        if res.returncode == 0:
            print(f"  FFmpeg lossless stream copy completed: {output}")
            return True
        print(f"  [warn] FFmpeg -c copy failed; attempting zero-degradation re-encode: {res.stderr.strip()[:200]}")
        # Step 2: Fallback re-encode with zero-degradation parameters (-crf 17 -pix_fmt yuv420p)
        res = subprocess.run(
            [ffmpeg, "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
             "-i", str(list_path), "-c:v", "libx264", "-crf", "17",
             "-pix_fmt", "yuv420p", "-vf", "scale='trunc(iw/2)*2':'trunc(ih/2)*2'", str(output)],
            capture_output=True, text=True,
        )
        if res.returncode == 0:
            print(f"  FFmpeg re-encoded concatenation completed: {output}")
            return True
        print(f"  [warn] FFmpeg re-encode also failed: {res.stderr.strip()[:200]}")
        return False
    finally:
        list_path.unlink(missing_ok=True)


def _pyav_concat(inputs: list[Path], output: Path) -> bool:
    try:
        import av
    except ImportError:
        return False
    import numpy as np  # noqa: F401
    first = av.open(str(inputs[0]))
    vs = first.streams.video[0]
    w, h = vs.codec_context.width, vs.codec_context.height
    rate = vs.average_rate
    first.close()

    out = av.open(str(output), mode="w")
    ostream = out.add_stream("h264", rate=rate)
    ostream.width, ostream.height = w, h
    ostream.pix_fmt = "yuv420p"
    ostream.options = {"crf": "17", "preset": "medium"}
    for p in inputs:
        cont = av.open(str(p))
        for frame in cont.decode(video=0):
            if frame.width != w or frame.height != h:
                frame = frame.reformat(width=w, height=h)
            for pkt in ostream.encode(frame):
                out.mux(pkt)
        cont.close()
    for pkt in ostream.encode(None):
        out.mux(pkt)
    out.close()
    print(f"  PyAV concatenation completed: {output}")
    return True


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Concatenate multi-scene whiteboard animation MP4s in sequential order")
    p.add_argument("--inputs", nargs="+", required=True, help="List of MP4 file paths in playback order")
    p.add_argument("--output", required=True, help="Path for merged output MP4 file")
    args = p.parse_args(argv)

    inputs = [Path(x) for x in args.inputs]
    missing = [str(x) for x in inputs if not x.exists()]
    if missing:
        print(f"[err] Missing input files: {', '.join(missing)}", file=sys.stderr)
        return 1
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    if _ffmpeg_concat_copy(inputs, output) or _pyav_concat(inputs, output):
        print(f"OUTPUT={output.resolve()}")
        return 0
    print("[err] Concatenation failed: Neither FFmpeg nor PyAV are operational", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
