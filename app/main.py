from fastapi import FastAPI
from app.middleware.CORSMiddleware import set_cors
from app.middleware.CustomMiddleware import log_requests


app = FastAPI()

set_cors(app)

app.middleware("http")(log_requests)