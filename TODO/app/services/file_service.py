"""File MIME validation and storage logic (placeholder)."""
import shutil
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

def save_file(file, filename: str):
    dest = UPLOAD_DIR / filename
    with dest.open("wb") as f:
        shutil.copyfileobj(file.file, f)
    return str(dest)
