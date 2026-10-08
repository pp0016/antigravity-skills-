import cv2
import numpy as np
import base64
import os
import glob
import sys

def create_star_map():
    WEDGE_B64 = "paWlpaWlpaWlpaWlpaWmpaWlpaampaWlpaampqampKWlpqanp6WkpqWmpqempqalpaalpaWWYKinpqSlpaWcaCQAp6akpKWkn3QwAAAApaSjpKWkfzcQAAAAAJ+goqKjjUgQAAAAAAAAnJ6goJlfGAAAAAAAAAAAoqGhoHkvAAAAAAAAAAAAAKCho5JOEQAAAAAAAAAAAAAAnJ+icyUAAAAAAAAAAAAAAAAAnqCWTQAAAAAAAAAAAAAAAAAAAKGjeywAAAAAAAAAAAAAAAAAAAAAop5cEgAAAAAAAAAAAAAAAAAAAAAAoYw/AAAAAAAAAAAAAAAAAAAAAAAAAJ9yJgAAAAAAAAAAAAAAAAAAAAAAAAAAlVkRAAAAAAAAAAAAAAAAAAAAAAAAAAAATSoA"
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

def get_mask(h, w):
    s = w / 1376.0
    cx, cy = w - 97.5 * s, h - 97.6 * s
    yy, xx = np.mgrid[0:h, 0:w]
    u, v = (xx - cx) / s + 32, (yy - cy) / s + 32
    a_map = bilinear_sample_grid(STAR, u, v)
    mask = np.zeros((h, w), dtype=np.uint8)
    mask[a_map > 0.02] = 255
    return cv2.dilate(mask, np.ones((5,5), np.uint8), iterations=1)

def process_image(model, filepath, out_path, InpaintRequest):
    try:
        with open(filepath, 'rb') as fp:
            img = cv2.imdecode(np.frombuffer(fp.read(), dtype=np.uint8), cv2.IMREAD_COLOR)
        if img is None: return False
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mask = get_mask(img_rgb.shape[0], img_rgb.shape[1])

        req = InpaintRequest()
        result = model(img_rgb, mask, req)
        result_bgr = cv2.cvtColor(result, cv2.COLOR_RGB2BGR)
        
        _, buf = cv2.imencode('.jpg', result_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
        with open(out_path, 'wb') as fp:
            fp.write(buf)
        return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input file or folder")
    parser.add_argument("output", nargs="?", help="Output folder")
    args = parser.parse_args()
    
    input_path = args.input
    out_dir = args.output
    
    img_exts = {'.png', '.jpg', '.jpeg', '.webp'}
    
    files = []
    if os.path.isdir(input_path):
        for ext in img_exts:
            files.extend(glob.glob(os.path.join(input_path, f'*{ext}')))
            files.extend(glob.glob(os.path.join(input_path, f'*{ext.upper()}')))
    else:
        files = [input_path]
        
    # Deduplicate in case of case-insensitive glob overlaps
    files = list(set(files))
    
    if len(files) == 0:
        print("No valid images found.")
        sys.exit(0)
        
    print(f"Found {len(files)} images to process.")
    sys.stdout.flush()
    
    print("Loading AI Model (this takes a few seconds)...")
    sys.stdout.flush()
    from iopaint.model_manager import ModelManager
    from iopaint.schema import InpaintRequest
    model = ModelManager("lama", device="cpu")
    print("Model loaded successfully.\n")
    sys.stdout.flush()
    
    for f in files:
        base, ext = os.path.splitext(os.path.basename(f))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
            out_path = os.path.join(out_dir, base + ext)
        else:
            out_path = f.replace(ext, f"-cleaned{ext}")
            
        print(f"Processing Image: {os.path.basename(f)}...")
        sys.stdout.flush()
        
        success = process_image(model, f, out_path, InpaintRequest)
            
        if success:
            print(f"  -> Saved {out_path}\n")
        else:
            print(f"  -> Failed\n")
        sys.stdout.flush()
