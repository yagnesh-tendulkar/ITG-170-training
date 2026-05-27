class InvalidEmailError(Exception):
    def __init__(self,message):
        super().__init__(message)

class InSufficientBalanceError(Exception):
    def __init__(self,message):
        super().__init__(message)

class InvalidAmountError(Exception):
    def __init__(self,message):
        super().__init__(message)

class UserNotFoundError(Exception):
    def __init__(self,message):
        super().__init__(message)

class BankUser:
    def __init__(self,name,gmail,password,balance,record_number):
        if "@" not in gmail or "." not in gmail:
            raise InvalidEmailError("Enter a vaild email address !!")
        self.name=name
        self.gmail=gmail
        self.password=password
        self.balance=balance
        self.record_number=record_number

    def Deposit(self,amount):
        if amount <=0:
            raise InvalidAmountError("Deposit amount should be positive integer.")
        self.balance+=amount
        print(f"Deposited Amount {amount} , Total balance {self.balance}")
        


    def Withdraw(self,amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal Amount should be positive integer")
        if amount>self.balance:
            raise InSufficientBalanceError("Insufficient Balance")
        self.balance-=amount
        print(f"Withdrawal Amount {amount} and the total balance : {self.balance}")


    def Check_balance(self):
        print(f"Current Balance is : {self.balance}")


class Bank_System:
    def __init__(self):
        self.Users = {}

    def register_user(self):
        print("====Register New User=====")
        try:
            name=input("Enter your Name : ")
            gmail=input("Enter your Gmail : ")
            password=input("Enter your password : ")
            balance=float(input("Enter your initial balance :"))
            record_number=input("Enter your record number : ")

            if record_number in self.Users:
                print("User alrrady Exist with this Record Number")
                return
            
            user=BankUser(name,gmail,password,balance,record_number)
            self.Users[record_number]=user
            print(f"User {name} record added Sucessfully")
        except InvalidEmailError as e:
            print(e)
        except ValueError:
            print("Invalid balance input , please enter a number.")


    def login_user(self):
        print("======User Login=====")
        record_number=input("Enter record number : ")
        
        user =self.Users.get(record_number)
        if not user:
            print(":::User Not found:::")
            return 
        
        attempts=0
        while attempts<3:
            password = input("Enter password : ")
            if user.password==password:
                print(f"Welcome back user {user.name}")
                self.user_menu(user)
                return 
            else:
                attempts+=1
                remaining=3-attempts
                
                if remaining >0:
                    print(f"you have remaining attempts {remaining} , enter password wisely this is attempt no {attempts+1}")
                else:
                    print(f"you have reached your password limits.")



    def user_menu(self,user):
        while True:
            print("\nChoose an action:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Logout")
            choice = input("Enter choice (1-4): ")
            try:
                if choice == "1":
                    amount = float(input("Enter amount to deposit: "))
                    user.Deposit(amount)
                elif choice == "2":
                    amount = float(input("Enter amount to withdraw: "))
                    user.Withdraw(amount)
                elif choice == "3":
                    user.Check_balance()
                elif choice == "4":
                    print(f"Logging out {user.name}...")
                    break
                else:
                    print("Invalid choice. Please select 1-4.")
            except (InvalidAmountError, InSufficientBalanceError) as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input. Please enter a numeric amount.")


    def main_menu(self):
        while True:
            print("Enter 1 to Register")
            print("Enter 2 for Login")
            print("Enter 3 for Exit")
            print("Enter value between (1-3)")
            choice = int(input("Enter Your Choice"))
            if choice==1:
                self.register_user()
            elif choice==2:
                self.login_user()
            elif choice==3:
                print("thank you for using Bank , visit again")
                break
            else:
                print("Invalid choice.. choose a valid one")


if __name__ == "__main__":
    bank = Bank_System()
    bank.main_menu()
    print(bank.Users)


