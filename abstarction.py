from abc import ABC,abstractmethod
class abstarct(ABC):
    @abstractmethod
    def ab_fun(self):
        pass
class concrete(abstarct):
    def ab_fun(self):
        print("this is implementation of an abstarct method")
concrete=concrete()
concrete.ab_fun()    
