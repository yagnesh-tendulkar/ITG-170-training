class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is working")

    def getSalary(self):
        print("Salary of", self.name, "is", self.salary)

class HRManager(Employee):

    def work(self):
        print(self.name, "is managing HR activities")

    def addEmployee(self, emp_name):
        print(emp_name, "has been added as a new employee")

hr = HRManager("Abhiram", 70000)


hr.work()
hr.getSalary()
hr.addEmployee("Rahul")