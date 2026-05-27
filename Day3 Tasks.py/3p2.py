class Employee:
    def __init__(self, salary):
        self.salary = salary
    def work(self):
        print("Employee is working on assigned tasks.")
    def get_salary(self):
        return self.salary
employee = Employee(65000.0)
employee.work()
print("Employee salary: $",employee.get_salary())
