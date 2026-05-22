from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
users=[]
class Users(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:Users):
    users.append(user)
    return {"data":user}

@app.put("/users/{user_id}")
def update_user(user_id:int,user:Users,notify:bool):
    if user_id<len(users):
        users[user_id]=user
        return {"data":user,
                "notify":notify
                }
    return {"message":"user not found"}


