from fastapi import APIRouter, HTTPException
from app.schemas import UserCreate, UserLogin
from app.database import get_db
from app.auth.password import hash_password, verify_password
from app.auth.jwt import create_access_token

router = APIRouter()

# ---------------- REGISTER ----------------
@router.post("/auth/register")
def register(user: UserCreate):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=%s", (user.email,))
    if cursor.fetchone():
        conn.close()
        raise HTTPException(status_code=400, detail="User already exists")

    hashed = hash_password(user.password)
    cursor.execute(
        "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
        (user.name, user.email, hashed)
    )
    conn.commit()
    conn.close()

    return {"message": "User registered successfully"}


# ---------------- LOGIN ----------------
@router.post("/auth/login")
def login(user: UserLogin):
    conn = get_db()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email=%s", (user.email,))
    db_user = cursor.fetchone()
    conn.close()

    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"user_id": db_user["id"], "email": db_user["email"]})
    return {"access_token": token, "token_type": "bearer"}
