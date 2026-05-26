class parent:
    def func1(self):
        print("This is parent class")
class child(parent):
    def func2(self):
        print("This is child class")
class child2(child):
    def func3(self):
        print("This is child2 class")
ch=child2()
ch.func1()
ch.func3()
