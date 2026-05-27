from fastapi import FastAPI, Query, Path
from models import UserRequest
from status_handler import APIExceptionHandler

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(user_id: int = Path(..., gt=0)):
    if user_id != 101:
        APIExceptionHandler.not_found("User ID not found")
    return {"status": "success", "user_id": user_id}

@app.get("/search")
async def search_user(name: str = Query(..., min_length=3)):
    if name.lower() != "balaji":
        APIExceptionHandler.not_found("User does not exist")
    return {"status": "success", "name": name}

@app.post("/create-user")
async def create_user(user: UserRequest):
    if "@gmail.com" not in user.email:
        APIExceptionHandler.bad_request("Only Gmail accounts are allowed")
    return APIExceptionHandler.created(f"User {user.name} created successfully")

@app.get("/divide")
async def divide_numbers(a: int, b: int):
    if b == 0:
        APIExceptionHandler.bad_request("Division by zero is not allowed")
    result = a / b
    return {"result": result}
