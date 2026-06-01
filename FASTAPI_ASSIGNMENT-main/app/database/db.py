import os
import mysql.connector
from mysql.connector import errorcode

from exceptions import DatabaseException


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "smart_task_db")


def create_database():
    with mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD) as conn:
        with conn.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
            cursor.execute(f"USE {DB_NAME}")

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS users(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    first_name VARCHAR(100),
                    last_name VARCHAR(100),
                    email VARCHAR(255) UNIQUE,
                    age INT,
                    password VARCHAR(255)
                )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    user_id INT NOT NULL,
                    title VARCHAR(255),
                    description TEXT,
                    priority ENUM('low','medium','high'),
                    status VARCHAR(50) DEFAULT 'created',
                    due_date DATETIME,
                    file_name VARCHAR(255),
                    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                )
            """
            )

        conn.commit()


def migrate_schema():
    try:
        with mysql.connector.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SHOW COLUMNS FROM tasks LIKE 'due_date'")
                if not cursor.fetchall():
                    cursor.execute("ALTER TABLE tasks ADD COLUMN due_date DATETIME")

                cursor.execute("SHOW COLUMNS FROM tasks LIKE 'user_id'")
                if not cursor.fetchall():
                    cursor.execute("ALTER TABLE tasks ADD COLUMN user_id INT NOT NULL DEFAULT 0")

            conn.commit()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Schema migration failed: {err}")


def get_connection():
    try:
        return mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            raise DatabaseException("Database access denied. Check DB_USER/DB_PASSWORD.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            try:
                create_database()
            except DatabaseException:
                raise
            try:
                return mysql.connector.connect(
                    host=DB_HOST,
                    user=DB_USER,
                    password=DB_PASSWORD,
                    database=DB_NAME,
                )
            except mysql.connector.Error as inner_err:
                raise DatabaseException(f"Unable to connect after database creation: {inner_err}")
        else:
            raise DatabaseException(f"Database connection failed: {err}")