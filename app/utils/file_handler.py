"""
Secure file handling utilities for uploads in a FastAPI application.

Provides helper functions to save uploaded files with unique filenames,
validate file types, safely delete files, and create upload folders.

Security notes:
- The original filename is not used except to extract a file extension.
- Filenames are replaced with UUIDs to prevent collisions and path traversal.
- Paths are resolved via `pathlib.Path.resolve()` to avoid relative path tricks.
"""
from __future__ import annotations

import logging
import os
import uuid
from pathlib import Path
from typing import List, Optional

from fastapi import UploadFile

logger = logging.getLogger("app.file_handler")

CHUNK_SIZE_BYTES = 1024 * 1024  # 1MB


def create_upload_folder(folder_path: str) -> Path:
    """
    Create an upload folder if it does not exist.

    Args:
        folder_path: Directory path to create.

    Returns:
        Path: The resolved directory Path.

    Raises:
        OSError: If the directory cannot be created.
    """
    path = Path(folder_path)
    resolved = path.resolve()
    try:
        resolved.mkdir(parents=True, exist_ok=True)
        return resolved
    except OSError as e:
        logger.exception("Failed to create upload folder: %s", folder_path)
        raise


def get_file_extension(filename: str) -> str:
    """
    Safely extract the file extension from a filename.

    Returns the extension in lower-case without the leading dot. If no
    extension exists, returns an empty string.

    Args:
        filename: The original filename (may include path components).

    Returns:
        str: Extension without dot (e.g., 'pdf', 'jpg') or '' if none.
    """
    try:
        return Path(filename).suffix.lower().lstrip(".")
    except Exception:
        logger.exception("Failed to extract extension from filename: %s", filename)
        return ""


def validate_file_type(filename: str, allowed_types: List[str]) -> bool:
    """
    Validate the file extension against a whitelist of allowed types.

    Args:
        filename: The filename or original UploadFile.filename.
        allowed_types: List of allowed extensions (e.g. ['pdf','png','jpg']).

    Returns:
        bool: True if allowed, False otherwise.
    """
    ext = get_file_extension(filename)
    allowed_normalized = {t.lower().lstrip(".") for t in allowed_types}
    return ext in allowed_normalized


async def save_upload_file(upload_file: UploadFile, destination_folder: str) -> str:
    """
    Save an uploaded file to `destination_folder` with a UUID filename.

    The original filename is only inspected for a file extension; a new
    filename is generated using UUIDv4 to avoid collisions and to prevent
    path traversal attacks.

    Args:
        upload_file: FastAPI `UploadFile` instance from the request.
        destination_folder: Target directory to store the uploaded file.

    Returns:
        str: Absolute path to the saved file as a string.

    Raises:
        ValueError: If upload_file is invalid or write fails.
    """
    if not upload_file or not hasattr(upload_file, "filename"):
        raise ValueError("Invalid upload file provided")

    # Ensure destination folder exists and is resolved
    dest_dir = create_upload_folder(destination_folder)

    # Preserve only the extension from the original filename
    ext = get_file_extension(upload_file.filename)

    # Generate a unique filename using UUID4
    unique_name = f"{uuid.uuid4()}" + (f".{ext}" if ext else "")

    # Final safe path (resolve to canonical absolute path)
    final_path = (dest_dir / unique_name).resolve()

    # Write file in chunks to avoid memory pressure on large files
    try:
        with final_path.open("wb") as buffer:
            while True:
                chunk = await upload_file.read(CHUNK_SIZE_BYTES)
                if not chunk:
                    break
                buffer.write(chunk)
        # Reset UploadFile file pointer for any further usage (best-effort)
        try:
            await upload_file.seek(0)
        except Exception:
            # Not critical — many callers won't reuse the UploadFile
            pass
        return str(final_path)
    except Exception:
        logger.exception("Failed to save uploaded file to %s", final_path)
        # Attempt remove partial file if present
        try:
            if final_path.exists():
                final_path.unlink(missing_ok=True)
        except Exception:
            logger.exception("Failed to clean up partial file: %s", final_path)
        raise


def delete_file(file_path: str) -> bool:
    """
    Safely delete a file if it exists.

    Args:
        file_path: Path to the file to delete.

    Returns:
        bool: True if file was deleted, False if file did not exist.

    Notes:
        - Uses Path.resolve() to get canonical path. Does not delete
          directories. Any exception is logged and results in False.
    """
    try:
        path = Path(file_path).resolve()
        if not path.exists():
            return False
        if not path.is_file():
            logger.warning("delete_file called on non-file path: %s", file_path)
            return False
        path.unlink()
        return True
    except Exception:
        logger.exception("Failed to delete file: %s", file_path)
        return False


# Optional convenience wrapper for allowed types default
def is_allowed_file_type(filename: str, allowed_types: Optional[List[str]] = None) -> bool:
    """
    Convenience wrapper around `validate_file_type` with sane defaults.

    Args:
        filename: Original filename to check.
        allowed_types: Optional list of allowed extensions. Defaults to a
                       common list used in this project.

    Returns:
        bool: True if extension is allowed.
    """
    if allowed_types is None:
        allowed_types = ["pdf", "docx", "png", "jpg", "jpeg", "csv"]
    return validate_file_type(filename, allowed_types)


if __name__ == "__main__":
    # Quick local sanity check (not a test harness)
    folder = "./uploads_test"
    p = create_upload_folder(folder)
    print("Created folder:", p)
