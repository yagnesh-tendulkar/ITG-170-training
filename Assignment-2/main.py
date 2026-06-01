from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PyPDF2 import PdfReader
import asyncio
import docx

app = FastAPI()

async def stream_text(text):
    for word in text.split():
        yield word + " "

        await asyncio.sleep(0)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = ""

    if file.filename.endswith(".txt"):
        data = await file.read()

        content = data.decode("utf-8")


    elif file.filename.endswith(".pdf"):
        with open("temp.pdf", "wb") as f:
            f.write(await file.read())

        pdf = PdfReader("temp.pdf")

        for page in pdf.pages:
            content += page.extract_text()


    elif file.filename.endswith(".docx"):
        with open("temp.docx", "wb") as f:
            f.write(await file.read())

        document = docx.Document("temp.docx")

        for para in document.paragraphs:
            content += para.text + " "
    else:
        content = "Unsupported file"

    return StreamingResponse(
        stream_text(content),
        media_type="text/plain"
    )