class Employee:
    def __init__(self, salary):
        self.salary = salary
    def work(self):
        print("Employee is working on assigned tasks.")
    def get_salary(self):
        return self.salary
class HRManager(Employee):
    def __init__(self, salary):
        super().__init__(salary)
    def work(self):
        print("HR Manager is maNaging")
    def add_employee(self):
        print("HR Manager is adding a new employee")
manager = HRManager(85000.0)
manager.work()
print("HR Manager salary: $",manager.get_salary())
manager.add_employee()
