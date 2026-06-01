from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.core.dependencies import (
    get_current_user
)

from app.schemas.task_schema import (
    TaskCreate,
    TaskUpdate
)

from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task_by_id,
    update_task,
    delete_task
)

from app.utils.responce import (
    success_response
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def add_task(
        task: TaskCreate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    created_task = create_task(
        db=db,
        user_id=current_user.id,
        title=task.title,
        description=task.description
    )

    return success_response(
        "Task Created Successfully",
        created_task
    )


@router.get("/")
def get_tasks(
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    tasks = get_all_tasks(
        db,
        current_user.id
    )

    return success_response(
        "Tasks Retrieved Successfully",
        tasks
    )


@router.get("/{task_id}")
def get_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    task = get_task_by_id(
        db,
        task_id,
        current_user.id
    )

    return success_response(
        "Task Retrieved Successfully",
        task
    )


@router.put("/{task_id}")
def edit_task(
        task_id: int,
        task_data: TaskUpdate,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    updated_task = update_task(
        db,
        task_id,
        current_user.id,
        task_data
    )

    return success_response(
        "Task Updated Successfully",
        updated_task
    )


@router.delete("/{task_id}")
def remove_task(
        task_id: int,
        db: Session = Depends(get_db),
        current_user=Depends(get_current_user)
):

    delete_task(
        db,
        task_id,
        current_user.id
    )

    return success_response(
        "Task Deleted Successfully"
    )