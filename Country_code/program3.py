
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
app = FastAPI()
class User(BaseModel):
    name:str
    age:int
    u_id :int
@app.get("/user")
def read_data():
    return {'msg':"data returned successfully"}
@app.post("/user{user_id}")
def create_data(user_id:int,u:User):
    return {"data":u}
@app.put("/user/{user_id}")
def update_data(user_id:int,u:User):
    if u.u_id != user_id:
        raise HTTPException(status_code=400,detail="user not exist")
    u.name = u.name
    u.age = u.age
    return{"data":u}
@app.delete("/user/{user_id}")
def delete_data(user_id:int):
    if user_id != 1:
        raise HTTPException(status_code=400,detail="user not exist")

    return{'data': "user deleted"}
