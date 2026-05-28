from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine
from routers.product_routes import router as product_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Inventory API",
    description="Production Ready FastAPI CRUD Application",
    version="1.0.0"
)


# CORS CONFIGURATION
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# INCLUDE ROUTES
app.include_router(product_router)


@app.get("/")
def home():
    return {
        "message": "Smart Inventory API Running Successfully"
    }