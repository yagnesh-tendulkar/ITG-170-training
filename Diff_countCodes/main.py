from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle%04123",
    database="fastapi_auth"
)

cursor = conn.cursor(dictionary=True)


country_codes = {
    "India": "+91",
    "USA": "+1",
    "UK": "+44",
    "Canada": "+1",
    "Australia": "+61"
}


class RegisterModel(BaseModel):
    name: str
    email: str
    phone: str
    country: str
    password: str


class LoginModel(BaseModel):
    email: str
    password: str



@app.middleware("http")
async def add_country_code(request: Request, call_next):

    # Execute only for register API
    if request.url.path == "/register":

        body = await request.json()

        country = body.get("country")
        phone = body.get("phone")

        # Add country code
        if country in country_codes:

            code = country_codes[country]

            # Avoid duplicate country code
            if not phone.startswith(code):
                body["phone"] = code + phone

        # Store modified body
        request._body = str(body).encode()

    response = await call_next(request)

    return response


@app.post("/register")
async def register(user: RegisterModel):

    # Check email already exists
    query = "SELECT * FROM users WHERE email=%s"

    cursor.execute(query, (user.email,))

    existing_user = cursor.fetchone()

    if existing_user:
        return JSONResponse(
            status_code=400,
            content={"message": "Email already registered"}
        )


    insert_query = """
    INSERT INTO users(name,email,phone,country,password)
    VALUES(%s,%s,%s,%s,%s)
    """

    values = (
        user.name,
        user.email,
        user.phone,
        user.country,
        user.password
    )

    cursor.execute(insert_query, values)

    conn.commit()

    return {
        "message": "User Registered Successfully",
        "data": values
    }


@app.post("/login")
async def login(user: LoginModel):

    query = """
    SELECT * FROM users
    WHERE email=%s AND password=%s
    """

    values = (user.email, user.password)

    cursor.execute(query, values)

    result = cursor.fetchone()

    if result:
        return {
            "message": "Login Successful",
            "user": result
        }

    return JSONResponse(
        status_code=401,
        content={"message": "Invalid Email or Password"}
    )