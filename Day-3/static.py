class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("School:", Student.school)

    @staticmethod
    def message():
        print("Welcome to the school")

s1 = Student("Arika")
s2 = Student("Rahul")

s1.display()
print()

s2.display()
print()

Student.message()
