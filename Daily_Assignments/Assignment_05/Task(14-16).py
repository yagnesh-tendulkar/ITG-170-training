class Student:

    # Static variable
    college = "ABC College"

    def __init__(self, name, marks, password):
        self.name = name
        self._marks = marks
        self.__password = password

    def display(self):
        print("Name:", self.name)
        print("Marks:", self._marks)

    # Static method
    @staticmethod
    def college_info():
        print("College Name:", Student.college)

    def show_password(self):
        print("Password:", self.__password)


s1 = Student("Rahul", 95, "rahul123")
s1.display()
# Accessing static variable
print("College:", Student.college)
# Calling static method
Student.college_info()
# Accessing public variable
print("Public Variable:", s1.name)
# Accessing protected variable
print("Protected Variable:", s1._marks)
# Accessing private variable using method
s1.show_password()