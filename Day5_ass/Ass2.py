#Write a Java program to create a class called Employee with methods called work() and getSalary().
class Employee:
    """def work(self):
        print("Dhanush is Working")
    def getSalary(self):
        print("Salary is 40000.")
obj=Employee()
obj.work()
obj.getSalary()"""
    def __init__(self,name,hours_per_day,salary_per_hour,working_days):
        self.name=name
        self.hours_per_day=hours_per_day
        self.salary_per_hour=salary_per_hour
        self.working_days=working_days
    def work(self):
        print(self.name,"is working")
    def get_salary(self):
        total_salary=(self.hours_per_day*self.salary_per_hour*self.working_days)
        print("Salary is ",total_salary)
emp=Employee("Dhanush",8,500,21)
emp.work()
emp.get_salary()

