from pyexpat import model


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"

    def start(self):
        print('Vehicle is running...')

class Car(Vehicle):
    def start(self):
        print('Car is running...')
    def stop(self):
        print('Car is stopped...')


class Truck(Vehicle):
    def start(self):
        print('Truck is running...')


class Motorcycle(Vehicle):
    def start(self):
        print('Motorcycle is running...')



v= Vehicle('genericVehicle','model',2000)
c= Car('Hyundai','i20',2015)
t= Truck('Tata','407',1990)
m= Motorcycle('KTM','duke',2000)

v.start()
c.start()
t.start()
m.start()
c.stop()