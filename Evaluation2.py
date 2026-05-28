# from fastapi import FastAPI
# from pydantic import BaseModel
# app=FastAPI()
# class Student(BaseModel):
#     name:str
#     age:int
# @app.post("/student")
# def student(name: str,age:int):
#     {
#         "name":"harinita",
#         "age":21
#     }
#     return Student

#
# from fastapi import FastAPI,Request
# from pydantic import BaseModel
# import time
# app=FastAPI()
# @app.middleware("http")
# async def add_headers(request: Request,call_next):
#     start_time = time.time()
#     print("Requested started.")
#     response = await call_next(request)
#     end_time = time.time()
#     print("Time taken to complete request: ", end_time - start_time)
#     response.headers["X-Time"] = str(int(end_time - start_time))
#     print("Stopped request")
#     return response
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# from fastapi import FastAPI
# from fastapi.responses import StreamingResponse
# import time
# app = FastAPI()
# def generators():
#     for i in range(1,6):
#         yield f"Number:{i}\n"
#         time.sleep(i)
# @app.get("/stream")
# def stream_data():
#     return StreamingResponse(generators(), media_type="text/plain")


from fastapi import FastAPI,HTTPException,status
app = FastAPI()
@app.get("/student",status_code=status.HTTP_404_NOT_FOUND)
def student():
    return {"message":"Log not found"}
@app.post("/created",status_code=status.HTTP_200_CREATED)
def create(id: int):
    return {"message":"Successfully registered"}
@app.get("/student/{id}", status_code=status.HTTP_503_SERVICE_UNAVAILABLE)
def get_student_by_id(id: int):
    return {
        "message": "Server Unavailable",
        "student_id": id
    }