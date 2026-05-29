# Create a subclass called Employee that adds a new method named
# getEmployeeId() and overrides the getLastName() method to include the
# employee's job title
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def getLastName(self):
        return self.last_name

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id, job_title):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id
        self.job_title = job_title

    def getEmployeeId(self):
        return self.employee_id

    def getLastName(self):
        return f"{super().getLastName()} ({self.job_title})"