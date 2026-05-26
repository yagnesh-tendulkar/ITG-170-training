from fastapi import FastAPI
from routes.employee_routes import router

app = FastAPI()

app.include_router(router)