from typing import Optional

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query
)

from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from database.session import get_db

from dependencies.auth_dependency import (
    get_current_user
)

from models.task_model import Task
from models.user_model import User
from services.task_service import TaskService
from schemas.task_schema import (
    TaskCreate,
    TaskUpdate
)

router = APIRouter(
    prefix="/api",
    tags=["Tasks"]
)


# ==========================================
# CREATE TASK
# ==========================================
@router.post("/tasks")
def create_task(
        request: TaskCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):
    return TaskService.create_task(
        request.title,
        request.description,
        current_user,
        db
    )


# ==========================================
# GET ALL TASKS
# PAGINATION + FILTERING
# ==========================================
@router.get("/tasks")
def get_my_tasks(
        page: int = Query(
            default=1,
            ge=1
        ),
        size: int = Query(
            default=10,
            ge=1,
            le=100
        ),
        status: Optional[str] = None,
        title: Optional[str] = None,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):
    query = (
        db.query(Task)
        .filter(
            Task.user_id == current_user.id,
            Task.is_deleted == False
        )
    )

    if status:
        query = query.filter(
            Task.status == status
        )

    if title:
        query = query.filter(
            Task.title.ilike(
                f"%{title}%"
            )
        )

    total_records = query.count()

    offset = (
        (page - 1) * size
    )

    tasks = (
        query
        .offset(offset)
        .limit(size)
        .all()
    )

    return {
        "page": page,
        "size": size,
        "total_records": total_records,
        "tasks": tasks
    }


# ==========================================
# EXPORT TASKS CSV
# KEEP ABOVE /{task_id}
# ==========================================
@router.get("/tasks/export/csv")
def export_tasks(
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    def generate():

        yield (
            "ID,TITLE,DESCRIPTION,STATUS\n"
        )

        tasks = (
            db.query(Task)
            .filter(
                Task.user_id == current_user.id,
                Task.is_deleted == False
            )
            .all()
        )

        for task in tasks:

            yield (
                f"{task.id},"
                f"{task.title},"
                f"{task.description},"
                f"{task.status}\n"
            )

    return StreamingResponse(
        generate(),
        media_type="text/csv",
        headers={
            "Content-Disposition":
                "attachment; filename=tasks.csv"
        }
    )


# ==========================================
# GET TASK BY ID
# ==========================================
@router.get("/tasks/{task_id}")
def get_task_by_id(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id,
            Task.is_deleted == False
        )
        .first()
    )

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    return task


# ==========================================
# UPDATE TASK
# ==========================================
@router.put("/tasks/{task_id}")
def update_task(
        task_id: int,
        request: TaskUpdate,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id,
            Task.is_deleted == False
        )
        .first()
    )

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    task.title = request.title
    task.description = request.description
    task.status = request.status

    db.commit()

    return {
        "message":
            "Task Updated Successfully"
    }


# ==========================================
# DELETE TASK
# ==========================================
@router.delete("/tasks/{task_id}")
def delete_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    task.is_deleted = True

    db.commit()

    return {
        "message":
            "Task Deleted Successfully"
    }


@router.put("/tasks/{task_id}/restore")
def restore_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.user_id == current_user.id
        )
        .first()
    )

    if not task:

        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    task.is_deleted = False

    db.commit()

    return {
        "message": "Task Restored Successfully"
    }


@router.get("/tasks/trash")
def get_deleted_tasks(
        db: Session = Depends(get_db),
        current_user: User = Depends(
            get_current_user
        )
):

    tasks = (
        db.query(Task)
        .filter(
            Task.user_id == current_user.id,
            Task.is_deleted == True
        )
        .all()
    )

    return tasks