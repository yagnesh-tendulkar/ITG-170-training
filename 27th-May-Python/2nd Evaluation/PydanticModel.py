from fastapi import FastAPI
app = FastAPI()
@app.get("/users/{user_id}")
async def read_item(user_id: int):
    return {"user_id": user_id}