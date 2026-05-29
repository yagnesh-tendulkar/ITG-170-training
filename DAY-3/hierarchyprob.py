class Employee:
    def __int_(self):
        pass
class Manager(Employee):
    def details(self,name,address,salary,jobtitle):
        self.name=name
        self.address=address
        self.salary=salary
        self.jobtitle=jobtitle
    def bonus(self):
        return self.salary*0.1
    def performance(self):
        return "Excellent"
    def project(self):
        return "Project A"
class Developer(Employee):
    def details(self,name,address,salary,jobtitle):
        self.name=name
        self.address=address
        self.salary=salary
        self.jobtitle=jobtitle
    def bonus(self):
        return self.salary*0.05
    def performance(self):
        return "Good"
    def project(self):
        return "Project B"
class Programmer(Employee):
    def details(self,name,address,salary,jobtitle):
        self.name=name
        self.address=address
        self.salary=salary
        self.jobtitle=jobtitle
    def bonus(self):
        return self.salary*0.03
    def performance(self):
        return "Average"
    def project(self):
        return "Project C"
def printDetails(self):
    print(f"Name: {self.name}")
    print(f"Address: {self.address}")
    print(f"Salary: {self.salary}")
    print(f"Job Title: {self.jobtitle}")
    print(f"Bonus: {self.bonus()}")
    print(f"Performance: {self.performance()}")
    print(f"Project: {self.project()}")

m1=Manager()
m1.details("Alice","123 Main St",80000,"Manager")
printDetails(m1)

d1=Developer()
d1.details("Bob","456 Elm St",60000,"Developer")
printDetails(d1)

p1=Programmer()
p1.details("Charlie","789 Oak St",40000,"Programmer")
printDetails(p1)