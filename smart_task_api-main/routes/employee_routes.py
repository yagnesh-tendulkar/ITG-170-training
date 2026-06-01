from fastapi import APIRouter
from pydantic import BaseModel
from database import mydb,mycursor
from exceptions.employee_exceptions import EmployeeAlreadyExistsException,EmployeeNotFoundException
from passlib.context import CryptContext
from schemas.employee_schema import Employee
from fastapi import APIRouter
router = APIRouter()
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


@router.post("/employees")
def create_employee(employee:Employee):
    check_sql='select * from employee where email=%s'
    check_val=(employee.email,)
    mycursor.execute(check_sql,check_val)
    result=mycursor.fetchone()
    if result:
        raise EmployeeAlreadyExistsException(employee.email)
    
    hashed_password = pwd_context.hash(
        employee.password
    )
    sql='insert into employee(name,email,password) values(%s,%s,%s)'
    val=(
        employee.name,
        employee.email,
        hashed_password
    )
    mycursor.execute(sql,val)
    mydb.commit() #to save changes permanently
    return {
        "message":"employee added successfully",
        "employee":employee
    }
@router.get("/employees")
def get_employee():
    sql='select * from employee'
    mycursor.execute(sql)
    result=mycursor.fetchall()
    return {
        "message":"employee details",
        "employee":result
    }
@router.get("/employees/{id}")
def get_employee_by_id(id:int):
    sql='select * from employee where id=%s'
    val=(id,)
    mycursor.execute(sql,val)
    result=mycursor.fetchone()
    if result is None:
        raise EmployeeNotFoundException(id)
    return {
        "message":"employee found",
        "employee":result
    }

@router.put("/employees/{id}")
def update_employee(id:int,name:str):
    check_sql='select * from employee where id=%s'
    check_val=(id,)
    mycursor.execute(check_sql,check_val)
    result=mycursor.fetchone()
    if result is None:
        raise EmployeeNotFoundException(id)
    sql='update employee set name=%s where id=%s'
    val=(name,id)
    mycursor.execute(sql,val)
    mydb.commit()
    return {
        "message":"updation successful"
    }

@router.delete("/employees/{id}")
def delete_employee(id:int):
    check_sql='select * from employee where id=%s'
    check_val=(id,)
    mycursor.execute(check_sql,check_val)
    result=mycursor.fetchone()
    if result is None:
        raise EmployeeNotFoundException(id)
    sql='delete from employee where id=%s'
    val=(id,)
    mycursor.execute(sql,val)
    mydb.commit()

    return {
        "message":"deletion successful"
    }

#query parameters
#searching
@router.get("/employees/search")
def search_employee(name:str):

    sql='select * from employee where name like %s'

    mycursor.execute(sql,(f"%{name}%",))
    result=mycursor.fetchall()

    return result

#sorting
@router.get("/employees/sort")
def sort_employee():

    sql='select * from employee order by name'

    mycursor.execute(sql)
    result=mycursor.fetchall()

    return result
#filtering
@router.get("/employees/filter")
def filter_employee(name:str):

    sql='select * from employee where name=%s'

    mycursor.execute(sql,(name,))
    result=mycursor.fetchall()

    return {
        "employee":result
    }

#pagination
@router.get("/employees/pagination")
def employee_pagination(page:int=1,limit:int=5):

    offset=(page-1)*limit

    sql='select * from employee limit %s offset %s'

    mycursor.execute(sql,(limit,offset))
    result=mycursor.fetchall()

    return {
        "employee":result
    }



