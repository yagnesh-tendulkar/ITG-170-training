import importlib
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from services.pdf_service import stream_pdf_text

_messages = importlib.import_module("global.messages")
_status_code = importlib.import_module("global.status_code")
Message = _messages.Message
StatusCode = _status_code.StatusCode

router = APIRouter()

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=StatusCode.BAD_REQUEST,
                detail=Message.PDF_ONLY
            )
        return StreamingResponse(
            stream_pdf_text(file),
            media_type="text/plain",
            status_code=StatusCode.SUCCESS
        )
    except HTTPException as e:
        raise e
    except Exception as e:

        print(e)

        raise HTTPException(
            status_code=StatusCode.INTERNAL_SERVER_ERROR,
            detail=str(e)
        )