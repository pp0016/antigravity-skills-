import requests
import base64
import os
import cv2
import numpy as np
import glob
import sys
import argparse
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

print("Starting API script...")
sys.stdout.flush()

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-inpainting"
WEDGE_B64 = "paWlpaWlpaWlpaWlpaWmpaWlpaampaWlpaampqampKWlpqanp6WkpqWmpqempqalpaalpaWWYKinpqSlpaWcaCQAp6akpKWkn3QwAAAApaSjpKWkfzcQAAAAAJ+goqKjjUgQAAAAAAAAnJ6goJlfGAAAAAAAAAAAoqGhoHkvAAAAAAAAAAAAAKCho5JOEQAAAAAAAAAAAAAAnJ+icyUAAAAAAAAAAAAAAAAAnqCWTQAAAAAAAAAAAAAAAAAAAKGjeywAAAAAAAAAAAAAAAAAAAAAop5cEgAAAAAAAAAAAAAAAAAAAAAAoYw/AAAAAAAAAAAAAAAAAAAAAAAAAJ9yJgAAAAAAAAAAAAAAAAAAAAAAAAAAlVkRAAAAAAAAAAAAAAAAAAAAAAAAAAAATSoA"
def create_star_map():
    wedge_bytes = base64.b64decode(WEDGE_B64)
    star = np.zeros((65, 65), dtype=np.float32)
    for j in range(65):
        for i in range(65):
            dx, dy = abs(i - 32), abs(j - 32)
            mx, mn = max(dx, dy), min(dx, dy)
            idx = int(mx * (mx + 1) / 2 + mn)
            val = wedge_bytes[idx] if idx < len(wedge_bytes) else 0
            star[j, i] = (val / 255.0) * 0.5
    return star
STAR = create_star_map()
def bilinear_sample_grid(a, x, y):
    h, w = a.shape
    x, y = np.asarray(x, dtype=np.float32), np.asarray(y, dtype=np.float32)
    x0, y0 = np.clip(np.floor(x).astype(np.int32), 0, w-1), np.clip(np.floor(y).astype(np.int32), 0, h-1)
    x1, y1 = np.clip(x0 + 1, 0, w-1), np.clip(y0 + 1, 0, h-1)
    tx, ty = x - x0, y - y0
    oob = (x < 0) | (x > w-1) | (y < 0) | (y > h-1)
    res = (a[y0, x0]*(1-tx) + a[y0, x1]*tx)*(1-ty) + (a[y1, x0]*(1-tx) + a[y1, x1]*tx)*ty
    return np.where(oob, 0.0, res)

def process_image_api(filepath, out_path, hf_token):
    headers = {"Authorization": f"Bearer {hf_token}"}
    try:
        with open(filepath, 'rb') as fp:
            img_bytes = fp.read()
            img = cv2.imdecode(np.frombuffer(img_bytes, dtype=np.uint8), cv2.IMREAD_COLOR)
        if img is None: return False
        
        h, w = img.shape[:2]
        s = w / 1376.0
        cx, cy = w - 97.5 * s, h - 97.6 * s
        yy, xx = np.mgrid[0:h, 0:w]
        u, v = (xx - cx) / s + 32, (yy - cy) / s + 32
        a_map = bilinear_sample_grid(STAR, u, v)

        mask = np.zeros((h, w), dtype=np.uint8)
        mask[a_map > 0.02] = 255
        mask = cv2.dilate(mask, np.ones((5,5), np.uint8), iterations=1)
        
        _, mask_buf = cv2.imencode('.png', mask)
        mask_bytes = mask_buf.tobytes()
        
        _, img_png_buf = cv2.imencode('.png', img)
        img_png_bytes = img_png_buf.tobytes()

        # Disable retries to fail fast
        session = requests.Session()
        retry = Retry(connect=0, read=0, redirect=0)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('https://', adapter)
        
        response = session.post(
            API_URL,
            headers=headers,
            data={"inputs": "background texture, seamless"},
            files={"image": img_png_bytes, "mask_image": mask_bytes},
            timeout=10
        )
        
        if response.status_code == 200:
            with open(out_path, 'wb') as fp:
                fp.write(response.content)
            return True
        else:
            print(f"API Error {response.status_code}: {response.text}", end=' ')
            return False
    except Exception as e:
        print(f"Network Error: {e}", end=' ')
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input image or folder")
    parser.add_argument("output", nargs="?", help="Output folder")
    parser.add_argument("--token", required=True, help="Hugging Face API Token")
    args = parser.parse_args()
    
    files = []
    if os.path.isdir(args.input):
        for ext in ('*.png', '*.jpg', '*.jpeg', '*.webp'):
            files.extend(glob.glob(os.path.join(args.input, ext)))
    else:
        files = [args.input]
        
    print(f"Found {len(files)} files to process using Hugging Face API...")
    sys.stdout.flush()
    
    for f in files:
        base, ext = os.path.splitext(os.path.basename(f))
        out_dir = args.output
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, base + ext)
        else:
            out_path = f.replace(ext, f"-cleaned{ext}")
            
        print(f"Cloud Processing {os.path.basename(f)}...", end=' ')
        sys.stdout.flush()
        if process_image_api(f, out_path, args.token):
            print(f"Done!")
        else:
            print(f"Failed!")
        sys.stdout.flush()
