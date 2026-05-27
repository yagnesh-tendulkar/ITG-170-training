# Program to Show Method Overloading in Python
class Calculator:
    def add(self, a, b=0, c=0):
        print("Sum =", a + b + c)

obj = Calculator()
# Calling method with different number of arguments
obj.add(10, 20)        
obj.add(10, 20, 30)    
obj.add(10)        