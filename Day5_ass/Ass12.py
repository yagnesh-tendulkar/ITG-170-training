#Write a program to explain Dynamic Binding.
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog Barks")


a = Dog()

a.sound()