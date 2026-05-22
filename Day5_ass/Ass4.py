#Program to Show Polymorphism in Class
class Dog:
    def sound(self):
        print("Dog Barks.")
class Cat:
    def sound(self):
        print("Cat meows")
d=Dog()
c=Cat()
d.sound()
c.sound()