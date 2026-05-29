# app/core/exceptions.py

class RideSharingException(Exception):
    """
    Custom exception class designed to instantly intercept business rules failures.
    """
    def __init__(self, status_code: int, error_summary: str, detail: str):
        self.status_code = status_code
        self.error_summary = error_summary
        self.detail = detail