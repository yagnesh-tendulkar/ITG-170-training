class Bird:

    def sound(self):
        print("Bird makes a sound")


class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


                 
def make_sound(animal):
    animal.sound()


# Creating objects
b = Bird()
d = Dog()
c = Cat()

# Calling same method for different objects
make_sound(b)
make_sound(d)
make_sound(c)
