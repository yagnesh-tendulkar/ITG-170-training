from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self):
        pass


class Developer(Employee):
    def work(self):
        print("Developer is working")

class Administrator(Employee):
    def work(self):
        print("Administrator is working")

# e= Employee() we cannot create object for this because iyt is an abstract class

d= Developer()
d.work()
a=Administrator()
a.work()