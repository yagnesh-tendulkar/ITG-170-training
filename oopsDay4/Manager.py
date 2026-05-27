class Manager:
    def work(self):
        print("work for 8 hours is mandatory")

class HRManager(Manager):
    def work(self):
        super().work()
        print("work for 10 hours is mandatory")

    def addEmployee(self,name):
        self.name=name
        print(f"New Employee {self.name} Added .")



mang = HRManager()
mang.work()
mang.addEmployee("Rishabh")