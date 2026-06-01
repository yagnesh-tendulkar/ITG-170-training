from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from services.file_service import (
    file_service
)

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    """
    Upload File
    """

    result = await file_service.save_file(
        file
    )

    return {
        "success": True,
        "message": "File uploaded successfully",
        "data": result
    }


@router.get("/{filename}")
def get_file_info(
    filename: str
):
    """
    Get File Information
    """

    file_info = file_service.get_file_info(
        filename
    )

    return {
        "success": True,
        "data": file_info
    }


@router.delete("/{filename}")
def delete_file(
    filename: str
):
    """
    Delete File
    """

    return file_service.delete_file(
        filename
    )