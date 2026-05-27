from fastapi import FastAPI
from database import Base
from database import engine
from routes.book_routes import router
from middleware.cors_config import setup_cors

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BookVerse API"
)

setup_cors(app)

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "BookVerse Runninge"
    }