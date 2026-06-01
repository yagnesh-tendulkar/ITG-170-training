from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return 'Car is started!!!'

class Bike(Vehicle):
    def start(self):
        return 'Bike is started!!!'

class Travel:
    def go(self,vehicle):
        print( vehicle.start() )

t= Travel()
t.go(Bike())