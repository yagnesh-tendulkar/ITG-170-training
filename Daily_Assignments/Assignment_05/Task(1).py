# 1. Single Inheritance
class Parent:
    def display_parent(self):
        print("This is Parent class")

class Child(Parent):
    def display_child(self):
        print("This is Child class")

print("Single Inheritance:")
obj1 = Child()
obj1.display_parent()
obj1.display_child()


# 2. Multiple Inheritance
class Father:
    def father_method(self):
        print("Father class method")

class Mother:
    def mother_method(self):
        print("Mother class method")

class Son(Father, Mother):
    def son_method(self):
        print("Son class method")

print("\nMultiple Inheritance:")
obj2 = Son()
obj2.father_method()
obj2.mother_method()
obj2.son_method()


# 3. Multilevel Inheritance
class Grandparent:
    def grandparent_method(self):
        print("Grandparent class method")

class Parent1(Grandparent):
    def parent_method(self):
        print("Parent class method")

class Child1(Parent1):
    def child_method(self):
        print("Child class method")

print("\nMultilevel Inheritance:")
obj3 = Child1()
obj3.grandparent_method()
obj3.parent_method()
obj3.child_method()


# 4. Hierarchical Inheritance
class Animal:
    def animal_method(self):
        print("Animal class method")

class Dog(Animal):
    def dog_method(self):
        print("Dog class method")

class Cat(Animal):
    def cat_method(self):
        print("Cat class method")

print("\nHierarchical Inheritance:")
obj4 = Dog()
obj4.animal_method()
obj4.dog_method()

obj5 = Cat()
obj5.animal_method()
obj5.cat_method()


# 5. Hybrid Inheritance
class A:
    def method_a(self):
        print("Class A method")

class B(A):
    def method_b(self):
        print("Class B method")

class C(A):
    def method_c(self):
        print("Class C method")

class D(B, C):
    def method_d(self):
        print("Class D method")

print("\nHybrid Inheritance:")
obj6 = D()
obj6.method_a()
obj6.method_b()
obj6.method_c()
obj6.method_d()