# Smart Task & File Processing API

A FastAPI-based backend application for user authentication, task management, file management, health monitoring, and Docker deployment.

---

## Project Overview

This project was developed as part of a backend training assignment using FastAPI and SQLAlchemy ORM.

The application provides:

* JWT-based Authentication & Authorization
* Task Management System
* File Upload & Download APIs
* Pagination & Filtering
* CSV Export using Streaming Response
* Logging Middleware
* Global Exception Handling
* Health Monitoring APIs
* Dockerized Deployment

---

# Features

## Authentication

* User Registration
* User Login
* User Logout
* JWT Token Generation
* Protected APIs using JWT Authentication

---

## Task Management

* Create Task
* Get All Tasks
* Get Task By ID
* Update Task
* Delete Task (Soft Delete)
* Restore Deleted Tasks
* Pagination Support
* Filtering Support
* User-Specific Task Access
* CSV Export

---

## File Management

* Upload Files
* Download Files
* File Type Validation
* File Size Validation
* User-Specific File Access

---

## Middleware

### Request Logging Middleware

Logs:

* HTTP Method
* Endpoint
* Response Status Code
* Request Processing Time

Example:

```text
POST /api/auth/login Status:200 Time:0.1234s
```

---

## Exception Handling

Global Exception Handling for:

* HTTP Exceptions
* Internal Server Errors
* Validation Errors

Standardized Error Responses.

---

## Health Monitoring

### Application Health Check

```http
GET /api/health
```

### Database Health Check

```http
GET /api/health/db
```

---

# Technology Stack

| Technology     | Purpose              |
| -------------- | -------------------- |
| Python 3.9     | Programming Language |
| FastAPI        | REST API Framework   |
| SQLAlchemy ORM | Database ORM         |
| MySQL          | Database             |
| Pydantic       | Data Validation      |
| JWT            | Authentication       |
| Docker         | Containerization     |
| Uvicorn        | ASGI Server          |

---

# Project Structure

```text
Smart Task & File Processing API
│
├── main.py
│
├── database
│   ├── base.py
│   ├── connection.py
│   └── session.py
│
├── models
│   ├── user_model.py
│   ├── task_model.py
│   └── file_model.py
│
├── schemas
│   ├── auth_schema.py
│   ├── task_schema.py
│   └── file_schema.py
│
├── routers
│   ├── auth_router.py
│   ├── task_router.py
│   ├── file_router.py
│   └── health_router.py
│
├── dependencies
│   └── auth_dependency.py
│
├── middleware
│   └── logging_middleware.py
│
├── exceptions
│   └── exception_handlers.py
│
├── utils
│   ├── jwt_handler.py
│   └── password_handler.py
│
├── uploads
│
├── requirements.txt
├── Dockerfile
├── .env
└── README.md
```

---

# Database Configuration

Database Name:

```text
ITG_170
```

Environment Variables:

Create a `.env` file in project root.

```env
DB_USER=root
DB_PASSWORD=Santosh@90
DB_HOST=localhost
DB_NAME=ITG_170

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/santoshksethy/ITG-170-training_6405/tree/SantoshKumarSethy_6405
cd 1st-June-Python
cd Smart-Task-File-Processing-API
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Environment

### Mac/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
uvicorn main:app --reload
```

---

# Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Authentication APIs

### Register User

```http
POST /api/auth/register
```

### Login User

```http
POST /api/auth/login
```

### Logout User

```http
POST /api/auth/logout
```

---

## Task APIs

### Create Task

```http
POST /api/tasks
```

### Get All Tasks

```http
GET /api/tasks
```

Supports:

* Pagination
* Filtering

Example:

```http
GET /api/tasks?page=1&size=5
```

---

### Get Task By ID

```http
GET /api/tasks/{task_id}
```

---

### Update Task

```http
PUT /api/tasks/{task_id}
```

---

### Delete Task

```http
DELETE /api/tasks/{task_id}
```

---

### Restore Deleted Task

```http
PUT /api/tasks/{task_id}/restore
```

---

### Export Tasks CSV

```http
GET /api/tasks/export/csv
```

---

## File APIs

### Upload File

```http
POST /api/files/upload
```

---

### Download File

```http
GET /api/files/{file_id}
```

---

## Health APIs

### Application Health

```http
GET /api/health
```

---

### Database Health

```http
GET /api/health/db
```

---

# Authentication Flow

1. Register User
2. Login User
3. Receive JWT Token
4. Click "Authorize" in Swagger
5. Enter:

```text
Bearer <jwt_token>
```

6. Access Protected APIs

---

# Docker Support

This application is fully Dockerized.

---

## Build Docker Image

```bash
docker build -t smart-task-api .
```

---

## Verify Docker Image

```bash
docker images
```

Expected Output:

```text
REPOSITORY       TAG       IMAGE ID
smart-task-api   latest    xxxxxxxxxxxx
```

---

## Create Environment File

```env
DB_USER=root
DB_PASSWORD=Santosh@90
DB_HOST=host.docker.internal
DB_NAME=ITG_170
```

Note:

`host.docker.internal` allows Docker containers to connect to the MySQL server running on the host machine.

---

## Run Docker Container

```bash
docker run \
-p 8000:8000 \
--env-file .env \
smart-task-api
```

---

## Check Running Containers

```bash
docker ps
```

---

## View Container Logs

```bash
docker logs <container_id>
```

---

## Stop Container

```bash
docker stop <container_id>
```

---

## Remove Container

```bash
docker rm <container_id>
```

---

## Remove Docker Image

```bash
docker rmi smart-task-api
```

---

## Open Swagger in Docker

```text
http://localhost:8000/docs
```

---

# Sample Login Response

```json
{
  "message": "Login successful",
  "token": "jwt_token_here",
  "user": {
    "id": 1,
    "username": "santosh",
    "email": "santosh@gmail.com"
  }
}
```

---

# Future Enhancements

* Role-Based Access Control (RBAC)
* Refresh Tokens
* Docker Compose
* Redis Caching
* Unit Testing
* CI/CD Pipeline
* API Rate Limiting

---

# Author

**Santosh Kumar Sethy**

Software Trainee

Miracle Software Systems

_FastAPI | SQLAlchemy | MySQL | JWT | Docker_
