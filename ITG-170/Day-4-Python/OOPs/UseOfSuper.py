class A:
    def m1(self):
        print('m1 from A')
class B(A):
    def m1(self):
        super().m1()

        print('m1 from B')
    def m2(self):
        print('m2 from B')
class C(A):
    def m1(self):
        super().m1()

        print('m1 from C')
class D(B):
    def m1(self):
        super().m1()

        print('m1 from D')
class E(C):
    def m1(self):
        super().m1()

        print('m1 from E')
class F(D,E):
    def m1(self):
        super().m1()
        print('m1 from F')

a= A()
b= B()
c= C()
d= D()
e= E()
f= F()


f.m1()