from fastapi import FastAPI
from app.routers.stream import router as stream_router
from app.core.cors import add_cors

app = FastAPI()
add_cors(app)
app.include_router(stream_router)
@app.get("/")
def root():
    return {"message": "Streaming API Running"}