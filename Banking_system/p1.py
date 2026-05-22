class Myeror(Exception):
    pass
class Banking:
    def __init__(self):
        self.name = "roshini"
        self.username = "roshini@gmail.com"
        self.password = 123455
        self.acc_number = 1234567
        self.attempts =0
        self.balance = 2200
    def login(self):
        while self.attempts < 3:
            u_name = input("Please enter your name ")
            pass_key = int(input("enter the password "))
            if u_name == self.name and pass_key == self.password:
                print(f"Welcome {u_name}")
                while True:
                    print("1.Deposit 2.withdraw 3.Check balance 4. exit")
                    choice = int(input())
                    if choice == 1:
                        self.deposit()
                    elif choice == 2:
                        self.withdraw()
                    elif choice == 3:
                        self.check_balance()
                    elif choice == 4:
                        break
                    else:
                        print("invalid option")
                    
            else:
                self.attempts += 1
                remaining = 3 - self.attempts

                print(f"The password is incorrect the remanining attempts you have are {remaining}")
        if self.attempts == 3:
            raise Myeror("Too many login attempts ")
        else :
            print("continue")
    def deposit(self):
        amount = int(input("enter how much amount to be depositied"))
        if amount > 500:
            print("Deposit succesful")
        else:
            raise Myeror('the amount is not sufficient')
        self.balance += amount
        print (f"the current balance is {self.balance}")
    # def exit():
    #     break
    def withdraw(self):
        withdraw = int(input("please enter the withdraw "))
        
        if self.balance > withdraw:
            self.balance -= withdraw 
        else:
            raise Myeror('the balance is not lined with the withdraw')
        print(f"the current balance after with draw is {self.balance}")

    def check_balance(self):
        acc_n = int(input("Enter the account number: "))
        
        if acc_n == self.acc_number:
            print(f"The balance is {self.balance}")
        else:
            raise Myeror("Invalid account number")
        
obj = Banking()
obj.login()
