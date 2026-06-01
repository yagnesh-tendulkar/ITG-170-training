from fastapi import APIRouter

router = APIRouter()

@router.post("/tasks")
def add_tasks():
    pass

@router.get("/tasks")
def get_tasks():
    pass

@router.get("/tasks/{id}")
def get_one_task():
    pass

@router.patch("/tasks/{id}")
def update_task():
    pass

@router.delete("/tasks/{id}")
def delete_task():
    pass

