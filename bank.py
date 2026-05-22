class NegativeNumberError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class InvalidCrendials(Exception):
     def __init__(self,msg):
        super().__init__(msg)       
class InsufficentAmount(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class Account:
    Accountno="12345678"
    Name="Rudra Prasad Tripathy"
    password="rudra@123"
    balance=10000
    gmail="rp@123@gmail.com"
    def __init__(self ):
        pass
    @staticmethod
    def login(accno,pas):
        
            if(Account.Accountno==accno and pas==Account.password):
                return True
                
            else:
                return False
    @staticmethod        
    def showBalance():
        print("your current balance is {}".format(Account.balance) )
    @staticmethod    
    def deposit(amount):

     while True:

        try:
            if amount < 0:
                raise NegativeNumberError("Amount cannot be negative")

            if amount < 500:
                print("Minimum deposit is 500")
                amount = int(input("Re-enter amount: "))
                continue   # give another chance

        except NegativeNumberError as e:
            print(e)
            amount = int(input("Re-enter amount: "))
            continue

        else:
            Account.balance += amount
            print("Deposit successful")
            Account.showBalance()
            break
    @staticmethod        
    def withdrwal(amount):
        try:
            if amount<0:
                raise NegativeNumberError("amount can not be negative")
            if Account.balance<amount:
                raise InsufficentAmount(" you have insufficent amount")  
        except (NegativeNumberError,InsufficentAmount) as e:
            print(e.args)
        else:
            Account.balance=Account.balance-amount
            print("you have suceessfully deducted amount")
            Account.showBalance() 
    @staticmethod         
    def showdetalils( account):
        if(Account.Accountno==account):
            print("Name : {}".format(Account.Name))   
            print("Account details : {}".format(Account.Accountno))
            print("Avalible Balance : {}".format(Account.balance))
        else :
            raise  InvalidCrendials("you are account number is not matching")       





