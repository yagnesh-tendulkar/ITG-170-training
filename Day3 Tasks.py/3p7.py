class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
    def getFirstName(self):
        return self.firstName
    def getLastName(self):
        return self.lastName
p = Person("Ram", "Kumar")
print("First Name:", p.getFirstName())
print("Last Name:", p.getLastName())