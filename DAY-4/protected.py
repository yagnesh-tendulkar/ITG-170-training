#protectedaccess

class Animal:
    def greet(self,_name):#protected access
        print(f"Hello, {_name}!")
class Dog(Animal):
    def greet(self,name):
        super().greet(name)
d=Dog()
d.greet("Buddy")
