from sqlalchemy.orm import Session

from models.task_model import Task
from models.user_model import User


class TaskService:

    @staticmethod
    def create_task(
            title: str,
            description: str,
            current_user: User,
            db: Session
    ):

        task = Task(
            title=title,
            description=description,
            user_id=current_user.id
        )

        db.add(task)

        db.commit()

        db.refresh(task)

        return {
            "message": "Task Created Successfully",
            "task_id": task.id
        }

    @staticmethod
    def get_user_tasks(
            current_user: User,
            db: Session
    ):

        return (
            db.query(Task)
            .filter(
                Task.user_id == current_user.id
            )
            .all()
        )