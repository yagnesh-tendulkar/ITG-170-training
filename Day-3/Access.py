class Student:

    def __init__(self, name, age, marks):
        self.name = name          # Public
        self._age = age           # Protected
        self.__marks = marks      # Private

    def display(self):
        print("Name (Public):", self.name)
        print("Age (Protected):", self._age)
        print("Marks (Private):", self.__marks)


# Creating object
s = Student("John", 20, 85)
s.display()
print("\nDirect Access:")
print(s.name)        
print(s._age)     

