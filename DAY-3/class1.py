#Write a program to create a class called Employee with methods called
#work() and getSalary().
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):#print the employee's name followed by " is working."
        print(f"{self.name} is working.")
    def getSalary(self):#print the employee's salary
        return self.salary
e1=Employee("Alice",50000)
e1.work()
print(f"{e1.name}'s salary is {e1.getSalary()}.")   