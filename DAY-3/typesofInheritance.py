#typesofInheritance
# Parent Class
class Animal:
    
    def sound(self):
        print("Animals make sounds")


# 1. Single Inheritance
class Dog(Animal):
    
    def bark(self):
        print("Dog barks")


# 2. Multiple Inheritance
class Father:
    
    def skill1(self):
        print("Father: Driving")


class Mother:
    
    def skill2(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    
    def skill3(self):
        print("Child: Coding")


# 3. Multilevel Inheritance
class Grandparent:
    
    def house(self):
        print("Grandparent's house")


class Parent(Grandparent):
    
    def car(self):
        print("Parent's car")


class Son(Parent):
    
    def bike(self):
        print("Son's bike")


# 4. Hierarchical Inheritance
class Bird:
    
    def fly(self):
        print("Bird can fly")


class Parrot(Bird):
    
    def speak(self):
        print("Parrot can speak")


class Eagle(Bird):
    
    def hunt(self):
        print("Eagle hunts")


# Objects and Method Calls

print("Single Inheritance")
d = Dog()
d.sound()
d.bark()

print("\nMultiple Inheritance")
c = Child()
c.skill1()
c.skill2()
c.skill3()

print("\nMultilevel Inheritance")
s = Son()
s.house()
s.car()
s.bike()

print("\nHierarchical Inheritance")
p = Parrot()
p.fly()
p.speak()

e = Eagle()
e.fly()
e.hunt()