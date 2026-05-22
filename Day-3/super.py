class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)  
        self.breed = breed

    def sound(self):
        super().sound()       
        print("Dog barks")

d = Dog("Buddy", "Golden Retriever")

print("Name:", d.name)
print("Breed:", d.breed)
d.sound()
