from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    computed_field
)


class FileUploadResponse(BaseModel):

    filename: str

    original_filename: str

    file_size: int

    content_type: str

    upload_time: datetime = Field(
        default_factory=datetime.utcnow
    )

    file_path: str

    @computed_field
    @property
    def file_size_kb(self) -> float:

        return round(
            self.file_size / 1024,
            2
        )


class FileInfoResponse(BaseModel):

    filename: str

    file_size: int

    content_type: Optional[str] = None

    upload_time: datetime

    file_path: str

    @computed_field
    @property
    def file_size_mb(self) -> float:

        return round(
            self.file_size / (1024 * 1024),
            2
        )


class FileDeleteResponse(BaseModel):

    message: str

    filename: str


class FileFilter(BaseModel):

    page: int = Field(
        default=1,
        ge=1
    )

    limit: int = Field(
        default=10,
        ge=1,
        le=100
    )

    filename: Optional[str] = None

    content_type: Optional[str] = None


class FileValidationRequest(BaseModel):

    filename: str

    @field_validator("filename")
    @classmethod
    def validate_filename(
        cls,
        value: str
    ):

        allowed_extensions = [
            ".pdf",
            ".txt",
            ".csv",
            ".docx"
        ]

        if not any(
            value.lower().endswith(ext)
            for ext in allowed_extensions
        ):

            raise ValueError(
                "Only .pdf, .txt, .csv and .docx files are allowed"
            )

        return value