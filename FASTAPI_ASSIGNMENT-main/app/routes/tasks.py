from typing import Optional

from fastapi import APIRouter, Depends, Query


from exceptions import NotFoundException
from schemas.task_schema import TaskCreate, TaskUpdate
from security.jwt_handler import verify_token
from services.task_service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


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
    task = get_task(task_id, current_user["user_id"])
    if not task:
        raise NotFoundException("Task not found")
    return task


@router.patch("/{task_id}")
def edit_task(task_id: int, task: TaskUpdate, current_user: dict = Depends(verify_token)):
    existing_task = get_task(task_id, current_user["user_id"])
    if not existing_task:
        raise NotFoundException("Task not found")
    return update_task(task_id, current_user["user_id"], task)


@router.delete("/{task_id}")
def remove_task(task_id: int, current_user: dict = Depends(verify_token)):
    existing_task = get_task(task_id, current_user["user_id"])
    if not existing_task:
        raise NotFoundException("Task not found")
    return delete_task(task_id, current_user["user_id"])

