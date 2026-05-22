#Program to Show Overriding of Methods in Classes
class Parent:

    def show(self):
        print("Parent Method")


class Child(Parent):

    def show(self):
        print("Child Method")


obj = Child()

obj.show()