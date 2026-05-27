from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
import PyPDF2
import io
import asyncio

app = FastAPI()

async def extract_text(file):

    pdf = PyPDF2.PdfReader(file)

    for page in pdf.pages:

        text = page.extract_text()

        lines = text.split("\n")

        for line in lines:
            yield line + "\n"
            await asyncio.sleep(0.5)   # streaming delay

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):

    contents = await file.read()

    pdf_file = io.BytesIO(contents)

    return StreamingResponse(
        extract_text(pdf_file),
        media_type="text/plain"
    )
