import os
from uuid import uuid4

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Query
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import get_current_user

from app.models.file import File as FileModel
router = APIRouter(
    prefix="/api/v1/files",
    tags=["Files"]
)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
def upload_file(
    file: UploadFile = File(...),
    task_id: int = Query(None),
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    file_ext = file.filename.split(".")[-1]
    unique_name = f"{uuid4()}.{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, unique_name)

    content = file.file.read()
    size = len(content)

    # save to disk
    with open(file_path, "wb") as f:
        f.write(content)

    # save to DB
    db_file = FileModel(
        filename=file.filename,
        filepath=file_path,
        content_type=file.content_type,
        size=size,
        owner_id=user.id,
        task_id=task_id
    )

    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {
        "message": "File uploaded successfully",
        "file_id": db_file.id,
        "filename": db_file.filename
    }
@router.get("/")
def get_files(
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    files = db.query(FileModel).filter(
        FileModel.owner_id == user.id
    ).all()

    return files
@router.get("/{file_id}")
def get_file(
    file_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    file_obj = db.query(FileModel).filter(
        FileModel.id == file_id,
        FileModel.owner_id == user.id
    ).first()

    if not file_obj:
        raise HTTPException(status_code=404, detail="File not found")

    return file_obj
@router.get("/download/{file_id}")
def download_file(
    file_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    file_obj = db.query(FileModel).filter(
        FileModel.id == file_id,
        FileModel.owner_id == user.id
    ).first()

    if not file_obj:
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=file_obj.filepath,
        filename=file_obj.filename,
        media_type=file_obj.content_type
    )
@router.delete("/{file_id}")
def delete_file(
    file_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    file_obj = db.query(FileModel).filter(
        FileModel.id == file_id,
        FileModel.owner_id == user.id
    ).first()

    if not file_obj:
        raise HTTPException(status_code=404, detail="File not found")

    # delete from disk
    if os.path.exists(file_obj.filepath):
        os.remove(file_obj.filepath)

    # delete from DB
    db.delete(file_obj)
    db.commit()

    return {"message": "File deleted successfully"}
