class Employee:

    def __init__(self, name, address, salary, jobTitle):
        self.name = name
        self.address = address
        self.salary = salary
        self.jobTitle = jobTitle

    def calculateBonus(self):
        return self.salary * 0.10

    def performanceReport(self):
        print(self.name, "has good performance.")

    def manageProject(self):
        print(self.name, "is managing a project.")

class Manager(Employee):

    def calculateBonus(self):
        return self.salary * 0.20

    def performanceReport(self):
        print(self.name, "is an excellent manager.")

class Developer(Employee):

    def calculateBonus(self):
        return self.salary * 0.15

    def manageProject(self):
        print(self.name, "is developing software projects.")

class Programmer(Employee):

    def calculateBonus(self):
        return self.salary * 0.12

    def performanceReport(self):
        print(self.name, "writes efficient code.")

m = Manager("Arika", "Hyderabad", 80000, "Manager")
d = Developer("Rahul", "Bangalore", 60000, "Developer")
p = Programmer("Sneha", "Chennai", 50000, "Programmer")

print("Manager Bonus:", m.calculateBonus())
m.performanceReport()
m.manageProject()

print()

print("Developer Bonus:", d.calculateBonus())
d.performanceReport()
d.manageProject()

print()

print("Programmer Bonus:", p.calculateBonus())
p.performanceReport()
p.manageProject()
