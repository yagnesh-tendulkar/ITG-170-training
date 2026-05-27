class InvalidAge(Exception):
    def __init__(self,message):
        super().__init__(message)

class Voter:
    def check_age(self,age):
        self.age=age
        if age<18:
            raise InvalidAge("Age is less than 18")
        else:
            print("Eligible")


v=Voter()
try:
    v.check_age(15)
except InvalidAge as e :
    print(e)
    