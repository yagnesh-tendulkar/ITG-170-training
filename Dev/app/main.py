from fastapi import FastAPI

from .database.connection import init_db
from .routes.developers import router as developer_router

app = FastAPI(title="Human-Centric Dev API")
app.include_router(developer_router)


@app.on_event("startup")
def startup_event():
    init_db()
