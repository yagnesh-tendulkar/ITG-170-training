from fastapi import APIRouter

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post("/")
def create_task():
    return {
        "message": "Task created"
    }


@router.get("/")
def get_tasks():
    return {
        "message": "Get all tasks"
    }


@router.get("/{task_id}")
def get_task(task_id: int):
    return {
        "task_id": task_id
    }


@router.patch("/{task_id}")
def update_task(task_id: int):
    return {
        "message": "Task updated",
        "task_id": task_id
    }


@router.delete("/{task_id}")
def delete_task(task_id: int):
    return {
        "message": "Task deleted",
        "task_id": task_id
    }