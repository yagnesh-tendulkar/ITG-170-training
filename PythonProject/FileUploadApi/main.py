import os
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from utils import extract_pdf_lines

app = FastAPI(title="PDF Upload + Streaming API")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# 📌 Upload PDF API
@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {
        "message": "PDF uploaded successfully",
        "filename": file.filename
    }


# 📌 Streaming API
@app.get("/stream-pdf/{filename}")
def stream_pdf(filename: str):
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    return StreamingResponse(
        extract_pdf_lines(file_path),
        media_type="text/plain"
    )