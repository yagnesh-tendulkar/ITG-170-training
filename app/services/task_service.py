from sqlalchemy.orm import Session

from app.models.task import Task

from app.exceptions.custom_exception import (
    ResourceNotFoundException,
    UnauthorizedAccessException
)


def create_task(
        db: Session,
        user_id: int,
        title: str,
        description: str
):

    task = Task(
        title=title,
        description=description,
        user_id=user_id
    )

    db.add(task)

    db.commit()

    db.refresh(task)

    return task


def get_all_tasks(
        db: Session,
        user_id: int
):

    return db.query(Task).filter(
        Task.user_id == user_id
    ).all()


def get_task_by_id(
        db: Session,
        task_id: int,
        user_id: int
):

    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise ResourceNotFoundException(
            "Task Not Found"
        )

    if task.user_id != user_id:
        raise UnauthorizedAccessException(
            "Unauthorized Access"
        )

    return task


def update_task(
        db: Session,
        task_id: int,
        user_id: int,
        data
):

    task = get_task_by_id(
        db,
        task_id,
        user_id
    )

    if data.title is not None:
        task.title = data.title

    if data.description is not None:
        task.description = data.description

    if data.status is not None:
        task.status = data.status

    db.commit()

    db.refresh(task)

    return task


def delete_task(
        db: Session,
        task_id: int,
        user_id: int
):

    task = get_task_by_id(
        db,
        task_id,
        user_id
    )

    db.delete(task)

    db.commit()

    return True