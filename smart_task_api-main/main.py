from exceptions.employee_exceptions import EmployeeNotFoundException,EmployeeAlreadyExistsException
from exceptions.exception_handler import employee_exists_handler,employee_not_found_handler
from exceptions.task_exceptions import TaskNotFoundException
from exceptions.exception_handler import task_not_found_handler
from middleware.cors_middleware import add_cors_middleware
from middleware.logging_middleware import logging_middleware
from middleware.auth_middleware import auth_middleware
from middleware.request_id_middleware import request_id_middleware
from routes.employee_routes import router as employee_router
from routes.task_routes import router as task_router
from fastapi import Depends
from database import get_db
from jose import JWTError
from fastapi import HTTPException,Header
from security.jwt_auth import (
    create_access_token,
    verify_token
)
from passlib.context import CryptContext

from fastapi import FastAPI
app=FastAPI()

app.include_router(employee_router)
app.include_router(task_router)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

app.middleware("http")(logging_middleware)

app.middleware("http")(request_id_middleware)

#app.middleware("http")(auth_middleware)

add_cors_middleware(app)
app.add_exception_handler(
    EmployeeNotFoundException,
    employee_not_found_handler
    
)
app.add_exception_handler(
    EmployeeAlreadyExistsException,
    employee_exists_handler
)

app.add_exception_handler(
    TaskNotFoundException,
    task_not_found_handler
)

@app.get("/db-check")
def check_db(db=Depends(get_db)):

    return {
        "message":"Database connection successful"
    }

@app.post("/login")
def login():

    token = create_access_token(
        {"user":"admin"}
    )

    return {
        "access_token":token
    }

@app.get("/protected")
def protected(
    authorization:str=Header(...)
):

    verify_token(authorization)

    return {
        "message":"Access Granted"
    }