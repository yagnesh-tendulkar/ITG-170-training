# Create a class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)


p1 = Person("Abhiram", 22)
p1.greet()
