#Create a subclass called HRManager that overrides the work() method and adds a new method called addEmployee().
class Employee:
    def work(self):
        print("Employee works.")

class HRManager(Employee):
    def work(self):
        print("HRManager manages employee.")
    def addEmployee(self):
        print("Employee is added.")

hr=HRManager()
hr.work()
hr.addEmployee()
