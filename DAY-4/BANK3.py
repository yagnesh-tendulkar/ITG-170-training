# Bank Management System with Enhanced Error Handling and Validation
# This program simulates a simple bank management system where users can log in, deposit money, withdraw money, and 
# check their balance. It includes robust error handling to manage invalid inputs and ensure a smooth user experience.
class DepositError(Exception):
    """Custom exception for deposit-related errors."""
    pass
class WithdrawError(Exception):
    """Custom exception for withdrawal-related errors."""
    pass
class LoginError(Exception):
    """Custom exception for login-related errors."""
    pass
class BalanceInquiryError(Exception):
    """Custom exception for balance inquiry-related errors."""
    pass

class Details:
    def __init__(self):
        self.name = "Balaji"
        self.gmail = "balaji@gmail.com"
        self.pswd = "1901"
        self.balance = 100000
        self.acct_no = 41191905958

class Bank(Details):
    def __init__(self):
        super().__init__()
    def run(self):
        while True:
            print("\nWelcome to the Bank")
            print("Enter userName:")
            try:
                userName = input()
                if userName != self.name:
                    raise ValueError("Invalid username.")
            except ValueError:
                print("Invalid input for username.")
                try: 
                    userName = input("Please enter a valid username (2nd chance): ")
                    if userName != self.name:
                        raise ValueError()
                except ValueError:
                    try: 
                        userName = input("Please enter a valid username (3rd chance): ")
                        if userName != self.name:
                            raise LoginError("Invalid username.")
                    except LoginError as e:
                        print("Too many invalid attempts. Exiting.")
                        break
                continue

            print("Enter password:")
            try:
                password = input()
                if password != self.pswd:
                    raise ValueError("Invalid password.")
            except LoginError as e:
                print("Error:", e)
            except:
                print("Invalid input for password.")
                try:
                    password = input("Please enter a valid password (2nd chance): ")
                    if password != self.pswd:
                        raise LoginError("Invalid password.")
                except LoginError :
                    print("Invalid input for password.")
                    try:
                        password = input("Please enter a valid password (3rd chance): ")
                        if password != self.pswd:
                            raise LoginError("Invalid password.")
                    except LoginError as e:
                        print("Too many invalid attempts. Exiting.")
                        break
                #continue
            if userName == self.name and password == self.pswd:
                print("Login successful.")
                
                # Inner loop for the menu after login
                while True:
                    print("\n1.Deposit\n2.Withdraw\n3.Balance Inquiry\n4.Exit")
                    try:
                        ch = int(input("Enter your choice: "))
                        if ch == 1:
                            amt = int(input("Enter amount to deposit: "))
                            self.deposit(amt)
                        elif ch == 2:
                            amt = int(input("Enter amount to withdraw: "))
                            self.withdraw(amt)
                        elif ch == 3:
                            self.balance_inquiry()
                        elif ch == 4:
                            return # Exits the entire program
                        else:
                            print("Invalid Choice")
                    except ValueError:
                        print("Please enter a number for the choice.")
            else:
                print("Invalid credentials. Please try again.")

    def deposit(self, amt):
        """Deposit money into the account with validation checks. Raises ValueError for invalid inputs.
        """
        try:
            if amt <= 0:
                raise DepositError("Amount must be positive.")
            if amt > 50000:
                raise DepositError("Deposit limit exceeded. Maximum allowed is 50,000.")
            if self.balance + amt > 1000000:
                raise DepositError("Balance limit exceeded. Maximum allowed is 1,000,000.")
            self.balance += amt
            print("Amount Deposited:", amt)
            print("Balance:", self.balance)
        except DepositError as e:
            print("Error:", e)

    def withdraw(self, amt):
        """Withdraw money from the account with validation checks. Raises ValueError for invalid inputs."""
        try:
            if amt <= 0:
                raise WithdrawError("Amount must be positive.")
            if self.balance < amt:
                raise WithdrawError("Insufficient Balance.")

            self.balance -= amt
            print("Amount Withdrawn:", amt)
        except WithdrawError as e:
            print("Error:", e)
    def balance_inquiry(self):
        """Check account balance with validation for account number. Raises ValueError for invalid inputs."""
        try:
            acct=int(input("Enter account number: "))
            if acct != self.acct_no:
                raise BalanceInquiryError("Invalid account number.")
        except BalanceInquiryError as e:
            try:
                acct=int(input("Please enter a valid account number (2nd chance): "))
                if acct != self.acct_no:
                    raise BalanceInquiryError("Invalid account number.")
            except BalanceInquiryError as e:
                    print("Too many invalid attempts. Exiting.", e)
                    return
            print("Balance:", self.balance)    
        print("Gmail:", self.gmail)
        print("Account Number:", self.acct_no)
        print("Balance:", self.balance)

    # def display(self):
    #     print(f"Name: {self.name}")
    #     print(f"Account: {self.acct_no}")
    #     print(f"Current Balance: {self.balance}")

b = Bank()
b.run()