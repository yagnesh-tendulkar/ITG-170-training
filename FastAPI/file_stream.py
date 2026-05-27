from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
import pdfplumber
import docx
import io
import time

app = FastAPI()
@app.post("/stream-file")
async def stream_file(file: UploadFile = File(...)):

    file_bytes = await file.read()
    name = file.filename.lower()

    def stream():

        if name.endswith(".pdf"):
            doc = pdfplumber.open(io.BytesIO(file_bytes))
            for page in doc.pages:
                text = page.extract_text()
                if text:
                    for line in text.split("\n"):
                        time.sleep(0.3)
                        yield f"{line}\n"
            doc.close()

        elif name.endswith(".docx"):
            doc = docx.Document(io.BytesIO(file_bytes))
            for para in doc.paragraphs:
                if para.text:
                    time.sleep(0.3)
                    yield f"{para.text}\n"
        else:
            yield "Unsupported file type\n"
    return StreamingResponse(stream(), media_type="text/plain")