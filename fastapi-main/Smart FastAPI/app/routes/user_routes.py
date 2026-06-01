from fastapi import APIRouter, HTTPException, Depends
from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter()

# ---------------- CREATE USER (optional admin use) ----------------
@router.post("/users")
def create_user(user: dict, current=Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
        (user["name"], user["email"], user["password"])
    )

    conn.commit()
    conn.close()

    return {"message": "User created"}


# ---------------- GET ALL USERS ----------------
@router.get("/users")
def get_users():
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users")
    users = cursor.fetchall()

    conn.close()
    return users


# ---------------- GET USER BY ID ----------------
@router.get("/users/{user_id}")
def get_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, name, email FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()

    conn.close()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


# ---------------- UPDATE USER ----------------
@router.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name=%s, email=%s WHERE id=%s",
        (user["name"], user["email"], user_id)
    )

    conn.commit()
    conn.close()

    return {"message": "User updated"}


# ---------------- DELETE USER ----------------
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    conn.close()

    return {"message": "User deleted"}