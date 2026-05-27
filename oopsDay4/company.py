class Employee:
    def __init__(self,name,address,salary,jobtitle):
        self.name=name
        self.address=address
        self.salary=salary
        self.jobtitle=jobtitle

    def calculate_bonus(self):
        return self.salary*0.1
    
    def perf_report(self):
        return f"Performance report for {self.name} , {self.jobtitle}"
    
    def manage_report(self):
        return f"{self.name} is involved in company project"
    
class Manager(Employee):
    def __init__(self,name,address,salary):
        super().__init__(name,address,salary,jobtitle="Manager")

    def calculate_bonus(self):
        return self.salary*0.2
    
    def perf_report(self):
        return f"{self.name} is managing project efffectively"
    
    def manage_report(self):
        return f"{self.name} is leading team effectively"
    
class Devloper(Employee):
    def __init__(self,name,address,salary,programming_lang):
        super().__init__(name,address,salary,jobtitle="Devloper")
        self.programming_lang=programming_lang

    def calculate_bonus(self):
        return self.salary*0.15
    
    def perf_report(self):
        return f"{self.name} is a developer and doing project in {self.programming_lang} tech stack"
    
    def manage_report(self):
        return f"{self.name} implements logic and manage version control"
    
class Programmer(Employee):
    def __init__(self, name, address, salary, skill_level):
        super().__init__(name,address, salary, jobtitle="Programmer")
        self.skill_level=skill_level

    def calculate_bonus(self):
        return self.salary*0.12
    
    def perf_report(self):
        return f"{self.name} is a {self.skill_level} level programmer"
    
    def manage_report(self):
        return f"{self.name} writes and test code"
    
employees = [
    Manager("Rishabh patel","vizag",80000),
    Devloper("santosh","odissa",60000,"java"),
    Devloper("rudra","odissa",50000,"Expert")
]

for emp in employees:
    print(f"Name : {emp.name}")
    print(f"Address : {emp.address}")
    print(f"salary : {emp.salary}")
    print(f"Job-title : {emp.jobtitle}")
    print(f"Bonus : {emp.calculate_bonus()}")
    print(emp.perf_report())
    print(emp.manage_report())
    print("="*30)
