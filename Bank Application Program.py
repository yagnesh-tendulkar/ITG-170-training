class BankAccount:
    def __init__(self, name, email, password, account_no, balance=50000):
        self.name = name
        self.email = email
        self.__password = password
        self.account_no = account_no
        self.balance = balance

    def login(self):
        attempts = 3

        while attempts > 0:
            username = input("Enter Username: ")
            
            try:
                password = int(input("Enter Password: "))
            except ValueError:
                print("Password must contain numbers only")
                continue

            if username == self.name and password == self.__password:
                print("\nLogin Successful")
                return True
            else:
                attempts -= 1
                print("Invalid Username or Password")
                print("Remaining Attempts:", attempts)

        print("\nAccount Temporarily Blocked")
        return False

    def deposit(self):
        try:
            amount = int(input("Enter Deposit Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0")

            elif amount < 500:
                print("Minimum deposit amount is 500")

            else:
                self.balance += amount
                print("Amount Deposited Successfully")
                print("Available Balance:", self.balance)

        except ValueError:
            print("Please enter numbers only")

    def withdraw(self):
        try:
            amount = int(input("Enter Withdraw Amount: "))

            if amount <= 0:
                print("Amount must be greater than 0")

            elif amount > self.balance:
                print("Insufficient Balance")

            else:
                self.balance -= amount
                print("Withdrawal Successful")
                print("Available Balance:", self.balance)

        except ValueError:
            print("Please enter numbers only")

    def check_balance(self):
        print("Current Balance:", self.balance)

    def menu(self):
        while True:
            print("\n===== BANK MENU =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Exit")

            try:
                choice = int(input("Enter Your Choice: "))

                if choice == 1:
                    self.deposit()

                elif choice == 2:
                    self.withdraw()

                elif choice == 3:
                    self.check_balance()

                elif choice == 4:
                    print("Thank You for Visiting")
                    break

                else:
                    print("Invalid Choice")

            except ValueError:
                print("Enter numbers only")

obj = BankAccount(
    "Vennela",
    "vennela@gmail.com",
    14251425,
    2514251425
)

if obj.login():
    obj.menu()