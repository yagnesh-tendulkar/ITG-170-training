import mysql.connector
from mysql.connector import errorcode

from database.db import get_connection
from exceptions import DatabaseException, NotFoundException, ValidationException
from services.auth_service import hash_password


def create_user(user):
    if user.password is None or len(user.password) < 8:
        raise ValidationException("Password is required and must be at least 8 characters long.")

    try:
        with get_connection() as conn, conn.cursor(dictionary=True) as cursor:
            query = """
            INSERT INTO users
            (first_name,last_name,email,age,password)
            VALUES (%s,%s,%s,%s,%s)
            """

            try:
                password_hash = hash_password(user.password)
            except ValueError as err:
                raise ValidationException(str(err)) from err

            cursor.execute(query, (
                user.first_name,
                user.last_name,
                user.email,
                user.age,
                password_hash,
            ))
            conn.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            raise ValidationException("A user with this email already exists.")
        raise DatabaseException(f"Unable to create user: {err}")

    return {"message": "User created successfully"}


def create_demo_user(email: str = "dev@localhost", password: str = "devpassword"):
    if get_user_by_email(email):
        return

    try:
        with get_connection() as conn, conn.cursor() as cursor:
            query = """
            INSERT INTO users
            (first_name, last_name, email, age, password)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, ("Demo", "User", email, 30, hash_password(password)))
            conn.commit()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_DUP_ENTRY:
            return
        raise DatabaseException(f"Unable to create demo user: {err}")


def get_user_by_email(email):
    try:
        with get_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
            return cursor.fetchone()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to fetch user by email: {err}")


def get_users():
    try:
        with get_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, first_name, last_name, email, age FROM users")
            return cursor.fetchall()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to fetch users: {err}")


def get_user(user_id):
    try:
        with get_connection() as conn, conn.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, first_name, last_name, email, age FROM users WHERE id=%s", (user_id,))
            user = cursor.fetchone()
            if not user:
                raise NotFoundException("User not found")
            return user
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to fetch user: {err}")


def update_user(user_id, data):
    if not any((data.email, data.age, data.first_name, data.last_name)):
        raise ValidationException("At least one field must be provided for update.")

    try:
        with get_connection() as conn, conn.cursor() as cursor:
            query = """
            UPDATE users
            SET first_name=%s, last_name=%s, email=%s, age=%s
            WHERE id=%s
            """
            cursor.execute(
                query,
                (
                    data.first_name,
                    data.last_name,
                    data.email,
                    data.age,
                    user_id,
                ),
            )
            if cursor.rowcount == 0:
                raise NotFoundException("User not found")
            conn.commit()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to update user: {err}")

    return {"message": "User updated successfully"}


def delete_user(user_id):
    try:
        with get_connection() as conn, conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id=%s", (user_id,))
            if cursor.rowcount == 0:
                raise NotFoundException("User not found")
            conn.commit()
    except mysql.connector.Error as err:
        raise DatabaseException(f"Unable to delete user: {err}")

    return {"message": "User deleted successfully"}
