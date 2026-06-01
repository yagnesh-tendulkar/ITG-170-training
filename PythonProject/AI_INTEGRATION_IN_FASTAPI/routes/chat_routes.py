from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from schemas.chat_schema import ChatRequest
from services.gemini_service import stream_gemini_response


router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):

    generator = stream_gemini_response(request.prompt)

    return StreamingResponse(
        generator,
        media_type="text/plain"
    )