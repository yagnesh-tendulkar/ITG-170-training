class Employee:
    company='Miracle Software Systems' # here this variable works as static variable for all objects

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e= Employee('John',45000)
print(e.company)