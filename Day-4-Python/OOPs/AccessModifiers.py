class Student:
    def __init__(self,name,age,fee):
        self.name=name #public
        self._age=age  #protected
        self.__fee=fee #private

s= Student('Alex',23,25000)

print(s.name)
print(s._age)
print(s.__fee)