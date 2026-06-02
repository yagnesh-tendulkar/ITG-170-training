from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        content = file.file.read()
        buffer.write(content)

    return {
        "message": "File uploaded successfully",
        "file_path": file_path
    }


def stream_file(file_path: str):

    with open(file_path, "r", encoding="utf-8") as f:

        for line in f:
            time.sleep(1)
            yield line


@app.get("/stream-file")
def stream_file_api(path: str):

    return StreamingResponse(
        stream_file(path),
        media_type="text/plain"
    )