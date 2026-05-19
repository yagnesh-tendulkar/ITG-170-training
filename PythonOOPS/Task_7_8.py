class Person:
    def __init__(self,first,last):
        self.first=first
        self.last=last
    def getFirstName(self):
        print(self.first)
    def getLastName(self):
        print(self.last)

class Employee(Person):
    def __init__(self,first,last,empid,jobtitle):
        super().__init__(first,last)
        self.empid=empid
        self.jobtitle=jobtitle
    def getEmployeeID(self):
        print(self.empid)
    def getLastName(self):
        print(self.last)
        print(self.jobtitle)
e=Employee("Bikash","Ranjan",6406,"Trainee")
e.getEmployeeID()
e.getFirstName()
e.getLastName()