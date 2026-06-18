from database.connection import get_connection


# CREATE BOOK
def create_book(data):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO books(title,author,price)
    VALUES(%s,%s,%s)
    """

    values = (
        data.title,
        data.author,
        data.price
    )

    cursor.execute(query, values)

    conn.commit()

    conn.close()

    return {
        "message": "Book Added Successfully"
    }


# GET ALL BOOKS
def get_all_books(author=None, price=None):

    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM books WHERE 1=1"

    values = []

    if author:
        query += " AND author=%s"
        values.append(author)

    if price:
        query += " AND price=%s"
        values.append(price)

    cursor.execute(query, values)

    books = cursor.fetchall()

    conn.close()

    return books


# GET SINGLE BOOK
def get_single_book(book_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM books WHERE id=%s"

    cursor.execute(query, (book_id,))

    book = cursor.fetchone()

    conn.close()

    return book


# UPDATE BOOK
def update_book(book_id, data):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE books
    SET title=%s,author=%s,price=%s
    WHERE id=%s
    """

    values = (
        data.title,
        data.author,
        data.price,
        book_id
    )

    cursor.execute(query, values)

    conn.commit()

    conn.close()

    return {
        "message": "Book Updated Successfully"
    }


# DELETE BOOK
def delete_book(book_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = "DELETE FROM books WHERE id=%s"

    cursor.execute(query, (book_id,))

    conn.commit()

    conn.close()

    return {
        "message": "Book Deleted Successfully"
    }