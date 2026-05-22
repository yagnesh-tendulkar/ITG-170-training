class LoginError(Exception):
    pass


class Bank:
    def __init__(self):
        self.name = "puspanjali"
        self.password = "12345"
        self.balance = 50000

    def deposit(self):
        amt = int(input("Enter amount: "))
        self.balance += amt
        print("Deposited. Balance:", self.balance)

    def withdraw(self):
        amt = int(input("Enter amount: "))
        if amt > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amt
            print("Withdraw successful. Balance:", self.balance)

    def view(self):
        print("Balance:", self.balance)


bank = Bank()

attempts = 0

while attempts < 3:
    name = input("Enter name: ")
    pwd = input("Enter password: ")

    try:
        if name != bank.name or pwd != bank.password:
            attempts += 1
            raise LoginError("Wrong credentials")
        else:
            print("Login successful")
            break

    except LoginError as e:
        print(e)
        print("Attempts left:", 3 - attempts)

else:
    print("Unable to proceed")
    exit()


while True:
    print("\n1.Deposit 2.Withdraw 3.View 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        bank.deposit()
    elif ch == 2:
        bank.withdraw()
    elif ch == 3:
        bank.view()
    elif ch == 4:
        print("Logged out")
        break