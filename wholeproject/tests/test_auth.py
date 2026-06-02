from fastapi.testclient import TestClient#send fake http requests to our API without running a server 
from app.main import app  #importing app form main file 
from app.database.database import dbUser   # importing database to clear the databse before testing

client = TestClient(app)# test client connected to our fast api app (now we can use client.post,client.get and so on )


def setup_function():
    dbUser.clear()#clearing the databse 
#if we don't clear the data before every task that we perform ,the tests could interfere with each other 

def test_register_user():#pytest autometically runs the functions starting with test_

    response = client.post(  #creating post request using client 
        "/register",
        json={          #passing the request body 
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    assert response.status_code == 200   # checks statuscode---if success return 200 ok --if failed return E AssertionError 
    assert response.json()["message"] == "User registered successfully"


def test_login_user():

    client.post(       # first we have to register because login reqires an existing account 
        "/register",
        json={
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    response = client.post(
        "/login",
        json={      #credentials are submitted 
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    assert response.status_code == 200   #verifies the success  ---- login has to be success

    data = response.json()   # return the response that is token and token type in json format 

    assert "access_token" in data    # checks whether token exists or not that is nothing but token is returned or not 
    assert data["token_type"] == "bearer"#if token  exists it returns the type 


def test_protected_route():

    client.post(
        "/register",
        json={
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    login_response = client.post(
        "/login",
        json={
            "id": 1,
            "name": "John",
            "email": "john@gmail.com",
            "age": 25,
            "password": "123456"
        }
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/protected",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200
    assert response.json()["message"] == "You are authenticated"