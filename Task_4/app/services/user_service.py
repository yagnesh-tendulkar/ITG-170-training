from app.db.database import db

class UserService:

    @staticmethod
    def get_user(user_id: int):
        return db.get(user_id)

    @staticmethod
    def create_user(user_id: int, user_data):
        db[user_id] = user_data
        return db[user_id]

    @staticmethod
    def update_user(user_id: int, user_data):
        db[user_id] = user_data
        return db[user_id]

    @staticmethod
    def delete_user(user_id: int):
        return db.pop(user_id)