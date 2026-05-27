from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pypdf import PdfReader
import asyncio

app = FastAPI()


async def read_pdf():
    reader = PdfReader("sample.pdf")

    for page in reader.pages:
        text = page.extract_text()

        if text:
            lines = text.split("\n")
            #to read all the lines and generate line by line
            for line in lines:
                yield line + "\n"
                await asyncio.sleep(1)

@app.get("/stream-pdf")
async def stream_pdf():

    return StreamingResponse(
        read_pdf(),
        media_type="text/plain"
    )