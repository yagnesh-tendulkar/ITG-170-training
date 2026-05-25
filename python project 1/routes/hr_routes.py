from fastapi import APIRouter, HTTPException
from app.schemas.hr_schema import HRCreate, HRResponse
from app.schemas.login_schema import LoginRequest

router = APIRouter(
    prefix="/hr",
    tags=["HR"]
)


# Temporary in-memory storage (replace with MySQL later)
hr_db = []


@router.post("/add", response_model=HRResponse)
def add_hr(hr: HRCreate):

    for existing_hr in hr_db:
        if existing_hr["hr_email"] == hr.hr_email:
            raise HTTPException(status_code=400, detail="HR already exists")

    new_hr = {
        "hr_id": len(hr_db) + 1,
        "hr_name": hr.hr_name,
        "hr_email": hr.hr_email,
        "hr_password": hr.hr_password
    }

    hr_db.append(new_hr)

    return new_hr


@router.post("/login")
def hr_login(data: LoginRequest):

    for hr in hr_db:
        if hr["hr_email"] == data.email and hr["hr_password"] == data.password:
            return {"message": "Login successful", "role": "HR"}

    raise HTTPException(status_code=401, detail="Invalid credentials")