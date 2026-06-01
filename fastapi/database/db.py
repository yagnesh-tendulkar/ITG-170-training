import hashlib
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="fastapi"
)


mycursor=mydb.cursor(dictionary=True)
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
    mycursor.execute("SELECT id FROM hr_users WHERE username=%s", ("hr",))
    if mycursor.fetchone() is None:
        mycursor.execute(
            "INSERT INTO hr_users (username, password_hash, role) VALUES (%s, %s, %s)",
            ("hr", _hash_password("1234"), "HR"),
        )
        mydb.commit()


_ensure_default_hr_user()

# Ensure `hired_at` column exists (add it if the table pre-dates this schema)
mycursor.execute("SHOW COLUMNS FROM employees LIKE 'hired_at'")
if mycursor.fetchone() is None:
    mycursor.execute("ALTER TABLE employees ADD COLUMN hired_at DATETIME")
    mydb.commit()

