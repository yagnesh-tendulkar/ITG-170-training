import mysql.connector


def get_connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="M1racle@123",
        database="Library"
    )

    cursor = conn.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS books(
        book_id INT PRIMARY KEY,
        book_title VARCHAR(255),
        book_description TEXT
    )
    """

    cursor.execute(query)

    conn.commit()

    return conn