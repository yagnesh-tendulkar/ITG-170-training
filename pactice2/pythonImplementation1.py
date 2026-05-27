class Dog:
    species="dog-species-canine"

    def __init__(self,name,age):
        self.name=name
        self.age=age

dog=Dog("chintu",10)
print("Dog name is : ",dog.name)
print("Dog belong to this species : ",dog.species)
print("Dog age is : ",dog.age)