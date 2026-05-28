from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app=FastAPI()
users_db = {
    1: {"name": "Amrita", "age": 22}
}
class User(BaseModel):
    name: str
    age: int
class CommonStatusCodes:
    @staticmethod
    @app.get("/users/{user_id}")
    def get_user(user_id: int):
        if user_id not in users_db:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return {
            "status_code": 200,
            "message": "User fetched successfully",
            "data": users_db[user_id]
        }

    @staticmethod
    @app.post("/create-user", status_code=201)
    def create_user(user: User):
        new_id = len(users_db) + 1

        users_db[new_id] = {
            "name": user.name,
            "age": user.age
        }

        return {
            "status_code": 201,
            "message": "User created successfully",
            "data": users_db[new_id]
        }

    @staticmethod
    @app.get("/bad-request")
    def bad_request(age: int):

        if age < 0:
            raise HTTPException(
                status_code=400,
                detail="Age cannot be negative"
            )

        return {
            "message": "Valid age"
        }

    @staticmethod
    @app.get("/unauthorized")
    def unauthorized(token: str = ""):

        if token != "admin123":
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return {
            "message": "Authorized"
        }

    @staticmethod
    @app.get("/admin")
    def admin(role: str):

        if role != "admin":
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return {
            "message": "Welcome Admin"
        }

    @staticmethod
    @app.get("/product/{product_id}")
    def product(product_id: int):

        products = [1, 2, 3]

        if product_id not in products:
            raise HTTPException(
                status_code=404,
                detail="Product not found"
            )

        return {
            "message": "Product found"
        }

    @staticmethod
    @app.post("/register")
    def register(user: User):

        for data in users_db.values():
            if data["name"] == user.name:
                raise HTTPException(
                    status_code=409,
                    detail="User already exists"
                )

        return {
            "message": "Registration successful"
        }

    @staticmethod
    @app.get("/validation")
    def validation(price: int):

        return {
            "price": price
        }

    @staticmethod
    @app.get("/server-error")
    def server_error():

        result = 10 / 0

        return result
