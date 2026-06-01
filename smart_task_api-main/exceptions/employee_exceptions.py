class EmployeeAlreadyExistsException(Exception):
    def __init__(self,email):
        self.email=email

class EmployeeNotFoundException(Exception):
    def __init__(self,employee_id):
        self.employee_id=employee_id