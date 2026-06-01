# 🚀 Smart Task & File Processing API

A production-ready backend application built with FastAPI that demonstrates enterprise-level backend development concepts in a single project.

---

## 📌 Project Overview

This project provides a scalable backend system where users can:

* Create and manage tasks
* Upload files
* Stream processing logs in real-time
* Apply filtering and pagination
* Authenticate using JWT
* Track request logs
* Handle exceptions gracefully
* Follow production-level architecture

---

## 🏗️ Tech Stack

| Category         | Technology         |
| ---------------- | ------------------ |
| Framework        | FastAPI            |
| Validation       | Pydantic           |
| ORM              | SQLAlchemy         |
| Database         | MySQL / PostgreSQL |
| Authentication   | JWT                |
| Streaming        | StreamingResponse  |
| Background Jobs  | BackgroundTasks    |
| Testing          | Pytest             |
| Containerization | Docker             |

---

# 📁 Project Structure

```text
app/
│
├── api/
│   ├── auth_routes.py
│   ├── task_routes.py
│   ├── file_routes.py
│   └── health_routes.py
│
├── schemas/
│   ├── auth_schema.py
│   ├── task_schema.py
│   └── file_schema.py
│
├── models/
│   ├── user_model.py
│   ├── task_model.py
│   └── uploaded_file_model.py
│
├── services/
│   ├── auth_service.py
│   ├── task_service.py
│   └── file_service.py
│
├── middleware/
│   ├── logging_middleware.py
│   ├── request_id_middleware.py
│   └── auth_middleware.py
│
├── dependencies/
│   └── auth_dependency.py
│
├── exceptions/
│   └── exception_handlers.py
│
├── database/
│   ├── connection.py
│   └── session.py
│
├── utils/
│   ├── jwt_handler.py
│   ├── password_handler.py
│   └── helpers.py
│
├── config/
│   └── settings.py
│
└── main.py
```

---

# ✨ Features

## 1️⃣ Authentication

### Register User

```http
POST /api/auth/register
```

### Login User

```http
POST /api/auth/login
```

### JWT Protected APIs

```http
Authorization: Bearer <token>
```

Features:

* Password Hashing
* JWT Token Generation
* JWT Validation
* Protected Routes

---

## 2️⃣ User Management

### Create User

```http
POST /api/users
```

### Get All Users

```http
GET /api/users
```

### Get User By ID

```http
GET /api/users/{user_id}
```

### Update User

```http
PUT /api/users/{user_id}
```

### Delete User

```http
DELETE /api/users/{user_id}
```

---

## 3️⃣ Task Management

### Create Task

```http
POST /api/tasks
```

### Get Tasks

```http
GET /api/tasks
```

### Get Task By ID

```http
GET /api/tasks/{task_id}
```

### Update Task

```http
PATCH /api/tasks/{task_id}
```

### Delete Task

```http
DELETE /api/tasks/{task_id}
```

---

## 4️⃣ Query Parameters

Supports:

### Pagination

```http
GET /api/tasks?page=1&limit=10
```

### Filtering

```http
GET /api/tasks?status=completed
```

### Search

```http
GET /api/tasks?search=fastapi
```

### Sorting

```http
GET /api/tasks?sort_by=created_at
```

---

## 5️⃣ Path Parameters

Examples:

```http
GET /api/tasks/{task_id}

DELETE /api/users/{user_id}
```

---

## 6️⃣ Request Body Validation

Example:

```json
{
  "title": "Learn FastAPI",
  "description": "Complete middleware implementation",
  "priority": "high"
}
```

Implemented using Pydantic.

---

# 🧠 Advanced Pydantic Features

### Field Validators

```python
@field_validator("age")
def validate_age(cls, value):
    if value < 18:
        raise ValueError("Age must be above 18")
    return value
```

### Model Validators

```python
@model_validator(mode="after")
def validate_due_date(self):
    return self
```

### Computed Fields

```python
@computed_field
@property
def is_overdue(self):
    return True
```

---

# 📦 Middleware

## Built-in Middleware

* CORS Middleware
* GZip Middleware
* Trusted Host Middleware

## Custom Middleware

### Request Logging Middleware

Logs:

```text
POST /api/tasks 201 23ms
```

### Request ID Middleware

Adds unique request IDs.

### Authentication Middleware

Protects sensitive routes.

---

# 📜 Centralized Logging

Supports:

* Console Logging
* Error Logging
* Request Logging
* Rotating File Logs

Example:

```text
2026-06-01 INFO POST /tasks 201 20ms
2026-06-01 ERROR ValidationError
```

---

# ⚠️ Exception Handling

Global Exception Handlers:

```python
HTTPException
ValidationError
Exception
```

Response Format:

```json
{
  "success": false,
  "message": "Task not found"
}
```

---

# 🔄 Streaming Response APIs

### Stream Task Processing

```http
GET /api/tasks/{id}/stream
```

Example Output:

```text
Processing started...
Reading file...
Generating embeddings...
Saving results...
Task completed...
```

Implemented using:

```python
StreamingResponse
```

---

# 📤 File Upload APIs

### Upload File

```http
POST /api/files/upload
```

Supported Features:

* File Validation
* MIME Type Validation
* Duplicate File Detection
* Size Restrictions

Supported Formats:

* PDF
* TXT
* CSV
* DOCX

---

# ⚙️ Dependency Injection

Implemented using:

```python
Depends()
```

Example:

```python
db: Session = Depends(get_db)
```

Benefits:

* Cleaner Architecture
* Reusable Components
* Easier Testing

---

# 🚀 Background Tasks

Implemented using:

```python
BackgroundTasks
```

Examples:

* Send Email
* Generate Reports
* Process Files

---

# 🔐 Security Features

Implemented:

* JWT Authentication
* Password Hashing
* Protected Endpoints
* API Key Support

---

# 📊 Health Check APIs

### Application Health

```http
GET /health
```

### Database Health

```http
GET /health/db
```

Response:

```json
{
  "status": "healthy"
}
```

---

# 🐳 Docker Support

## Build Image

```bash
docker build -t smart-task-api .
```

## Run Container

```bash
docker run -p 8000:8000 smart-task-api
```

Dockerfile:

```dockerfile
FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# 🧪 Testing

Implemented Using:

```text
Pytest
```

Test Coverage:

* CRUD APIs
* Authentication APIs
* Validation Rules
* Middleware
* Exception Handlers

---

# ▶️ Run Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
uvicorn main:app --reload
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

Open ReDoc:

```text
http://127.0.0.1:8000/redoc
```

---

# 🏁 Deliverables

* Source Code
* README.md
* Dockerfile
* requirements.txt
* Postman Collection
* Unit Tests
* Swagger Screenshots

---

# ⭐ Conclusion

This project demonstrates enterprise-grade FastAPI backend development concepts including authentication, CRUD operations, middleware, dependency injection, exception handling, streaming responses, file processing, logging, testing, and Docker deployment within a single production-ready application.
