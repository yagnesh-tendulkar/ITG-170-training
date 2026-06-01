from exceptions.employee_exceptions import EmployeeAlreadyExistsException,EmployeeNotFoundException
from fastapi import Request
from fastapi.responses import JSONResponse
from exceptions.task_exceptions import TaskNotFoundException

async def employee_exists_handler(
        request:Request,
        exc:EmployeeAlreadyExistsException):
    return JSONResponse(
        status_code=400,
        content={"message":"employee already exists"}
    )

async def employee_not_found_handler(
        request:Request,
        exc:EmployeeNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message":"employee not found"}
    )

async def task_not_found_handler(
    request:Request,
    exc:TaskNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "message":f"Task with id {exc.id} not found"
        }
    )
