
class Animal:

    def sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)
