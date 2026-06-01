from fastapi import APIRouter, BackgroundTasks, Depends

from app.dependencies.auth import get_current_user
from app.services.background_service import (
    process_file,
    process_task,
    send_email
)

router = APIRouter(
    prefix="/api/v1/background",
    tags=["Background Tasks"]
)
@router.post("/file/{file_id}")
def run_file_processing(
    file_id: int,
    background_tasks: BackgroundTasks,
    user=Depends(get_current_user)
):

    background_tasks.add_task(process_file, file_id)

    return {
        "message": "File processing started in background",
        "file_id": file_id
    }
@router.post("/task/{task_id}")
def run_task_processing(
    task_id: int,
    background_tasks: BackgroundTasks,
    user=Depends(get_current_user)
):

    background_tasks.add_task(process_task, task_id)

    return {
        "message": "Task processing started",
        "task_id": task_id
    }
@router.post("/email")
def run_email(
    email: str,
    background_tasks: BackgroundTasks,
    user=Depends(get_current_user)
):

    background_tasks.add_task(send_email, email)

    return {
        "message": "Email sending started",
        "email": email
    }
