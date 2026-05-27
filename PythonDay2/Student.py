class Student:
    def __init__(self,name,age,pin):
        self.name=name
        self._age=age
        self.__pin=pin

    def diplay_public(self):
        print("This is Public member :")
        print("Name :",self.name)
    
    def display_protected(self):
        print("This is Protected member :")
        print("Age :",self._age)

    def display_private(self):
        print("This is Private member :")
        print("Pin :",self.__pin)

    
x1=Student("Rishabh",21,7878)
x1.diplay_public()
x1.display_private()
x1.display_protected()

print("Direct Access\n")
print("public",x1.name)
print("protected",x1._age)

print("private",x1.__pin)


