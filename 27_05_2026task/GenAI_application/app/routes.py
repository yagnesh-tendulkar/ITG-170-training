from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models import ChatRequest
from app.chatbot import chatbot_stream
router = APIRouter()
@router.get("/health")
async def health():
    return {
        "status": "success",
        "message": "Groq Chatbot Running"
    }
@router.post("/chat")
async def chat(request: ChatRequest):
    return StreamingResponse(
        chatbot_stream(
            request.message
        ),
        media_type="text/plain"
    )