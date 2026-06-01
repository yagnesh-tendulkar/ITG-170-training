from fastapi import APIRouter, HTTPException
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi.responses import FileResponse
import os

from sqlalchemy.orm import Session

from database.session import get_db

from dependencies.auth_dependency import (
    get_current_user
)

from models.user_model import User
from models.file_model import UploadedFile
from services.file_service import FileService

router = APIRouter(
    prefix="/api/files",
    tags=["Files"]
)


@router.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        current_user: User = Depends(
            get_current_user
        ),
        db: Session = Depends(get_db)
):

    upload_dir = "uploads"

    os.makedirs(
        upload_dir,
        exist_ok=True
    )

    file_path = (
        f"{upload_dir}/{file.filename}"
    )

    with open(
            file_path,
            "wb"
    ) as buffer:

        content = await file.read()

        FileService.validate_file(
            file.filename,
            content
        )

        buffer.write(content)

    uploaded_file = UploadedFile(
        file_name=file.filename,
        file_path=file_path,
        user_id=current_user.id
    )

    db.add(uploaded_file)

    db.commit()

    return {
        "message":
            "File Uploaded Successfully"
    }


@router.get("/{file_id}")
def download_file(
        file_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    file = (
        db.query(UploadedFile)
        .filter(
            UploadedFile.id == file_id,
            UploadedFile.user_id ==
            current_user.id
        )
        .first()
    )

    if not file:

        raise HTTPException(
            status_code=404,
            detail="File Not Found"
        )

    return FileResponse(
        path=file.file_path,
        filename=file.file_name
    )