#Program to write explain different types of Inheritances using classes.
class parent:
    def display_p(self,x):
        print("parent class",x)
class child(parent):
    def display_c(self,x):
        print("child class:",x)
obj=child()
obj.display_p(4)
obj.display_c(6)