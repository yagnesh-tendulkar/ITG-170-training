from fastapi import FastAPI,HTTPException
app=FastAPI()
@app.get("/")
def greet():
    return {"Hello world"}

@app.post("/user/{user_id}")
def details(user_id:int):
    if user_id <= 0:
        raise HTTPException(status_code=400, detail="Invalid user_id")

    return {"user_id": user_id}
@app.put("/user/{user_id}")
def update(user_id:int):
    if user_id:
        return {"user_id":user_id}
    raise HTTPException(status_code=404,detail="Not found")
@app.delete("/user/{user_id}")
def delete(user_id:int):
    if user_id:
        return {"MSG":"Deleted"}
    
