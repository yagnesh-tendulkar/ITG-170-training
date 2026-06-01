class InvalidCard(BaseException):
    def __init__(self,message):
        super().__init__(message)

try:
    card=int(input("Enter your card cvv: "))
    if len(str(card))!=3:
        raise InvalidCard('Your card is invalid')
    else:
        print('Payment successful')
except (InvalidCard,Exception) as e:
    if isinstance(e,InvalidCard):
        print(e)
    else:
        print('Please check your cvv once again!')
