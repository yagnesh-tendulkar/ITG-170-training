class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

class Employee(Person):
    def __init__(self, first_name, last_name, emp_id, job_title):
        super().__init__(first_name, last_name)
        self.emp_id = emp_id
        self.job_title = job_title

    def getEmployeeId(self):
        return self.emp_id

    def getLastName(self):
        return self.last_name + " (" + self.job_title + ")"

e1 = Employee("Rahul", "Sharma", 101, "Manager")

print("First Name:", e1.getFirstName())
print("Last Name:", e1.getLastName())
print("Employee ID:", e1.getEmployeeId())