class ATM:
    def __init__(self):
        self.name = "Sumathi Ganta"
        self.gmail = "arikaneemadarshita@gmail.com"
        self.password = 9027
        self.balance = 10000
        self.accountNumber = 899559444077


#Creating custom exception here
class AtmError(Exception):
    pass

class Operations(ATM):

    def viewbalance(self):
        print("Your current balance is:", self.balance)

    def deposit(self):
        try:
            amount = int(input("Please enter your deposit amount: "))

            if amount <= 0:
                raise AtmError("Amount should be greater than 0")

            self.balance += amount

            print("Amount deposited successfully")
            print("Updated balance is:", self.balance)

        except AtmError as e:
            print(e)

        except ValueError:
            print("Please enter numbers only")

    def withdraw(self):
        try:
            amount = int(input("Enter withdraw amount: "))

            if amount > self.balance:
                raise AtmError("Insufficient balance")

            self.balance -= amount

            print("Withdrawal successful")
            print("Remaining balance is:", self.balance)

        except AtmError as e:
            print(e)

        except ValueError:
            print("Please enter numbers only")

    def changepassword(self):
        try:
            oldpassword = int(input("Enter old password: "))
            newpassword = int(input("Enter new password: "))

            if oldpassword != self.password:
                raise AtmError("Old password is incorrect")

            self.password = newpassword

            print("Password changed successfully")

        except AtmError as e:
            print(e)

        except ValueError:
            print("Password should contain numbers only")

    def emailverification(self):
        try:
            email = input("Enter your email: ")

            if email != self.gmail:
                raise AtmError("Email is incorrect")

            print("Email verified successfully")

        except AtmError as e:
            print(e)

    @staticmethod
    def exit():
        print("Thank you for visiting ATM")


# Object is being created for the operations method so that we can call the values using obj
obj = Operations()

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        username = input("Enter username: ")
        userpassword = int(input("Enter password: "))

    except ValueError:
        print("Password should contain numbers only")
        continue

    if username == obj.name and userpassword == obj.password:

        print("\nLogin Successful\n")

        while True:

            try:
                choice = int(input(
                    "\n1. Balance Enquiry\n"
                    "2. Deposit\n"
                    "3. Withdraw\n"
                    "4. Change Password\n"
                    "5. Email Verification\n"
                    "6. Exit\n"
                    "Enter your choice: "
                ))

                match choice:

                    case 1:
                        obj.viewbalance()

                    case 2:
                        obj.deposit()

                    case 3:
                        obj.withdraw()

                    case 4:
                        obj.changepassword()

                    case 5:
                        obj.emailverification()

                    case 6:
                        obj.exit()
                        break

                    case _:
                        print("Invalid choice")

            except ValueError:
                print("Please enter numbers only")

        break

    else:
        attempts += 1
        print("Please enter correct login credentials")
        print("Remaining attempts:", max_attempts - attempts)


if attempts == max_attempts:
    print("\nYou crossed maximum login attempts")
    print("Your account is temporarily blocked")
