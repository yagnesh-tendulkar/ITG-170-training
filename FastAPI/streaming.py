from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import time

app = FastAPI()


def generate_numbers():
    for i in range(1, 6):
        yield f"Number: {i}\n"
        time.sleep(1)


@app.get("/stream")
def stream_numbers():
    return StreamingResponse(
        generate_numbers(),
        media_type="text/plain"
    )