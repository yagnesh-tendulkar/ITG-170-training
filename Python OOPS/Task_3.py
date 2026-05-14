class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(self.name,"is working")
    def getSalary(self):
        print(self.salary)

class HRManager(Employee):
    def work(self):
        print(self.name," have completed working")
    def addEmployee(self,emp_name):
        print(emp_name," have been added")
h1=HRManager("Bikash",50000)
h1.work()
h1.getSalary()
h1.addEmployee("Rahul")
