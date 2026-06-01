class Employee:
    def __init__(self,salary,name):
        self.salary = salary
        self.name=name
    def work(self):
        print('Employee is working')
    def getSalary(self):
        return self.salary
    def getName(self):
        return self.name

e= Employee(34000,"Smith")
e.work()
print(e.getName(),' is working for ',e.getSalary())


class HRManager(Employee):
    def __init__(self):
        pass
    def work(self):
        print('HR Manager is working')
    def addEmployee(self,employee):
        print(employee.getName(),' is added to work')

hr= HRManager()
hr.work()
hr.addEmployee(e)