# from fastapi import FastAPI
# from middleware.logging_middleware import log_requests
# from routes.employee_routes import router as employee_router
# from routes.auth_routes import router as auth_router
# app = FastAPI()

# app.middleware("http")(log_requests)
# app.include_router(auth_router)
# app.include_router(employee_router)
from fastapi import FastAPI

from routes.auth_routes import router as auth_router
from routes.employee_routes import router as employee_router
# from routes.task_routes import router as task_router
from routes.file_routes import router as file_router
from routes.log_routes import router as log_router

from middleware.logging_middleware import log_requests
from middleware.auth_middleware import auth_middleware

app = FastAPI()

app.middleware("http")(auth_middleware)
app.middleware("http")(log_requests)

app.include_router(auth_router)
app.include_router(employee_router)
# app.include_router(task_router)
app.include_router(file_router)
app.include_router(log_router)