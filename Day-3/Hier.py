class Parent:
    def display(self):
        print("This is parent class")

class Child1(Parent):
    def show1(self):
        print("This is child1")

class Child2(Parent):
    def show2(self):
        print("This is child2")

c1 = Child1()
c2 = Child2()

c1.display()
c1.show1()

c2.display()
c2.show2()
