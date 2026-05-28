from fastapi import HTTPException, status
class AppStatus:
    # SUCCESS STATUS CODES
    HTTP_200_OK = status.HTTP_200_OK
    HTTP_201_CREATED = status.HTTP_201_CREATED
    # ERROR STATUS CODES
    HTTP_400_BAD_REQUEST = status.HTTP_400_BAD_REQUEST
    HTTP_401_UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
    HTTP_404_NOT_FOUND = status.HTTP_404_NOT_FOUND
    HTTP_500_INTERNAL_SERVER_ERROR = status.HTTP_500_INTERNAL_SERVER_ERROR
    # SUCCESS MESSAGES
    STUDENT_CREATED = "Student Added Successfully"
    STUDENT_UPDATED = "Student Updated Successfully"
    STUDENT_DELETED = "Student Deleted Successfully"
    STUDENT_FETCHED = "Student Retrieved Successfully"
    # ERROR MESSAGES
    STUDENT_NOT_FOUND = "Student Not Found"
    STUDENT_ALREADY_EXISTS = "Student Already Exists"
    INVALID_STUDENT_DATA = "Invalid Student Data"
class StudentNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=AppStatus.HTTP_404_NOT_FOUND,
            detail=AppStatus.STUDENT_NOT_FOUND
        )
class StudentAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=AppStatus.HTTP_400_BAD_REQUEST,
            detail=AppStatus.STUDENT_ALREADY_EXISTS
        )

