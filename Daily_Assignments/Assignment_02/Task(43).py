class Student:

    # public variable
    name = "Abhiram"

    # protected variable
    _course = "Python"

    # private variable
    __marks = 95

    def display(self):
        print("Name:", self.name)
        print("Course:", self._course)
        print("Marks:", self.__marks)


s = Student()

# accessing public member
print("Public:", s.name)

# accessing protected member
print("Protected:", s._course)

# accessing private member using method
s.display()