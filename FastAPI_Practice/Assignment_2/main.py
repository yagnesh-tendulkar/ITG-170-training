from fastapi import FastAPI
from routes.pdf_routes import router

app = FastAPI()
app.include_router(router)