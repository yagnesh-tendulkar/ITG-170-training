class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()

d.sound()   # inherited method
d.bark()
