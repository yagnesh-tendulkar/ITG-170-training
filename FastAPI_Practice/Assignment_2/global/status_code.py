from fastapi import status

class StatusCode:
    SUCCESS = status.HTTP_200_OK
    BAD_REQUEST = status.HTTP_400_BAD_REQUEST
    INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR