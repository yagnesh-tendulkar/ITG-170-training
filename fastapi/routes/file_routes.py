import os
from pathlib import Path
from datetime import datetime

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from schemas.employee_schema import EmployeeCreate
from services.employee_service import (
    create_employee,
    get_employees
)
from auth.auth_dependencies import verify_auth

router = APIRouter()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/employees/upload")
async def upload_employees(
    file: UploadFile = File(...),
    user: dict = Depends(verify_auth)
):

    # 1. File Validation
    if not file.filename.endswith(".txt"):
        raise HTTPException(
            status_code=400,
            detail="Only .txt files are allowed"
        )

    # 2. MIME Validation
    if file.content_type != "text/plain":
        raise HTTPException(
            status_code=400,
            detail="Only text/plain files are allowed"
        )

    content = await file.read()

    # 3. Size Restriction (Max 1 MB)
    max_size = 1024 * 1024

    if len(content) > max_size:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 1 MB"
        )

    if not content:
        raise HTTPException(
            status_code=400,
            detail="File is empty"
        )

    safe_name = os.path.basename(file.filename)
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    destination = UPLOAD_DIR / f"{timestamp}_{safe_name}"

    with open(destination, "wb") as out_file:
        out_file.write(content)

    lines = content.decode().splitlines()

    existing_employees = get_employees()

    existing_emails = {
        emp["email"]
        for emp in existing_employees
    }

    uploaded_count = 0

    for line in lines:

        parts = line.split(",")

        if len(parts) != 5:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid format: {line}"
            )

        name, email, position, salary, hired_at = parts

        email = email.strip()

        # 4. Duplicate Check
        if email in existing_emails:
            raise HTTPException(
                status_code=400,
                detail=f"Duplicate employee email: {email}"
            )

        employee = EmployeeCreate(
            name=name.strip(),
            email=email,
            position=position.strip(),
            salary=float(salary),
            hired_at=hired_at.strip()
        )

        create_employee(employee)

        existing_emails.add(email)

        uploaded_count += 1

    return {
        "message": "Employees uploaded successfully",
        "count": uploaded_count,
        "saved_file": str(destination)
    }