from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
import pandas as pd
import io
import asyncio
import fitz
import mysql.connector
app = FastAPI()
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="file_streaming_db"
)
cursor = db.cursor()
def save_file_metadata(filename, file_type):
    query = """
    INSERT INTO uploaded_files(filename, file_type)
    VALUES(%s, %s)
    """
    values = (filename, file_type)
    cursor.execute(query, values)
    db.commit()
    return cursor.lastrowid
def save_extracted_data(
        file_id,
        page_number,
        line_number,
        extracted_text
):
    query = """
    INSERT INTO extracted_data(
        file_id,
        page_number,
        line_number,
        extracted_text
    )
    VALUES(%s, %s, %s, %s)
    """
    values = (
        file_id,
        page_number,
        line_number,
        extracted_text
    )
    cursor.execute(query, values)
    db.commit()
async def extract_data(
        file: UploadFile,
        file_id: int
):
    try:
        filename = file.filename.lower()
        if filename.endswith(".txt"):
            content = await file.read()
            text = content.decode("utf-8")
            lines = text.splitlines()
            for line_no, line in enumerate(lines, start=1):
                await asyncio.sleep(0.5)
                save_extracted_data(
                    file_id,
                    1,
                    line_no,
                    line
                )
                yield f"{line_no}. {line}\n"
        elif filename.endswith(".csv"):
            content = await file.read()
            df = pd.read_csv(io.BytesIO(content))
            for index, row in df.iterrows():
                await asyncio.sleep(0.5)
                row_data = str(row.to_dict())
                save_extracted_data(
                    file_id,
                    1,
                    index + 1,
                    row_data
                )
                yield f"Row {index + 1}: {row_data}\n"
        elif filename.endswith(".xlsx"):
            content = await file.read()
            df = pd.read_excel(io.BytesIO(content))
            for index, row in df.iterrows():
                await asyncio.sleep(0.5)
                row_data = str(row.to_dict())
                save_extracted_data(
                    file_id,
                    1,
                    index + 1,
                    row_data
                )
                yield f"Row {index + 1}: {row_data}\n"
        elif filename.endswith(".pdf"):
            content = await file.read()
            pdf_document = fitz.open(
                stream=content,
                filetype="pdf"
            )
            for page_number in range(len(pdf_document)):
                page = pdf_document[page_number]
                text = page.get_text()
                lines = text.splitlines()
                for line_no, line in enumerate(lines, start=1):
                    await asyncio.sleep(0.3)
                    save_extracted_data(
                        file_id,
                        page_number + 1,
                        line_no,
                        line
                    )
                    yield f"Page {page_number + 1}, Line {line_no}: {line}\n"
        else:
            yield "Unsupported file type\n"
    except Exception as e:
        yield f"Error: {str(e)}\n"
@app.post("/uploadfile")
async def uploadfile(
        file: UploadFile = File(...)
):
    if not file.filename:

        raise HTTPException(
            status_code=400,
            detail="File name is missing"
        )
    file_type = file.filename.split(".")[-1]
    file_id = save_file_metadata(
        file.filename,
        file_type
    )
    return StreamingResponse(
        extract_data(file, file_id),
        media_type="text/plain"
    )


