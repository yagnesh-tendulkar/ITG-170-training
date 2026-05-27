
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    name : str
    phno : int
    
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

@app.get('/user/{user_id}')
def get_single_user(user_id : int):
    if user_id not in user_details:
        raise HTTPException(status_code=404,details="user not found")
    return user_details[user_id]


@app.put('/user/{user_id}')
def update_user(user_id : int,user :User):
    if user_id not in user_details:
        raise HTTPException(status_code=404,details="user not found")
    user_details[user_id]=user
    return {"msg":"updated user","user": user}


@app.delete('/user/{user_id}')
def delete_user(user_id : int):
    if user_id not in user_details:
        raise HTTPException(status_code=404,details="user not found")
    delete= user_details.pop(user_id)
    return {"msg":"deleted the user","user" : delete}