from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.dependencies.auth import get_current_user

from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

from app.services.task_service import (
    create_task,
    get_task,
    get_tasks,
    update_task,
    delete_task
)

router = APIRouter(
    prefix="/api/v1/tasks",
    tags=["Tasks"]
)
@router.post("/", response_model=TaskResponse)
def create(
    request: TaskCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    return create_task(db, request, user.id)
@router.get("/", response_model=list[TaskResponse])
def list_tasks(
    skip: int = 0,
    limit: int = 10,
    status: str = None,
    priority: str = None,
    search: str = None,
    sort_by: str = "created_at",
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    return get_tasks(
        db,
        user.id,
        skip,
        limit,
        status,
        priority,
        search,
        sort_by
    )
@router.get("/{task_id}", response_model=TaskResponse)
def get_one(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    task = get_task(db, task_id, user.id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task
@router.put("/{task_id}", response_model=TaskResponse)
def update(
    task_id: int,
    request: TaskUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    task = get_task(db, task_id, user.id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return update_task(db, task, request)
@router.delete("/{task_id}")
def delete(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    task = get_task(db, task_id, user.id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    delete_task(db, task)

    return {"message": "Task deleted successfully"}
@router.patch("/{task_id}/complete")
def mark_complete(
    task_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):

    task = get_task(db, task_id, user.id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = "COMPLETED"

    db.commit()
    db.refresh(task)

    return task