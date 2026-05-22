from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Child class
class Cat(Animal):

    def sound(self):
        print("Cat meows")


# Create objects
d = Dog()
c = Cat()

# Call methods
d.sound()
c.sound()
