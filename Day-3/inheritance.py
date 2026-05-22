#single inheritance

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")



#multilevel Inheritance

class Puppy(Dog):
    def weep(self):
        print("Puppy is weeping")



#hierarchical Inheritance

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")



#multiple Inheritance

class Father:
    def skills(self):
        print("Father: Gardening")


class Mother:
    def talents(self):
        print("Mother: Painting")


class Child(Father, Mother):
    def show(self):
        print("Child inherits from both Father and Mother")


print("Single Inheritance")
d = Dog()
d.eat()
d.bark()

print("\nMultilevel Inheritance")
p = Puppy()
p.eat()
p.bark()
p.weep()

print("\nHierarchical Inheritance")
c = Cat()
c.eat()
c.meow()

print("\nMultiple Inheritance")
ch = Child()
ch.skills()
ch.talents()
ch.show()


