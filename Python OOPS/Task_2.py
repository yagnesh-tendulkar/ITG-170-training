class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def work(self):
        print(self.name,"is working")
    def getSalary(self):
        print(self.salary)
e1=Employee("Bikash",50000)
e1.work()
e1.getSalary()