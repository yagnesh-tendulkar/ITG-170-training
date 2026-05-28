from PyPDF2 import PdfReader
import io
import asyncio

async def stream_pdf_text(file):
    contents = await file.read()
    pdf = PdfReader(io.BytesIO(contents))
    for page_no, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text is None:
            text = "No text found on this page"

        clean_text = " ".join(text.split())
        yield f"\n--- Page {page_no + 1} ---\n"
        yield clean_text + "\n"
        await asyncio.sleep(1)