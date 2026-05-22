
# Object-Oriented Programming (Classes, Inheritance, Encapsulation)


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # Encapsulation using private variable

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.get_balance() * rate / 100
        self.deposit(interest)


account = SavingsAccount("Arika", 5000)
account.deposit(1000)
account.withdraw(2000)
account.add_interest(5)

print("Final Balance:", account.get_balance())

