import os
import sys
from fastapi import FastAPI
sys.path.insert(0, os.path.dirname(__file__))
from endpoint import router

app = FastAPI()
app.include_router(router)
