from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_service import save_file

router = APIRouter()

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):

    # MIME validation
    if file.content_type not in [
        "image/png",
        "image/jpeg",
        "application/pdf"
    ]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    path = save_file(file)

    return {
        "message": "File uploaded successfully",
        "path": path
    }