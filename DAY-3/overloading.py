#method overloading/static binding/compile time polymorphism
class Employee:
    def work(self):
        print("Employee is working.")
    def work(self,dept):
        print(f"Employee is working in {dept} department.")
    def work(self,dept,shift):
        print(f"Employee is working in {dept} department during {shift} shift.")
    def work(self,dept,shift,location):
        print(f"Employee is working in {dept} department during {shift} shift at {location} location.")
e1=Employee()
e1.work("IT","Morning")

#create an anothreer class called Calculator with a method called add that takes two parameters and returns their sum.
class Calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c

c1=Calculator()
#print(c1.add(2,3))
print(c1.add(2,3,4))