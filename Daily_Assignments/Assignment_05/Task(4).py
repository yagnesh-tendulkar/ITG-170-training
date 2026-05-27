# Program to Show Polymorphism in Class
class Bird:
    def sound(self):
        print("Bird makes a sound")

class Sparrow(Bird):
    def sound(self):
        print("Sparrow chirps")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

def make_sound(bird):
    bird.sound()

b1 = Sparrow()
b2 = Crow()

make_sound(b1)
make_sound(b2)