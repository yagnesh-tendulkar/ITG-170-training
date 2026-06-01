from fastapi import UploadFile, HTTPException
from typing import List

ALLOWED_MIME_TYPES: List[str] = [
    "image/jpeg",
    "image/png",
    "application/pdf",
    "text/plain",
    "text/csv",
]

MAX_FILE_SIZE_MB = 5
MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


async def validate_file(file: UploadFile) -> bytes:
    if file.content_type not in ALLOWED_MIME_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"File type '{file.content_type}' is not allowed. Allowed: {ALLOWED_MIME_TYPES}",
        )

    content = await file.read()

    if len(content) > MAX_FILE_SIZE_BYTES:
        raise HTTPException(
            status_code=400,
            detail=f"File size exceeds the {MAX_FILE_SIZE_MB}MB limit",
        )

    return content
