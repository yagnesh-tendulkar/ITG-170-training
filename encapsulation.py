class person:
    def __init__(self,fname,lname):
        self.__Fname=fname
        self.__Lname=lname

    def getFname(self):
        return self.__Fname
    def getLname(self):
        return self.__Lname
class employye(person):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.__id=c  
    def getEmploeeId(self):
        return self.__id
    def getLname(self):
        return "employye last name is {}".format(super().getLname())      
p1=person("rudra","prasad")
emp=employye("rudra","prasad",101)

print(p1.getFname())
print(p1.getLname()) 
print(emp.getEmploeeId())
print(emp.getLname())

        