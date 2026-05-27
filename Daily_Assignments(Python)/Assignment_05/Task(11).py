# Program to create a class hierarchy for employees
# Base class
class Employee:

    def __init__(self, name, address, salary, job_title):
        self.name = name
        self.address = address
        self.salary = salary
        self.job_title = job_title

    def calculate_bonus(self):
        return self.salary * 0.10

    def performance_report(self):
        print(self.name, "has good performance.")

    def manage_project(self):
        print(self.name, "is managing a project.")


# Subclass Manager
class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20

    def performance_report(self):
        print(self.name, "is an excellent Manager.")

    def manage_project(self):
        print(self.name, "is managing the company team.")


# Subclass Developer
class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.15

    def performance_report(self):
        print(self.name, "is developing software successfully.")

    def manage_project(self):
        print(self.name, "is working on development projects.")


# Subclass Programmer
class Programmer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.12

    def performance_report(self):
        print(self.name, "writes efficient code.")

    def manage_project(self):
        print(self.name, "is handling programming tasks.")

m = Manager("Rahul", "Hyderabad", 80000, "Manager")
d = Developer("Sneha", "Delhi", 60000, "Developer")
p = Programmer("Arjun", "Chennai", 50000, "Programmer")

employees = [m, d, p]

for emp in employees:
    print("\nName:", emp.name)
    print("Address:", emp.address)
    print("Job Title:", emp.job_title)
    print("Salary:", emp.salary)
    print("Bonus:", emp.calculate_bonus())

    emp.performance_report()
    emp.manage_project()