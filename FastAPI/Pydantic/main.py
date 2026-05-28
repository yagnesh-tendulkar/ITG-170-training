from fastapi import FastAPI

from Pydantic.database.database import (
    Base,
    engine
)

from Pydantic.routers.user_router import (
    router as user_router
)


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="FastAPI Production CRUD",
    version="1.0.0"
)


app.include_router(user_router)