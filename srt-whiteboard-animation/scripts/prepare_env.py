#!/usr/bin/env python3
"""
Stream Whiteboard Animation - Environment Setup & Verification Script

Responsibilities:
  1. Create an isolated Python virtual environment (.venv) under the skill directory (reuses if existing).
  2. Verify all required third-party libraries can be imported.
  3. Automatically install missing packages via pip.
  4. Print ENV_PY=<interpreter_path> on the last line for caller scripts / orchestrators to capture.

Usage:
  python prepare_env.py          # Setup venv + install dependencies, prints ENV_PY
  python prepare_env.py --check  # Probe environment only; exits non-zero if dependencies are missing
"""
from __future__ import annotations

import os
import subprocess
import sys
import venv
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

# Skill root directory = two levels up from this script
SKILL_ROOT = Path(__file__).resolve().parent.parent
VENV_ROOT = SKILL_ROOT / ".venv"

# Module import name -> pip package name
DEPS: dict[str, str] = {
    "cv2": "opencv-python",
    "numpy": "numpy",
    "av": "av",        # PyAV: pure-pip H.264 fallback encoder without external ffmpeg
    "PIL": "Pillow",    # Pillow: preview generation with region labeling
}


def interpreter_path() -> Path:
    """Path to the python executable inside the virtual environment (cross-platform)."""
    if sys.platform.startswith("win"):
        return VENV_ROOT / "Scripts" / "python.exe"
    return VENV_ROOT / "bin" / "python"


def ensure_venv(check_only: bool) -> Path:
    py = interpreter_path()
    if VENV_ROOT.exists() and py.exists():
        print(f"[ok] Reusing existing virtual environment: {VENV_ROOT}")
        return py

    if check_only:
        print(f"[err] Virtual environment does not exist: {VENV_ROOT}")
        sys.exit(1)

    print(f"[..] Creating virtual environment: {VENV_ROOT}")
    venv.create(str(VENV_ROOT), with_pip=True, system_site_packages=True)
    print("[ok] Virtual environment ready")
    return py


def can_import(py: Path, import_name: str) -> bool:
    probe = subprocess.run(
        [str(py), "-c", f"import {import_name}"],
        capture_output=True,
    )
    return probe.returncode == 0


def install(py: Path, packages: list[str]) -> bool:
    if not packages:
        return True
    print(f"[..] Installing packages: {', '.join(packages)}")
    res = subprocess.run(
        [str(py), "-m", "pip", "install", "--quiet", *packages],
        capture_output=True,
        text=True,
    )
    if res.returncode != 0:
        print(f"[err] Installation failed:\n{res.stderr}")
        return False
    print("[ok] Package installation finished successfully")
    return True


def main() -> None:
    check_only = "--check" in sys.argv

    py = ensure_venv(check_only)

    missing: list[str] = []
    for import_name, pip_name in DEPS.items():
        if can_import(py, import_name):
            print(f"[ok] {pip_name}")
        else:
            print(f"[miss] {pip_name}")
            missing.append(pip_name)

    if missing:
        if check_only:
            print(f"\nMissing {len(missing)} dependencies: {', '.join(missing)}")
            sys.exit(1)
        if not install(py, missing):
            sys.exit(1)

    # Last line: contract output for upstream caller to capture
    print(f"\nENV_PY={py}")


if __name__ == "__main__":
    main()
