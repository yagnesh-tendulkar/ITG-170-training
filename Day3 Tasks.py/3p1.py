class School:
    def school_name(self):
        return "Academy"
class Father(School):
    def driving_skill(self):
        return "Drives a car"
class Mother(School):
    def cooking_skill(self):
        return "Cooks meals"
class Grandparent:
    def gold_asset(self):
        return "Family Gold"
class Parent(Grandparent):
    def house_asset(self):
        return "Family House"
class Child(Father, Mother, Parent):
    def child_skill(self):
        return "Plays games"
class Sibling(Father):
    def sibling_skill(self):
        return "Paints pictures"
obj = Child()
sibling_obj = Sibling()
print(obj.house_asset())
print(obj.driving_skill())
print(obj.cooking_skill())
print(obj.school_name())
print(sibling_obj.school_name())
