from fastapi import FastAPI
from app.routes import router
import uvicorn
app = FastAPI(
    title="Production GenAI Chatbot",
    version="1.0.0",
    description="Streaming AI Chatbot API"
)
app.include_router(router)
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000
    )
