class Animal:
    def sound(self, a=None, b=None):
        if a is not None and b is not None:
            print(a, b)
        elif a is not None:
            print(a)
        else:
            print("Animal Sound")
obj = Animal()
obj.sound()
obj.sound("Dog")
obj.sound("Cat", "Cow")