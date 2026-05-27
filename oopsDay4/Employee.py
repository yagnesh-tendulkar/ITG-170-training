class Employee:

    def work(self,hrs):
        self.hrs=hrs
        print(f"you have worked {hrs} hours.")

    def getSalary(self):
        print("your salary is 1000")


emp = Employee()
emp.work(8)
emp.getSalary()