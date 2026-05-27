from fastapi import APIRouter, HTTPException, status
from app.database import get_connection
from app.schemas import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, age) VALUES (%s, %s)",
        (user.name, user.age)
    )

    conn.commit()

    return {
        "message": "User created successfully"
    }


@router.get("/", status_code=status.HTTP_200_OK)
def get_users():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    return users


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user(user_id: int):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM users WHERE id=%s",
        (user_id,)
    )

    user = cursor.fetchone()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=%s, age=%s WHERE id=%s",
        (user.name, user.age, user_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User updated successfully"
    }


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=%s",
        (user_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return