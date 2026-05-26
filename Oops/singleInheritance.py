class parent:
    def func1(self):
        print("This is the parent class")
class child(parent):
    def func2(self):
        print("This is child class")
ch=child()
ch.func1()
ch.func2()
# This is overriding the method
class car:
    def __init__(self , a,b):
        self.a=a
        self.b=b
    def add(self):
        print(sum(self.a,self.b))
class bike(car):
    def __init__(self, a, b):
        super().__init__(a, b)
    def add(self):
        print(self.a*self.b)
b=bike(10,20)
b.add()
        
