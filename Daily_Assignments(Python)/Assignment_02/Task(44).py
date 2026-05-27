class Student:
    def show_student(self):
        print("This is Student Class")


class Teacher:
    def show_teacher(self):
        print("This is Teacher Class")


class Principal:
    def show_principal(self):
        print("This is Principal Class")


s = Student()
t = Teacher()
p = Principal()

s.show_student()
t.show_teacher()
p.show_principal()