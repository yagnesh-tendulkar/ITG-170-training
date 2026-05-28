from fastapi import status

class StatusCode:
    OK = status.HTTP_200_OK
    CREATED = status.HTTP_201_CREATED
    BAD_REQUEST = status.HTTP_400_BAD_REQUEST
    NOT_FOUND = status.HTTP_404_NOT_FOUND
    INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR


class Message:
    BOOK_CREATED = "Book created successfully"
    BOOK_UPDATED = "Book updated successfully"
    BOOK_DELETED = "Book deleted successfully"


    BOOK_FETCHED = "Book fetched successfully"
    BOOKS_FETCHED = "Books fetched successfully"

    MEMBER_CREATED = "Member created successfully"
    MEMBER_UPDATED = "Member updated successfully"
    MEMBER_DELETED = "Member deleted successfully"

    BOOK_NOT_FOUND = "Book not found"
    MEMBER_NOT_FOUND = "Member not found"

    BOOK_BORROWED = "Book borrowed successfully"
    BOOK_RETURNED = "Book returned successfully"

    NO_COPIES = "No copies available"


class ResponseModel:
    
    @staticmethod
    def success(message, data=None):
        return {
            "success": True,
            "message": message,
            "data": data
        }

    @staticmethod
    def error(message):
        return {
            "success": False,
            "message": message
        }