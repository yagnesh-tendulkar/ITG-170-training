import mysql.connector


def get_connection():

    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="M1racle@123",
        database="fastapi_db"
    )