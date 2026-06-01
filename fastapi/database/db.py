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

# Ensure `hired_at` column exists (add it if the table pre-dates this schema)
mycursor.execute("SHOW COLUMNS FROM employees LIKE 'hired_at'")
if mycursor.fetchone() is None:
    mycursor.execute("ALTER TABLE employees ADD COLUMN hired_at DATETIME")
    mydb.commit()

