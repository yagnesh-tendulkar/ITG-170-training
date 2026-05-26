from abc import ABC,abstractmethod
class appliance(ABC):
    @abstractmethod
    def Switch_on(self):
        pass
class Fan(appliance):
    def Switch_on(self):
        print("The fan was turned on")
class Washingmachine(appliance):
    def Switch_on(self):
        print("The washing machine was running")
f=Fan()
f.Switch_on()
w=Washingmachine()
w.Switch_on()



from abc import ABC,abstractmethod
class Mobile:
    @abstractmethod
    def features(self):
        pass
class samsung(Mobile):
    def features(self):
        print("This samsung has more extra features than other android")
class apple(Mobile):
    def features(self):
        print("This has most unique features")
a=apple()
a.features()
s=samsung()
s.features()
