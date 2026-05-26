class Employee:
    def work(self):
        print("Employee is working now")
    def getsalary(self):
        print("Employee gets the salary : 50000")
class Hrmanager(Employee):
    def work(self):
        print("Hr manager is working on hr tasks")
    def add_employee(self):
        print("Hr added the new employee")
hr=Hrmanager()
hr.work()
hr.getsalary()
hr.add_employee()