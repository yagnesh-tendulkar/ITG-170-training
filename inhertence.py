# 1. Program to write explain different types of Inheritances using classes.
class Parent:
    def show(self):
        print("parent class")
class Child(Parent):
    def display(self):
        print("child class")
obj=Child()
obj.show()
obj.display()


#Multiple Inhertence
class Father:
    def fath_prop(self):
        print("Father prop")

class Mother:
    def moth_prop(self):
        print("mother prop")
class Child(Father,Mother):
    pass

obj=Child()
obj.fath_prop()
obj.moth_prop()


#multi-level inh
class Gp:
    def grand(self):
        print("Grand parent class")
class Parent(Gp):
    def parent(self):
        print("Parent class")
class Child(Parent):
    def child(self):
        print("child class")
        
obj=Child()
obj.grand()


#hierachial
class Parent:
    def show(self):
        print("Parent Class")

class Child1(Parent):
    def display1(self):
        print("Child1 Class")

class Child2(Parent):
    def display2(self):
        print("Child2 Class")


obj1 = Child1()
obj2 = Child2()

obj1.show()
obj1.display1()

obj2.show()
obj2.display2()

#hybrid 

class A:
    def method_a(self):
        print("Class A")

class B(A):
    def method_b(self):
        print("Class B")

class C(A):
    def method_c(self):
        print("Class C")

class D(B, C):
    def method_d(self):
        print("Class D")

obj = D()
obj.method_a()
obj.method_b()
obj.method_c()
obj.method_d()

        