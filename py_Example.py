from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class employee(BaseModel):
    id:int
    first_name:str
    last_name:str
    phone:str
@app.post("/employee")
async def detail(emp:employee):
    return f"Details entered of {emp}"
@app.get("/employee/{emp_id}")
def geting(emp_id:int):
    return {"Emp_id":emp_id}
