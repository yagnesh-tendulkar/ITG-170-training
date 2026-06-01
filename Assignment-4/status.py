from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/success")
def success():

    return {
        "status_code": 200,
        "message": "Request successful"
    }


@app.get("/created", status_code=status.HTTP_201_CREATED)
def created():

    return {
        "status_code": 201,
        "message": "Data created successfully"
    }


@app.get("/badrequest")
def bad_request():

    raise HTTPException(
        status_code=400,
        detail="Bad request"
    )


@app.get("/unauthorized")
def unauthorized():

    raise HTTPException(
        status_code=401,
        detail="Unauthorized access"
    )


@app.get("/forbidden")
def forbidden():

    raise HTTPException(
        status_code=403,
        detail="Access forbidden"
    )


@app.get("/notfound")
def not_found():

    raise HTTPException(
        status_code=404,
        detail="Data not found"
    )


@app.get("/servererror")
def server_error():

    raise HTTPException(
        status_code=500,
        detail="Internal server error"
    )