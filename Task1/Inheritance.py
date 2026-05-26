class Animal:             # Grandparent class
    def sound(self):
        print("Animal makes generic sound")

class Dog(Animal):         # Parent class
    def sound(self):       # overriding Animal's sound()
        print("Dog barks")

class Puppy(Dog):          # Child class
    def sound(self):       # overriding Dog's sound()
        print("Puppy whines")

# Create object of Puppy
p = Puppy()

p.sound()  # This will call Puppy’s method