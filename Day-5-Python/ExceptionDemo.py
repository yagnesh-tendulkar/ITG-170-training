class InvalidAge(Exception):
    def __init__(self,message):
        super().__init__(message)


try:
    age = int(input("Enter your age: "))

    if age<18:
        gap= 18-age
        raise InvalidAge(f'Please come after {gap} year(s)')
    else:
        print('You are eligible for voting!!')
except (InvalidAge , Exception) as e:
    if isinstance(e,InvalidAge):
        print(e)
    else:
        print('Please enter your age in numbers')