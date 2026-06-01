class Bank:
    def __init__(self):
        self.name = "Varshitha"
        self.gmail = "varshitha@gmail.com"
        self.password = 123456
        self.balance = 1000
        self.account_no = 12345678
class Error(Exception):
    pass
class Operations(Bank):
    def deposit(self):
        try:
            value = int(input("Enter the depositing amount: "))
            if value < 500:
                raise Error("Amount should be greater than 500")
            self.balance += value
            print("Deposited successfully")
            print("Current balance is:", self.balance)
        except Error as e:
            print(e)
        except ValueError:
            print("Please enter numbers only")
    def withDraw(self):
        try:
            amount = int(input("Enter the withdraw amount: "))
            if amount > self.balance:
                raise Error("Insufficient balance")
            self.balance -= amount
            print("Withdraw successful")
            print("Remaining balance is:", self.balance)
        except Error as e:
            print(e)
        except ValueError:
            print("Please enter numbers only")
    def viewBalance(self):
        print("Your current balance is:", self.balance)
    def exit(self):
        print("Thank you for visiting the bank")
obj = Operations()
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_name = input("Enter username: ")
    try:
        user_password = int(input("Enter password: "))
    except ValueError:
        print("Password should contain numbers only")
        continue
    if user_name == obj.name and user_password == obj.password:
        print("\nLogin Successful\n")
        while True:
            try:
                number = int(input(
                    "\nEnter:\n1-Deposit\n2-Withdraw\n3-View Balance\n4-Exit\n"
                ))
                match number:
                    case 1:
                        obj.deposit()
                    case 2:
                        obj.withDraw()
                    case 3:
                        obj.viewBalance()
                    case 4:
                        obj.exit()
                        break
                    case _:
                        print("Invalid choice")
            except ValueError:
                print("Please enter numbers only")
        break
    else:
        attempts += 1
        print("Incorrect username or password")
        print(f"Remaining attempts: {max_attempts - attempts}")
if attempts == max_attempts:
    print("\nYou crossed the maximum login attempts")
    print("Your account is temporarily blocked")