import math
import random


class InvalidPassword(Exception):
    def __init__(self,message):
        super().__init__(message)

class InsufficientBalance(Exception):
    def __init__(self,message):
        super().__init__(message)

class InvalidChoiceError(Exception):
    def __init__(self,message):
        super().__init__(message)


class Account:
    def __init__(self, name, age, password,amount):
        if len(password) < 6:
            raise InvalidPassword('Password must contain at least 6 characters')
        self.name = name
        self.age = age
        self.password = password
        self.amount = amount
try:
    name= input('Enter your name: ')
    age=  int(input('Enter your age: '))
    password = input('Enter your password: ')
    amount=int(input('Enter your amount: '))
    account= Account(name,age,password,amount)
    print(f'Your account created with a/c number:  {random.randint(1,999999999999)}')
    flag=True
    while(flag):
        print('1.Deposit\n2.Withdraw\n3.Exit')
        option= int(input('Enter your option: '))
        if option==1:
            amount=int(input('Enter your amount: '))
            pw=input('Enter your password: ')
            if pw==account.password:
                account.amount+=amount
                print(f'Your amount is deposited to: {account.amount}')
            else:
                raise InvalidPassword('Your password is not correct, please come again!!')
        elif option==2:
            amount=int(input('Enter your amount: '))
            if amount>account.amount:
                raise InsufficientBalance('Insufficient balance')
            else:
                pw=input('Enter your password: ')
                if pw==account.password:
                    account.amount-=amount
                    print(f'Your amount has been updated to {account.amount}')
        elif option==3:
            print(f'Thank you {account.name} for using this application')
            flag=False
            break
        else:
            raise InvalidChoiceError('Invalid option')
except (InvalidPassword,ValueError,Exception) as e:
    print(e)
