import os
from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
# from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
from google import genai  # pip install google-genai python-dotenv pymysql cryptography

# -----------------------------
# ENV & GEN AI CONFIGURATION
# -----------------------------
# Load environment variables from a .env file
load_dotenv()

# Initialize the Gemini client
ai_client = genai.Client()

# -----------------------------
# MYSQL DATABASE SETUP (UPDATED)
# -----------------------------
# 1. Pull connection string from .env file or fallback to local defaults
# Format: mysql+pymysql://username:password@hostname:port/database_name
DATABASE_URL = os.getenv("MYSQL_URL", "mysql+pymysql://root:M1racle%40123@localhost:3306/testdb")

# 2. Setup engine without SQLite check_same_thread args
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Sample Database Model (UPDATED for MySQL requirements)
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    # MySQL requires an explicit string size limit for unique/indexed columns
    email = Column(String(255), unique=True, index=True)
    name = Column(String(255))


# Create tables in MySQL if they don't exist
Base.metadata.create_all(bind=engine)


# -----------------------------
# PYDANTIC SCHEMAS
# -----------------------------
class UserCreate(BaseModel):
    email: EmailStr
    name: str


class ChatRequest(BaseModel):
    message: str
    session_id: str  # Tracks specific conversation sessions


# -----------------------------
# FASTAPI APP INSTANCE
# -----------------------------
app = FastAPI(title="FastAPI User (MySQL) & Gemini Chat Service")


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# -----------------------------
# CUSTOM ERROR & GLOBAL HANDLER
# -----------------------------
class AppError(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message

class ErrorCodes:
    USER_NOT_FOUND = (404, "User not found")
    EMAIL_EXISTS = (400, "Email already exists")
    DB_ERROR = (500, "Database error")


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "error": exc.message
        }
    )


# -----------------------------
# USER ENDPOINTS
# -----------------------------
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise AppError(*ErrorCodes.USER_NOT_FOUND)

    return user


@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    # Check for existing email first
    existing = db.query(UserDB).filter(UserDB.email == user.email).first()
    if existing:
        raise AppError(*ErrorCodes.EMAIL_EXISTS)

    try:
        db_user = UserDB(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError:
        db.rollback()
        raise AppError(*ErrorCodes.DB_ERROR)


# -----------------------------
# GEMINI CHAT ENDPOINT
# -----------------------------
@app.post("/chat")
async def chat_with_gemini(payload: ChatRequest):
    try:
        # Create a real-time conversation session with system instructions
        chat = ai_client.chats.create(
            model="gemini-2.5-flash",
            config=genai.types.GenerateContentConfig(
                system_instruction="You are a helpful assistant integrated into a FastAPI app."
            )
        )

        # Send the user's prompt to Gemini
        response = chat.send_message(payload.message)
        ai_reply = response.text

        return {
            "success": True,
            "session_id": payload.session_id,
            "response": ai_reply
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Gemini API Error: {str(e)}"
        }