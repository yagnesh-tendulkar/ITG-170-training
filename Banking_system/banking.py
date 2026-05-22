class Myeror(Exception):
    pass

class Banking:
    def __init__(self):
        self.name = "roshini"
        self.gmail = "roshini@gmail.com"
        self.password = 123455
        self.acc_number = 1234567
        self.attempts = 0
        self.balance = 2200

    def login(self):
        while self.attempts < 3:
            try:
                u_name = input("Please enter your name: ")
                pass_key = int(input("Enter the password: "))
            except ValueError:
                print("Password must be numeric")
                continue

            if u_name == self.name and pass_key == self.password:
                print(f"Welcome {u_name}")

                while True:
                    print("\n1. Deposit  2. Withdraw  3. Check Balance  4. Exit")

                    try:
                        choice = int(input("Enter your choice: "))
                    except ValueError:
                        print("Please enter a valid number option")
                        continue

                    if choice == 1:
                        self.deposit()

                    elif choice == 2:
                        self.withdraw()

                    elif choice == 3:
                        self.check_balance()

                    elif choice == 4:
                        print("Thank you for using banking system")
                        break

                    else:
                        print("Invalid option")

                break  # exit login loop after successful session

            else:
                self.attempts += 1
                remaining = 3 - self.attempts
                print(f"Incorrect credentials. Remaining attempts: {remaining}")

        if self.attempts == 3:
            raise Myeror("Too many login attempts")


    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: "))
        except ValueError:
            print("Amount must be a number")
            return

        if amount > 500:
            self.balance += amount
            print(f"Deposit successful. Current balance: {self.balance}")
        else:
            raise Myeror("Minimum deposit amount is 500")


    def withdraw(self):
        try:
            amount = int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Amount must be a number")
            return

        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful. Current balance: {self.balance}")
        else:
            raise Myeror("Insufficient balance")


    def check_balance(self):
        try:
            acc_n = int(input("Enter account number: "))
        except ValueError:
            print("Account number must be numeric")
            return

        if acc_n == self.acc_number:
            print(f"Your balance is: {self.balance}")
        else:
            raise Myeror("Invalid account number")

obj = Banking()
obj.login()