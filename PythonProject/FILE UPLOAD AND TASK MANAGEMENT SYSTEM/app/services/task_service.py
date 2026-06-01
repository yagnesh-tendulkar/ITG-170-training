from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.task import Task


# CREATE TASK
def create_task(db: Session, data, user_id: int):

    task = Task(
        title=data.title,
        description=data.description,
        priority=data.priority,
        owner_id=user_id
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


# GET SINGLE TASK (USER SCOPED)
def get_task(db: Session, task_id: int, user_id: int):

    return db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == user_id
    ).first()


# LIST TASKS (FILTER + SEARCH + PAGINATION)
def get_tasks(
    db: Session,
    user_id: int,
    skip: int = 0,
    limit: int = 10,
    status: str = None,
    priority: str = None,
    search: str = None,
    sort_by: str = "created_at"
):

    query = db.query(Task).filter(Task.owner_id == user_id)

    # FILTER: status
    if status:
        query = query.filter(Task.status == status)

    # FILTER: priority
    if priority:
        query = query.filter(Task.priority == priority)

    # SEARCH
    if search:
        query = query.filter(
            or_(
                Task.title.contains(search),
                Task.description.contains(search)
            )
        )

    # SORTING
    if sort_by == "priority":
        query = query.order_by(Task.priority.desc())
    else:
        query = query.order_by(Task.created_at.desc())

    return query.offset(skip).limit(limit).all()


# UPDATE TASK
def update_task(db: Session, task: Task, data):

    if data.title is not None:
        task.title = data.title

    if data.description is not None:
        task.description = data.description

    if data.status is not None:
        task.status = data.status

    if data.priority is not None:
        task.priority = data.priority

    db.commit()
    db.refresh(task)

    return task


# DELETE TASK
def delete_task(db: Session, task: Task):

    db.delete(task)
    db.commit()