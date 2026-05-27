class Student:
    name = "Ram"
    marks = 90
    salary = 50000
    def display(self):
        print("Public:", self.name)
        print("Protected:", self._marks)
        print("Private:", self.__salary)
obj = Student()
print(obj.name)
print(obj._marks)
obj.display()
print(obj._Student__salary)