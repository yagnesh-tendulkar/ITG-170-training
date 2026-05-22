#Create a subclass called Employee that adds a new method named getEmployeeId() and overrides the getLastName() method to include the employee's job title.
class Person:

    def getLastName(self):
        print("Vujji")


class Employee(Person):

    def getEmployeeId(self):
        print("EMP101")

    def getLastName(self):
        print("Vujji - Developer")


emp = Employee()

emp.getEmployeeId()
emp.getLastName()