class Animal:
    
    def __init__(self, name="Bageera"):
        self.name = name
    
    def printName(self):
        print(f"{self.name} is an animal.")


class Chettah(Animal):
    
    def __init__(self, name, ability):
        
        # Taking name from parent class
        super().__init__(name)
        
        # Adding ability in child class
        self.ability = ability
    
    def printAbility(self):
        print(f"{self.name} can {self.ability}.")


c1 = Chettah("Cheetah", "run fast")

c1.printName()
c1.printAbility()