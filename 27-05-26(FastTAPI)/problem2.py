import asyncio

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse

from extract import extract_pdf_text, extract_docx_text

app = FastAPI()


# STREAMING GENERATOR
async def text_streamer(text: str):
    words = text.split()

    for word in words:
        yield word + " "

        await asyncio.sleep(0.1)


# STREAM RESPONSE
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename.lower()

    # PDF Extraction
    if filename.endswith(".pdf"):

        extracted_text = extract_pdf_text(file.file)

    # DOCX Extraction
    elif filename.endswith(".docx"):

        extracted_text = extract_docx_text(file.file)
    else:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and DOCX files are allowed"
        )

    # Streaming Response
    return StreamingResponse(
        text_streamer(extracted_text),
        media_type="text/plain"
    )