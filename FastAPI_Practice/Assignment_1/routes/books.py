from fastapi import FastAPI
from fastapi.responses import JSONResponse

from middleware.cors import cors_middleware
from schemas import Book
from database import get_connection

from classes import (
    StatusCode,
    Message,
    ResponseModel
)

app = FastAPI()

#-------------Middleware----------
cors_middleware(app)

#-----------POST----------------
@app.post("/books")
def add_book(new_book: Book):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO books(
            book_id,
            book_title,
            book_description
        )
        VALUES (%s, %s, %s)
        """

        cursor.execute(
            query,
            (
                new_book.book_id,
                new_book.book_title,
                new_book.book_description
            )
        )

        conn.commit()

        return JSONResponse(
            status_code=StatusCode.CREATED,
            content=ResponseModel.success(
                Message.BOOK_CREATED
            )
        )

    except Exception as error:
        return JSONResponse(
            status_code=StatusCode.INTERNAL_SERVER_ERROR,
            content=ResponseModel.error(str(error))
        )

    finally:
        if conn:
            conn.close()

#-----------PUT----------------
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM books WHERE book_id=%s",
            (book_id,)
        )

        existing_book = cursor.fetchone()

        if not existing_book:
            return JSONResponse(
                status_code=StatusCode.NOT_FOUND,
                content=ResponseModel.error(
                    Message.BOOK_NOT_FOUND
                )
            )

        query = """
        UPDATE books
        SET
            book_id=%s,
            book_title=%s,
            book_description=%s
        WHERE book_id=%s
        """

        cursor.execute(
            query,
            (
                updated_book.book_id,
                updated_book.book_title,
                updated_book.book_description,
                book_id
            )
        )

        conn.commit()

        return JSONResponse(
            status_code=StatusCode.OK,
            content=ResponseModel.success(
                Message.BOOK_UPDATED
            )
        )

    except Exception as error:
        return JSONResponse(
            status_code=StatusCode.INTERNAL_SERVER_ERROR,
            content=ResponseModel.error(str(error))
        )

    finally:
        if conn:
            conn.close()

#-----------GET ALL BOOKS----------------
@app.get("/books")
def get_all_books():
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()

        data = []

        for book in books:
            data.append({
                "book_id": book[0],
                "book_title": book[1],
                "book_description": book[2]
            })

        return JSONResponse(
            status_code=StatusCode.OK,
            content=ResponseModel.success(
                Message.BOOKS_FETCHED,
                data
            )
        )

    except Exception as error:
        return JSONResponse(
            status_code=StatusCode.INTERNAL_SERVER_ERROR,
            content=ResponseModel.error(str(error))
        )

    finally:
        if conn:
            conn.close()

#-----------GET BOOK BY ID----------------
@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM books WHERE book_id=%s",
            (book_id,)
        )

        book = cursor.fetchone()

        if not book:
            return JSONResponse(
                status_code=StatusCode.NOT_FOUND,
                content=ResponseModel.error(
                    Message.BOOK_NOT_FOUND
                )
            )

        data = {
            "book_id": book[0],
            "book_title": book[1],
            "book_description": book[2]
        }

        return JSONResponse(
            status_code=StatusCode.OK,
            content=ResponseModel.success(
                Message.BOOK_FETCHED,
                data
            )
        )

    except Exception as error:
        return JSONResponse(
            status_code=StatusCode.INTERNAL_SERVER_ERROR,
            content=ResponseModel.error(str(error))
        )

    finally:
        if conn:
            conn.close()

#-----------DELETE BOOK----------------
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM books WHERE book_id=%s",
            (book_id,)
        )

        existing_book = cursor.fetchone()

        if not existing_book:
            return JSONResponse(
                status_code=StatusCode.NOT_FOUND,
                content=ResponseModel.error(
                    Message.BOOK_NOT_FOUND
                )
            )

        cursor.execute(
            "DELETE FROM books WHERE book_id=%s",
            (book_id,)
        )

        conn.commit()

        return JSONResponse(
            status_code=StatusCode.OK,
            content=ResponseModel.success(
                Message.BOOK_DELETED
            )
        )

    except Exception as error:
        return JSONResponse(
            status_code=StatusCode.INTERNAL_SERVER_ERROR,
            content=ResponseModel.error(str(error))
        )

    finally:
        if conn:
            conn.close()