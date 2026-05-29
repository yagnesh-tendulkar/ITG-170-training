#privateaccess
class Student:
    def __init__(self,id,name):#private access
        self.__id = id
        self._name=name

    def attend(self, name):
        print(f"Student with ID {self.__id} is attending class.")
        print("Student Name:", self._name)
    def get_id(self):
        return self.__id
s=Student(12345, "Alice")
s.attend("Alice")
#print(type(s.__id))#This will raise an AttributeError because __id is a private attribute and cannot be accessed outside the class.
print(s.get_id())
print(s.__dict__)