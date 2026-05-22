# Write a  program to create a class called Employee with methods called 
# work() and getSalary().


class Employee:
    def work(self):
        print("work")
    def getsalary(self):
        print("salary")
obj=Employee()
obj.work()


# Create a subclass called HRManager that overrides the work() method and
# adds a new method called addEmployee().


class Employee:
    def work(self):
        print("work")
    def getsalary(self):
        print("salary")

# Program to Show Polymorphism in Class

class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

class Cow:
    def sound(self):
        print("Cow moos")

for animal in (Dog(), Cat(), Cow()):
    animal.sound()