from fastapi import HTTPException


class AppException:
    @staticmethod
    def not_found():
        raise HTTPException(status_code=404,detail="user not found")
    @staticmethod
    def wrong_data():
        raise HTTPException(status_code=400,detail="Unauthorized data")
    @staticmethod
    def conflict():
        raise HTTPException(status_code=409,detail="Resource already exists")
    @staticmethod
    def forbidden():
        raise HTTPException(status_code=403,detail="Forbidden")
    @staticmethod
    def server_error():
        raise HTTPException(status_code=500,detail="This is an internal server issue")
    @staticmethod
    def unavailable_server():
        raise HTTPException(status_code=503,detail="This server is not available")
    @staticmethod
    def Work_done():
        raise HTTPException(status_code=200,detail="Ok this is done")
    @staticmethod
    def created():
        raise HTTPException(status_code=201,detail="Something new was created")
    