from abc import ABC, abstractmethod

class Vechicle:

    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def stopEngine(self):
        pass

class Bike(Vechicle):

    def startEngine(self):
        print("Bike engine started.")

    def stopEngine(self):
        print("Bike engine stopped.")

    
class Car(Vechicle):

    def startEngine(self):
        print("car engine started")

    def stopEngine(self):
        print("Car engine stopped")


vechicle = [Bike(),Car()]

for v in vechicle:
    v.startEngine()
    v.stopEngine()
    
