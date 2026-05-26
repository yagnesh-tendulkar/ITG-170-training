class calculation:
    def mul(self,a=1,b=1,*args):
        result=a*b
        for i in args:
            result*=i
        return result
cal=calculation()
print(cal.mul(2))
print(cal.mul(4,5,6,7))
#This is method overriding
class Animal:
    def sound(self):
        print("Some sound")
class Dog:
    def sound(self):
        print("Bark")
class Cat:
    def sound(self):
        print("Meow")
Animals=[Animal(),Dog(),Cat()]
for i in Animals:
    i.sound()
