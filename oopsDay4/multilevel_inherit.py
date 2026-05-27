class Grandfather:
    def gen1(self):
        print("This is generation 1 grandfather")

class Father(Grandfather):
    def gen2(self):
        print("this is generation 2 father")

class Son(Father):
    def gen3(self):
        print("This is the young generation 3 ")

print("Implementation of the multilevel Inheritance")

g=Son()
g.gen3()
g.gen2()
g.gen1()