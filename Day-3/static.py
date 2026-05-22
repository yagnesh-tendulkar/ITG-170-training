class Student:

    school_name = "ABC School"  

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("School:", Student.school_name)

    @staticmethod
    def show_rules():
        print("School rules: Wear uniform and be on time")
s1 = Student("John")
s2 = Student("Emma")

s1.display()
s2.display()
Student.show_rules()
