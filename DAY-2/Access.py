class Demo:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def show(self):
        print(self.a)
        print(self._b)
        print(self.__c)

class Child(Demo):
    def display(self):
        print(self.a)
        print(self._b)

obj = Child()

obj.display()
obj.show()

print(obj.a)
print(obj._b)
