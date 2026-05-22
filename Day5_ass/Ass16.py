#Program to Show Usage of Access Modifier
class Test:

    public = "Public"

    _protected = "Protected"

    __private = "Private"


    def display(self):

        print(self.public)
        print(self._protected)
        print(self.__private)


obj = Test()

obj.display()