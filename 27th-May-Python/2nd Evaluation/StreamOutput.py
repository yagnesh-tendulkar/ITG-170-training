from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()

# Generator function
def generate_data():
    for i in range(5):
        yield f"Message {i}\n"
        time.sleep(1)

@app.get("/stream")
def stream_response():
    return StreamingResponse(generate_data(), media_type="text/plain")