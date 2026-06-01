from fastapi import APIRouter
from fastapi import Query

from schemas.task_schema import (
    TaskCreate,
    TaskUpdate
)

from services.task_service import (
    task_service
)

from utils.pagination import (
    paginate
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_task(
    task: TaskCreate
):
    """
    Create Task
    """

    return {
        "success": True,
        "message": "Task created successfully",
        "data": task_service.create_task(
            task.model_dump()
        )
    }


@router.get("/")
def get_all_tasks(
    page: int = Query(
        default=1,
        ge=1
    ),
    limit: int = Query(
        default=10,
        ge=1,
        le=100
    )
):
    """
    Get All Tasks With Pagination
    """

    tasks = task_service.get_all_tasks()

    return paginate(
        data=tasks,
        page=page,
        limit=limit
    )


@router.get("/{task_id}")
def get_task_by_id(
    task_id: int
):
    """
    Get Task By ID
    """

    return {
        "success": True,
        "data": task_service.get_task_by_id(
            task_id
        )
    }


@router.patch("/{task_id}")
def update_task(
    task_id: int,
    task: TaskUpdate
):
    """
    Partial Update Task
    """

    updated_task = task_service.update_task(
        task_id,
        task.model_dump(
            exclude_unset=True
        )
    )

    return {
        "success": True,
        "message": "Task updated successfully",
        "data": updated_task
    }


@router.delete("/{task_id}")
def delete_task(
    task_id: int
):
    """
    Delete Task
    """

    return task_service.delete_task(
        task_id
    )