class Animals:
    def sound(self):
        print("Animal makes sound")

class Dog(Animals):
    def sound(self):
        print("Dog makes sound bark- bark")
    
class Cat(Animals):
    def sound(self):
        print("cat makes sound meow - meow")

animals = [Animals(),Dog(),Cat()]
for animal in animals:
    animal.sound()
