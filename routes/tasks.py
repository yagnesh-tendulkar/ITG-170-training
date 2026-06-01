from typing import Optional

from fastapi import APIRouter, UploadFile, File, Depends, Query
from fastapi.responses import StreamingResponse

from schemas.task_schema import ChatRequest, TaskCreate, TaskUpdate
from security.jwt_handler import verify_token
from services.stream_service import (
    extract_text_from_file,
    generate_chat_response,
    stream_file_service,
    upload_file_service,
)
from services.task_service import create_task, delete_task, get_task, get_tasks, update_task

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def _require_task(task_id: int, user_id: int):
    return get_task(task_id, user_id)


@router.post("/")
def add_task(task: TaskCreate, current_user: dict = Depends(verify_token)):
    return create_task(task, current_user["user_id"])


@router.get("/")
def all_tasks(
    current_user: dict = Depends(verify_token),
    priority: Optional[str] = Query(
        None,
        description="Filter tasks by priority",
        regex="^(low|medium|high)$",
    ),
):
    return get_tasks(current_user["user_id"], priority)


@router.get("/{task_id}")
def get_one_task(task_id: int, current_user: dict = Depends(verify_token)):
    return get_task(task_id, current_user["user_id"])


@router.patch("/{task_id}")
def edit_task(task_id: int, task: TaskUpdate, current_user: dict = Depends(verify_token)):
    return update_task(task_id, current_user["user_id"], task)


@router.delete("/{task_id}")
def remove_task(task_id: int, current_user: dict = Depends(verify_token)):
    return delete_task(task_id, current_user["user_id"])


@router.post("/{task_id}/upload")
async def upload_file(task_id: int, file: UploadFile = File(...), current_user: dict = Depends(verify_token)):
    _require_task(task_id, current_user["user_id"])
    return await upload_file_service(task_id, current_user["user_id"], file)


@router.get("/{task_id}/extract")
def extract_file(task_id: int, current_user: dict = Depends(verify_token)):
    _require_task(task_id, current_user["user_id"])
    return extract_text_from_file(task_id, current_user["user_id"])


@router.post("/{task_id}/chat")
def chat_task(task_id: int, request: ChatRequest, current_user: dict = Depends(verify_token)):
    _require_task(task_id, current_user["user_id"])
    result = extract_text_from_file(task_id, current_user["user_id"])
    return {
        "task_id": task_id,
        "prompt": request.prompt,
        "response": generate_chat_response(result["extracted_text"], request.prompt, request.max_tokens),
    }


@router.get("/{task_id}/stream")
def stream_file(task_id: int, current_user: dict = Depends(verify_token)):
    _require_task(task_id, current_user["user_id"])
    return StreamingResponse(
        stream_file_service(task_id, current_user["user_id"]), media_type="application/octet-stream"
    )
