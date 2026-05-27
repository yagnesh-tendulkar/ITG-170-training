"""
ATM System - Improved Version
Author: Geetha Gangabattula
Features:
- Login System
- Deposit / Withdraw
- Balance Check
- Email Verification
- Password Change
- Input validation
- Custom exceptions
"""

from typing import Optional

# =========================
# CONSTANTS
# =========================
MIN_BALANCE = 0
MAX_ATTEMPTS = 3


# =========================
# CUSTOM EXCEPTION
# =========================
class ATMError(Exception):
    pass


# =========================
# ATM CORE CLASS
# =========================
class ATM:
    def __init__(self):
        self.name = "Geetha"
        self.email = "geetha@gmail.com"
        self.password = 1234
        self.balance = 10000


# =========================
# VALIDATION FUNCTIONS
# =========================
def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Enter numbers only")


def get_amount(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("❌ Amount must be greater than 0")
                continue
            return value
        except ValueError:
            print("❌ Enter valid amount")


# =========================
# OPERATIONS
# =========================
class ATMOperations(ATM):

    def balance(self):
        print(f"\n💰 Current Balance: {self.balance}")

    def deposit(self):
        amount = get_amount("Enter deposit amount: ")
        self.balance += amount
        print(f"✅ Deposited successfully. Balance: {self.balance}")

    def withdraw(self):
        amount = get_amount("Enter withdraw amount: ")

        if amount > self.balance:
            print("❌ Insufficient balance")
            return

        self.balance -= amount
        print(f"✅ Withdraw successful. Balance: {self.balance}")

    def change_password(self):
        old = get_int("Enter old password: ")

        if old != self.password:
            print("❌ Wrong password")
            return

        new = get_int("Enter new password: ")
        self.password = new
        print("✅ Password updated")

    def verify_email(self):
        email = input("Enter email: ")

        if email != self.email:
            print("❌ Email mismatch")
        else:
            print("✅ Email verified")

    def exit_atm(self):
        print("🙏 Thank you for using ATM")


# =========================
# LOGIN SYSTEM
# =========================
def login(atm: ATMOperations) -> bool:
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        try:
            username = input("Enter username: ")
            password = int(input("Enter password: "))

            if username == atm.name and password == atm.password:
                print("\n✅ LOGIN SUCCESSFUL\n")
                return True

            attempts += 1
            print(f"❌ Invalid login. Attempts left: {MAX_ATTEMPTS - attempts}")

        except ValueError:
            print("❌ Password must be numeric")

    print("🚫 Account locked")
    return False


# =========================
# MENU SYSTEM
# =========================
def menu(atm: ATMOperations):
    while True:
        print("""
====================
ATM MENU
====================
1. Balance
2. Deposit
3. Withdraw
4. Change Password
5. Email Verify
6. Exit
""")

        choice = get_int("Enter choice: ")

        if choice == 1:
            atm.balance()
        elif choice == 2:
            atm.deposit()
        elif choice == 3:
            atm.withdraw()
        elif choice == 4:
            atm.change_password()
        elif choice == 5:
            atm.verify_email()
        elif choice == 6:
            atm.exit_atm()
            break
        else:
            print("❌ Invalid choice")


# =========================
# MAIN
# =========================
def main():
    atm = ATMOperations()

    if login(atm):
        menu(atm)


if __name__ == "__main__":
    main()
