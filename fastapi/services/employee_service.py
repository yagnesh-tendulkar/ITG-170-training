from database.db import mydb, mycursor
from utils.audit import log_action


def create_employee(employee, username=None):

    query = """
    INSERT INTO employees(name, email, position, salary, hired_at)
    VALUES(%s, %s, %s, %s, %s)
    """

    values = (
        employee.name,
        employee.email,
        employee.position,
        employee.salary,
        employee.hired_at,
    )

    mycursor.execute(query, values)

    mydb.commit()

    if username:
        try:
            log_action(username, f"CREATED EMPLOYEE : {employee.name}")
        except Exception:
            pass

    return {"message": "Employee Created"}


def get_employees():

    mycursor.execute("SELECT * FROM employees")

    return mycursor.fetchall()


def get_employee(employee_id):

    query = "SELECT * FROM employees WHERE id=%s"

    mycursor.execute(query, (employee_id,))

    return mycursor.fetchone()


def delete_employee(employee_id, username=None):

    query = "DELETE FROM employees WHERE id=%s"

    mycursor.execute(query, (employee_id,))

    mydb.commit()

    if mycursor.rowcount == 0:
        return {"message": "Employee not found"}

    if username:
        try:
            log_action(username, f"DELETED EMPLOYEE ID : {employee_id}")
        except Exception:
            pass

    return {"message": "Employee Deleted"}


def update_employee(employee_id, employee, username=None):

    query = """
    UPDATE employees
    SET name=%s, email=%s, position=%s, salary=%s, hired_at=%s
    WHERE id=%s
    """

    values = (
        employee.name,
        employee.email,
        employee.position,
        employee.salary,
        employee.hired_at,
        employee_id,
    )

    mycursor.execute(query, values)
    mydb.commit()

    if mycursor.rowcount == 0:
        return {"message": "Employee not found"}

    if username:
        try:
            log_action(username, f"UPDATED EMPLOYEE ID : {employee_id}")
        except Exception:
            pass

    return {"message": "Employee Updated"}


def patch_employee(employee_id, employee_update, username=None):

    fields = {}

    if employee_update.name is not None:
        fields["name"] = employee_update.name
    if employee_update.email is not None:
        fields["email"] = employee_update.email
    if employee_update.position is not None:
        fields["position"] = employee_update.position
    if employee_update.salary is not None:
        fields["salary"] = employee_update.salary
    if employee_update.hired_at is not None:
        fields["hired_at"] = employee_update.hired_at

    if not fields:
        return {"message": "No fields provided to update"}

    set_clause = ", ".join([f"{key}=%s" for key in fields])
    values = tuple(fields.values()) + (employee_id,)

    query = f"UPDATE employees SET {set_clause} WHERE id=%s"

    mycursor.execute(query, values)
    mydb.commit()

    if mycursor.rowcount == 0:
        return {"message": "Employee not found"}

    if username:
        try:
            log_action(username, f"PARTIALLY UPDATED EMPLOYEE ID : {employee_id} FIELDS: {', '.join(fields.keys())}")
        except Exception:
            pass

    return {"message": "Employee partially updated"}

