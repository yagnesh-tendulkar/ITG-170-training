from database.connection import get_connection


# CREATE EMPLOYEE
def create_employee(data):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    INSERT INTO employees(name,email,department,salary)
    VALUES(%s,%s,%s,%s)
    """

    values = (
        data.name,
        data.email,
        data.department,
        data.salary
    )

    cursor.execute(query, values)

    conn.commit()

    employee_id = cursor.lastrowid

    conn.close()

    return {
        "message": "Employee Created Successfully",
        "employee_id": employee_id
    }


# GET ALL EMPLOYEES
def get_all_employees():

    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM employees"

    cursor.execute(query)

    employees = cursor.fetchall()

    conn.close()

    return employees


# GET SINGLE EMPLOYEE
def get_single_employee(emp_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = "SELECT * FROM employees WHERE id=%s"

    cursor.execute(query, (emp_id,))

    employee = cursor.fetchone()

    conn.close()

    return employee


# UPDATE EMPLOYEE
def update_employee(emp_id, data):

    conn = get_connection()

    cursor = conn.cursor()

    query = """
    UPDATE employees
    SET name=%s,email=%s,department=%s,salary=%s
    WHERE id=%s
    """

    values = (
        data.name,
        data.email,
        data.department,
        data.salary,
        emp_id
    )

    cursor.execute(query, values)

    conn.commit()

    conn.close()

    return {
        "message": "Employee Updated Successfully"
    }


# DELETE EMPLOYEE
def delete_employee(emp_id):

    conn = get_connection()

    cursor = conn.cursor()

    query = "DELETE FROM employees WHERE id=%s"

    cursor.execute(query, (emp_id,))

    conn.commit()

    conn.close()

    return {
        "message": "Employee Deleted Successfully"
    }