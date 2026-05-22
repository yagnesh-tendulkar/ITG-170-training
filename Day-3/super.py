class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Student(Person):

    def __init__(self, name, rollNo):
        super().__init__(name)
        self.rollNo = rollNo

    def show(self):

        super().display()
        print("Roll Number:", self.rollNo)

s = Student("Arika", 101)

s.show()
