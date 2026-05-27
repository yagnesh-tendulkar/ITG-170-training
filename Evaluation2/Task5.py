from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()
def data():
    for i in range(5):
        time.sleep(1)
        yield f"Message {i}\n"

@app.get("/stream")
def stream():
    return StreamingResponse(data(), media_type="text/plain")