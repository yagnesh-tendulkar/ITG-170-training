class InvalidCredentialsError(Exception):
    pass
class InsufficientFundsError(Exception):
    pass 
class MinimumDepositError(Exception):
    pass 
class AccountBlockError(Exception):
    pass        
      
class Bank:
    def __init__(self, name, account_no, password, gmail,  balance):
        self.name = name
        self.__account_no = account_no
        self.__gmail = gmail
        self.__password = password
        self.__balance = balance
        
    def enter_bank(self):
        chances = 3
        while chances>0:
            try:
                try:
                    account_no = int(input("Enter Account Number: "))
                except ValueError:
                    print("Enter valid account number")
                    print()
                    continue
                pass_word = input("Enter password: ")
                print()

                validAccountNo = self.__account_no
                validPassword = self.__password
                if account_no != validAccountNo or pass_word != validPassword:
                    if chances == 1:
                        raise AccountBlockError("Account Blocked")
                    raise InvalidCredentialsError("Invalid Credentials")
                
                print("Login Successful")
                self.next_step()
                return
            
            except InvalidCredentialsError as e:
                chances-=1
                print(e)
                print("Try Again... Chances left:", chances)
                print()
            except AccountBlockError as e:
                print(e)
                print()
                break    
                
    def next_step(self):
        print("Welcome, ",self.name)
        print()
        print("Option 1: Deposit")
        print("Option 2: WithDraw")
        print("Option 3: Check Balance")
        print("Option 4: Exit")
        print()
        
        while True:
            try:
                option = int(input("Enter the option number: "))
                print()
                match option:
                    case 1:
                        try:
                            amount = int(input("Enter amount to deposit: "))
                            status = self.deposit(amount)
                            print(status)
                            print()
                        except ValueError as e:
                            print(e)
                            print()
                    case 2:
                        try:
                            amount = int(input("Enter amount to withdraw: "))
                            status = self.withdraw(amount)
                            print(status)
                            print()
                        except ValueError as e:
                            print(e)
                            print()
        
                    case 3:
                        current_balance = self.get_balance()
                        print("Current Balance: ",current_balance)
                    case 4: 
                        print("Thank You") 
                        break  
                    case _:
                        print("Invalid Option, Please try again...")
            except ValueError:
                print("Enter a valid option")
                print()
            except InsufficientFundsError as e:
                print(e)
                print() 
            except MinimumDepositError as e:
                print(e)
                print()         

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance=balance
   
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount < 500:
            raise  MinimumDepositError("Minimum deposit amount is 500")  
        current = self.get_balance()
        current += amount
        self.set_balance(current)
        return f"Amount Deposited: {amount}"

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        current = self.get_balance()

        if amount > current:
            raise InsufficientFundsError("Insufficient Funds")

        current -= amount
        self.set_balance(current)
        return f"Amount Withdrawn: {amount}"        

bank_user = Bank("ABHI", 1234, "pass", "abhi@gmail.com", 0)
bank_user.enter_bank()        