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

    def run_atm(self):
        attempts = 0
        while attempts < 3:
            print("\n--- Welcome to the Bank ---")
            try:
                user = input("Enter userName: ")
                if user != self.name:
                    raise ValueError("Incorrect Username.")
                
                pwd = input("Enter password: ")
                if pwd != self.pswd:
                    raise ValueError("Incorrect Password.")
                
                print("Login successful!")
                self.show_menu()
                break # Exit login loop to show menu

            except ValueError as e:
                attempts += 1
                print(f"Error: {e} Attempt {attempts}/3")
                if attempts == 3:
                    print("Too many invalid attempts. Card Blocked.")
        
    def show_menu(self):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Display\n4. Exit")
            try:
                ch = int(input("Enter your choice: "))
                if ch == 1:
                    amt = float(input("Enter amount to deposit: "))
                    self.deposit(amt)
                elif ch == 2:
                    amt = float(input("Enter amount to withdraw: "))
                    self.withdraw(amt)
                elif ch == 3:
                    self.display()
                elif ch == 4:
                    print("Thank you for using our bank!")
                    break
                else:
                    print("Invalid Choice. Please pick 1-4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def deposit(self, amt):
        try:
            if amt <= 0:
                raise ValueError("Amount must be positive.")
            if amt > 50000:
                raise ValueError("Deposit limit exceeded ($50,000 max).")
            
            self.balance += amt
            print(f"Amount Deposited: {amt}")
            print(f"New Balance: {self.balance}")
        except ValueError as e:
            print(f"Transaction Failed: {e}")

    def withdraw(self, amt):
        try:
            if amt <= 0:
                raise ValueError("Amount must be positive.")
            if self.balance < amt:
                raise ValueError("Insufficient Balance.")
            
            self.balance -= amt
            print(f"Amount Withdrawn: {amt}")
        except ValueError as e:
            print(f"Transaction Failed: {e}")
        else:
            print(f"Success! Current Balance: {self.balance}")

    def display(self):
        print(f"\n--- Account Details ---")
        print(f"User: {self.name}")
        print(f"Acct No: {self.acct_no}")
        print(f"Balance: {self.balance}")

# START THE PROGRAM
if __name__ == "__main__":
    my_bank = Bank()
    my_bank.run_atm()