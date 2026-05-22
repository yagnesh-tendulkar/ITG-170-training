from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
mylist=[]
class Todo(BaseModel):
    id:int
    title:str
    completed:bool


@app.post("/todos")
def create_todo(todo:Todo):
    mylist.append(todo)
    return {"data":todo}

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for i in mylist:
        if i.id==todo_id:
            return i
    return {"error":"item not found"}
@app.put("/todos/{todo_id}")
def update_item(todo_id:int,updated_id:Todo):
    for index,i in enumerate(mylist):
        if i.id==todo_id:
            mylist[index]=updated_id
            return {"message":"updated successfully",
                    "data":updated_id
                    }
    return {"error":"item not found"}

@app.delete("/todos/{item_id}")
def delete_item(item_id:int):
    for index,i in mylist:
        if i.id==item_id:
            mylist.pop(index)
            return {"message":"item deleted Successfully"}
    return {"error":"item not found"}









