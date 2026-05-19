class Employee:
    def __init__(self,name,gmail,password,role,salary):
        self.name=name
        self.gmail=gmail
        self.password=password
        self.role=role
        self.salary=salary
class HR(Employee):
    def __init__(self,name,gmail,password,salary):
        super().__init__(self,name,gmail,password,salary)
        self.role="HR"
class Trainer(Employee):
    def __init__(self,name,gmail,password,salary):
        super().__init__(self,name,gmail,password,salary)
        self.role="Trainer"
class Trainee(Employee):
    def __init__(self,name,gmail,password,salary):
        super().__init__(self,name,gmail,password,salary)
        self.role="Trainee"
