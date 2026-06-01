from fastapi import APIRouter

route = APIRouter()

@route.post("/users")
def add_user():
    pass

@route.get("/users")
def get_user():
    pass

@route.get("/users/{id}")
def get_one_user():
    pass

@route.put("/users/{id}")
def update_user():
    pass

@route.delete("/users/{id}")
def delete_user():
    pass

