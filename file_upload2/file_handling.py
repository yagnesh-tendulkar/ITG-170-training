from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse, FileResponse
from docx import Document
from PIL import Image
import pdfplumber
import pytesseract
import asyncio
import os

app = FastAPI()
UPLOAD_DIR = "uploads"
OUTPUT_DIR = "outputs"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
def read_txt(path):

    with open(path, "r", encoding="utf-8") as file:

        for line in file:
            yield line.strip()
def read_docx(path):

    doc = Document(path)

    for para in doc.paragraphs:

        if para.text.strip():
            yield para.text
def read_pdf(path):

    with pdfplumber.open(path) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:

                lines = text.split("\n")

                for line in lines:

                    if line.strip():
                        yield line
def read_image(path):

    image = Image.open(path)

    text = pytesseract.image_to_string(image)

    lines = text.split("\n")

    for line in lines:

        if line.strip():
            yield line
async def stream_data(lines):

    output_text = ""

    for line in lines:

        clean_line = line.strip()

        if clean_line:

            output_text += clean_line + "\n"

            yield clean_line + "\n"

            await asyncio.sleep(0.3)

    with open("outputs/output.txt", "w", encoding="utf-8") as file:

        file.write(output_text)
@app.post("/process-file")
async def process_file(file: UploadFile = File(...)):

    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as f:

        content = await file.read()

        f.write(content)

    extension = file.filename.split(".")[-1].lower()
    if extension == "txt":

        lines = read_txt(file_path)

    elif extension == "docx":

        lines = read_docx(file_path)

    elif extension == "pdf":

        lines = read_pdf(file_path)

    elif extension in ["png", "jpg", "jpeg"]:

        lines = read_image(file_path)

    else:

        return {
            "error": "Unsupported file type"
        }

    # Stream response line by line
    return StreamingResponse(
        stream_data(lines),
        media_type="text/plain"
    )
@app.get("/download")
async def download_file():

    return FileResponse(
        path="outputs/output.txt",
        filename="output.txt",
        media_type="text/plain"
    )
@app.get("/")
async def home():

    return {
        "message": "Real Time File Processing API Running"
    }