
from fastapi import FastAPI, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

from database import get_db
from models import User, StatusEnum
from auth import get_current_user, hr_only_access_check, hash_password, verify_password
from crud import get_employees, get_employee, create_employee, update_employee, delete_employee
from utils import generate_password

app = FastAPI(title="HR Employee Portal")


# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Session middleware (simple in-memory for demo)
from starlette.middleware.sessions import SessionMiddleware
app.add_middleware(SessionMiddleware, secret_key="supersecretkeychangeinproduction")

# Status display map
STATUS_DISPLAY = {
    "a": "Active",
    "i": "Inactive",
    "p": "Pending",
    "b": "Blocked"
}

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return RedirectResponse("/login")

@app.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.password):
        request.session["user_id"] = user.id
        return RedirectResponse("/dashboard", status_code=303)
    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Invalid credentials"
    })

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login")

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(hr_only_access_check)
):
    employees = get_employees(db)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "employees": employees,
        "status_display": STATUS_DISPLAY,
        "user": current_user
    })

@app.get("/add-employee", response_class=HTMLResponse)
async def add_employee_page(
    request: Request,
    current_user = Depends(hr_only_access_check)
):
    return templates.TemplateResponse("add_employee.html", {"request": request})

@app.post("/add-employee")
async def add_employee(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(...),
    department: str = Form(...),
    db: Session = Depends(get_db),
    current_user = Depends(hr_only_access_check)
):
    employee = create_employee(db, first_name, last_name, department)
    return RedirectResponse("/dashboard", status_code=303)

@app.get("/edit-employee/{emp_id}", response_class=HTMLResponse)
async def edit_employee_page(
    request: Request,
    emp_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(hr_only_access_check)
):
    employee = get_employee(db, emp_id)
    if not employee:
        raise HTTPException(404, "Employee not found")
    return templates.TemplateResponse("edit_employee.html", {
        "request": request,
        "employee": employee
    })

@app.post("/edit-employee/{emp_id}")
async def edit_employee(
    request: Request,
    emp_id: int,
    first_name: str = Form(...),
    last_name: str = Form(...),
    department: str = Form(...),
    status: str = Form(...),
    db: Session = Depends(get_db),
    current_user = Depends(hr_only_access_check)
):
    update_employee(db, emp_id, first_name, last_name, department, status)
    return RedirectResponse("/dashboard", status_code=303)

@app.post("/delete-employee/{emp_id}")
async def delete_employee_route(
    emp_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(hr_only_access_check)
):
    delete_employee(db, emp_id)
    return RedirectResponse("/dashboard", status_code=303)