---
name: kokoro-local-tts
description: >-
  Use this skill to generate high-quality text-to-speech audio locally and completely free using Kokoro-ONNX.
  It runs directly on CPU with 8GB RAM and requires no API keys or internet connection.
---

# Kokoro Local TTS

This skill allows you to generate text-to-speech locally using the Kokoro v1.0 ONNX model.
The installation is fully self-contained in `c:\Users\renu5\Downloads\after github\kokoro-tts`.

## How to Generate Audio

To use this skill, create a python script in the workspace or run python via terminal.

### Usage Example
```python
import sys
import soundfile as sf
from kokoro_onnx import Kokoro

def generate_tts(text, output_file="output.wav", voice="af_sarah"):
    # Load model and voices
    kokoro = Kokoro(
        "c:/Users/renu5/Downloads/after github/kokoro-tts/kokoro-v1.0.onnx",
        "c:/Users/renu5/Downloads/after github/kokoro-tts/voices-v1.0.bin"
    )
    
    print(f"Generating audio for text: {text[:50]}...")
    samples, sample_rate = kokoro.create(
        text, 
        voice=voice, 
        speed=1.0, 
        lang="en-us"
    )
    
    sf.write(output_file, samples, sample_rate)
    print(f"Audio successfully saved to {output_file}")

if __name__ == "__main__":
    generate_tts("Hello, this is a test of Kokoro TTS running completely locally on your laptop.")
```

### Steps for the AI (When the user asks you to use Kokoro):
1. Navigate to the `kokoro-tts` directory: `c:\Users\renu5\Downloads\after github\kokoro-tts`.
2. Write a Python script like the one above, importing from `kokoro_onnx`.
3. Execute the script using the dedicated virtual environment:
   `c:\Users\renu5\Downloads\after github\kokoro-tts\venv\Scripts\python.exe your_script.py`
4. The generated `.wav` file will be created.

### Features
* **Zero Cost**: No API keys needed.
* **CPU Friendly**: Optimized to run fast without VRAM, perfectly suited for standard 8GB RAM laptops.
* **Voices**: Voices are packed in `voices-v1.0.bin`. Common English voices: `af_sarah`, `af_bella`, `am_michael`, `am_adam`, `bf_emma`, `bm_george`.
