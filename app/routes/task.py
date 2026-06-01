from fastapi import APIRouter, Query
from typing import Optional
from app.database import db
from app.models import model
from app.exceptions.exception import AppException

task_router = APIRouter(prefix="/tasks", tags=["tasks"])


# CREATE TASK
@task_router.post("/task")
def create_task(task: model.tasks):
    db.task.append(task.model_dump())
    return task


# GET ALL TASKS
@task_router.get("/task")
def get_tasks():
    return db.task


# GET TASK BY ID
@task_router.get("/task/{task_id}")
def get_task(task_id: int):

    for task in db.task:
        if task["id"] == task_id:
            return task
    raise AppException.not_found("Task is not available")


# UPDATE TASK
@task_router.put("/task/{task_id}")
def update_task(task_id: int, update_task: model.tasks):
    for task in db.task:
        if task["id"] == task_id:
            task.update(update_task.model_dump())
            return task

    raise AppException.not_found("No task found")


# DELETE TASK
@task_router.delete("/task/{task_id}")
def delete_task(task_id: int):
    for task in db.task:
        if task["id"] == task_id:
            db.task.remove(task)
            return task
    raise AppException.not_found("Task is not available")

#using querry params and sorting , filtering and sorting
@task_router.get("/task")
def get_tasks(
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    sort_by: str = Query("id"),
    order: str = Query("asc"),
    page: int = Query(1),
    limit: int = Query(10)
):
    results = db.task
    # FILTER
    if status:
        results = [t for t in results if t["status"] == status]
    if priority:
        results = [t for t in results if t["priority"] == priority]

    # SEARCH (only by other fields)
    if search:
        results = [
            t for t in results
            if search.lower() in str(t.get("status", "")).lower()
            or search.lower() in str(t.get("priority", "")).lower()
        ]

    # SORT
    reverse = order == "desc"
    results = sorted(results, key=lambda x: x.get(sort_by), reverse=reverse)

    # PAGINATION
    start = (page - 1) * limit
    end = start + limit
    return {
        "page": page,
        "limit": limit,
        "total": len(results),
        "data": results[start:end]
    }