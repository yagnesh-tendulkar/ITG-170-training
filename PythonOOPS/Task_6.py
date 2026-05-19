class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
a=Animal()
d=Dog()
c=Cat()
a.sound()
c.sound()
d.sound()
