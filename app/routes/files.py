from fastapi import APIRouter
from fastapi import File
from fastapi import UploadFile

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):
    return {
        "filename": file.filename
    }