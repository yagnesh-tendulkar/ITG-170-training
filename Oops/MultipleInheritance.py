class Mother:
    mother=""
    def func1(self):
        print(self.mother)
class Father:
    father=""
    def func2(self):
        print(self.father)
class son(Father,Mother):
    def parents(self):
        print("Father :", self.father)
        print("Mother :", self.mother)
sn=son()
sn.father="Ram"
sn.mother="Sitha"
sn.func2()
sn.func1()
sn.parents()
