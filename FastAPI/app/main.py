from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.tasks import router as task_router
from app.routes.users import router as user_router

app = FastAPI(
    title="Smart Task API",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(task_router)
app.include_router(health_router)


@app.get("/")
def root():
    return {"message": "Smart Task API Running"}