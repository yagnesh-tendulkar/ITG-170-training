class Student:
    college = "ABC College"
    def __init__(self, name):
        self.name = name
s1 = Student("Ram")
s2 = Student("Ravi")
print(s1.name, s1.college)
print(s2.name, s2.college)