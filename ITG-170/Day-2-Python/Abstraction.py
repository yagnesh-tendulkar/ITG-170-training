from abc import ABC,abstractmethod


class Super:
    @abstractmethod
    def method(self):
        pass

    def method2(self):
        print('Super class concrete method')
    def method2(self,x):
        print(x)

class Sub(Super):

    def method(self):
        print('Sub class is printing the abstract method')


sub= Sub()
x= Super()
sub.method()
# sub.method2()
sub.method2(5)