# Program to create a class Employee with methods work() and getSalary()

class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is working")

    def getSalary(self):
        print("Salary of", self.name, "is", self.salary)

emp1 = Employee("Rahul", 50000)

# Calling methods
emp1.work()
emp1.getSalary()