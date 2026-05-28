from fastapi import HTTPException


class AppException:

    @staticmethod
    def not_found(message: str = "Resource not found"):
        raise HTTPException(status_code=404, detail=message)

    @staticmethod
    def conflict(message: str = "Resource already exists"):
        raise HTTPException(status_code=409, detail=message)

    @staticmethod
    def bad_request(message: str = "Bad request"):
        raise HTTPException(status_code=400, detail=message)

    @staticmethod
    def unauthorized(message: str = "Unauthorized"):
        raise HTTPException(status_code=401, detail=message)

    @staticmethod
    def forbidden(message: str = "Forbidden"):
        raise HTTPException(status_code=403, detail=message)

    @staticmethod
    def server_error(message: str = "Internal server error"):
        raise HTTPException(status_code=500, detail=message)