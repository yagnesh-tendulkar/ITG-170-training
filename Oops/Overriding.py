class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def start(self):  # overriding
        print("Car started")

v = Vehicle()
v.start()

c = Car()
c.start()


class Employee:
    def salary(self):
        print("Salary of emp : 30000")
class manager(Employee):
    def salary(self):
        print("Salary of manager : 30000+bonus")
m=manager()
m.salary()
e=Employee()
e.salary()