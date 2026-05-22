from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle:", self.length * self.width)
r = Rectangle(10, 5)
r.area()
