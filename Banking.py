#Creating Custom Exceptions
class InvalidCredentialException(Exception):
    pass
class MinimumDepositException(Exception):
    pass
class InsufficientBalanceException(Exception):
    pass
 #Creating Main Class
class Bank:
    def __init__(self,gmail,name,password,balance,account_number):
        self.gmail = gmail
        self.name = name
        self.password = password
        self.balance = balance
        self.account_number = account_number
    def verify_user(self,acc,pwd):
        if self.account_number == acc and self.password == pwd:
            return True
        else:
            raise InvalidCredentialException("Invalid Account Number or Password")
    def deposit(self,amount):
        if amount<500:
            raise MinimumDepositException("Minimum Deposit amount is 500")
        else:
            self.balance+=amount
            print("Amount Deposited Successfully")
            print("Available Balance",self.balance)
    def withdraw(self,amount):
        if amount >self.balance:
            raise InsufficientBalanceException("Insufficient Balance")
        else:
            self.balance-=amount
            print("Amount Withdraw Successfully")
            print("Available Balance",self.balance)
    def view_balance(self):
        print("Available Balance: ",self.balance)
#Object Creation
user = Bank("bikash@gmail.com","Bikash","bikash123",10000,123456)
attempt =0
while attempt<3:

    try:
        acc = int(input("Enter Account Number: "))
        pwd = input("Enter Password: ")
        if user.verify_user(acc,pwd):
            while True:
                print("Banking Options:")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.View Balance")
                print("4.Exit")

                choice = int(input("Enter Your Choice: "))
                if choice ==1:
                    try:
                        amount = int(input("Enter Amount: "))
                        user.deposit(amount)

                    except MinimumDepositException as e:
                        print(e)
                elif choice == 2:
                    try:
                        amount = int(input("Enter Amount: "))
                        user.withdraw(amount)
                    except InsufficientBalanceException as e:
                        print(e)
                elif choice ==3:
                    user.view_balance()
                elif choice ==4:
                    print("Thank you for using Banking")
                    break
                else:
                    print("Invalid Choice")
        break
    except InvalidCredentialException as e:
        attempt +=1
        print(e)
        print("Attempt Left",3-attempt)
        if  attempt ==3:
            print("Maximum Limit Reached")
            print("Please contact your Bank")



