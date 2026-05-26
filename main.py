
from fastapi import FastAPI,HTTPException
app=FastAPI()
@app.get("/")
def root_url():
    return  {"meassage" : "welcome to fastapi"}
@app.get("/sub")
def internal_url():
    return  {"meassage" : "welcome to fastapi internal"}

users={
    1:{"name" : "suresh",
    "orders" : {
        101:{"item" : "laptop","amt":5000},
        102:{"item" : "phone","amt":5400}
    }},
    2:{"name" : "ramesh",
       "orders" :{
        201:{ "item":"lap","amt":40},
        202 :{"item" : "phone","amt" : 2000}
       }
}}

@app.get("/user/{user_id}/order/{order_id}")
def get_user(user_id : int,order_id :int):
    if user_id not in users:
        raise HTTPException(status_code=404,detail="product id not found")

    return users[user_id]["orders"][order_id]