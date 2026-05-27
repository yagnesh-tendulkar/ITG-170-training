print("code for single inheritance")

class Animal:
    def animal_sound(self):
        print("Animal makes sound")
    

class Cow(Animal):
    def cow_sound(self):
        print("Cow makes sound mooo-mooo")

print("Single Inheritance")

c=Cow()
c.cow_sound()
c.animal_sound()