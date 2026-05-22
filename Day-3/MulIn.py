class Father:
    def skills(self):
        print("Father: Gardening")

class Mother:
    def talents(self):
        print("Mother: Painting")

class Child(Father, Mother):
    pass

c = Child()

c.skills()
c.talents()
