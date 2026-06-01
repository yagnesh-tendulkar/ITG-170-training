import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="M1racle@123",
    database="employee_task"
)
mycursor=mydb.cursor()
def get_db():
    return mydb