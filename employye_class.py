class employee:
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def get_details(self):
        print(self.name,self.dept,self.salary) 
    def get_salary(self):
        print(" salary is "+str(self.salary))       
    def work(self):
        print(" work is done") 
class HrManager(employee):
    def work(self):
        print("Acurire new employee")
    def addEmployee(self):
        print("new employee is added")               
emp1= employee("rudra","development",120000)
emp2= employee("sibuni","development",343000)
hr=HrManager("ram","hrmanagement",50000)
emp1.get_details()
emp2.get_details()     
emp1.get_salary()
emp2.get_salary()
hr.work() 
