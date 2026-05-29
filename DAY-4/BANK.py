class Details:
    def __init__(self):
        self.name="Balaji"
        self.gmail="balaji@gmail.com"
        self.pswd="1901"
        self.balance=100000
        self.acct_no=41191905958
class Bank(Details):
    def __init__(self):
        super().__init__(self)
    while(True):
        print("\nWelcome to the Bank")
        print("Enter userName:")
        try:
            userName=input()
            if userName!=Details.name:
                raise ValueError("Invalid username.")
        except ValueError as e:
            print("Invalid input for username.")
            try: 
                userName=input("Please enter a valid username: ")
                if not userName:
                    raise ValueError("This is your 2nd chance to enter a valid username.")
            except ValueError as e:
                try: 
                    userName=input("Please enter a valid username: ")
                    if not userName:
                        raise ValueError("This is your 3rd chance to enter a valid username.")
                except ValueError as e:
                    print("Too many invalid attempts. Exiting.", e)
                    break
            continue
        print("Enter password:")
        password=input()
        if userName==self.name and password==self.pswd:
            print("Login successful.")
            break
        else:
            print("Invalid credentials. Please try again.")
        print("1.Deposit\n2.Withdraw\n3.Display\n4.Exit")
        ch=int(input("Enter your choice:"))
        if ch==1:
            amt=int(input("Enter amount to deposit:"))
            self.deposit(amt)
        elif ch==2:
            amt=int(input("Enter amount to withdraw:"))
            self.withdraw(amt)
        elif ch==3:
            self.display()
        elif ch==4:
            self.exit1()
        else:
            print("Invalid Choice")
    def deposit(self,amt):
        try:
            if amt<=0:
                raise ValueError("Amount must be positive.")
            if amt > 50000:
                raise ValueError("Deposit limit exceeded. Maximum allowed is 50,000.")
            if self.balance + amt > 1000000:
                raise ValueError("Balance limit exceeded. Maximum allowed is 1,000,000.")
        except ValueError as e:
                print("Error:", e)
        self.balance+=amt
        print("Amount Deposited:",amt)
        print("Balance:",self.balance)
    def withdraw(self,amt):
        try:
            if amt<=0:
                raise ValueError("Amount must be positive.")
            if self.balance<amt:
                raise ValueError("Insufficient Balance.")
        except ValueError as e:
            print("Error:", e)
        else:
            self.balance-=amt
            print("Amount Withdrawn:",amt)
        print("Gmail:",self.gmail)
        print("Account Number:",self.acct_no)
        print("Balance:",self.balance)