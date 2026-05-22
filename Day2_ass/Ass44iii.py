"""
How Python Access Modifiers is Useful for Programming in Python?
 Public
 Private
 Protected
"""
class Student:

    def __init__(self):

        self.__salary = 50000   # Private variable

    def display(self):

        print(self.__salary)

s = Student()

s.display()