import time
from PyPDF2 import PdfReader

def extract_pdf_lines(file_path: str):
    """
    Extract text from PDF and yield line by line (streaming)
    """

    reader = PdfReader(file_path)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if not text:
            continue

        lines = text.split("\n")

        for line_number, line in enumerate(lines, start=1):
            time.sleep(0.3)  # simulate processing delay

            yield f"Page {page_number} | Line {line_number}: {line}\n"