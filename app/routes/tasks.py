import os
import asyncio
from typing import List, Optional
from fastapi import (
    APIRouter, Depends, status, UploadFile, File,
    BackgroundTasks, Query
)
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc

from database import get_db
from models import Task, User
from schemas import TaskCreate, TaskUpdate, TaskResponse
from services.auth import get_current_user
from services.notifications import send_task_created_email, send_task_completed_email
from exceptions import TaskNotFoundException
from utils.file_utils import validate_file

router = APIRouter(prefix="/tasks", tags=["Tasks"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ──────────────────────────── CREATE ────────────────────────────

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = Task(
        title=payload.title,
        description=payload.description,
        priority=payload.priority.value,
        tags=payload.tags,
        due_date=payload.due_date,
        owner_id=current_user.id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)

    background_tasks.add_task(send_task_created_email, current_user.email, task.title)
    return task


# ──────────────────────────── LIST (filter + paginate) ────────────────────────────

@router.get("", response_model=List[TaskResponse])
def list_tasks(
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    sort_by: str = Query("created_at"),
    order: str = Query("desc"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    query = db.query(Task).filter(Task.owner_id == current_user.id)

    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))

    sort_col = getattr(Task, sort_by, Task.created_at)
    query = query.order_by(desc(sort_col) if order == "desc" else asc(sort_col))

    return query.offset((page - 1) * limit).limit(limit).all()


# ──────────────────────────── GET ONE ────────────────────────────

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task:
        raise TaskNotFoundException(task_id)
    return task


# ──────────────────────────── PATCH ────────────────────────────

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task:
        raise TaskNotFoundException(task_id)

    update_data = payload.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        if hasattr(value, "value"):     # Enum → string
            value = value.value
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    if task.status == "completed":
        background_tasks.add_task(send_task_completed_email, current_user.email, task.title)

    return task


# ──────────────────────────── DELETE ────────────────────────────

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task:
        raise TaskNotFoundException(task_id)
    db.delete(task)
    db.commit()


# ──────────────────────────── FILE UPLOAD ────────────────────────────

@router.post("/{task_id}/upload", response_model=TaskResponse)
async def upload_file(
    task_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task:
        raise TaskNotFoundException(task_id)

    # Duplicate check
    if task.file_path:
        from fastapi import HTTPException
        raise HTTPException(status_code=409, detail="A file is already attached to this task")

    content = await validate_file(file)

    file_location = os.path.join(UPLOAD_DIR, f"task_{task_id}_{file.filename}")
    with open(file_location, "wb") as f:
        f.write(content)

    task.file_path = file_location
    db.commit()
    db.refresh(task)
    return task


# ──────────────────────────── STREAMING ────────────────────────────

@router.get("/{task_id}/stream")
async def stream_task_processing(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task:
        raise TaskNotFoundException(task_id)

    async def event_generator():
        steps = [
            f"Processing started for task: '{task.title}'...\n",
            "Reading task metadata...\n",
            "Validating attached file...\n",
            "Generating processing report...\n",
            "Finalizing...\n",
            "Task processing complete ✅\n",
        ]
        for step in steps:
            yield step
            await asyncio.sleep(0.5)

    return StreamingResponse(event_generator(), media_type="text/plain")
