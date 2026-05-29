# Error API

A small FastAPI example that demonstrates basic request handling, path/query parameters, Pydantic validation, and custom error responses.

## What this app does

This project contains simple endpoints for:

- fetching a user by path parameter
- searching a user by query parameter
- creating a user with Pydantic validation
- dividing two numbers with a zero-check

## Files

- `main.py` — FastAPI routes and application logic
- `models.py` — Pydantic request model (`UserRequest`)
- `status_handler.py` — Helper methods to raise HTTP exceptions and return created responses

## Endpoints

### 1. Get user by ID
- `GET /user/{user_id}`
- Example: `/user/101`
- Returns success if `user_id == 101`, otherwise `404 Not Found`

### 2. Search user by name
- `GET /search?name=balaji`
- Returns success if the name is `balaji`, otherwise `404 Not Found`

### 3. Create user
- `POST /create-user`
- Body example:
  ```json
  {
    "name": "Balaji",
    "age": 25,
    "email": "balaji@gmail.com"
  }
  ```
- Only Gmail email addresses are accepted.

### 4. Divide two numbers
- `GET /divide?a=10&b=2`
- Returns the result of `a / b`.
- If `b == 0`, returns `400 Bad Request`.

## Run the app

From this folder:

```bash
uvicorn main:app --reload
```

Then open:

- `http://127.0.0.1:8000/docs` for Swagger UI

## Notes

- This is a simple learning project.
- The current logic uses a basic in-memory validation approach and custom exception helpers.
