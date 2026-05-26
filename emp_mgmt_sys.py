# inhertinace concept

class Emp:
    def __init__(self,nam,id):
        self.name = nam
        self.id = id
    def show_details(self):
        print(f"The emp named {self.name} is having an id {self.id}")
class Developer(Emp):
    def __init__(self,name,id,language):
        super().__init__(name,id)
        self.language = language
    def work(self):
        print(f"{self.name} is working on {self.language}")
dev = Developer("alice",101,"c#")
dev.work()
emp = Emp("bob",102)
emp.show_details()  




    
