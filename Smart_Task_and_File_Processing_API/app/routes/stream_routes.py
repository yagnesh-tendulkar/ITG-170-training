from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from services.stream_service import (
    stream_service
)

router = APIRouter(
    prefix="/stream",
    tags=["Streaming"]
)


@router.get("/task/{task_id}")
async def stream_task(
    task_id: int
):
    """
    Stream task processing logs.
    """

    return StreamingResponse(
        stream_service.process_task_stream(
            task_id
        ),
        media_type="text/plain"
    )


@router.get("/file/{filename}")
async def stream_file(
    filename: str
):
    """
    Stream file processing logs.
    """

    return StreamingResponse(
        stream_service.process_file_stream(
            filename
        ),
        media_type="text/plain"
    )


@router.get("/health")
async def stream_health():
    """
    Stream health status.
    """

    return StreamingResponse(
        stream_service.health_check_stream(),
        media_type="text/plain"
    )