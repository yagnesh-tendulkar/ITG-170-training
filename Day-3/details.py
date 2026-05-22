class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

class Employee(Person):

    def __init__(self, firstName, lastName, employeeId, jobTitle):
        super().__init__(firstName, lastName)
        self.employeeId = employeeId
        self.jobTitle = jobTitle

    def getEmployeeId(self):
        return self.employeeId

    def getLastName(self):
        return self.lastName + "(" + self.jobTitle + ")"

emp = Employee("Ganta", "Sumathi", 6421, "Asst Professor")

print("First Name:", emp.getFirstName())
print("Last Name:", emp.getLastName())
print("Employee ID:", emp.getEmployeeId())
