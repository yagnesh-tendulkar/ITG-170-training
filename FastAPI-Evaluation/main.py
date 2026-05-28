import time
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

users = []


class User(BaseModel):

    user_id: int = Field(gt=0)
    user_name: str
    user_age: int = Field(ge=18)

    @field_validator("user_name")
    @classmethod
    def validate_name(cls, value):

        if not value.isalpha():
            raise ValueError("Username must contain only alphabets")

        return value

@app.middleware("http")
async def log_requests(request: Request, call_next):

    print("URL :", request.url)
    print("METHOD :", request.method)
    print("TIME :", time.time())

    response = await call_next(request)

    return response


@app.post("/register")
def add_user(user: User):

    users.append(user)

    return {
        "message": "User inserted successfully",
        "data": user
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):

    for user in users:

        if user.user_id == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.get("/users")
def get_all_users():

    return users


@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):

    for user in users:

        if user.user_id == user_id:

            user.user_name = updated_user.user_name
            user.user_age = updated_user.user_age

            return {
                "message": "User updated successfully",
                "data": user
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user.user_id == user_id:

            users.remove(user)

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


def stream_response():

    for user in users:

        yield user.json() + "\n"

        time.sleep(1)


@app.get("/stream-users")
def get_stream():

    return StreamingResponse(
        stream_response(),
        media_type="application/json"
    )