from PyPDF2 import PdfReader
from docx import Document
def extract_pdf_text(file):
    pdf = PdfReader(file)
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:   # ✅ handle None
            text += page_text + "\n"

    return text
def extract_docx_text(file):
    doc = Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text