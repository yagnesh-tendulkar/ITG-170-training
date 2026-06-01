from abc import ABC,abstractmethod

class interface(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass
class Concrete(interface):
    def m1(self):
        print('m1')
    def m2(self):
        print('m2')
    def m3(self):
        print('m3')

c= Concrete()
c.m1()
c.m2()
c.m3()