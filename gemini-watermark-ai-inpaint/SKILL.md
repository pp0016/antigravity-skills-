---
name: gemini-watermark-ai-inpaint
description: >
  Advanced Generative AI Image Inpainting. Uses LaMa (Local) or Stable Diffusion (API) to perfectly hallucinate and synthesize missing textures over the Gemini Sparkle watermark, matching commercial software (Erasio) quality.
---

# gemini-watermark-ai-inpaint

This skill completely replaces mathematical un-blending with a **Generative AI Pipeline** to literally hallucinate missing textures on heavily compressed or complex backgrounds. 

It comes with two scripts:
1. **Local Version (`remove_sparkle_ai.py`)**: Runs 100% offline and free forever on your PC.
2. **API Version (`remove_sparkle_api.py`)**: Uses Hugging Face's Cloud API (requires API key) if you want to offload the AI work.

## Usage (Local - Recommended, 100% Free)
Single Image:
python C:\path\to\gemini-watermark-ai-inpaint\scripts\remove_sparkle_ai.py "C:\path\to\image.jpeg"

## Usage (Cloud API - Requires Hugging Face Token)
Single Image:
python C:\path\to\gemini-watermark-ai-inpaint\scripts\remove_sparkle_api.py "C:\path\to\image.jpeg" --token "hf_YourTokenHere"
