from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app = FastAPI()
users=[]
class User(BaseModel):
    name:str
    id:int

#create
@app.post("/users")
def create_user(user:User):
    users.append(user)
    return {
        "message":"User Created",
    "Status Code": 200,}

#Read
@app.get("/users")
def read_users():
    return {
        f"Users : {users}",
        "Status Code : 200",}

#Update
@app.put("/users/{user_id}")
def update_user(user_id:int, u_user:User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index]= u_user
            return {
                "Message":"User Updated Succesfully",
                "Stauts Code" : 200}
    return HTTPException(status_code=404, detail="User Not Found")

#Delete
@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {
                "Message":"User Deleted Successfully",
                "Stauts Code" : 200
            }
    return HTTPException(status_code=404, detail="User Not Found")
