"""Write a Java program that creates a class hierarchy for employees of a
company. The base class should be Employee, with subclasses Manager,
Developer, and Programmer. Each subclass should have properties such as
name, address, salary, and job title.Implement methods for calculating
bonuses, generating performance reports, and managing projects."""
class Employee:

    def bonus(self):
        print("Bonus calculated")


class Manager(Employee):

    def manage(self):
        print("Managing Team")


class Developer(Employee):

    def code(self):
        print("Writing Code")


m = Manager()
d = Developer()

m.bonus()
m.manage()

d.bonus()
d.code()