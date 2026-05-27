from fastapi import HTTPException, status

class APIExceptionHandler:

    @staticmethod
    def bad_request(message="Bad Request"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message
        )

    @staticmethod
    def not_found(message="Resource Not Found"):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message
        )

    @staticmethod
    def unauthorized(message="Unauthorized Access"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=message
        )

    @staticmethod
    def internal_server_error(message="Internal Server Error"):
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=message
        )

    @staticmethod
    def created(message="Resource Created Successfully"):
        return {
            "status_code": status.HTTP_201_CREATED,
            "message": message
        }