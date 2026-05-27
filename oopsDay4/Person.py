class Person:
    def __init__(self,firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName

    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
    
class Employeee(Person):
    def __init__(self, firstName, lastName,employeeId,jobTitle):
        super().__init__(firstName, lastName)
        self.employeeId=employeeId
        self.jobTitle=jobTitle

    def getEmployeeID(self):
        return self.employeeId
    
    def getLastName(self):
        return f"{self.lastName} {self.jobTitle}"
    

p1=Person("Rishabh","patel")
print("First Name : ",p1.getFirstName())
print("Last Name : ",p1.getLastName())

e1=Employeee("santosh","suri","E4567","Intern")
print("First Name: ",e1.getFirstName())
print("last name: ",e1.getLastName())
print("Employee id: ",e1.getEmployeeID())