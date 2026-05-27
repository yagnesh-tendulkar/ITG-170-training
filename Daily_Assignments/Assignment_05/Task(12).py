# Program to explain Dynamic Binding in Python

# Parent class
class Animal:

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

# Function demonstrating dynamic binding
def make_sound(animal):
    animal.sound()

a = Animal()
d = Dog()
c = Cat()

make_sound(a)
make_sound(d)
make_sound(c)