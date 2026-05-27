class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive Fast")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Moving")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Flying")
car1 = Car("Ford", "FX")        
boat1 = Boat("Titanic", "TY") 
plane1 = Plane("Emirates", "EZ")     
for x in (car1, boat1, plane1):
  x.move()