class person:
    def __init__(self,First_name,Last_name):
        self.First_name=First_name
        self.Last_name=Last_name
    def get_first_name(self):
        return self.First_name
    def get_last_name(self):
        return self.Last_name
class Employee(person):
    def __init__(self,First_name,Last_name,Emp_id,Job_title):
        super().__init__(First_name,Last_name)
        self.Emp_id=Emp_id
        self.Job_title=Job_title
    def get_last_name(self):
        return self.Last_name
    def get_Emp_id(self):
        return self.Emp_id
    def get_JOb_title(self):
        return self.Job_title
Emp=Employee("Abhi","Katta",6410,"Software Trainee")
print(Emp.get_first_name())
print(Emp.get_last_name())
print(Emp.get_Emp_id())
print(Emp.get_JOb_title())
