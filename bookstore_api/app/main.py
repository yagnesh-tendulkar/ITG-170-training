# app/main.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import items from other directories
from app.core.config import settings
from app.middleware.logging import add_process_time_header
from app.api.v1.books import router as books_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# 1. Register CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Register Custom Performance Logging Middleware
app.middleware("http")(add_process_time_header)

# 3. Mount API Routers
# This prepends "/books" to all paths defined in your api/v1/books.py router
app.include_router(books_router, prefix="/books", tags=["Books Management"])


# 4. Programmatic Server Execution
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True  # Helpful for development, turn off in actual production
    )