from datetime import time

from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.middleware("http")
def custom_middleware(request:Request, next_call):
    print(f"Requested on : {time.now('%H%M-%D%m')}")