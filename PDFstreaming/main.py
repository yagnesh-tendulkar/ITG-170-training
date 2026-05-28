from dns import name
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from pypdf import PdfReader
from docx import Document
import asyncio
import io

app = FastAPI(name="PDF-Streaming API")


def extract_pdf_text(file_bytes):
    pdf = PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"

    return text


def extract_docx_text(file_bytes):
    doc = Document(io.BytesIO(file_bytes))
    text = "\n".join(
        para.text for para in doc.paragraphs
    )

    return text


async def stream_text(text):
    words = text.split()

    for word in words:
        yield f"data: {word}\n\n"
        await asyncio.sleep(0.05)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = extract_pdf_text(content)

    elif filename.endswith(".docx"):
        text = extract_docx_text(content)

    else:
        return {
            "error": "Only PDF and DOCX supported"
        }

    return StreamingResponse(
        stream_text(text),
        media_type="text/event-stream"
    )
