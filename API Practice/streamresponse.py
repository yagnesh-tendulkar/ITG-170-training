import asyncio
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

async def fake_video_streamer():
    for i in range(10):
        # Yield data chunks as bytes or strings
        yield f"Chunk {i}\n"
        await asyncio.sleep(0.5)  # Simulate data generation delay

@app.get("/stream")
async def main():
    return StreamingResponse(fake_video_streamer(), media_type="text/plain")
