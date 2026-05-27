from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import time

app = FastAPI()


@app.post("/upload")
def save_document(file: UploadFile = File(...)):
    saved_file = f"data_{file.filename}"

    with open(saved_file, "wb") as f:
        file_data = file.file.read()
        f.write(file_data)
    return {
        "message": "Upload completed",
        "path": saved_file
    }


def read_lines(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        for text in f:
            time.sleep(1)
            yield text


@app.get("/read-file")
def read_file(file_name: str):
    return StreamingResponse(
        read_lines(file_name),
        media_type="text/plain"
    )