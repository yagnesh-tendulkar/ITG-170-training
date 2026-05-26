class shape:
    """The same method name behaves differently depending on the object"""
    def area(self):
        print("Area of the shape")
class Rec(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(f"Area of Rectangle with {self.l} and {self.b} parameters is : ",self.l*self.b)
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("Area of circle : ",(3.14*self.r*self.r))
c=circle(10)
rec=Rec(10,20)
c.area()
rec.area()