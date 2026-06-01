A high-performance backend system built using FastAPI that provides authentication, task management, file handling, monitoring, and containerized deployment.

This project follows a modular, production-ready architecture with clean separation of concerns.
✨ Features
🔐 Authentication System
User registration & login
JWT token authentication
Protected routes
Secure logout mechanism


📋 Task Management
Create, update, delete tasks
Soft delete & restore
Pagination & filtering
User-specific task isolation
CSV export (streaming response)


📁 File Management
Upload & download files
File validation (type & size)
Secure user-based access control


🧠 Middleware & Logging
Request logging middleware:
HTTP method
Endpoint
Status code
Execution time

⚠️ Exception Handling
Global exception handler
Validation error handling
Consistent API error responses

❤️ Health Monitoring
Application health check
Database connectivity check


📦 Smart Task & File Processing API
├── main.py
├── database/
├── models/
├── schemas/
├── routers/
├── dependencies/
├── middleware/
├── exceptions/
├── utils/
├── uploads/
├── requirements.txt
├── Dockerfile
└── .env

.env

DB_USER=root
DB_PASSWORD=M1racle@123
DB_HOST=localhost
DB_NAME=fastapi

SECRET_KEY=generate secret key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60