class Employee:
    def __init__(self, name, address, salary, jobTitle):
        self.name = name
        self.address = address
        self.salary = salary
        self.jobTitle = jobTitle
    def bonus(self):
        print("Bonus:", self.salary * 0.10)
    def performance(self):
        print("Good Performance")
    def project(self):
        print("Managing Project")
class Manager(Employee):
    pass
class Developer(Employee):
    pass
class Programmer(Employee):
    pass
m = Manager("Ram", "Hyderabad", 50000, "Manager")
m.bonus()
m.performance()
m.project()