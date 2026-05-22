
class Employee:
    def __init__(self,name,salary):
    	self.name=name
    	self.salary=salary
    
    def work(self):
    	print(self.name,"is working")
    	
    def getSalary(self):
    	print("salary:",self.salary)
    	
employee1 = Employee("sumathi", 1000000)

employee1.work()
employee1.getSalary()
    
    
