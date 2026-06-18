from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()
@app.middleware("http")
async def custom_middleware(request: Request, call_next):
    print("Request received")
    response = await call_next(request)
    print("Response sent")
    return response
@app.get("/")
async def home():
    return {"message": " login request time"}

