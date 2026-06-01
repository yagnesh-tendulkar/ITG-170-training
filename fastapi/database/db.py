import hashlib
import os

from dotenv import load_dotenv
import mysql.connector

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
HR_USERNAME = os.getenv("HR_USERNAME")
HR_PASSWORD = os.getenv("HR_PASSWORD")
HR_ROLE = os.getenv("HR_ROLE", "HR")

if not all([DB_HOST, DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError(
        "Database credentials are required. Set DB_HOST, DB_USER, DB_PASSWORD and DB_NAME in .env or the environment."
    )

mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
)

mycursor = mydb.cursor(dictionary=True)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    position VARCHAR(100),
    salary DOUBLE,
    hired_at DATETIME
)
""")
mydb.commit()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS hr_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    role VARCHAR(50)
)
""")
mydb.commit()


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def _ensure_default_hr_user() -> None:
    if not HR_USERNAME or not HR_PASSWORD:
        return

    mycursor.execute("SELECT id FROM hr_users WHERE username=%s", (HR_USERNAME,))
    if mycursor.fetchone() is None:
        mycursor.execute(
            "INSERT INTO hr_users (username, password_hash, role) VALUES (%s, %s, %s)",
            (HR_USERNAME, _hash_password(HR_PASSWORD), HR_ROLE),
        )
        mydb.commit()


_ensure_default_hr_user()

# Ensure `hired_at` column exists (add it if the table pre-dates this schema)
mycursor.execute("SHOW COLUMNS FROM employees LIKE 'hired_at'")
if mycursor.fetchone() is None:
    mycursor.execute("ALTER TABLE employees ADD COLUMN hired_at DATETIME")
    mydb.commit()

