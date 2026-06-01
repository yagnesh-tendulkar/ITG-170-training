from fastapi import FastAPI

from routes.chat_routes import router
from middleware.logging_middleware import LoggingMiddleware


app = FastAPI(
    title="Gemini Streaming API"
)


app.add_middleware(LoggingMiddleware)


app.include_router(router)