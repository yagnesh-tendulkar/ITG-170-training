from fastapi import HTTPException
from app.constants_loader import (ERROR_MESSAGES, STATUS_CODES)

class ProductNotFoundException(HTTPException):
    def __int__(self):
        super().__init__(status_code = STATUS_CODES[
            "HTTP_404_NOT_FOUND"
        ],
        detail = ERROR_MESSAGES["PRODUCT_NOT_FOUND"]
)