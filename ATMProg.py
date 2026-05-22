class BankException(Exception):
    pass


class MinimumDepositError(Exception):
    pass


class Insuf_bal(Exception):
    pass


class Inval_pswd(Exception):
    pass


class ATM:

    def __init__(self, name, gmail, balance, acc_num, pin):
        self.name = name
        self.gmail = gmail
        self.balance = balance
        self.acc_num = acc_num
        self.pin = pin

    def deposit(self, amount):

        if amount < 500:
            raise MinimumDepositError(
                "Minimum deposit amount should be 500"
            )

        self.balance += amount

        print("Amount Deposited Successfully")
        print("Current Balance:", self.balance)

    def withdraw(self, amount):

        if amount > self.balance:
            raise Insuf_bal(
                "Insufficient Balance"
            )

        self.balance -= amount

        print("Amount Withdrawn Successfully")
        print("Current Balance:", self.balance)

    def view_bal(self):

        print("Balance :", self.balance)


name = input("Enter Name: ")
gmail = input("Enter Gmail: ")
balance = int(input("Enter Initial Balance: "))
acc_num = int(input("Enter Account Number: "))
pin = input("Create PIN: ")


user = ATM(name, gmail, balance, acc_num, pin)

ep = input("\nEnter ATM PIN: ")

if ep != user.pin:
    raise Inval_pswd("Wrong PIN")


while True:

    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:

            try:
                amount = int(input("Enter Deposit Amount: "))
                user.deposit(amount)

            except MinimumDepositError as e:
                print("Exception:", e)

        case 2:

            try:
                amount = int(input("Enter Withdraw Amount: "))
                user.withdraw(amount)

            except Insuf_bal as e:
                print("Exception:", e)

        case 3:

            user.view_bal()

        case 4:

            print("Thank You for Using ATM")
            break

        case _:

            print("Invalid Choice")