import sys
import subprocess
import os

def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    finally:
        globals()[package] = __import__(package)

install_and_import('pymupdf4llm')
import pymupdf4llm

def convert(pdf_path, md_path):
    print(f"Converting {pdf_path} to {md_path}...")
    md_text = pymupdf4llm.to_markdown(pdf_path)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_text)
    print("Done!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert.py <pdf_path> [md_path]")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    
    if len(sys.argv) >= 3:
        md_path = sys.argv[2]
    else:
        # Default md path
        base = os.path.splitext(pdf_path)[0]
        md_path = base + ".md"
        
    convert(pdf_path, md_path)
