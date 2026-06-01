import os

from fastapi import HTTPException


class FileService:

    ALLOWED_EXTENSIONS = [
        ".pdf",
        ".txt",
        ".csv",
        ".xlsx"
    ]

    MAX_FILE_SIZE = 5 * 1024 * 1024

    @staticmethod
    def validate_file(
            filename: str,
            content: bytes
    ):

        extension = os.path.splitext(
            filename
        )[1].lower()

        if extension not in FileService.ALLOWED_EXTENSIONS:

            raise HTTPException(
                status_code=400,
                detail="Unsupported file type"
            )

        if len(content) > FileService.MAX_FILE_SIZE:

            raise HTTPException(
                status_code=400,
                detail="File exceeds 5 MB limit"
            )