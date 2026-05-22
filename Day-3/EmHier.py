class Employee:

    def __init__(self, name, address, salary, job_title):
        self.name = name
        self.address = address
        self.salary = salary
        self.job_title = job_title

    def calculate_bonus(self):
        return self.salary * 0.10  # default 10% bonus

    def performance_report(self):
        return f"{self.name} has good performance as {self.job_title}"

class Manager(Employee):

    def manage_projects(self):
        return f"{self.name} is managing company projects."

    def calculate_bonus(self):
        return self.salary * 0.20  # 20% bonus

class Developer(Employee):

    def manage_projects(self):
        return f"{self.name} is developing software projects."

    def calculate_bonus(self):
        return self.salary * 0.15  # 15% bonus

class Programmer(Employee):

    def manage_projects(self):
        return f"{self.name} is writing and maintaining code."

    def calculate_bonus(self):
        return self.salary * 0.12  # 12% bonus


# obj
m = Manager("Alice", "Delhi", 80000, "Manager")
d = Developer("Bob", "Mumbai", 60000, "Developer")
p = Programmer("Charlie", "Chennai", 50000, "Programmer")

# Output
print(m.performance_report())
print(m.manage_projects())
print("Bonus:", m.calculate_bonus())

print()

print(d.performance_report())
print(d.manage_projects())
print("Bonus:", d.calculate_bonus())

print()

print(p.performance_report())
print(p.manage_projects())
print("Bonus:", p.calculate_bonus())
