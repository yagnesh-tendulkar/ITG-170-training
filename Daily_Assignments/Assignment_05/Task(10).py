# Program to Create an Interface in Python
from abc import ABC, abstractmethod

# Interface
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(10, 5)
c = Circle(7)

print("Area of Rectangle =", r.area())
print("Area of Circle =", c.area())