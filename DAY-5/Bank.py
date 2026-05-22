class InvalidLogin(Exception):
    pass

class InvalidAccNo(Exception):
    pass

class InvalidAmt(Exception):
    pass


class Bank:

    def __init__(self):
        self.balance = 5000
        self.name = "Vaishnavi"
        self.pwd = "4321"
        self.AccNo = 1234
        self.c=0

    def pwdCheck(self):

        Name = input("Enter your name: ")
        Pwd = input("Enter your password: ")

        try:
            if self.name != Name or self.pwd != Pwd:
                raise InvalidLogin("Invalid username or password")

            print("Login successful")

            print("1.Deposit  2.Withdraw  3.Check Balance  4.Exit")
            a = int(input("Enter your option: "))

            if a == 1:

                amount = int(input("Enter amount: "))

                try:
                    if amount < 500:
                        raise InvalidAmt("Enter amount greater than 500")

                    self.balance += amount
                    print("Updated balance:", self.balance)

                except InvalidAmt as e:
                    print(e)

            elif a == 2:

                amount = int(input("Enter amount: "))

                try:
                    if amount > self.balance:
                        raise InvalidAmt("Insufficient balance")

                    self.balance -= amount
                    print("Updated balance:", self.balance)

                except InvalidAmt as e:
                    print(e)

            elif a == 3:

                try:
                    accNo = int(input("Enter account number: "))

                    if accNo != self.AccNo:
                        raise InvalidAccNo("Account number not valid")

                    print("Your balance is:", self.balance)

                except InvalidAccNo as e:
                    print(e)

            elif a == 4:
                print("Exit")

        except InvalidLogin as e:
            print(e)


obj = Bank()
obj.pwdCheck()

