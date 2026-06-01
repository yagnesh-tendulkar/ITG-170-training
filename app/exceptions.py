from fastapi import status


class AppException(Exception):
    """Base application exception with an HTTP status code."""

    def __init__(self, detail: str, status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR, code: str = "error"):
        self.detail = detail
        self.status_code = status_code
        self.code = code
        super().__init__(detail)


class ValidationException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, code="validation_error")


class NotFoundException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail, status_code=status.HTTP_404_NOT_FOUND, code="not_found")


class AuthenticationException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail, status_code=status.HTTP_401_UNAUTHORIZED, code="authentication_error")


class DatabaseException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, code="database_error")


class FileException(AppException):
    def __init__(self, detail: str):
        super().__init__(detail, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, code="file_error")
