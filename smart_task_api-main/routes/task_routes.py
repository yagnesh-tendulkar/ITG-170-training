from fastapi import APIRouter,BackgroundTasks
from pydantic import BaseModel,Field,field_validator
from fastapi.responses import StreamingResponse
import time
from fastapi import UploadFile, File, HTTPException
import os
from schemas.task_schema import Task

from database import mydb,mycursor
from exceptions.task_exceptions import TaskNotFoundException

router = APIRouter()
@router.post("/tasks")
def create_task(task:Task):

    sql='''
    insert into tasks(title,priority,status,user_id)
    values(%s,%s,%s,%s)
    '''
    val=(
        task.title,
        task.priority,
        task.status,
        task.user_id
    )
    mycursor.execute(sql,val)
    mydb.commit()

    return {
        "message":"task added successfully",
        "task":task
    }

@router.get("/tasks")
def get_tasks():

    sql='select * from tasks'

    mycursor.execute(sql)
    result=mycursor.fetchall()

    return {
        "message":"task details",
        "task":result
    }

@router.get("/tasks/{id}")
def get_task_by_id(id:int):

    sql='select * from tasks where id=%s'
    val=(id,)

    mycursor.execute(sql,val)
    result=mycursor.fetchone()

    if result is None:
        raise TaskNotFoundException(id)

    return {
        "message":"task found",
        "task":result
    }

@router.put("/tasks/{id}")
def update_task(id:int,status:str):

    check_sql='select * from tasks where id=%s'
    check_val=(id,)

    mycursor.execute(check_sql,check_val)
    result=mycursor.fetchone()

    if result is None:
        raise TaskNotFoundException(id)

    sql='update tasks set status=%s where id=%s'
    val=(status,id)

    mycursor.execute(sql,val)
    mydb.commit()

    return {
        "message":"updation successful"
    }


@router.delete("/tasks/{id}")
def delete_task(id:int):

    check_sql='select * from tasks where id=%s'
    check_val=(id,)

    mycursor.execute(check_sql,check_val)
    result=mycursor.fetchone()

    if result is None:
        raise TaskNotFoundException(id)

    sql='delete from tasks where id=%s'
    val=(id,)

    mycursor.execute(sql,val)
    mydb.commit()

    return {
        "message":"deletion successful"
    }
#query parameters
#filtering
@router.get("/tasks/filter")
def filter_tasks(status:str):

    sql='select * from tasks where status=%s'

    mycursor.execute(sql,(status,))
    result=mycursor.fetchall()

    return {
        "tasks":result
    }

#pagination
@router.get("/tasks/pagination")
def pagination(page:int=1,limit:int=5):

    offset=(page-1)*limit

    sql='select * from tasks limit %s offset %s'

    mycursor.execute(sql,(limit,offset))
    result=mycursor.fetchall()

    return {
        "tasks":result
    }

#sorting
@router.get("/tasks/sort")
def sort_tasks():

    sql='select * from tasks order by priority'

    mycursor.execute(sql)
    result=mycursor.fetchall()

    return {
        "tasks":result
    }

#searching
@router.get("/tasks/search")
def search_task(title:str):

    sql='select * from tasks where title like %s'

    mycursor.execute(sql,(f"%{title}%",))
    result=mycursor.fetchall()

    return {
        "tasks":result
    }

#streaming response
@router.get("/tasks/{id}/stream")
def stream_task(id:int):

    def generator():

        yield f"Processing Task {id}\n"
        time.sleep(1)

        yield "Checking status...\n"
        time.sleep(1)

        yield "Task completed...\n"

    return StreamingResponse(
        generator(),
        media_type="text/plain"
    )

#file upload 

@router.post("/tasks/{id}/upload")
async def upload_file(
    id:int,
    file:UploadFile = File(...)
):

    # Task Exists Check
    mycursor.execute(
        "select * from tasks where id=%s",
        (id,)
    )

    task = mycursor.fetchone()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    # MIME Validation
    allowed_types = [
        "application/pdf",
        "image/png",
        "image/jpeg"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, PNG and JPG files are allowed"
        )

    # Duplicate Check
    file_path = f"uploads/{file.filename}"

    if os.path.exists(file_path):
        raise HTTPException(
            status_code=409,
            detail="File already exists"
        )

    # Size Restriction (2 MB)
    content = await file.read()

    if len(content) > 2 * 1024 * 1024:
        raise HTTPException(
            status_code=400,
            detail="File size must be less than 2MB"
        )

    # Save File
    with open(file_path,"wb") as f:
        f.write(content)

    return {
        "message":"File uploaded successfully",
        "file_name":file.filename
    }

#background tasks

def notify_employee():

    print(
        "Task assigned notification sent"
    )
@router.post("/tasks/notify")
def notify_task(
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(
        notify_employee
    )

    return {
        "message":
        "Notification processing started"
    }