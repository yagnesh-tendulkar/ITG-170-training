from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate
router = APIRouter()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/tasks")
def createtask(task:TaskCreate,db:Session=Depends(get_db)):
    new_task= Task(title=task.title,description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()
@router.get("/tasks")
def getting(task_id:int,db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id==task_id)
    if not task:
        raise HTTPException(status_code=404,detail="task are nill or empty")
    return task
@router.put("/tasks/{task_id}")
def update_task(task_id:int,task:TaskCreate,db:Session=Depends(get_db)):
    db_task=db.query(Task).filter(Task.id==task_id).first()
    if not db_task:
        raise HTTPException(status_code=404,detail="task not found")
    db_task.title = task.title
    db_task.descriptions = task.description
    db.commit()
    db.refresh(db_task)
    return db_task
@router.delete("/tasks/{task_id}")
def delete_task(task_id:int,db:Session=Depends(get_db)):
    task = db.query(Task).filter(Task.id==task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="task not found")
    db.delete(task)
    db.commit()
    return {"message":"User deleted successfully"}