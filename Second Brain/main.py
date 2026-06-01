from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.notes import router as notes_router
from routers.snippets import router as snippets_router
from routers.search import router as search_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes_router)
app.include_router(snippets_router)
app.include_router(search_router)