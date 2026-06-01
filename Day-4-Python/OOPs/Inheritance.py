class A:
    def m1(self):
        print('m1 from A')
class B(A):
    def m1(self):
        print('m1 from B')
    def m2(self):
        print('m2 from B')
class C(A):
    def m1(self):
        print('m1 from C')
class D(B):
    def m1(self):
        print('m1 from D')
class E(C):
    def m1(self):
        print('m1 from E')
class F(D,E):
    def m1(self):
        print('m1 from F')

a= A()
b= B()
c= C()
d= D()
e= E()
f= F()

a.m1()
b.m1()
c.m1()
d.m1()
e.m1()
f.m1()
b.m2()
d.m2()
f.m2()