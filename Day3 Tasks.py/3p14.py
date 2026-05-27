class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(self.name)
s = Student("Ram")
s.display()