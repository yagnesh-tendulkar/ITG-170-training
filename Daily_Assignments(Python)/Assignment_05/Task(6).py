# Program to Show Method Overriding in Python
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

a = Animal()
d = Dog()

a.sound()
d.sound()