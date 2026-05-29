# Write a  program to create a class known as Person with methods called
# getFirstName() and getLastName()
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def getFirstName(self):
        return self.fname
    def getLastName(self):
        return self.lname
p1=Person("John","Doe")
print(f"First Name: {p1.getFirstName()}")
print(f"Last Name: {p1.getLastName()}")