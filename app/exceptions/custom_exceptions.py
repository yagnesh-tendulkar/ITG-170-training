"""
Application-specific exception classes for the Employee HR Management System.

These exceptions provide structured, typed errors that services and routes can
raise and that exception handlers can translate into appropriate HTTP responses.

Design:
- `AppException` is the base class carrying a status code, message, and
  optional details payload.
- Specific exceptions derive from `AppException` and provide sensible defaults.

Usage example (service layer):
    raise NotFoundException(message="Employee not found", details={"id": 123})

An exception handler in FastAPI can map these to `fastapi.HTTPException` or
return a JSON response with structured error information.
"""
from __future__ import annotations

from typing import Any, Dict, List, Optional, Union


DetailsType = Optional[Union[Dict[str, Any], List[Any]]]


class AppException(Exception):
    """
    Base application exception.

    Attributes:
        status_code: HTTP status code appropriate for the error (e.g., 400, 404).
        message: Human-readable message describing the error.
        details: Optional machine-readable details (dict or list) for clients/logs.
    """

    def __init__(self, *, status_code: int, message: str, details: DetailsType = None) -> None:
        super().__init__(message)
        self.status_code: int = status_code
        self.message: str = message
        self.details: DetailsType = details

    def to_dict(self) -> Dict[str, Any]:
        """Return a serializable representation of the exception."""
        payload: Dict[str, Any] = {"message": self.message, "status_code": self.status_code}
        if self.details is not None:
            payload["details"] = self.details
        return payload

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"{self.__class__.__name__}(status_code={self.status_code}, message={self.message!r})"


class NotFoundException(AppException):
    """Resource not found (HTTP 404)."""

    def __init__(self, message: str = "Resource not found", details: DetailsType = None) -> None:
        super().__init__(status_code=404, message=message, details=details)


class BadRequestException(AppException):
    """Invalid request or business rule violation (HTTP 400)."""

    def __init__(self, message: str = "Bad request", details: DetailsType = None) -> None:
        super().__init__(status_code=400, message=message, details=details)


class UnauthorizedException(AppException):
    """Authentication failure (HTTP 401)."""

    def __init__(self, message: str = "Unauthorized", details: DetailsType = None) -> None:
        super().__init__(status_code=401, message=message, details=details)


class ForbiddenException(AppException):
    """Authorization / permission denied (HTTP 403)."""

    def __init__(self, message: str = "Forbidden", details: DetailsType = None) -> None:
        super().__init__(status_code=403, message=message, details=details)


class ConflictException(AppException):
    """Conflict such as duplicate resource (HTTP 409)."""

    def __init__(self, message: str = "Conflict", details: DetailsType = None) -> None:
        super().__init__(status_code=409, message=message, details=details)
