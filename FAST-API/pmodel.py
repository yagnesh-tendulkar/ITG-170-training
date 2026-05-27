from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    name : str
    phno : int
    email : str
user_details={}
count_id=1
@app.post("/create")
def create_user(user: User):
    global count_id
    user_details[count_id]=user
    response={
        'msg' :"syccesfully created",
        "user_id": count_id,
        "user_details": user_details[count_id],

    }
    count_id +=1
    return response
@app.get("/user")
def get_user():
    return user_details