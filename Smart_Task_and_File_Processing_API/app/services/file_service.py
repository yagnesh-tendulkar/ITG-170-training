import os
import shutil
from uuid import uuid4

from exceptions.custom_exceptions import (
    FileValidationException
)


class FileService:

    ALLOWED_EXTENSIONS = {
        ".pdf",
        ".txt",
        ".csv",
        ".docx"
    }

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    UPLOAD_DIRECTORY = "uploads"

    def __init__(self):

        os.makedirs(
            self.UPLOAD_DIRECTORY,
            exist_ok=True
        )

    def validate_file(
        self,
        file
    ):
        """
        Validate uploaded file.
        """

        extension = os.path.splitext(
            file.filename
        )[1].lower()

        if extension not in self.ALLOWED_EXTENSIONS:

            raise FileValidationException(
                "Unsupported file type"
            )

        return True

    async def save_file(
        self,
        file
    ):
        """
        Save uploaded file.
        """

        self.validate_file(file)

        unique_filename = (
            f"{uuid4()}_{file.filename}"
        )

        file_path = os.path.join(
            self.UPLOAD_DIRECTORY,
            unique_filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        return {
            "filename": unique_filename,
            "path": file_path
        }

    def get_file_info(
        self,
        filename: str
    ):
        """
        Return file information.
        """

        file_path = os.path.join(
            self.UPLOAD_DIRECTORY,
            filename
        )

        if not os.path.exists(file_path):

            raise FileValidationException(
                "File not found"
            )

        return {
            "filename": filename,
            "size": os.path.getsize(
                file_path
            ),
            "path": file_path
        }

    def delete_file(
        self,
        filename: str
    ):
        """
        Delete file.
        """

        file_path = os.path.join(
            self.UPLOAD_DIRECTORY,
            filename
        )

        if not os.path.exists(file_path):

            raise FileValidationException(
                "File not found"
            )

        os.remove(file_path)

        return {
            "message": "File deleted successfully"
        }


file_service = FileService()