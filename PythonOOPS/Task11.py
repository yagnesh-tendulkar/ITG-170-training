class Employee:
    def __init__(self,name,address,salary,jobtitle):
        self.name=name
        self.address=address
        self.salary=salary
        self.jobtitle=jobtitle
class Manager(Employee):
    def __init__(self,name,address,salary,jobtitle):
        