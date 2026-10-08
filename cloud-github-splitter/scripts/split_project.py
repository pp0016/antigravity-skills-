import os
import shutil
import sys
import argparse

def scrub_secrets(filepath):
    secrets = [
        "YOUR_OPENROUTER_API_KEY_HERE",
        "YOUR_GROQ_API_KEY_HERE"
    ]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changed = False
        for secret in secrets:
            if secret in content:
                content = content.replace(secret, "REMOVED_FOR_SECURITY")
                changed = True
                
        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
    except Exception:
        pass

def create_merge_instructions(github_dest, project_name):
    instruction_path = os.path.join(github_dest, "MERGE_INSTRUCTIONS_AI.md")
    content = f"""# AI Merge & Restore Instructions for '{project_name}'

**Action Required by AI Agent:** 
The user has downloaded their GitHub repo (as a zip and extracted it) and downloaded their heavy media files from the cloud. They will provide you with the paths to both folders. Your job is to merge them and restore dependencies.

## Step 1: Auto-Merge the Cloud Files
1. Ask the user to paste the paths for BOTH the extracted GitHub folder and the Cloud leftover folder (if they haven't provided them already).
2. Automatically copy all files and folders from the Cloud leftover directory directly into the GitHub repository folder, merging the structures together perfectly.

## Step 2: Restore Dependencies
Because dependency folders were ignored during backup, you must restore them automatically:
- If you see a `package.json`, run `npm install`
- If you see a `requirements.txt`, run `pip install -r requirements.txt`
- If you see a `pyproject.toml` or `uv.lock`, run the appropriate `uv` or `pip` install command.

Once complete, notify the user that the project is 100% merged and ready to use!
"""
    with open(instruction_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", help="The source project directory path")
    args = parser.parse_args()

    source = os.path.abspath(args.source)
    if not os.path.exists(source):
        print(f"Error: Source directory '{source}' does not exist.")
        sys.exit(1)

    project_name = os.path.basename(source)
    backup_root = r"C:\Users\renu5\Downloads\backup"
    
    staging_dir = os.path.join(backup_root, f"{project_name}_staging")
    github_dest = os.path.join(backup_root, "github", f"{project_name} copy for git")
    cloud_dest = os.path.join(backup_root, "leftover for cloud", f"{project_name} copy for git leftover")

    media_exts = {
        '.mp4', '.mp3', '.wav', '.mov', '.avi', '.mkv', '.webm', '.wmv', 
        '.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.bmp', '.tiff'
    }
    ignore_dirs = {'.git', 'node_modules', '.venv', 'venv', '__pycache__'}
    
    MAX_SIZE_BYTES = 100 * 1024 * 1024 

    print(f"Phase 1: Copying '{project_name}' to backup folder...")
    if os.path.exists(staging_dir):
        shutil.rmtree(staging_dir)
    
    def ignore_func(dir_path, contents):
        return [c for c in contents if c in ignore_dirs and os.path.isdir(os.path.join(dir_path, c))]
        
    shutil.copytree(source, staging_dir, ignore=ignore_func)

    print("Phase 2: Dividing files...")
    for root, dirs, files in os.walk(staging_dir):
        for file in files:
            src_path = os.path.join(root, file)
            rel_path = os.path.relpath(src_path, staging_dir)
            ext = os.path.splitext(file)[1].lower()
            file_size = os.path.getsize(src_path)
            
            if ext in media_exts or file_size >= MAX_SIZE_BYTES:
                dest_path = os.path.join(cloud_dest, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.move(src_path, dest_path)
            else:
                dest_path = os.path.join(github_dest, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.move(src_path, dest_path)
                
                if ext in {'.py', '.md', '.json', '.js', '.ts', '.tsx', '.jsx', '.env', '.sh', '.txt'}:
                    scrub_secrets(dest_path)

    # Automatically generate the AI merge instructions in the GitHub folder
    create_merge_instructions(github_dest, project_name)

    shutil.rmtree(staging_dir)
    print("Splitting completed successfully! The original folder remains untouched.")
    print("Generated MERGE_INSTRUCTIONS_AI.md in the GitHub folder.")

if __name__ == "__main__":
    main()
