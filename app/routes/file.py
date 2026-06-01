from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)

from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

import shutil
import os

from app.core.database import get_db

from app.core.dependencies import (
    get_current_user
)

from app.utils.file_utils import (
    generate_unique_filename
)

from app.services.file_service import (
    save_file_record,
    get_user_files,
    get_file_by_id,
    delete_file_record
)

from app.utils.responce import (
    success_response
)

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)


@router.post("/upload")
def upload_file(
        uploaded_file: UploadFile = File(...),
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    unique_name = generate_unique_filename(
        uploaded_file.filename
    )

    file_path = os.path.join(
        "uploads",
        unique_name
    )

    with open(
            file_path,
            "wb"
    ) as buffer:

        shutil.copyfileobj(
            uploaded_file.file,
            buffer
        )

    file_record = save_file_record(
        db,
        uploaded_file.filename,
        file_path,
        current_user.id
    )

    return success_response(
        "File Uploaded Successfully",
        file_record
    )


@router.get("/")
def get_files(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    files = get_user_files(
        db,
        current_user.id
    )

    return success_response(
        "Files Retrieved Successfully",
        files
    )


@router.get("/{file_id}")
def get_file(
        file_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    file_record = get_file_by_id(
        db,
        file_id,
        current_user.id
    )

    return success_response(
        "File Retrieved Successfully",
        file_record
    )


@router.get("/download/{file_id}")
def download_file(
        file_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    file_record = get_file_by_id(
        db,
        file_id,
        current_user.id
    )

    return FileResponse(
        path=file_record.filepath,
        filename=file_record.filename
    )


@router.delete("/{file_id}")
def delete_file(
        file_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    delete_file_record(
        db,
        file_id,
        current_user.id
    )

    return success_response(
        "File Deleted Successfully"
    )