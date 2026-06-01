class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary
    def setSalary(self, newSalary):
        self.salary = newSalary
    def getName(self):
        return self.name
    def setName(self, newName):
        self.name = newName

e= Employee("Emil", 5000)
e.setName(10000)
e.setName('Smith')
print(e.getSalary())
print(e.getName())