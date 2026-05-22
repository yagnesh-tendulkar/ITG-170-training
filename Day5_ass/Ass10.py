#Program to Create an Interface
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Square(Shape):

    def area(self):
        print("Area = side × side")


s = Square()

s.area()