class A:
    def show(self):
        print("Sound")
class B(A):
    def show(self):
        print("Bark")
class C(A):
    def show(self):
        print("Meow")
a=C()
a.show()
a.show()
a.show()