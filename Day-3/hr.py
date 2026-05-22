
class Employee:
    def work(self):
        print("Employee is working.")
    def getSalary(self):
        salary = 50000
        print("Salary:", salary)
class HRManager(Employee):
    def work(self):
        print("HR Manager is managing employees.")
    def addEmployee(self):
        print("New employee added.")

hr = HRManager()


hr.work()         
hr.getSalary()   
hr.addEmployee()   
