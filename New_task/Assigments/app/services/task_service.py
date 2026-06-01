from sqlalchemy.orm import Session
from app.models.tasks import Task
from app.schemas.tasks import TaskCreate,TaskUpdate

def create_task(db:Session,task:TaskCreate):
    new_task = Task(
        title = task.title,
        description = task.description,
        priority = task.priority,
        user_id = task.user_id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
# GET all tasks
def get_all_tasks(db: Session):
    return db.query(Task).all()

# GET single task by ID
def get_task_by_id(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

# UPDATE a task
def update_task(db: Session, task_id: int, task: TaskUpdate):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if not existing_task:
        return None
    if task.title is not None:
        existing_task.title = task.title
    if task.description is not None:
        existing_task.description = task.description
    if task.completed is not None:
        existing_task.completed = task.completed
    if task.priority is not None:
        existing_task.priority = task.priority
    db.commit()
    db.refresh(existing_task)
    return existing_task

# DELETE a task
def delete_task(db: Session, task_id: int):
    existing_task = db.query(Task).filter(Task.id == task_id).first()
    if not existing_task:
        return None
    db.delete(existing_task)
    db.commit()
    return {"message": "Task deleted successfully"}

