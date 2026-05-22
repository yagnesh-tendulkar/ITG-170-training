#Program to Show Overloading of Methods in Class.
class Addition:
    def add(self,a,b,c=0):
        print("Sum:",a+b+c)
a=Addition()
a.add(2,3)
a.add(2,3,4)