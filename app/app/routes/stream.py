import asyncio

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


async def complaint_streamer():

    logs = [
        "Complaint received...",
        "Complaint assigned...",
        "Issue under processing...",
        "Complaint resolved..."
    ]

    for log in logs:
        await asyncio.sleep(2)
        yield log + "\n"


@router.get("/stream/logs")
async def stream_logs():
    return StreamingResponse(
        complaint_streamer(),
        media_type="text/plain"
    )