# FastAPI Employee Management API

A simple FastAPI application for employee management with authentication, file upload support, audit logging, and streamed logs.

## Features

- JWT-based login authentication
- API key authentication support
- CRUD operations for employee records
- Employee upload from `.txt` files with validation
- Request logging middleware
- Audit logging for user actions
- Streaming logs endpoint for demo/testing

## Requirements

- Python 3.11+ (or compatible)
- MySQL database
- Dependencies in `requirements.txt`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The app loads configuration from environment variables or a `.env` file.
Create a `fastapi/.env` file with values for:

- `DB_HOST`
- `DB_USER`
- `DB_PASSWORD`
- `DB_NAME`
- `JWT_SECRET`
- `HR_USERNAME`
- `HR_PASSWORD`
- `HR_ROLE` (optional, default `HR`)

The database module also creates the `employees` and `hr_users` tables automatically if they do not exist.

> Do not store credentials in code. Add `.env` to `.gitignore` and keep secrets out of version control.

## Start the Server

Run the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

## Authentication

### JWT Login

Use the `/login` endpoint after setting the HR credentials in `.env`.
If `HR_USERNAME` and `HR_PASSWORD` are supplied, the app will seed that user automatically when the database is initialized.

The default HR credentials are:

- `username=hr`
- `password=1234`

Request example:

```bash
curl -X POST "http://127.0.0.1:8000/login?username=hr&password=1234"
```

Response example:

```json
{
  "access_token": "<jwt-token>"
}
```

## API Endpoints

### Employee Endpoints

All `/employees` endpoints require authentication.

- `POST /employees`
  - Create a new employee
  - Request body: `EmployeeCreate`

- `GET /employees`
  - List all employees
  - Supports optional query params:
    - `department`
    - `page` (default `1`)
    - `limit` (default `5`)

- `GET /employees/{employee_id}`
  - Get a single employee by ID

- `PUT /employees/{employee_id}`
  - Fully update an employee record
  - Request body: `EmployeeCreate`

- `PATCH /employees/{employee_id}`
  - Partially update an employee record
  - Request body: `EmployeeUpdate`

- `DELETE /employees/{employee_id}`
  - Delete an employee by ID

### File Upload

- `POST /employees/upload`
  - Upload a text file containing employee records
  - File format: one employee per line, with comma-separated values
  - Required fields per line: `name,email,position,salary,hired_at`
  - Example file contents:

    ```text
    John Doe,john.doe@example.com,Developer,60000,2026-01-01T09:00:00
    Jane Smith,jane.smith@example.com,Manager,75000,2025-06-15T09:00:00
    ```

  - Restrictions:
    - Only `.txt` files
    - MIME type `text/plain`
    - Maximum file size 1 MB
    - No duplicate employee emails

### Logs Streaming

- `GET /logs/stream`
  - Streams sample logs as a plain-text response

## Data Models

### `EmployeeCreate`

- `name` - string, 3-50 chars
- `email` - string
- `position` - string
- `salary` - float, must be positive
- `hired_at` - datetime

### `EmployeeUpdate`

- `name` - optional string
- `email` - optional string
- `position` - optional string
- `salary` - optional positive float
- `hired_at` - optional datetime

## Notes

- JWT tokens are signed using `mysecret` in `auth/jwt_handler.py` and expire in 30 minutes.
- Audit records are saved to `audit_logs` via `utils/audit.py`.
- Requests are logged through `middleware/logging_middleware.py` and authentication is enforced through `middleware/auth_middleware.py`.

## Suggested Improvements

- Move database credentials into environment variables
- Add tests for authentication, upload validation, and CRUD operations
- Add API documentation to `README` with full request/response examples
- Improve error handling for database failures
