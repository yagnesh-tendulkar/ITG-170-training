from fastapi import FastAPI

app = FastAPI()

db = {}
@app.post("/age/{user_id}/{age}")
async def add_age(user_id: int, age: int):
    db[user_id] = age
    return {"message": "Data saved", "data": db}

@app.put("/age/{user_id}/{age}")
async def update_age(user_id: int, age: int):
    db[user_id] = age
    return {"message": "Data updated", "data": db}

@app.get("/age/{user_id}/{age}")
async def get_age(user_id: int, age: int):
    return {"user_id": user_id, "age": age}

