class Base:
    def base_method(self):
        print("This is base class called")

class A(Base):
    def A_method(self):
        print("this is derived class A from base")

class B(Base):
    def B_method(self):
        print("This is derived class B from Base")

class C(A,B):
    def C_method(self):
        print("This is child class derived from A and B")


child_a = B()
child_a.base_method()
child_b = A()
child_b.base_method()
child_c = C()
child_c.A_method()
child_c.B_method()