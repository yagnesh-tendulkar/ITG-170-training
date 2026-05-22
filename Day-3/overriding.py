

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is working")

    def getSalary(self):
        print("Salary:", self.salary)


class HRManager(Employee):

    def work(self):
        print(self.name, "is working at miracle")

    def addEmployee(self):
        print(self.name, "is adding new employee")

hr = HRManager("sumathi", 78907657900000)

hr.work()
hr.addEmployee()
hr.getSalary()
