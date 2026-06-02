#Program1 : INHERITENCE
#Single Inheritence
class Parent:
    def display_parent(self):
        print("This is Parent class")


class Child(Parent):
    def display_child(self):
        print("This is Child class")


obj = Child()

obj.display_parent()
obj.display_child()

# Multiple Inheritance
class Father:
    def father_method(self):
        print("Father class method")


class Mother:
    def mother_method(self):
        print("Mother class method")


class Child(Father, Mother):
    def child_method(self):
        print("Child class method")


obj = Child()

obj.father_method()
obj.mother_method()
obj.child_method()

# Multilevel Inheritance
class Grandfather:
    def grandparent_method(self):
        print("Grandfather class")


class Father(Grandfather):
    def parent_method(self):
        print("Father class")


class Child(Father):
    def child_method(self):
        print("Child class")


obj = Child()

obj.grandparent_method()
obj.parent_method()
obj.child_method()

# Hierarchical Inheritance
class Parent:
    def parent_method(self):
        print("Parent class method")


class Child1(Parent):
    def child1_method(self):
        print("Child1 class method")


class Child2(Parent):
    def child2_method(self):
        print("Child2 class method")


obj1 = Child1()
obj2 = Child2()

obj1.parent_method()
obj1.child1_method()

obj2.parent_method()
obj2.child2_method()

# Hybrid Inheritance
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

# Program 2 : Employee Class
class Employee:

    def work(self):
        print("Employee is working")

    def getSalary(self):
        print("Salary is 50000")


emp = Employee()

emp.work()
emp.getSalary()

# Program 3 : HR Manager Subclass
class Employee:

    def work(self):
        print("Employee is working")

    def getSalary(self):
        print("Salary is 50000")

class HRManager(Employee):

    def work(self):
        print("HR Manager is managing employees")

    def addEmployee(self):
        print("New employee added")


hr = HRManager()

hr.work()
hr.getSalary()
hr.addEmployee()

# Program 4 : Polymorphism in class
class Dog:

    def sound(self):
        print("Dog barks")


class Cat:

    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)

# Program 5: Method Overloading
class Addition:

    def add(self, a, b, c=0):
        print("Sum =", a + b + c)

obj = Addition()

obj.add(10, 20)

obj.add(10, 20, 30)

# Program 6: Method Overriding
class Parent:

    def show(self):
        print("This is Parent class method")


class Child(Parent):

    def show(self):
        print("This is Child class method")

obj = Child()

obj.show()

#Program 7: Person Class
class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

p1 = Person("John", "David")

print("First Name:", p1.getFirstName())
print("Last Name:", p1.getLastName())

# Program 8 : Employee subclass
class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

class Employee(Person):

    def __init__(self, firstName, lastName, employeeId, jobTitle):
        super().__init__(firstName, lastName)
        self.employeeId = employeeId
        self.jobTitle = jobTitle

    def getEmployeeId(self):
        return self.employeeId

    def getLastName(self):
        return self.lastName + " - " + self.jobTitle

emp = Employee("John", "David", 101, "Software Engineer")

print("First Name:", emp.getFirstName())
print("Last Name:", emp.getLastName())
print("Employee ID:", emp.getEmployeeId())

#Program 9 : Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):

    def start(self):
        print("Car starts with key")

class Bike(Vehicle):

    def start(self):
        print("Bike starts with button")

c = Car()
b = Bike()

c.start()
b.start()

# Program 10 : Creating Interface
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

d = Dog()
c = Cat()

d.sound()
c.sound()

# Program 11 : Employee Class Hierarchy
class Employee:

    def __init__(self, name, address, salary, job_title):
        self.name = name
        self.address = address
        self.salary = salary
        self.job_title = job_title

    def calculate_bonus(self):
        return self.salary * 0.10

    def performance_report(self):
        print(f"{self.name} is performing well as a {self.job_title}")

    def manage_project(self):
        print(f"{self.name} is managing a project")

class Manager(Employee):

    def calculate_bonus(self):
        return self.salary * 0.20

    def manage_project(self):
        print(f"Manager {self.name} is managing company projects")

class Developer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.15

    def performance_report(self):
        print(f"Developer {self.name} completed coding tasks successfully")

class Programmer(Employee):

    def calculate_bonus(self):
        return self.salary * 0.12

    def performance_report(self):
        print(f"Programmer {self.name} fixed bugs efficiently")

m = Manager("John", "Hyderabad", 80000, "Manager")
d = Developer("Alice", "Chennai", 60000, "Developer")
p = Programmer("David", "Bangalore", 50000, "Programmer")

print("Manager Bonus:", m.calculate_bonus())
m.performance_report()
m.manage_project()

print()

print("Developer Bonus:", d.calculate_bonus())
d.performance_report()
d.manage_project()

print()

print("Programmer Bonus:", p.calculate_bonus())
p.performance_report()
p.manage_project()

#Program 12 : Dynamic Binding
class Animal:

    def sound(self):
        print("Animal makes sound")

class Dog(Animal):

    def sound(self):
        print("Dog barks")

class Cat(Animal):

    def sound(self):
        print("Cat meows")

def make_sound(animal):
    animal.sound()

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)

# Program 13 : Super keyword in class
class Parent:

    def __init__(self):
        print("Parent Constructor")

    def show(self):
        print("Parent class method")


class Child(Parent):

    def __init__(self):
       
        super().__init__()
        print("Child Constructor")

    def display(self):
       
        super().show()
        print("Child class method")


obj = Child()

obj.display()

#Program 14 : This Keyword in class
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

s1 = Student("John", 21)

s1.display()

#Program 15 : Static Keyword in class
class Student:

    college = "ABC College"

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)
        print("College:", Student.college)

    @staticmethod
    def show():
        print("This is a static method")

s1 = Student("John")
s2 = Student("David")

s1.display()
print()

s2.display()
print()

Student.show()

# Program 16 : Access Modifier
class Student:
    def __init__(self):

        self.name = "John"

        self._course = "Python"

        self.__marks = 95

    def display(self):
        print("Name:", self.name)
        print("Course:", self._course)
        print("Marks:", self.__marks)


s = Student()

print("Public Variable:", s.name)

print("Protected Variable:", s._course)

s.display()