import asyncio
from fastapi import Request
from fastapi.responses import StreamingResponse
from app.utils.logger import logger
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database.connection import get_db
from app.models.models import TaskModel
from app.schemas.schemas import TaskCreate, TaskResponse, TaskUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
    # Hardcoded user_id=1 for now. We will replace this once Auth is implemented.
    new_task = TaskModel(**task_data.model_dump(), user_id=1)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=List[TaskResponse])
def read_all_tasks(
    status: Optional[str] = Query(None, pattern="^(pending|completed)$"),
    priority: Optional[str] = Query(None, pattern="^(low|medium|high)$"),
    search: Optional[str] = Query(None),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(TaskModel)
    
    # Filtering Implementation
    if status:
        query = query.filter(TaskModel.status == status)
    if priority:
        query = query.filter(TaskModel.priority == priority)
    if search:
        query = query.filter(TaskModel.title.contains(search) | TaskModel.description.contains(search))
    
    # Pagination Engine
    offset = (page - 1) * limit
    return query.offset(offset).limit(limit).all()

@router.get("/{task_id}", response_model=TaskResponse)
def read_single_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Requested Task record not found.")
    return task

@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task_query = db.query(TaskModel).filter(TaskModel.id == task_id)
    task = task_query.first()
    if not task:
        raise HTTPException(status_code=404, detail="Target task modifications rejected: Not Found")
    
    update_data = task_update.model_dump(exclude_unset=True)
    task_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Target task deletion rejected: Not Found")
    db.delete(task)
    db.commit()
    return None

async def task_processing_generator(task_id: int, request_id: str):
    """Asynchronous generator simulating state processing pipelines."""
    extra = {"request_id": request_id}
    
    stages = [
        "Initializing worker environment...",
        "Fetching data payloads from storage cache...",
        "Executing heavy vector calculations and embedding text fields...",
        "Cleaning transient system memory structures...",
        "Task sync completed successfully!"
    ]
    
    logger.info(f"Streaming job sequence initialized for task {task_id}", extra=extra)
    
    for i, stage in enumerate(stages, 1):
        await asyncio.sleep(1.5)  # Simulate chunk processing delays safely
        logger.info(f"Stream Progress Stage [{i}/5]: {stage}", extra=extra)
        # Yielding chunk format back across active HTTP pipes
        yield f"data: {{\"task_id\": {task_id}, \"step\": {i}, \"message\": \"{stage}\"}}\n\n"

@router.get("/{task_id}/stream")
async def stream_task_processing(task_id: int, request: Request):
    """
    Streams processing metrics or log checkpoints for long running operations back to client.
    """
    # Retrieve request id from middleware state tracking engine
    req_id = getattr(request.state, "request_id", "SYSTEM")
    
    return StreamingResponse(
        task_processing_generator(task_id, req_id), 
        media_type="text/event-stream"
    )