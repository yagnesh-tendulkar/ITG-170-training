from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from app.database.connection import engine

from app.models.product_model import Base

from app.api.product_routes import router


# CREATE TABLES
Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="Production Standard CRUD API"
)


# CORS MIDDLEWARE
app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# INCLUDE ROUTES
app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "API Running Successfully"
    }