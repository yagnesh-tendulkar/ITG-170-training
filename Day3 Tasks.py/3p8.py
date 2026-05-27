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
        return self.lastName + " - " + self.jobTitle
e = Employee("Ram", "Kumar", 101, "Manager")
print("First Name:", e.getFirstName())
print("Last Name:", e.getLastName())
print("Employee ID:", e.getEmployeeId())