class User(Exception):
    name="Harinita"
    password="Hari@321"
    balance=33000
    gmail="vujjinh987@gmail.com"
    account_number=863997564912
    def deposit(self,amount):
        if amount<=500:
            raise User("Deposit amount should be greater than 500.")
        self.balance+=amount
        print("Successfully added.")
        print("Available balance:",self.balance)
    def with_draw(self,amount):
        if amount>self.balance:
            raise User("Insufficient balance.")
        self.balance-=amount
        print("Available balance after withdrawal:",self.balance)
    def view_balance(self):
        print("Available balance:",self.balance)
u=User()
attempts=3
while attempts>0:
    try:
        print("Login")
        user_name=input("Enter user name:")
        password=input("Enter password:")
        if user_name!=u.name or password!=u.password:
            attempts-=1
            raise User("Invalid username or password.")
        else:
            print("Login Successful.")
        while True:
            try:
                print("\nBank Menu")
                print("1.Deposit")
                print("2.Withdraw")
                print("3.View Balance")
                print("4.Exit")
                choice=int(input("Enter your choice:"))
                match choice:
                    case 1:
                        amount=int(input("Enter amount to deposit:"))
                        u.deposit(amount)
                    case 2:
                        amount=int(input("Enter amount to withdraw:"))
                        u.with_draw(amount)
                    case 3:
                        u.view_balance()
                    case 4:
                        print("Thank you.")
                        break
                    case _:
                        raise User("Invalid Choice")
            except User as e:
                print("Error:",e)
            except ValueError:
                print("Enter numbers only.")
        break
    except User as e:
        print("Error:",e)
if attempts==0:

    print("Your 3 attempts are finished.")
    print("You failed to login.")