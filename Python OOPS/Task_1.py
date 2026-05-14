#Single Inheritance
class Animal:
    def set_name(self,name):
        self.name=name
    def show(self):
        print(self.name)
class Cat(Animal):
    pass
s1=Cat()
s1.set_name("Meow")
s1.show()

#Multi-Level
class Dog(Animal):
    def sound(self):
        print("Bark")
class Fish(Dog):
    def sound2(self):
        print("swim")
s2=Fish()
s2.sound2()
s2.sound()

#Multiple
class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("Cooking")
class Child(Father, Mother):
    pass
c=Child()
c.skill1()
c.skill2()

#Hireachical
class Grandfather:
    def property(self):
        print("House")
class Father(Grandfather):
    pass
class Son(Grandfather):
    pass
f=Father()
s3=Son()
f.property()
s3.property()