from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
import fitz

app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "PDF Extraction API Running"
    }
@app.post("/extract-pdf")
async def extract_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {
            "Error": "Only PDF files are allowed"
        }
    #read
    pdf_bytes = await file.read()

    #open
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    extracted_text = ""

    #extract
    for page in pdf_document:
        extracted_text += page.get_text()
    pdf_document.close()
    return {
        "filename": file.filename,
        "extracted_text": extracted_text
    }


