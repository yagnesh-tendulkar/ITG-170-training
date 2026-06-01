class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last
    def getFirstName(self):
        return self.first
    def getLastName(self):
        return self.last

p = Person('john','jacob')
print(p.getFirstName())
print(p.getLastName())


class Employee(Person):
    def __init__(self,first,last,id,title):
        super().__init__(first,last)
        self.id = id
        self.title = title
    def getLastName(self):
        return self.last+' '+self.title

    def getEmployeeId(self):
        return self.id

e= Employee('john','jacob',101,'developer')
print(e.getLastName())
print(e.getEmployeeId())
