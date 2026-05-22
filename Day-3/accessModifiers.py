class Student:

    def __init__(self):

        self.name = "Arika"

        self._course = "Python"

        self.__marks = 95

    def display(self):
        print("Name:", self.name)
        print("Course:", self._course)
        print("Marks:", self.__marks)

s = Student()

print("Public:", s.name)

print("Protected:", s._course)

s.display()
