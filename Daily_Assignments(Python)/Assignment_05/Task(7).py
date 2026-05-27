# Program to create a class Person with methods getFirstName() and getLastName()

class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def getFirstName(self):
        return self.first_name

    def getLastName(self):
        return self.last_name

p1 = Person("Rahul", "Sharma")

print("First Name:", p1.getFirstName())
print("Last Name:", p1.getLastName())